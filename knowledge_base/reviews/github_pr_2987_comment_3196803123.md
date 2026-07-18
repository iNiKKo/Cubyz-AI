# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** selection rule, default case, .all, redundant, architectural review
**Symbols:** register, zon, SelectionRule, SelectionCapability
**Concepts:** default behavior, configuration redundancy

## Summary
The change introduces a new variable `selectionCapabilities` and modifies the handling of the default selection rule.

## Explanation
The reviewer suggests that setting the default selection rule to `.all` when unspecified might be clearer. However, they also point out that allowing `.all` in the configuration could be redundant. The architectural concern here is ensuring that the default behavior is intuitive and that configurations do not introduce unnecessary complexity.

## Related Questions
- What is the purpose of introducing `selectionCapabilities`?
- Why is there a concern about redundancy in the configuration?
- How does this change affect the default selection rule behavior?
- Is there any potential impact on performance or correctness with this modification?
- What are the implications for backwards compatibility?
- Could this change lead to any unintended side effects?
- How should the reviewer's suggestion be implemented?
- Are there any other architectural considerations that need to be addressed?
- What is the expected behavior if `.all` is specified in the configuration?
- How does this modification align with the overall design goals of Cubyz?

*Source: unknown | chunk_id: github_pr_2987_comment_3196803123*
