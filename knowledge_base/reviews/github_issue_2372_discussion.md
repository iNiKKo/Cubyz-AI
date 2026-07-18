# [issues/issue_2372.md] - Issue #2372 discussion

**Type:** review
**Keywords:** organization, folder structure, Zig files, nesting, import redundancy, module nesting
**Symbols:** network.zig, server.zig, items.zig, renderer.zig, utils.zig
**Concepts:** file organization, module structure, import paths

## Summary
Discussion on organizing Zig files by moving them into folders of the same name, with a preference for nesting structure.

## Explanation
The discussion revolves around whether to move specific Zig files (like network.zig) into folders named after themselves. The maintainer notes uncertainty about the best approach and seeks input on the reasoning behind different organizational strategies. A user prefers organizing files such that the main file resides in the root directory while components are placed in subdirectories, mirroring module nesting. This approach avoids redundancy in imports, such as `network/network.zig`, which the user finds odd.

## Related Questions
- What are the potential benefits of organizing Zig files by moving them into folders of the same name?
- How does the proposed file organization affect import paths in a Zig project?
- Can you provide examples of how other projects handle similar file organization issues in Zig?
- What are the trade-offs between having main files in the root directory and components in subdirectories versus keeping all related files in one folder?
- How might this change impact backwards compatibility with existing Zig projects?
- Are there any performance implications associated with different file organization strategies in Zig?

*Source: unknown | chunk_id: github_issue_2372_discussion*
