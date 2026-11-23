# cryptonews.is MCP server

<img src="assets/icon-400.png" alt="cryptonews.is" width="96" align="right">

Live crypto news as data for agents. cryptonews.is reads over 1,000 sources, groups their reports into stories, summarises each story in 28 languages, and scores the tone of the news minute by minute. This remote MCP server gives an agent the same data.

- **Server:** `https://mcp.cryptonews.is/mcp` (Streamable HTTP)
- **Sign-in:** OAuth 2.1 with dynamic client registration (sign in with your email), or an API key as a Bearer header
- **Registry name:** `is.cryptonews/news` in the [official MCP Registry](https://registry.modelcontextprotocol.io)
- **Docs:** https://mcp.cryptonews.is/docs?utm_source=github&utm_campaign=mcp-listing

This repository holds connection examples and listing metadata only. The service itself is hosted; there is nothing to install or run.

## Tools

Every tool is read-only except `create_watch` and `delete_watch`, which save and remove your own watches and need an API key.

| Tool | What it returns | Plans |
| --- | --- | --- |
| `get_brief` | The daily brief of a completed day: a short cited write-up, the day's closing sentiment and its top stories | All |
| `latest_stories` | Ranked current stories, each with its coins, category, sentiment and how many outlets cover it | All |
| `get_sentiment` | The news sentiment reading (15 minutes to 24 hours) and the stories driving it | All |
| `get_market` | Market quotes, top coins, total market cap and coins named in current stories | All |
| `get_coin` | One coin in one call: quote, rank and window changes, technicals verdict, latest stories that mention it and the sentiment of those stories | All |
| `get_technicals` | Technical readings for ten large coins (trend, momentum, stretch; today, this week, this month), with the signals behind them on Standard and Pro. Signals, not advice | All |
| `status` | Plan, usage and upstream freshness | All |
| `get_developing` | Developing big events (a major hack, for example) as a cited synthesis: figures, who said what, and a dated timeline | Standard, Pro |
| `get_calendar` | Dated events coming up (unlocks, votes, hearings, launches, deadlines, macro releases), found in the news, with how firm each date is and the stories behind it | Standard, Pro |
| `get_story` | One story with every outlet's report, in 28 languages, including archived stories | Standard, Pro |
| `get_sentiment_history` | Historical sentiment readings | Standard, Pro |
| `get_impact` | What prices did after the news: for stories about a priced coin, the price when the story broke and its move 15 minutes, 1 hour, 4 hours and 24 hours later, with medians per coin. Past observations, not a forecast | Standard, Pro |
| `changes_since` | Stories added, changed or merged since a cursor | Standard, Pro |
| `list_watches` | Your saved filters (watches): 3 on Standard, 25 on Pro | Standard, Pro |
| `get_watch_events` | The stories added or changed since a cursor that match your watches, one event per story, with the same gap markers as `changes_since` | Standard, Pro |
| `create_watch` | Save a filter over the change feed: coins, categories, prominence, coverage, terms, evidence status, first-report language, or a developing thread. API key only | Standard, Pro |
| `delete_watch` | Delete one of your watches. API key only | Standard, Pro |
| `search_stories` | Full-text story search ranked by relevance | Pro |

On live stories, on every plan:

- **`evidence`**: how firm the story is (`reported`, `corroborated`, `confirmed`, `rumoured` or `disputed`), with its basis, stage, number of independent origins and first report. `get_story` adds the history of status changes.
- **`lead`**: the outlet and language that reported it first, how long English coverage took, and `ahead_of_english` while no English outlet the service follows has reported it.

Standard and Pro can filter `latest_stories` by `evidence`, `ahead_of_english` and `lead_language`; `search_stories` takes the same filters.

**Replay (Pro):** pass `as_of` to `latest_stories`, `get_story`, `get_developing` or `get_sentiment` to read them as recorded at that moment, for backtests. Anything not recorded is marked in the response. Editions recorded since 22 November 2026.

Example questions: "What happened in crypto yesterday?", "What's moving crypto right now?", "Why is crypto news bearish today?", "Show every outlet's report on the top story in German.", "Which stories were reported in Chinese before English today?", "How did ETH move after its last five high-importance stories?"

Prompts for clients that show them: `morning_briefing`, `coin_check` (a symbol) and `what_moved` (a window).

New and updated tools reach connected clients through `notifications/tools/list_changed`; clients that support it refresh their tool list without reconnecting.

## Plans

One account covers MCP and REST.

| Plan | Price | Calls/day | Per minute |
| --- | --- | --- | --- |
| Free | $0 | 100 | 10 |
| Standard | $29 / 30 days | 10,000 | 60 |
| Pro | $99 / 30 days | 50,000 | 300 |

See the [docs](https://mcp.cryptonews.is/docs?utm_source=github&utm_campaign=mcp-listing) for limits, errors and arguments.

## Connect

**Claude (claude.ai and Claude Desktop):** Settings → Connectors → Add custom connector → `https://mcp.cryptonews.is/mcp`, then sign in.

**Claude Code:**

```bash
claude mcp add --transport http cryptonews https://mcp.cryptonews.is/mcp
```

**Other clients:** see [`examples/`](examples) for Cursor, VS Code, Windsurf, API-key and REST setups.

## Use and terms

Free is for personal use with credit. Standard and Pro may display data with credit and a link to the story. No resale or model training. The service and its data are governed by the [terms and privacy policy](https://mcp.cryptonews.is/terms). The examples in this repository are MIT licensed.

Support: api@cryptonews.is
