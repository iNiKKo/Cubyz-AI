# [issues/issue_1341.md] - Issue #1341 discussion

**Type:** review
**Keywords:** blueprint assets, relative paths, disallow `..`, new commands, access controls, flags, scopes, asset management, ID constraints, multiplayer security
**Symbols:** /blueprint load, /sbb <load|store|list>, --server, --local, --assets, --world, /blueprint move
**Concepts:** asset management, command system, scope selection, multiplayer security, ID constraints

## Summary
The discussion revolves around enhancing the accessibility of blueprint assets through a new command system and flags to specify different scopes (server, local, assets, world). The goal is to improve asset management and security, particularly in multiplayer environments.

## Explanation
The current method of accessing blueprint assets via relative paths is deemed inadequate due to security concerns related to disallowing `..`. The proposed solution involves creating a new set of commands (`/sbb <load|store|list>`) with more restrictive access controls suitable for multiplayer scenarios. Additionally, flags like `--server`, `--local`, `--assets`, and `--world` are introduced to specify the scope of blueprint operations. These flags aim to address issues such as #1263 by enforcing ID constraints on asset paths. The specific functionalities of these flags are as follows:
- `--server`/`-s`: This flag results in currently implemented behavior, using server-side `<cwd>/blueprints/` folder as the default.
- `--local`/`-l`: This flag uses local `<cwd>/blueprints/` folder regardless of whether you are on a remote server or localhost.
- `--assets`/`-a`: This flag allows accessing things in server-side `assets/<addon>/blueprints/` folder.
- `--world`/`-w`: This flag allows accessing things in server-side `<world>/assets/<addon>/blueprints/` folder. On localhost, `--server` and `--local` are the same thing.
The discussion also mentions adding a `/blueprint move` command for relocating assets between different scopes, further enhancing asset management capabilities.

## Related Questions
- What are the proposed new commands for blueprint asset management?
- How do the `--server`, `--local`, `--assets`, and `--world` flags differ in their functionality?
- What is the motivation behind using IDs instead of paths for blueprint assets?
- How does the `/blueprint move` command fit into the proposed system?

*Source: unknown | chunk_id: github_issue_1341_discussion*
