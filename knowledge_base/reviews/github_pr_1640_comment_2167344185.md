# [src/items.zig] - PR #1640 review diff

**Type:** review
**Keywords:** BaseItemIndex, enum, no_value, optional, memory cost, alignment, in-memory storage, in-file storage, networking, bug prevention
**Symbols:** BaseItemIndex, MaterialProperty, no_value
**Concepts:** optional handling, memory usage, code clarity, architectural design

## Summary
The review suggests changing `BaseItemIndex` from a packed struct with an index field to an enum with a `no_value` variant. The reviewer emphasizes that using an enum is more explicit about optionality and avoids potential bugs by requiring checks in every use case.

## Explanation
The architectural change involves replacing a packed struct with a single u16 field with an enum type that includes a `no_value` variant. This change aims to improve code clarity and correctness by making the optional nature of the index explicit. The reviewer points out that while using an `optional` type would add 25 extra bytes per tool, which could be concerning for in-memory storage, it does not affect alignment issues as previously thought. For in-file storage or networking, other compression methods can be employed. The primary advantage of this change is the explicit handling of optionality, reducing the risk of bugs related to uninitialized or invalid indices.

## Related Questions
- What are the potential performance implications of using an enum with a `no_value` variant instead of a packed struct?
- How does the change impact memory usage for in-memory storage?
- Can you provide examples of how to check for `no_value` in different use cases?
- What are the benefits and drawbacks of using `optional` versus `no_value` in this context?
- How does this change affect compatibility with existing code that uses `BaseItemIndex`?
- Are there any specific alignment issues to consider when changing from a packed struct to an enum?

*Source: unknown | chunk_id: github_pr_1640_comment_2167344185*
