# [medium/docs_docs_development_multiplayer.md] - Chunk 4

**Type:** documentation
**Keywords:** permissions, whitelist, perm add, perm remove, playerIndex, admin privileges, Show Player ID, Social tab
**Symbols:** /perm add whitelist, /perm remove whitelist, playerIndex

## Summary
How to manage player permissions on a Cubyz server using the `/perm` commands.

## Explanation
Grant permissions with `/perm add whitelist @<playerIndex> <path>`; remove them with `/perm remove whitelist @<playerIndex> <path>`. `@<playerIndex>` is the player's unique ID -- find it by enabling "Show Player ID" in the in-game Social tab, or as a server owner by checking the `players` folder inside the world save directory (config files are named after each player's ID). `<path>` is the permission path to modify: `/` grants full administrator privileges, while `/command/spawn` grants access specifically to the `/spawn` command.

## Related Questions
- What commands are used to manage player permissions in Cubyz?
- What command grants a player full admin permissions in Cubyz?
- What command grants a player access to just the /spawn command in Cubyz?
- How do you find a player's index/ID for Cubyz permission commands?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_4*
