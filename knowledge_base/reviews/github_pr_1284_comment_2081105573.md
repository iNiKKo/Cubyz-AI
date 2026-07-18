# [src/blueprint.zig] - PR #1284 review diff

**Type:** review
**Keywords:** mask, destructive, constructive, block modification, user convenience, global mask, local mask
**Symbols:** Blueprint, set, Pattern, Mask
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The `set` function in `blueprint.zig` has been updated to accept an optional `mask` parameter, allowing for more granular control over which blocks are modified.

## Explanation
This change introduces a destructive mask into the `set` function, enabling it to modify only those blocks that match the specified mask. This is in contrast to the `/replace` command, which will have a constructive mask, modifying only blocks that meet certain criteria. The reviewer emphasizes that this distinction is crucial for user convenience and clarity, as players can set a global mask that affects all commands or use a local mask with specific commands like `/replace`. The architectural review highlights the importance of separating destructive and constructive operations to prevent unintended block modifications.

## Related Questions
- What is the purpose of the `mask` parameter in the updated `set` function?
- How does the destructive mask differ from the constructive mask mentioned for `/replace`?
- Can you explain the implications of using a global mask versus a local mask in Cubyz?
- What are the potential performance impacts of introducing an optional mask parameter to the `set` function?
- How does this change affect backwards compatibility with existing commands?
- Are there any thread safety concerns introduced by the new mask functionality?

*Source: unknown | chunk_id: github_pr_1284_comment_2081105573*
