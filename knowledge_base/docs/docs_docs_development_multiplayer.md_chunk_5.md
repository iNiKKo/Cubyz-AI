# [medium/docs_docs_development_multiplayer.md] - Chunk 5

**Type:** documentation
**Keywords:** updating server, manual update, world backup, saves folder, DDoS protection, VPS, Cloudflare, relay proxy, server security
**Symbols:** VPS, Cloudflare

## Summary
How to update a Cubyz server, back up world saves, and protect a server from DDoS/network exposure.

## Explanation
**Updating:** currently manual -- download the latest release, extract it, and manually copy over any custom configurations from the previous server directory.

**World backup:** also manual -- copy the specific world folder. On Windows: `C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME`. On Linux: `/home/USERNAME/.cubyz/saves/WORLD_NAME`.

**Server security:** port forwarding and sharing your public IP exposes your local network to the internet, risking DDoS attacks and unauthorized access. Mitigations: use a VPS to keep your home IP private and isolate the server from personal devices (costs a subscription fee); use a domain name behind a proxy like Cloudflare for DDoS mitigation and IP masking (requires a cheap custom domain, ~£10/year, so players connect via e.g. `ashframe.net`); or route traffic through a cheap VPS relay/proxy to hide your home IP, at the cost of some added latency.

## Related Questions
- How do you update a Cubyz server to a new version?
- Where should you back up your Cubyz world files, on Windows vs Linux?
- What security measures are recommended for protecting a Cubyz server?
- Why does port forwarding expose a Cubyz server to security risks?
- What are the tradeoffs of using a VPS vs a domain+proxy vs a relay to protect a Cubyz server?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_5*
