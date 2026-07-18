# [issues/issue_1378.md] - Issue #1378 discussion

**Type:** review
**Keywords:** cubyz:, Pattern, Mask, expressions, inference, autocomplete, complexity, ambiguity, IDs, addon names
**Concepts:** prefix inference, autocomplete, ID parsing

## Summary
The proposal to infer the `cubyz:` prefix in Pattern and Mask expressions was rejected due to concerns about added complexity and edge cases.

## Explanation
The maintainer of Cubyz rejected the proposal to automatically infer the `cubyz:` prefix in Pattern and Mask expressions, citing that it would introduce unnecessary complexity and potential ambiguity. The primary concern is that without autocomplete functionality, users might misinterpret IDs as addon names, leading to errors. The maintainer suggests revisiting this issue after implementing autocomplete features.

## Related Questions
- What is the primary reason for rejecting the prefix inference proposal?
- How does autocomplete relate to the decision on prefix inference?
- What potential issues arise from inferring the `cubyz:` prefix?
- When might Cubyz revisit the prefix inference issue?
- What are the benefits of having autocomplete in Cubyz?
- How could the current ID parsing logic be improved without adding complexity?

*Source: unknown | chunk_id: github_issue_1378_discussion*
