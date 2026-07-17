# [easy/docs_docs_development_permission_layer.md] - Chunk 0

**Type:** documentation
**Keywords:** permission, tree, root, command, whitelist, blacklist, spawn, access, override, descendant
**Symbols:** /, /command, /perm add whitelist, /perm add blacklist
**Concepts:** permission layer, permission tree, whitelisting, blacklisting, path hierarchy

## Summary
The permission layer uses a tree rooted at / with only the child /command; permissions are granted via whitelist or blocked via blacklist, where blacklist overrides whitelist.

## Explanation
The permission system is organized as a tree starting at root /. The sole immediate child of root is the node command, under which all game commands reside (e.g., spawn). A full path is formed by joining nodes; for spawn the path is /command/spawn. Whitelisting a path grants access to that path and every descendant in the tree—whitelisting /command therefore allows any command. Blacklisting works analogously but denies access; blacklisted paths take precedence over whitelisted ones, so a user can have all commands allowed except those explicitly blacklisted.

## Related Questions
- What is the root node of the permission tree?
- Which child exists directly under the root in the permission tree?
- How do you grant a user access to all commands using the permission layer?
- How do you block a specific command like spawn while allowing others?
- What happens when a path is both whitelisted and blacklisted?
- Does whitelisting /command give access only to that exact node or its children as well?
- Can a user run every command if they have the whitelist for /command?
- Is there any other child besides /command under the root according to this documentation?
- What is the full permission path for the spawn command?
- How does blacklist priority affect combined whitelist and blacklist entries?

*Source: unknown | chunk_id: docs_docs_development_permission_layer.md_chunk_0*
