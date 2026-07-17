# [src/items.zig] - PR #2381 review diff

**Type:** review
**Keywords:** runtime data, loadtime data, struct refactoring, hashmap, blocks, separation of concerns
**Symbols:** BaseItem, tooltip, onUse
**Concepts:** architectural design, data separation, hashmap usage

## Summary
The reviewer suggests refactoring the `BaseItem` struct to separate runtime and loadtime data, similar to how it's handled for blocks.

## Explanation
The reviewer is concerned about mixing runtime and loadtime data within the same struct (`BaseItem`). They propose using a hashmap to aggregate item zones, similar to the method used for blocks. This change aims to improve architectural clarity and separation of concerns, preventing potential issues related to data management and ensuring that the system remains maintainable and scalable.

## Related Questions
- What is the current method for handling item zones in Cubyz?
- How does the proposed hashmap solution differ from the existing approach?
- Are there any potential performance implications of using a hashmap for item zones?
- Can you provide examples of how similar refactoring has been applied to other parts of the codebase?
- What are the benefits of separating runtime and loadtime data in the `BaseItem` struct?
- How does this change impact backwards compatibility with existing Cubyz versions?

*Source: unknown | chunk_id: github_pr_2381_comment_2637109731*
