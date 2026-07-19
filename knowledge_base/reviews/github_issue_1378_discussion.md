# [issues/issue_1378.md] - Issue #1378 discussion

**Type:** review
**Keywords:** cubyz:, Pattern, Mask, expressions, inference, autocomplete, complexity, ambiguity, IDs, addon names
**Concepts:** prefix inference, autocomplete, ID parsing

## Summary
The proposal to infer the `cubyz:` prefix in Pattern and Mask expressions was rejected due to concerns about added complexity and edge cases.

## Explanation
The proposal to infer the `cubyz:` prefix in Pattern and Mask expressions was rejected due to concerns about added complexity and potential ambiguity. The maintainer of Cubyz noted that IDs can be identified unambiguously without the `cubyz:` prefix because there is only one 'stone' ID, which is `cubyz:stone`. However, the proposal introduces a disadvantage where in expressions without an addon name data segment must also be omitted to avoid misinterpreting block IDs as addon names. The maintainer suggests revisiting this issue after implementing autocomplete features.

## Related Questions
- What specific ID is mentioned as an example of unambiguous identification?
- What is the disadvantage of inferring the `cubyz:` prefix in expressions without an addon name?

*Source: unknown | chunk_id: github_issue_1378_discussion*
