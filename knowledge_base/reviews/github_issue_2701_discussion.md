# [issues/issue_2701.md] - Issue #2701 discussion

**Type:** review
**Keywords:** block rotation, data loss, function implementation, block type replacement, error handling
**Symbols:** replaceBlock, replaceBlockType
**Concepts:** block data preservation, function design

## Summary
The issue involves the loss of block data (like rotation) when using the `.replaceblocktype` function. The maintainer suggests adding a new `replaceBlockType` function to handle this scenario.

## Explanation
The issue involves the loss of block data (like rotation) when using the `.replaceblocktype` function. The maintainer suggests adding a new `replaceBlockType` function to handle this scenario. The current implementation of the `replaceBlock` function is converting blocks but losing their associated data such as rotation. This behavior is expected because `replaceBlock` is designed to replace the entire block, including its data.

To reproduce the issue, you can use the provided test addon [replacetest.zip](https://github.com/user-attachments/files/25833353/replacetest.zip). The before and after images show that when a log is converted into a variant of a log using `replaceBlock`, its rotation data is lost.

The maintainer proposes adding a new function, `replaceBlockType`, which will specifically handle the replacement of block types while preserving the existing block data and printing an error if the rotation modes differ. This change aims to provide more control over block transformations and prevent unintended data loss.

The proposed `replaceBlockType` function would work as follows:
- It will replace only the block type, leaving the existing block data intact.
- If the rotation modes of the original and target blocks differ, it will print an error message to indicate that the replacement cannot be performed due to differing rotation modes.

## Related Questions
- What is the current behavior of the replaceBlock function?
- How does the proposed replaceBlockType function differ from replaceBlock?
- Will adding replaceBlockType introduce any new errors or issues?
- Is there a risk of data loss with the new replaceBlockType function?
- How will the new function handle cases where rotation modes differ?
- What are the potential performance implications of adding this new function?

*Source: unknown | chunk_id: github_issue_2701_discussion*
