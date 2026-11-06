---
name: x
description: Use when building applications that interact with X (formerly
  Twitter) data. Agents should reach for this skill when working with posts,
  users, search, streaming, authentication, rate limits, pagination, or any X
  API v2 endpoints. Essential for tasks like searching posts, retrieving user
  data, managing content, building real-time applications, or integrating X data
  into applications.
metadata:
  mintlify-proj: x
  version: "1.0"
---

# X API Skill

## Product summary

The X API provides programmatic access to X's public conversation through modern REST endpoints. Agents use it to search posts, retrieve user data, manage content, access trends, handle direct messages, and build real-time applications. The API uses pay-per-usage pricing with no subscriptions.

**Key files and commands:**
- Bearer Token authentication (app-only) or OAuth 1.0a/2.0 (user context)
- Base URL: `https://api.x.com/2/`
- Official SDKs: Python (`xdk`) and TypeScript (`@xdevplatform/xdk`)
- CLI tool: `xurl` for curl-like requests with built-in OAuth
- Credentials stored in Developer Console at https://console.x.com

[Primary docs: https://docs.x.com/x-api/introduction](https://docs.x.com/x-api/introduction)

## When to use

Reach for this skill when:
- **Searching posts**: Find posts by keywords, hashtags, users, dates, or operators (recent 7 days or full archive)
- **User lookups**: Retrieve user profiles, followers, following, or search for users
- **Managing content**: Create, delete, or hide posts; manage likes, reposts, bookmarks
- **Real-time data**: Set up filtered streams with rules to receive posts as they're published
- **Building integrations**: Embed X data into applications, dashboards, or analysis tools
- **Handling authentication**: Implement OAuth flows for user-context requests
- **Monitoring rate limits**: Track usage and implement backoff strategies
- **Pagination**: Navigate large result sets with next_token
- **Streaming**: Connect to persistent streams for real-time post delivery

## Quick reference

### Authentication methods

| Method | Use case | Credentials |
|:-------|:---------|:------------|
| Bearer Token (app-only) | Read public data, no user context | API Key + Secret → Bearer Token |
| OAuth 1.0a User Context | Act on behalf of a user | API Key + Secret + Access Token + Secret |
| OAuth 2.0 Authorization Code | User login flows, PKCE support | Client ID + Secret |
| Basic Auth | Enterprise APIs | Username + password |

### Common endpoints

| Task | Endpoint | Method |
|:-----|:---------|:--------|
| Look up user by username | `/2/users/by/username/:username` | GET |
| Search recent posts | `/2/tweets/search/recent` | GET |
| Search full archive | `/2/tweets/search/all` | GET |
| Get post by ID | `/2/tweets/:id` | GET |
| Create post | `/2/tweets` | POST |
| Delete post | `/2/tweets/:id` | DELETE |
| Get user's posts | `/2/users/:id/tweets` | GET |
| Filtered stream rules | `/2/tweets/search/stream/rules` | GET/POST |
| Connect to stream | `/2/tweets/search/stream` | GET |

### Request parameters

| Parameter | Purpose | Example |
|:----------|:--------|:--------|
| `tweet.fields` | Request additional post data | `created_at,public_metrics,lang` |
| `user.fields` | Request additional user data | `created_at,description,public_metrics` |
| `expansions` | Include related objects | `author_id,referenced_tweets.id` |
| `max_results` | Results per page (default varies) | `100` |
| `pagination_token` | Navigate pages | Use `next_token` from response |
| `query` | Search operator string | `from:xdevelopers lang:en` |

### Response headers (rate limits)

```
x-rate-limit-limit: 450
x-rate-limit-remaining: 425
x-rate-limit-reset: 1705420800
```

## Decision guidance

### When to use Bearer Token vs. OAuth

| Scenario | Use Bearer Token | Use OAuth 1.0a/2.0 |
|:---------|:-----------------|:-------------------|
| Read public data only | ✓ | — |
| Act on behalf of user | — | ✓ |
| Manage user's posts/likes | — | ✓ |
| Build user login flow | — | ✓ (OAuth 2.0) |
| Server-to-server app | ✓ | — |

### When to use search vs. filtered stream

| Need | Use search | Use filtered stream |
|:-----|:-----------|:-------------------|
| Historical data lookup | ✓ | — |
| Recent 7 days only | ✓ (recent endpoint) | ✓ |
| Full archive (back to 2006) | ✓ (full-archive endpoint) | — |
| Real-time delivery | — | ✓ |
| One-time query | ✓ | — |
| Persistent monitoring | — | ✓ |

### When to use fields vs. expansions

| Situation | Use fields | Use expansions |
|:----------|:-----------|:---------------|
| Get more data on primary object | ✓ | — |
| Include related objects (author, media) | — | ✓ |
| Customize response structure | ✓ | — |
| Reduce payload size | ✓ | — |

## Workflow

### 1. Set up authentication

1. Create a developer account at https://console.x.com
2. Create a Project and App
3. Generate credentials:
   - For app-only: Copy Bearer Token
   - For user context: Generate API Key, Secret, Access Token, Access Token Secret
4. Store credentials in environment variables (never hardcode)
5. Verify access: Test with `GET /2/users/me` (user context) or user lookup (app-only)

### 2. Make your first request

1. Choose an endpoint (start with user lookup or recent search)
2. Construct the URL with base `https://api.x.com/2/`
3. Add required parameters (e.g., `?user.fields=created_at`)
4. Set Authorization header: `Authorization: Bearer $BEARER_TOKEN`
5. Make GET/POST request
6. Parse JSON response; primary data is in `data` field
7. Check `meta.next_token` for pagination

### 3. Search posts

1. Build query using operators: `from:user`, `#hashtag`, `lang:en`, `-is:retweet`, `has:images`
2. Choose endpoint: `/2/tweets/search/recent` (7 days) or `/2/tweets/search/all` (full archive)
3. Set `query` parameter with your operator string
4. Request fields: `tweet.fields=created_at,public_metrics,author_id`
5. Request expansions if needed: `expansions=author_id`
6. Handle pagination with `next_token`
7. Monitor rate limits in response headers

### 4. Set up filtered stream

1. Create rules: `POST /2/tweets/search/stream/rules` with rule value (e.g., `from:xdevelopers`)
2. Verify rules: `GET /2/tweets/search/stream/rules`
3. Connect to stream: `GET /2/tweets/search/stream`
4. Keep connection open; parse JSON objects as they arrive
5. Implement exponential backoff for reconnections
6. Monitor for disconnections and reconnect automatically

### 5. Handle pagination

1. Make initial request with `max_results` parameter
2. Check response `meta.next_token`
3. If token exists, make next request with `pagination_token=<next_token>`
4. Repeat until `next_token` is absent or response is empty
5. Use SDKs for automatic pagination handling

### 6. Manage rate limits

1. Check response headers after each request
2. If `x-rate-limit-remaining` is low, slow down requests
3. On 429 error, wait until `x-rate-limit-reset` timestamp
4. Implement exponential backoff: wait 1s, 2s, 4s, 8s...
5. Cache responses to reduce repeated requests
6. Use streaming instead of polling for real-time data

## Common gotchas

- **Hardcoded credentials**: Never commit API keys to git. Use environment variables and `.gitignore`.
- **Wrong authentication method**: Bearer Token is app-only (public data). Use OAuth for user-context endpoints.
- **Missing fields parameter**: Endpoints return minimal data by default. Always request fields you need.
- **Forgetting expansions**: To get author details on a post, you need both `expansions=author_id` AND `user.fields=...`.
- **Ignoring rate limits**: 429 errors mean you've hit limits. Check headers and implement backoff before retrying.
- **Polling instead of streaming**: Don't repeatedly call search for new posts. Use filtered stream for real-time data.
- **Not handling pagination**: Large result sets require pagination. Always check for `next_token` and paginate until it's absent.
- **Streaming connection drops**: Implement automatic reconnection with exponential backoff. Expect disconnections.
- **Query syntax errors**: Test operators in isolation. Common mistakes: missing quotes around phrases, invalid operators, typos.
- **Deleted/protected posts**: Deleted posts return 404. Protected accounts' posts need authorization. Withheld posts vary by region.
- **Bearer Token regeneration**: Regenerating tokens invalidates old ones. Update environment variables immediately.
- **Exceeding query length**: Recent search: 512 chars (4,096 for Enterprise). Full-archive: 1,024 chars (4,096 for Enterprise).

## Verification checklist

Before submitting work with X API integration:

- [ ] Credentials are stored in environment variables, not hardcoded
- [ ] Correct authentication method used (Bearer Token vs. OAuth)
- [ ] All required fields requested via `tweet.fields`, `user.fields`, etc.
- [ ] Expansions included if accessing related objects
- [ ] Pagination implemented (checking for `next_token`)
- [ ] Rate limit handling in place (checking headers, implementing backoff)
- [ ] Error handling for 401 (auth), 403 (access), 404 (not found), 429 (rate limit)
- [ ] Streaming connections have reconnection logic
- [ ] Query syntax validated (operators, quotes, length limits)
- [ ] Response parsing handles null/missing fields
- [ ] Tests use sandbox/mock data, not production credits
- [ ] Documentation includes endpoint URLs and required parameters

## Resources

**Comprehensive navigation:** [https://docs.x.com/llms.txt](https://docs.x.com/llms.txt)

**Critical pages:**
1. [X API Introduction](https://docs.x.com/x-api/introduction) — Overview, pricing, key features
2. [Make Your First Request](https://docs.x.com/make-your-first-request) — Quick start with cURL and code examples
3. [Authentication Overview](https://docs.x.com/fundamentals/authentication/overview) — Auth methods and credential management
4. [Rate Limits](https://docs.x.com/x-api/fundamentals/rate-limits) — Per-endpoint limits and handling strategies
5. [Search Posts](https://docs.x.com/x-api/posts/search/introduction) — Query operators and search endpoints
6. [Filtered Stream](https://docs.x.com/x-api/posts/filtered-stream/introduction) — Real-time streaming setup
7. [Fields & Expansions](https://docs.x.com/x-api/fundamentals/fields) — Customizing response data
8. [Pagination](https://docs.x.com/x-api/fundamentals/pagination) — Navigating large result sets
9. [Error Handling](https://docs.x.com/x-api/fundamentals/response-codes-and-errors) — Status codes and troubleshooting
10. [Official SDKs](https://docs.x.com/tools-and-libraries) — Python and TypeScript libraries

---

> For additional documentation and navigation, see: https://docs.x.com/llms.txt