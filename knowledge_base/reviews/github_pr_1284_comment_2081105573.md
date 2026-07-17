# [src/blueprint.zig] - PR #1284 review diff

**Type:** review
**Keywords:** destructive mask, global mask, constructive mask, block modification, internal implementation, user command
**Symbols:** Blueprint, set, Pattern, Mask
**Concepts:** masking, command architecture, user interface design

## Summary
The `set` function in `Blueprint` now accepts an optional `mask` parameter, allowing for more granular control over which blocks are modified.

## Explanation
This change introduces a destructive mask to the `set` function, enabling it to modify only blocks that match the specified mask. This is an internal implementation detail and not exposed directly to users through the `/set` command. Instead, users can set a global mask that limits all commands. The review also mentions plans for a `/replace` command with a constructive mask, which will modify all blocks matching the mask, providing convenience for players by avoiding the need to invert masks manually. The `/replace` mask is intended to be local and per-command.

## Related Questions
- What is the purpose of the `mask` parameter in the `set` function?
- How does the global mask differ from the local mask for the `/replace` command?
- Can you explain the difference between destructive and constructive masks?
- Why was it decided to keep the `mask` parameter as an implementation detail?
- What are the potential performance implications of using a mask in block modification functions?
- How does this change affect backwards compatibility with existing commands?

*Source: unknown | chunk_id: github_pr_1284_comment_2081105573*
