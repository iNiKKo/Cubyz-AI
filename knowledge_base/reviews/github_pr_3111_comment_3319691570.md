# [src/blueprint.zig] - PR #3111 review diff

**Type:** review
**Keywords:** capture, swap, inclusivity, exclusivity, minPos, maxPos, Selection, Blueprint, Vec3i, NeverFailingAllocator
**Symbols:** Blueprint, CaptureResult, Vec3i, NeverFailingAllocator, Selection
**Concepts:** architectural review, correctness, clarity

## Summary
The review suggests removing a function that incorrectly swaps positions between two vectors due to mismatched inclusivity/exclusivity, recommending explicit field assignment instead.

## Explanation
The reviewer points out a critical architectural issue in the `capture` function within the `Blueprint` struct. The function attempts to swap positions between two vectors (`pos1` and `pos2`) without considering that one is inclusive and the other is exclusive, which can lead to incorrect behavior. The reviewer advises removing this function entirely and replacing it with a new method that explicitly assigns values to the `minPos` and `maxPos` fields of a newly defined `Selection` struct. This change aims to improve clarity and correctness by avoiding implicit assumptions about vector inclusivity/exclusivity.

## Related Questions
- What is the purpose of the `capture` function in the `Blueprint` struct?
- Why was the `capture` function deemed incorrect by the reviewer?
- How does the new `Selection` struct improve upon the original approach?
- What are the implications of removing the `capture` function?
- Can you explain the difference between inclusive and exclusive positions in this context?
- How should the `init` method of the `Selection` struct be used correctly?

*Source: unknown | chunk_id: github_pr_3111_comment_3319691570*
