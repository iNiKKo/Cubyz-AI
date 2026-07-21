# [medium/docs_docs_development_multiplayer.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz server, in-game hosting, headless server, dedicated server, launchConfig.zig, settings.zig, defaultPort, autoEnterWorld
**Symbols:** Host World, Invite Player, launchConfig.zig, settings.zig, headlessServer, autoEnterWorld, defaultPort

## Summary
The two ways to set up a Cubyz server: quick in-game hosting, and a headless (dedicated) server, plus how to change the default port.

## Explanation
**Method 1 -- In-Game Hosting:** fast to start, but requires the game to stay running -- closing it or leaving the world disconnects everyone. Steps: click Multiplayer -> Host World, configure world settings and launch, then open the menu and click Invite Player -> Invite to let outside players connect. This shows your public IP and port, which external players need to join. External connections still require port forwarding that port (see the networking chunk for how).

**Method 2 -- Headless Setup (dedicated server):** preferred for a background/always-on server (e.g. on a VPS or dedicated hardware); has no UI, though you can still connect to it from a separate Cubyz window on the same machine. Steps: open `launchConfig.zig`, set `.headlessServer = true`, and set `.autoEnterWorld = "<world name>"` -- the world must already exist (created via a normal-mode run first) before enabling this.

**Changing the default port (optional):** the default is `47649`, set by `defaultPort: u16 = 47649;` in `settings.zig` (inside the `src` folder) -- edit that line directly to change it, and remember to update your port forwarding rule to match.

## Related Questions
- What are the two methods for setting up a Cubyz server?
- What is the default multiplayer server port in Cubyz, and how do you change it?
- What is required to run a headless Cubyz server?
- What happens if you close the game while in-game hosting a Cubyz server?
- What must exist before you can enable headlessServer in launchConfig.zig?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_0*
