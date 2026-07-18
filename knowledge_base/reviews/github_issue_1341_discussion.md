# [issues/issue_1341.md] - Issue #1341 discussion

**Type:** review
**Keywords:** blueprint assets, relative paths, disallow `..`, new commands, access controls, flags, scopes, asset management, ID constraints, multiplayer security
**Symbols:** /blueprint load, /sbb <load|store|list>, --server, --local, --assets, --world, /blueprint move
**Concepts:** asset management, command system, scope selection, multiplayer security, ID constraints

## Summary
The discussion revolves around enhancing the accessibility of blueprint assets through a new command system and flags to specify different scopes (server, local, assets, world). The goal is to improve asset management and security, particularly in multiplayer environments.

## Explanation
The current method of accessing blueprint assets via relative paths is deemed inadequate due to the need to disallow `..` for security reasons. The proposed solution involves creating a new set of commands (`/sbb <load|store|list>`) with more restrictive access controls suitable for multiplayer scenarios. Additionally, flags like `--server`, `--local`, `--assets`, and `--world` are introduced to specify the scope of blueprint operations. These flags aim to address issues such as #1263 by enforcing ID constraints on asset paths. The discussion also mentions adding a `/blueprint move` command for relocating assets between different scopes, further enhancing asset management capabilities.

## Related Questions
- What are the proposed new commands for blueprint asset management?
- How do the `--server`, `--local`, `--assets`, and `--world` flags differ in their functionality?
- What is the motivation behind using IDs instead of paths for blueprint assets?
- How does the `/blueprint move` command fit into the proposed system?
- What are the security implications of allowing different scopes for blueprint operations?
- How will the new command system address issue #1263?
- Is there a plan to integrate player names into asset IDs, and why is it challenging?
- What are the potential benefits of using flags to specify scope in blueprint commands?

*Source: unknown | chunk_id: github_issue_1341_discussion*
