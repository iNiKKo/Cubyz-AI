# [issues/issue_1722.md] - Issue #1722 discussion

**Type:** review
**Keywords:** replace, rotation, flag, set, behavior, block
**Concepts:** Command Behavior, Block Rotation

## Summary
The `/replace` command loses block rotation states during execution. A discussion suggests adding a flag to optionally preserve these states.

## Explanation
The current implementation of the `/replace` command in Cubyz does not retain the rotation states of blocks, which can lead to unexpected behavior when replacing blocks with similar rotations. The maintainer acknowledges that while this behavior is not always desirable, it could be useful to have an option to preserve these states. This discussion also extends to considering similar changes for the `/set` command.

## Related Questions
- What is the current behavior of the `/replace` command regarding block rotations?
- How can we implement a flag to preserve block rotation states during the `/replace` command execution?
- Are there any potential side effects of adding such a flag to the `/replace` command?
- Should similar changes be considered for the `/set` command as well?
- What are the architectural implications of modifying the `/replace` command to include an optional flag for rotation preservation?
- How can we ensure that the new flag does not introduce any regressions in the command's functionality?

*Source: unknown | chunk_id: github_issue_1722_discussion*
