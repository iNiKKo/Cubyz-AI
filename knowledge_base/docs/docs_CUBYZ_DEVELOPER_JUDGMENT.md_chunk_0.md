# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 0

**Type:** documentation
**Keywords:** explicit code, predictable, allocator-conscious, magic, DRY, debugging-style response, design-review response, judgment patterns
**Symbols:** N/A
**Concepts:** overall review philosophy, response categorization

## Summary
This document is synthesized from all 649 real GitHub PR review threads in Cubyz's history. Its single biggest meta-pattern, and how to categorize a review response as debugging-style vs. design-review.

## Explanation
This document is synthesized from reading all 649 real GitHub PR review threads in this project's history (crunched into `github_reviews.jsonl`), not from raw code inspection -- an attempt to internalize the recurring judgment patterns Cubyz maintainers apply, so responses reflect how this specific project actually thinks, not generic "best practices." Every rule in this document is grounded in multiple independent real review threads, with PR numbers cited so any claim can be traced to its source.

The single biggest meta-pattern across all 649 reviews: this project strongly prefers explicit, predictable, allocator-conscious code over clever/generic/automatic solutions, even when the generic solution is more DRY. "Magic" is treated as a mild pejorative here. If unsure which of two approaches to suggest, the more explicit and more locally-reasoned-about one is usually the one this project's reviewers would pick.

Review response categorization: a debugging-style response applies when a change addresses a genuine bug or "why doesn't this work" problem -- broken/incorrect runtime behavior. A design-review response applies when the discussion is about a design, style, or architectural choice with no broken behavior involved (e.g. issue #3279's excessive Zig cache disk usage was explicitly treated as "not a bug per se," just something to optionally mitigate; PR #2682's SparseSet-vs-VirtualList revert was an architectural/pointer-stability tradeoff discussion, not a bug fix). Misreading a design preference as a bug report (or vice versa) leads to fixing something that was never broken, or dismissing a real defect as "just style."

## Related Questions
- What is the single biggest meta-pattern across Cubyz's 649 PR review threads?
- In a Cubyz code review, what's the difference between when a change should get a debugging-style response vs a design-review response?
- Why was issue #3279's excessive Zig cache disk usage not treated as a bug?
- What kind of tradeoff was PR #2682's SparseSet-vs-VirtualList revert?
- How does Cubyz feel about "magic"/implicit code versus explicit code?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_0*
