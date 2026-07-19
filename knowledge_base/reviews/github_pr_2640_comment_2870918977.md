# [src/lang.zig] - PR #2640 review diff

**Type:** review
**Keywords:** StringHashMapUnmanaged, array, ZonMapEntry, filtering, performance, optimization, memory, management, data structures, hash map
**Symbols:** std, main, ZonElement, ZonMapEntry, Category, languages
**Concepts:** data structures, performance optimization, memory management

## Summary
The reviewer suggests using a `StringHashMapUnmanaged` instead of an array of `ZonMapEntry` for better performance and management.

## Explanation
The reviewer suggests using a `StringHashMapUnmanaged` instead of an array of `ZonMapEntry` for better performance and management. The reviewer points out that while `assets.zig` uses `StringHashMapUnmanaged`, the current implementation in `lang.zig` stores entries in an array. The reviewer questions why this approach is chosen, suggesting that using a map would be more efficient, especially if filtering is required. This change could improve performance by leveraging the optimized operations provided by hash maps. The reviewer specifically mentions that they only see `StringHashMapUnmanaged` being used in `assets.zig`, and they question why an array is used instead of a map in `lang.zig`. The explanation should clarify that the current implementation uses an array, and it does not explicitly state why this choice was made.

## Related Questions
- What are the advantages of using `StringHashMapUnmanaged` over an array in this context?
- How does filtering entries affect the decision to use a hash map?
- Can you explain the performance implications of using a hash map instead of an array?
- Why might the current implementation prefer using an array of `ZonMapEntry`?
- What are the potential memory usage differences between using a hash map and an array in this scenario?
- How does the choice of data structure impact the overall architecture of the module?

*Source: unknown | chunk_id: github_pr_2640_comment_2870918977*
