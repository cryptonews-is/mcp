#!/bin/sh
# The 24-hour news sentiment reading and the two stories driving it most.
curl "https://api.cryptonews.is/v1/sentiment?window=24h&limit=2" \
  -H "Authorization: Bearer $CRYPTONEWS_API_KEY"
