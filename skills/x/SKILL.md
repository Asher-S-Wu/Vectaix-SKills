---
name: x
description: Use when building applications that interact with X (formerly
  Twitter) data—reading posts, managing users, searching content, streaming
  real-time data, sending direct messages, or managing lists. Agents should
  reach for this skill when users request API integration, data access,
  authentication setup, or troubleshooting X API calls.
metadata:
  mintlify-proj: x
  version: "1.0"
---

# X API Skill Reference

## Product summary

The X API provides programmatic access to X's public conversation through modern REST endpoints. Agents use it to read posts, search content, manage users, access trends, send direct messages, and stream real-time data. The API uses pay-per-usage pricing with no commitments. Key entry points: [X API Introduction](/x-api/introduction), [Make Your First Request](/make-your-first-request), [Developer Console](https://console.x.com). Official SDKs available for Python and TypeScript handle authentication, pagination, and rate limiting automatically.

## When to use

Reach for this skill when:
- A user wants to integrate X data into an application or workflow
- Building search, analytics, or monitoring tools that consume X posts or user data
- Implementing authentication flows (OAuth 1.0a, OAuth 2.0, or Bearer tokens)
- Troubleshooting API errors (401, 403, 429, rate limits)
- Setting up streaming or webhook delivery for real-time posts
- Paginating through large result sets
- Customizing API responses with fields and expansions
- Migrating from older X API versions or other platforms
- Debugging authentication, token, or credential issues

## Quick reference

### Authentication methods

| Method | Use case | Credentials needed |
|:-------|:---------|:-------------------|
| **Bearer Token (App-only)** | Read public data, no user context | API Key + Secret → Bearer Token |
| **OAuth 1.0a User Context** | Act on behalf of a user, private data | API Key, Secret, Access Token, Access Token Secret |
| **OAuth 2.0 Authorization Code** | User login flows, delegated access | Client ID, Client Secret, redirect URL |
| **Basic Auth** | Enterprise APIs only | Username + password (HTTP Basic) |

### Core endpoints by category

| Category | Common endpoints | Purpose |
|:---------|:-----------------|:--------|
| **Posts** | `/2/tweets/search/recent`, `/2/tweets/{id}`, `/2/tweets/search/stream` | Search, retrieve, stream posts |
| **Users** | `/2/users/by/username/{username}`, `/2/users/{id}`, `/2/users/search` | Look up users, search profiles |
| **Timelines** | `/2/users/{id}/tweets`, `/2/users/{id}/mentions` | Get user's posts or mentions |
| **Streams** | `/2/tweets/search/stream`, `/2/tweets/search/stream/rules` | Real-time filtered posts |
| **Direct Messages** | `/2/dm_conversations`, `/2/dm_events` | Send/receive private messages |
| **Lists** | `/2/lists/{id}`, `/2/lists/create` | Manage curated lists |
| **Spaces** | `/2/spaces/{id}`, `/2/spaces/search` | Access live audio conversations |

### Request parameters

| Parameter | Purpose | Example |
|:----------|:--------|:--------|
| `tweet.fields` | Request post data fields | `created_at,public_metrics,lang` |
| `user.fields` | Request user data fields | `description,public_metrics,verified` |
| `expansions` | Include related objects | `author_id,attachments.media_keys` |
| `max_results` | Results per page | `100` (varies by endpoint) |
| `pagination_token` | Cursor for next page | From `meta.next_token` in response |
| `query` | Search filter | `from:xdevelopers lang:en` |

### Response structure

All responses follow this pattern:

```json
{
  "data": [...],           // Primary results
  "includes": {...},       // Related objects (users, media, etc.)
  "meta": {                // Pagination and metadata
    "result_count": 10,
    "next_token": "abc123"
  }
}
```

### Rate limit headers

Check these headers in every response:

| Header | Meaning |
|:-------|:--------|
| `x-rate-limit-limit` | Max requests in 15-minute window |
| `x-rate-limit-remaining` | Requests left in window |
| `x-rate-limit-reset` | Unix timestamp when window resets |

## Decision guidance

### When to use Bearer Token vs OAuth 1.0a

| Scenario | Bearer Token | OAuth 1.0a |
|:---------|:-------------|:-----------|
| Reading public posts only | ✓ Use this | Not needed |
| Acting on behalf of a user | ✗ Can't do this | ✓ Use this |
| Liking/retweeting as a user | ✗ Can't do this | ✓ Use this |
| Sending DMs | ✗ Can't do this | ✓ Use this |
| Simple app-only access | ✓ Use this | Overkill |
| User login required | ✗ Can't do this | ✓ Use this |

### When to use search vs filtered stream

| Need | Search | Filtered Stream |
|:-----|:-------|:-----------------|
| Historical data (7+ days back) | ✓ Use search/all | ✗ Not available |
| Real-time posts as published | ✗ Delayed | ✓ Use this |
| One-time query | ✓ Use this | Overkill |
| Continuous monitoring | ✗ Polling is inefficient | ✓ Use this |
| Complex filtering rules | ✓ Supported | ✓ Supported |
| Cost-sensitive | ✓ Pay per call | ✓ Pay per post |

### When to use fields vs expansions

| Goal | Use fields | Use expansions |
|:-----|:-----------|:---------------|
| Get more data on primary object | ✓ `tweet.fields=created_at` | ✗ Not for this |
| Include related objects (author, media) | ✗ Not for this | ✓ `expansions=author_id` |
| Get fields on related objects | ✓ `user.fields=description` | ✓ `expansions=author_id` (both needed) |
| Reduce response size | ✗ Opposite effect | ✗ Opposite effect |

## Workflow

### 1. Set up authentication

1. Go to [Developer Console](https://console.x.com) and create an app
2. Generate credentials:
   - For app-only access: Copy the **Bearer Token**
   - For user context: Generate **Access Token & Secret** (OAuth 1.0a)
3. Store credentials securely in environment variables (never hardcode)
4. Test with a simple request:
   ```bash
   curl "https://api.x.com/2/users/by/username/xdevelopers" \
     -H "Authorization: Bearer $BEARER_TOKEN"
   ```

### 2. Understand the data model

1. Identify what you need: posts, users, trends, DMs, etc.
2. Find the relevant endpoint in the [API Reference](/x-api/overview)
3. Check what fields are available by default (minimal)
4. Plan which `fields` and `expansions` you need
5. Review rate limits for that endpoint

### 3. Build and test the request

1. Start with minimal parameters (just required ones)
2. Add `fields` to request additional data
3. Add `expansions` to include related objects
4. Test with cURL or Postman first
5. Check response structure and error codes
6. Implement pagination if results exceed `max_results`

### 4. Handle pagination

1. Check if response includes `meta.next_token`
2. If present, make another request with `pagination_token=<next_token>`
3. Repeat until no `next_token` is returned
4. Use SDKs for automatic pagination handling

### 5. Implement error handling

1. Catch 401 (auth failed): Check token validity and format
2. Catch 403 (forbidden): Verify app has endpoint access
3. Catch 429 (rate limited): Implement exponential backoff
4. Check `x-rate-limit-reset` header for retry timing
5. Log errors with request details for debugging

### 6. Deploy to production

1. Use official SDKs (Python or TypeScript) for automatic handling
2. Store credentials in secure vault, not environment files
3. Implement monitoring for rate limits and errors
4. Set up alerts for failed requests
5. Test with real data before going live

## Common gotchas

- **Minimal fields by default**: Requests return only `id`, `text`, and `edit_history_tweet_ids` for posts. Always specify `tweet.fields` for additional data.
- **Expansions require fields**: To get author details, use both `expansions=author_id` AND `user.fields=description` (not just one).
- **Bearer Token is app-only**: Can't like, retweet, or send DMs. Need OAuth 1.0a or 2.0 for user actions.
- **Rate limits are per endpoint**: Different endpoints have different limits. Check headers after each request.
- **429 errors need exponential backoff**: Don't retry immediately. Start with 1 minute, double each time.
- **Pagination tokens expire**: Don't store tokens for later use. Resume pagination immediately or restart.
- **Search is limited to 7 days**: Use `/2/tweets/search/all` (Enterprise) for historical data.
- **Streaming requires persistent connection**: Don't treat it like REST. Handle disconnections and reconnect.
- **Field order in responses varies**: Don't assume fields appear in request order.
- **Null fields are omitted**: Missing data means the field is null or empty, not an error.
- **Credentials displayed once**: Save immediately. Regenerating invalidates old ones.
- **OAuth 1.0a signature is complex**: Use SDKs or libraries. Manual signing is error-prone.

## Verification checklist

Before submitting work with X API integration:

- [ ] Authentication credentials stored securely (not in code)
- [ ] Bearer Token or OAuth tokens are valid and not expired
- [ ] Request includes required `Authorization` header
- [ ] `fields` parameters added for all needed data (not relying on defaults)
- [ ] `expansions` used correctly with corresponding `fields` for related objects
- [ ] Pagination implemented if results may exceed `max_results`
- [ ] Error handling covers 401, 403, 429, and network errors
- [ ] Rate limit headers checked and exponential backoff implemented
- [ ] Response JSON structure validated (check for `data`, `includes`, `meta`)
- [ ] Tested with real API calls (not just mock data)
- [ ] No hardcoded credentials in code or config files
- [ ] Official SDK used (Python or TypeScript) for production code
- [ ] Streaming connections handle disconnections and reconnect
- [ ] Webhook endpoints validate CRC tokens on registration

## Resources

- **Comprehensive navigation**: [llms.txt](/llms.txt) — Full page-by-page index of all documentation
- **Getting started**: [Make Your First Request](/make-your-first-request) — Step-by-step guide with cURL examples
- **API Reference**: [X API Overview](/x-api/overview) — Complete endpoint documentation
- **Authentication guide**: [Authentication Overview](/fundamentals/authentication/overview) — All auth methods explained
- **Fundamentals**: [Fields](/x-api/fundamentals/fields), [Pagination](/x-api/fundamentals/pagination), [Rate Limits](/fundamentals/rate-limits)
- **Official SDKs**: [Python XDK](/xdks/python/overview), [TypeScript XDK](/xdks/typescript/overview)
- **Tools**: [Postman Collection](https://www.postman.com/xapidevelopers/x-api-public-workspace/collection/34902927-2efc5689-99c6-4ab6-8091-996f35c2fd80), [xurl CLI](/tools/xurl)

---

> For additional documentation and navigation, see: https://docs.x.com/llms.txt