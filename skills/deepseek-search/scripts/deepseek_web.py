#!/usr/bin/env python3
"""Call DeepSeek Search or Fetch once and write the JSON response to stdout."""

import argparse
import ipaddress
import json
import math
import os
import sys
from http.client import HTTPException, HTTPSConnection
from urllib.parse import urlsplit


def short_text(value):
    if not 1 <= len(value) <= 128:
        raise argparse.ArgumentTypeError("长度应为 1～128 个 Unicode 字符")
    return value


def query_text(value):
    short_text(value)
    if not value.strip():
        raise argparse.ArgumentTypeError("搜索词需要包含非空白字符")
    return value


def result_count(value):
    number = int(value)
    if not 1 <= number <= 50:
        raise argparse.ArgumentTypeError("返回条数应为 1～50")
    return number


def timeout_seconds(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("超时秒数应为有限正数")
    return number


def ip_address(value):
    try:
        ipaddress.ip_address(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("localization 应为 IP 地址") from error
    return value


def page_url(value):
    try:
        parsed = urlsplit(value)
        valid = (
            1 <= len(value) <= 8192
            and parsed.scheme in ("http", "https")
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
            and not any(char.isspace() for char in value)
        )
        parsed.port
    except ValueError as error:
        raise argparse.ArgumentTypeError("请提供有效的网页 URL") from error
    if not valid:
        raise argparse.ArgumentTypeError(
            "URL 应为带主机名的 HTTP/HTTPS 地址，最长 8192 字符，且无用户名和密码"
        )
    return value


def build_parser():
    parser = argparse.ArgumentParser(description="DeepSeek 网页搜索与正文抓取")
    commands = parser.add_subparsers(dest="command", required=True)

    search = commands.add_parser("search", help="按关键词搜索网页")
    search.add_argument("query", type=query_text)
    search.add_argument("--count", type=result_count, default=10)
    search.add_argument("--need-content", action="store_true")
    search.add_argument("--ori-question", type=short_text)
    search.add_argument("--localization", type=ip_address)

    fetch = commands.add_parser("fetch", help="抓取指定网页的 Markdown 正文")
    fetch.add_argument("url", type=page_url)

    for command in (search, fetch):
        command.add_argument("--timeout", type=timeout_seconds, default=60)
    return parser


def request_json(command, payload, api_key, timeout):
    connection = HTTPSConnection("api.deepseek.com", timeout=timeout)
    try:
        connection.request(
            "POST",
            f"/v1/tools/{command}",
            body=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )
        response = connection.getresponse()
        return response.status, response.read().decode("utf-8")
    finally:
        connection.close()


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        parser.error("请先在运行环境中设置 DEEPSEEK_API_KEY")
    if not api_key.isascii() or "\r" in api_key or "\n" in api_key:
        parser.error("DEEPSEEK_API_KEY 应为单行 ASCII 文本，请检查配置")

    if args.command == "search":
        payload = {
            "query": args.query,
            "count": args.count,
            "need_content": args.need_content,
        }
        if args.ori_question is not None:
            payload["ori_question"] = args.ori_question
        if args.localization is not None:
            payload["localization"] = args.localization
    else:
        payload = {"url": args.url}

    try:
        status, body = request_json(args.command, payload, api_key, args.timeout)
    except (OSError, HTTPException, UnicodeError) as error:
        diagnostic = str(error).replace(api_key, "[REDACTED]")
        print(f"请求失败：{diagnostic}", file=sys.stderr)
        return 1

    if status != 200:
        diagnostic = body.replace(api_key, "[REDACTED]")
        print(f"HTTP {status}\n{diagnostic}", file=sys.stderr)
        return 1

    try:
        result = json.loads(body)
    except json.JSONDecodeError:
        print("服务端返回 HTTP 200，响应体未通过 JSON 解析", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
