---
name: x
description: "Use when building applications that interact with X (formerly
  Twitter) data and functionality. Reach for this skill when agents need to:
  read or search posts, manage user accounts, access real-time streams, send
  direct messages, manage lists, or integrate X data into applications. Use for
  API integration, authentication setup, request building, pagination, error
  handling, and rate limit management."
metadata:
  mintlify-proj: x
  version: "1.0"
---

# X API Skill Reference

## Product summary

The X API provides programmatic access to X's public conversation through modern REST endpoints. Agents use it to read posts, search content, manage users, access real-time streams, send direct messages, and analyze trends. The API uses pay-per-usage pricing with no commitments. Key files and commands: Bearer Token (app-only auth), OAuth 1.0a/2.0 credentials (user context), API endpoints at `https://api.x.com/2/`, official SDKs (Python XDK, TypeScript XDK). Primary docs: https://docs.x.com/x-api/introduction

## When to use

Reach for this skill when:
- Building integrations that read, search, or publish posts
- Implementing user authentication or account management
- Setting up real-time data streams (filtered stream, volume streams)
- Managing direct messages, lists, or user relationships
- Accessing analytics, trends, or compliance data
- Handling pagination, rate limits, or error responses
- Choosing between authentication methods (OAuth 1.0a vs 2.0, app-only vs user context)
- Debugging API errors (401, 403, 429, etc.)

## Quick reference

### Authentication methods

| Method | Use case | Credentials |
|--------|----------|-------------|
| **Bearer Token (App-only)** | Read public data, no user context | Single token from Developer Console |
| **OAuth 1.0a User Context** | Act on behalf of a user, legacy integrations | API Key, Secret, Access Token, Token Secret |
| **OAuth 2.0 Authorization Code** | User login flows, fine-grained scopes | Client ID, Client Secret, Authorization Code |
| **OAuth 2.0 App-Only** | Server-to-server, public data access | Client ID, Client Secret |

### Common endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/2/users/by/username/{username}` | GET | Look up user by handle |
| `/2/tweets/{id}` | GET | Get post by ID |
| `/2/tweets/search/recent` | GET | Search posts from last 7 days |
| `/2/tweets/search/all` | GET | Full-archive search (Enterprise) |
| `/2/tweets/search/stream` | GET | Real-time filtered stream |
| `/2/tweets/search/stream/rules` | POST/GET | Manage stream rules |
| `/2/tweets` | POST | Create a post |
| `/2/tweets/{id}` | DELETE | Delete a post |
| `/2/users/{id}/tweets` | GET | Get user's posts |
| `/2/direct_messages/conversations/with/{participant_id}/messages` | POST | Send DM |

### Request parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `tweet.fields` | Request post fields | `created_at,public_metrics,lang` |
| `user.fields` | Request user fields | `created_at,description,public_metrics` |
| `expansions` | Include related objects | `author_id,attachments.media_keys` |
| `max_results` | Results per page | `100` (varies by endpoint) |
| `pagination_token` | Cursor for next page | From `meta.next_token` in response |
| `query` | Search filter | `from:xdevelopers lang:en` |

### Response structure

```json
{
  "data": [...],           // Primary results
  "includes": {...},       // Related objects (users, media, etc.)
  "meta": {
    "result_count": 10,
    "next_token": "abc123"  // Use for pagination
  }
}
```

### Rate limit headers

| Header | Meaning |
|--------|---------|
| `x-rate-limit-limit` | Max requests in 15-minute window |
| `x-rate-limit-remaining` | Requests left in current window |
| `x-rate-limit-reset` | Unix timestamp when window resets |

## Decision guidance

### When to use Bearer Token vs OAuth 1.0a

| Scenario | Use Bearer Token | Use OAuth 1.0a |
|----------|------------------|----------------|
| Reading public posts | ✓ | ✓ |
| Publishing posts | ✗ | ✓ |
| Acting on behalf of user | ✗ | ✓ |
| Server-to-server automation | ✓ | ✓ |
| User login flow | ✗ | ✓ |
| Simplicity | ✓ | ✗ |

### When to use fields vs expansions

| Need | Use fields | Use expansions |
|------|-----------|----------------|
| Get more data on primary object | ✓ | ✗ |
| Include related objects (author, media) | ✗ | ✓ |
| Reduce response size | ✓ | ✓ |
| Get nested object data | ✓ (with expansion) | ✓ |

### When to use search vs filtered stream

| Scenario | Use search | Use filtered stream |
|----------|-----------|-------------------|
| Historical data lookup | ✓ | ✗ |
| Real-time monitoring | ✗ | ✓ |
| One-time queries | ✓ | ✗ |
| Continuous listening | ✗ | ✓ |
| Full-archive access | ✓ (Enterprise) | ✗ |

## Workflow

1. **Set up credentials**
   - Go to console.x.com and create an app
   - Generate Bearer Token (app-only) or OAuth credentials
   - Store credentials securely; they display only once
   - Copy token/keys to environment variables

2. **Choose authentication method**
   - For reading public data: use Bearer Token
   - For user actions (post, like, follow): use OAuth 1.0a or 2.0
   - For server automation: use Bearer Token or OAuth 2.0 App-Only
   - For user login flows: use OAuth 2.0 Authorization Code

3. **Build the request**
   - Select endpoint from API reference
   - Add required path parameters (user ID, post ID, etc.)
   - Add `fields` parameter to request additional data
   - Add `expansions` to include related objects
   - Add `query` parameter for search endpoints
   - Set `max_results` for pagination

4. **Make the request**
   - Include `Authorization: Bearer $TOKEN` header
   - Use correct HTTP method (GET, POST, DELETE)
   - URL-encode query parameters
   - Send JSON body for POST requests

5. **Handle the response**
   - Check HTTP status code (200 = success, 4xx = client error, 5xx = server error)
   - Extract data from `data` field
   - Extract related objects from `includes` field
   - Check `meta.next_token` for pagination
   - Match IDs between primary and included objects

6. **Implement pagination**
   - Check if `meta.next_token` exists in response
   - If present, make next request with `pagination_token=<next_token>`
   - Repeat until no `next_token` returned
   - Use SDKs for automatic pagination

7. **Handle rate limits**
   - Monitor `x-rate-limit-remaining` header
   - If you receive 429 response, wait until `x-rate-limit-reset` timestamp
   - Implement exponential backoff: start with 1 minute, double on each retry
   - Cache responses to reduce repeated requests

## Common gotchas

- **Missing fields in response**: By default, endpoints return minimal fields (id, text for posts). Always add `tweet.fields` or `user.fields` to get additional data.
- **Forgetting expansions**: To get author details on a post, you need both `expansions=author_id` AND `user.fields=...`. Expansions alone return only the ID.
- **Bearer Token vs OAuth confusion**: Bearer Token is app-only and can't post or act on behalf of users. Use OAuth 1.0a or 2.0 for user actions.
- **Pagination token expiration**: Tokens may expire after time. Don't store them long-term; regenerate if needed.
- **Rate limit 429 errors**: Don't retry immediately. Check `x-rate-limit-reset` header and wait until that Unix timestamp. Implement exponential backoff.
- **401 Unauthorized**: Verify Bearer Token is correct and hasn't been regenerated. Check `Authorization: Bearer $TOKEN` header format.
- **403 Forbidden**: App may lack permissions for this endpoint. Check Developer Console app settings. Some endpoints require user-context auth.
- **404 Not Found**: Post or user doesn't exist, was deleted, or is protected. Verify ID format and that resource is public.
- **Null fields in response**: X API omits null values from JSON. If a field is missing, its value is null/empty.
- **Query syntax errors**: Search queries use operators (from:, lang:, has:media). Wrap complex queries in quotes. Test in API reference first.
- **Streaming connection drops**: Implement reconnection logic with exponential backoff. Use backfill_minutes parameter to recover missed data (Academic Research only).
- **DM endpoint confusion**: Direct Messages use different endpoints than posts. Use `/2/direct_messages/` prefix, not `/2/tweets/`.

## Verification checklist

Before submitting work with X API integration:

- [ ] Credentials stored securely (environment variables, not hardcoded)
- [ ] Correct authentication method chosen for use case
- [ ] `Authorization` header present and correctly formatted
- [ ] Required path parameters included in URL
- [ ] `fields` parameter added to request additional data beyond defaults
- [ ] `expansions` parameter added if accessing related objects
- [ ] Response parsing handles `data`, `includes`, and `meta` objects
- [ ] Pagination implemented if `max_results` < total results
- [ ] Rate limit headers monitored; exponential backoff implemented for 429
- [ ] Error responses handled (401, 403, 404, 429 cases covered)
- [ ] Query syntax validated (especially for search endpoints)
- [ ] Tested with actual API calls, not just documentation examples
- [ ] Bearer Token or OAuth credentials regenerated if exposed
- [ ] API usage monitored in Developer Console for unexpected costs

## Resources

**Comprehensive navigation**: https://docs.x.com/llms.txt

**Critical documentation pages**:
1. [X API Introduction](https://docs.x.com/x-api/introduction) — Overview of endpoints and capabilities
2. [Make Your First Request](https://docs.x.com/make-your-first-request) — Quick start with cURL examples
3. [Authentication Overview](https://docs.x.com/fundamentals/authentication/overview) — All auth methods explained
4. [Fields & Expansions](https://docs.x.com/x-api/fundamentals/fields) — How to customize response data
5. [Pagination](https://docs.x.com/x-api/fundamentals/pagination) — Cursor-based pagination patterns
6. [Rate Limits](https://docs.x.com/fundamentals/rate-limits) — Request limits and backoff strategy
7. [Error Codes](https://docs.x.com/x-api/fundamentals/response-codes-and-errors) — HTTP status meanings and solutions

---

> For additional documentation and navigation, see: https://docs.x.com/llms.txt