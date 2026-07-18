# [src/items.zig] - PR #2381 review diff

**Type:** review
**Keywords:** runtime data, loadtime data, hashmap, refactoring, architecture
**Symbols:** BaseItem, tooltip, onUse
**Concepts:** architectural consistency, data separation

## Summary
The reviewer suggests refactoring the `BaseItem` struct to separate runtime and loadtime data, similar to how it's handled for blocks.

## Explanation
The reviewer points out that mixing runtime and loadtime data within the same struct (`BaseItem`) is not ideal. They recommend using a hashmap to aggregate item zones, similar to the method employed for blocks. This change aims to improve architectural consistency and potentially enhance maintainability by clearly separating different types of data.

## Related Questions
- How is the `BaseItem` struct currently handling runtime and loadtime data?
- What specific method is used for blocks to aggregate item zones?
- Why is it important to separate runtime and loadtime data in the `BaseItem` struct?
- Can you provide an example of how a hashmap could be used to aggregate item zones in the `BaseItem` struct?
- What potential benefits might come from refactoring the `BaseItem` struct as suggested by the reviewer?
- How does this change impact the overall architecture of the Cubyz project?

*Source: unknown | chunk_id: github_pr_2381_comment_2637109731*
