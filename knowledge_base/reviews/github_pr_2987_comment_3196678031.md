# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** nullable, non-nullable, default capability, allocation, architectural review
**Symbols:** register, zon, SelectionRule, selectionCapabilities
**Concepts:** nullability, default values, code simplicity

## Summary
The change introduces a new variable `selectionCapabilities` and suggests using a default `.all` capability instead of a nullable value.

## Explanation
The reviewer recommends replacing the nullable `SelectionRule` with a non-nullable default capability, specifically `.all`. This change aims to simplify the code by avoiding null checks and potential allocation issues. The reviewer believes that using a default capability is more architecturally sound and easier to manage. Additionally, the reviewer suggests using `&.{.all}` without needing to do any allocation.

## Related Questions
- What is the purpose of the `selectionCapabilities` variable?
- Why does the reviewer prefer a `.all` capability over a nullable value?
- How does this change impact memory allocation in the code?
- Can you explain the benefits of using a default capability instead of nullability?
- What potential issues might arise from changing to a non-nullable default capability?
- How does this modification affect the overall architecture of the `blocks.zig` file?

*Source: unknown | chunk_id: github_pr_2987_comment_3196678031*
