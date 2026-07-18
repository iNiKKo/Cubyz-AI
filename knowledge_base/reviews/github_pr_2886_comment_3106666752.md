# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** blockTags, tags, bulk replacements, renaming, global variables, simplification
**Symbols:** _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _tags, Tag
**Concepts:** naming conventions, code readability

## Summary
Renamed `_blockTags` array to `_tags` in `blocks.zig`, removing the redundant 'block' prefix.

## Explanation
The change involves renaming a global variable from `_blockTags` to `_tags`. The reviewer approves of this modification, as it simplifies the naming by removing the redundant 'block' prefix. However, the reviewer cautions about being careful with bulk replacements to avoid unintended changes in similar contexts.

## Related Questions
- What is the purpose of the `_tags` array in `blocks.zig`?
- How does removing the 'block' prefix from `_blockTags` improve code readability?
- Are there any potential risks associated with bulk replacements in this context?
- Can you provide examples of other similar global variables that might benefit from renaming?
- What is the impact of this change on backward compatibility?
- Is there a specific reason for choosing `_tags` as the new variable name?

*Source: unknown | chunk_id: github_pr_2886_comment_3106666752*
