# [medium/docs_docs_development_multiplayer.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz server, in-game hosting, headless setup, port forwarding, permission management, DDoS protection, VPS, domain name, proxy, firewall
**Symbols:** Multiplayer, Host World, Invite Player, launchConfig.zig, settings.zig, defaultPort, ipconfig, ip route, ip a, /perm add whitelist, /perm remove whitelist, @<playerIndex>, <path>, Show Player ID, players folder
**Concepts:** Server Setup, Maintenance, Updates, Permissions, Networking, Port Forwarding, Security

## Summary
This page covers server setup, maintenance, updates, and permissions for Cubyz. It includes methods for in-game hosting, headless setup, networking configurations like port forwarding, permission management commands, and security recommendations.

## Explanation
The documentation provides detailed steps for setting up a Cubyz server using two methods: in-game hosting and headless setup. In-game hosting is quick but requires the game to remain open, while headless setup allows running the server as a background task. Networking configurations, such as port forwarding, are crucial for external player access. Permission management commands allow granting or removing specific permissions to players. Security recommendations include using VPS, domain names with proxies, and relays to protect against DDoS attacks and unauthorized access.

The server's default port is **47649** (set via `defaultPort: u16 = 47649;` in the server config;
change it by modifying that line and updating your port forwarding rule to match). When
configuring port forwarding on a router, the protocol to select is **UDP** -- Cubyz's networking
does not use TCP for gameplay traffic.

Permission commands, exact syntax:
- Grant: `/perm add whitelist @<playerIndex> <path>`
- Remove: `/perm remove whitelist @<playerIndex> <path>`
- `@<playerIndex>` is the player's unique ID, found via "Show Player ID" in the in-game Social tab, or (as server owner) the `players` folder inside the world save directory.
- `<path>` is the permission path being modified: `/` grants FULL ADMINISTRATOR privileges (the root, which cascades to every child in the permission tree); `/command/spawn` grants access specifically to just the `/spawn` command.
- So the full-admin command is exactly `/perm add whitelist @<playerIndex> /`, and the spawn-only command is exactly `/perm add whitelist @<playerIndex> /command/spawn`.

## Related Questions
- How do I set up a Cubyz server using in-game hosting?
- What are the steps for setting up a headless server in Cubyz?
- How do I configure port forwarding for my Cubyz server?
- What is the default multiplayer server port in Cubyz?
- What network protocol does Cubyz's server use for port forwarding?
- How do I manage player permissions in Cubyz?
- What are the recommended security measures for a Cubyz server?
- How do I update to a new version of Cubyz?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_0*
