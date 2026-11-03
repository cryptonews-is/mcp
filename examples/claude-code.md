# Claude Code

OAuth (sign in with your email when prompted):

```bash
claude mcp add --transport http cryptonews https://mcp.cryptonews.is/mcp
```

With an API key from https://mcp.cryptonews.is/account:

```bash
claude mcp add --transport http cryptonews https://mcp.cryptonews.is/mcp --header "Authorization: Bearer $CRYPTONEWS_API_KEY"
```
