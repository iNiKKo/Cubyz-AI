# [medium/docs_docs_development_multiplayer.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz server, in-game hosting, headless server, port forwarding, permission commands, manual updates, world backups, VPS security, DDoS protection
**Symbols:** Multiplayer, Host World, Invite Player, launchConfig.zig, settings.zig, /perm add whitelist, /perm remove whitelist, VPS, Cloudflare
**Concepts:** server setup, maintenance, permissions, networking, security, updates, backups

## Summary
This page provides detailed instructions on setting up, maintaining, and securing a Cubyz multiplayer server, including methods for hosting, networking configurations, permission management, updates, backups, and security measures.

## Explanation
The documentation covers two main methods of server setup: in-game hosting (quick, but requires the game to keep running -- closing it disconnects everyone) and headless (dedicated) server (runs in the background with no UI, set via `.headlessServer = true` and `.autoEnterWorld = "<world name>"` in `launchConfig.zig`; a world must already exist before enabling it). The server's default port is 47649 (set by `defaultPort: u16 = 47649;` in `settings.zig`, changeable there directly). Port forwarding uses this same default port unless changed, and the router's port-forward rule must select the UDP protocol specifically (not TCP) -- Cubyz's server networking runs over UDP. Permission management uses `/perm add whitelist @<playerIndex> <path>` and `/perm remove whitelist @<playerIndex> <path>`; `/` grants full administrator privileges, `/command/spawn` grants access to just the `/spawn` command. Updates are manual, requiring copying custom configurations from previous versions. Backups must be done manually by copying the world save folder: on Windows this is `C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME`, and on Linux it's `/home/USERNAME/.cubyz/saves/WORLD_NAME`. Security recommendations include using a VPS to keep your home IP private, a domain name behind a proxy (e.g. Cloudflare) for DDoS mitigation, or a relay/VPS proxy to hide your home IP at the cost of some latency.

## Related Questions
- What are the two methods for setting up a Cubyz server?
- How do you configure port forwarding in Cubyz?
- What is the default multiplayer server port in Cubyz?
- What network protocol does Cubyz's server use for port forwarding?
- What commands are used to manage player permissions in Cubyz?
- What command grants a player full admin permissions in Cubyz?
- What command grants a player access to just the /spawn command in Cubyz?
- How do you update a Cubyz server to a new version?
- Where should you back up your Cubyz world files?
- What security measures are recommended for protecting a Cubyz server?
- How can you change the default port for a Cubyz server?
- What is required to run a headless Cubyz server?
- How do you find your router's IP address and login details?
- What are the steps to configure port forwarding on a router?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_0*
