---
name: x
description: Use when building integrations with X (formerly Twitter) to read
  posts, search content, manage user interactions, stream real-time data, or
  access trends and analytics. Agents should reach for this skill when users
  request API integration, data retrieval, automation, or real-time monitoring
  of X platform data.
metadata:
  mintlify-proj: x
  version: "1.0"
---

# X API Skill Reference

## Product summary

The X API provides programmatic access to X's public conversation through modern REST endpoints. Agents use it to read posts, search content, manage users, stream real-time data, and access trends. The API uses pay-per-usage pricing with no commitments. Key entry points: Bearer Token authentication for app-only requests, OAuth 2.0 for user-context actions. Primary docs: https://docs.x.com/x-api/introduction. Official SDKs available for Python and TypeScript handle authentication, pagination, and rate limiting automatically.

## When to use

Reach for this skill when:
- User requests to search or retrieve posts from X
- Building automation to post content, like, repost, or follow users
- Streaming real-time posts matching specific keywords or rules
- Looking up user profiles, followers, or engagement metrics
- Integrating X data into dashboards or analytics tools
- Managing direct messages or lists programmatically
- Implementing webhooks for event-driven workflows
- Accessing historical post data or trends

Do NOT use this skill for: website embedding (use X for Websites), ad campaign management (use X Ads API), or livestream operations (use Livestream API).

## Quick reference

### Authentication methods

| Method | Use case | Credentials |
|--------|----------|-------------|
| Bearer Token (App-only) | Read public data only | Single token, simplest |
| OAuth 2.0 Authorization Code | User-context actions (post, like, follow) | Client ID + Secret + user approval |
| OAuth 1.0a User Context | Legacy user-context requests | API Key + Secret + Access Token + Secret |

### Essential endpoints

| Task | Endpoint | Method |
|------|----------|--------|
| Look up user by username | `/2/users/by/username/{username}` | GET |
| Look up post by ID | `/2/tweets/{id}` | GET |
| Search recent posts (7 days) | `/2/tweets/search/recent` | GET |
| Search full archive | `/2/tweets/search/all` | GET |
| Get user's posts | `/2/users/{id}/tweets` | GET |
| Create post | `/2/tweets` | POST |
| Delete post | `/2/tweets/{id}` | DELETE |
| Like post | `/2/users/{id}/likes` | POST |
| Follow user | `/2/users/{id}/following` | POST |
| Stream filtered posts | `/2/tweets/search/stream` | GET |
| Add stream rule | `/2/tweets/search/stream/rules` | POST |

### Field parameters (customize response data)

Request additional fields with query parameters:

```bash
# Posts
?tweet.fields=created_at,public_metrics,lang,author_id

# Users
?user.fields=created_at,description,public_metrics,verified

# Media
?media.fields=url,preview_image_url,alt_text,type

# Expansions (include related objects)
?expansions=author_id,attachments.media_keys
```

### Rate limits

- Check headers: `x-rate-limit-limit`, `x-rate-limit-remaining`, `x-rate-limit-reset`
- 429 response = rate limited; wait until `x-rate-limit-reset` timestamp
- Implement exponential backoff: start 1 minute, double each retry
- Use streaming instead of polling for real-time data

### Common HTTP status codes

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Bad Request | Check parameter formatting, required fields |
| 401 | Unauthorized | Verify Bearer Token or OAuth credentials |
| 403 | Forbidden | Check app permissions, user scopes |
| 404 | Not Found | Resource deleted or doesn't exist |
| 429 | Rate Limited | Wait and retry with exponential backoff |

## Decision guidance

### When to use Bearer Token vs OAuth 2.0

| Scenario | Use Bearer Token | Use OAuth 2.0 |
|----------|-----------------|--------------|
| Reading public posts only | ✓ | — |
| Posting, liking, following | — | ✓ |
| Accessing user's DMs | — | ✓ |
| Simple read-only automation | ✓ | — |
| Multi-user app | — | ✓ |
| Accessing private user data | — | ✓ |

### When to use search vs filtered stream

| Need | Use search | Use filtered stream |
|------|-----------|-------------------|
| Historical data (7+ days old) | ✓ | — |
| Recent posts (last 7 days) | ✓ | ✓ |
| Real-time delivery | — | ✓ |
| One-time query | ✓ | — |
| Continuous monitoring | — | ✓ |
| Persistent connection | — | ✓ |

### When to use SDK vs raw HTTP

| Scenario | Use SDK | Use raw HTTP |
|----------|---------|-------------|
| Production code | ✓ | — |
| Testing/prototyping | ✓ | ✓ |
| Simple one-off requests | — | ✓ |
| Pagination needed | ✓ | — |
| Streaming data | ✓ | — |
| Language not supported | — | ✓ |

## Workflow

### 1. Set up credentials
- Navigate to https://console.x.com and sign in with X account
- Create a new app, accept Developer Agreement
- Copy Bearer Token (for app-only) or OAuth credentials (for user actions)
- Store credentials in environment variables, never hardcode

### 2. Choose authentication method
- For reading public data only: use Bearer Token
- For posting, liking, following: use OAuth 2.0 (recommended) or OAuth 1.0a
- Verify app has required permissions in Developer Console

### 3. Make your first request
- Start with simple endpoint: user lookup, post lookup, or recent search
- Use cURL or SDK to test: `curl "https://api.x.com/2/users/by/username/xdevelopers" -H "Authorization: Bearer $TOKEN"`
- Parse JSON response; data is in `data` field, related objects in `includes`

### 4. Customize response with fields and expansions
- Identify what data you need (created_at, metrics, author info)
- Add `tweet.fields`, `user.fields`, `media.fields` parameters
- Use `expansions` to include related objects (author, media, referenced posts)
- Example: `?tweet.fields=created_at,public_metrics&expansions=author_id&user.fields=username`

### 5. Handle pagination
- Check response for `meta.next_token` (indicates more results)
- Pass `next_token` in next request to get next page
- SDKs handle pagination automatically with iterators
- Don't poll repeatedly; use `since_id` for incremental updates

### 6. Implement error handling
- Catch 401 (auth failed), 403 (permission denied), 429 (rate limited)
- For 429: read `x-rate-limit-reset` header, wait, retry with exponential backoff
- Log errors with request details for debugging

### 7. For streaming: set up rules and connect
- POST rules to `/2/tweets/search/stream/rules` with operators (keywords, users, hashtags)
- GET `/2/tweets/search/stream` to establish persistent connection
- Process each line as JSON; blank lines are keep-alive signals
- Implement reconnection logic for disconnections

## Common gotchas

- **Forgetting Bearer Token prefix**: Use `Authorization: Bearer YOUR_TOKEN`, not just the token
- **Requesting non-existent fields**: Check data dictionary; some fields require specific tiers or authentication
- **Not handling 429 rate limits**: Implement exponential backoff; don't retry immediately
- **Polling instead of streaming**: Use filtered stream for real-time; polling wastes credits
- **Missing expansions for related data**: To get author details, add `expansions=author_id` AND `user.fields=...`
- **Hardcoding credentials**: Always use environment variables; never commit tokens to git
- **Assuming all endpoints support all fields**: Check endpoint docs; some fields only available on certain endpoints
- **Not checking x-rate-limit-reset**: This header tells you exactly when to retry; use it
- **Forgetting to add rules before streaming**: Stream returns 409 Conflict if no rules exist
- **Assuming Bearer Token works for user actions**: Bearer Token is app-only; use OAuth for posting, liking, following
- **Not handling keep-alive signals in streams**: Blank lines every 20 seconds are normal; don't treat as errors
- **Requesting too many fields at once**: Each field adds cost; request only what you need

## Verification checklist

Before submitting work:

- [ ] Credentials stored in environment variables, not hardcoded
- [ ] Authentication method matches use case (Bearer Token for read-only, OAuth for user actions)
- [ ] Correct endpoint chosen for the task (search vs stream, recent vs archive)
- [ ] Fields and expansions added to customize response (not requesting unnecessary data)
- [ ] Error handling implemented for 401, 403, 429 responses
- [ ] Rate limit headers checked; exponential backoff implemented for 429
- [ ] Pagination handled correctly (next_token passed in subsequent requests)
- [ ] For streaming: rules added before connecting to stream endpoint
- [ ] Response parsed correctly (data in `data` field, related objects in `includes`)
- [ ] Tested with cURL or SDK before deploying
- [ ] No credentials in logs or error messages

## Resources

**Comprehensive navigation**: https://docs.x.com/llms.txt

**Critical documentation**:
- [X API Introduction](https://docs.x.com/x-api/introduction) — Overview of endpoints and capabilities
- [Make Your First Request](https://docs.x.com/make-your-first-request) — Step-by-step quickstart with examples
- [Authentication Overview](https://docs.x.com/fundamentals/authentication/overview) — All auth methods explained
- [Fields & Expansions](https://docs.x.com/x-api/fundamentals/fields) — Customize response data
- [Filtered Stream](https://docs.x.com/x-api/posts/filtered-stream/introduction) — Real-time streaming setup
- [Rate Limits](https://docs.x.com/fundamentals/rate-limits) — Understand and handle rate limiting
- [Response Codes & Errors](https://docs.x.com/x-api/fundamentals/response-codes-and-errors) — Error reference
- [Python SDK](https://docs.x.com/xdks/python/overview) — Official Python library
- [TypeScript SDK](https://docs.x.com/xdks/typescript/overview) — Official TypeScript library

---

> For additional documentation and navigation, see: https://docs.x.com/llms.txt