# [issues/issue_2701.md] - Issue #2701 discussion

**Type:** review
**Keywords:** block rotation, data loss, function implementation, block type replacement, error handling
**Symbols:** replaceBlock, replaceBlockType
**Concepts:** block data preservation, function design

## Summary
The issue involves the loss of block data (like rotation) when using the `.replaceblocktype` function. The maintainer suggests adding a new `replaceBlockType` function to handle this scenario.

## Explanation
The current implementation of the `replaceBlock` function is converting blocks but losing their associated data such as rotation. This behavior is expected because `replaceBlock` is designed to replace the entire block, including its data. The maintainer proposes adding a new function, `replaceBlockType`, which will specifically handle the replacement of block types while preserving the existing block data. This change aims to provide more control over block transformations and prevent unintended data loss.

## Related Questions
- What is the current behavior of the replaceBlock function?
- How does the proposed replaceBlockType function differ from replaceBlock?
- Will adding replaceBlockType introduce any new errors or issues?
- Is there a risk of data loss with the new replaceBlockType function?
- How will the new function handle cases where rotation modes differ?
- What are the potential performance implications of adding this new function?

*Source: unknown | chunk_id: github_issue_2701_discussion*
