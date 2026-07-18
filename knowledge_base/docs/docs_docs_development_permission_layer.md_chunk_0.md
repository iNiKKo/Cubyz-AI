# [easy/docs_docs_development_permission_layer.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz, permissions, permission tree, whitelist, blacklist, path, commands
**Symbols:** /perm, /command/spawn
**Concepts:** permission layer, permission tree, whitelisting, blacklisting

## Summary
This page provides information on the workings of the permission layer and how to use it.

## Explanation
The permission layer in Cubyz handles permissions through a tree structure. The root is at `/`, with `command` as its only child, containing all commands as its children -- e.g. the `spawn` command forms the path `/command/spawn`. The full command syntax (per the engine's actual `perm.zig` implementation) is `/perm <add/remove> <whitelist/blacklist> @<playerIndex> <permissionPath>`. To grant a player full admin permissions, use `/perm add whitelist @<playerIndex> /` (whitelisting the root path grants every command, since whitelisting gives access to a path and all its children). To grant a player access to just the `/spawn` command, use `/perm add whitelist @<playerIndex> /command/spawn`. Blacklisting uses the same syntax with `blacklist` in place of `whitelist` and blocks a path and its children instead of granting them -- e.g. whitelisting `/command` but then blacklisting `/command/spawn` lets a player run every command except spawn. If a path is both whitelisted and blacklisted, the blacklist takes precedence.

## Related Questions
- What is the root of the permission tree in Cubyz?
- What command grants a player full admin permissions in Cubyz?
- What command grants a player access to just the /spawn command in Cubyz?
- How do you whitelist a permission path in Cubyz?
- What does it mean if a permission is both whitelisted and blacklisted?
- Can users run all commands after being whitelisted for `/command`?
- What are some examples of permission paths in Cubyz?
- How do you blacklist a specific command like `spawn`?
- What is the purpose of the `command` node in the permission tree?
- How do you join nodes in the permission tree to form a path?
- What happens if a permission path is both whitelisted and blacklisted?

*Source: unknown | chunk_id: docs_docs_development_permission_layer.md_chunk_0*
