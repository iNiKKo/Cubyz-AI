# [issues/issue_2696.md] - Issue #2696 discussion

**Type:** review
**Keywords:** tool damage, rounding, integers, tooltip, block breaking speed
**Concepts:** user-friendliness, gameplay balance

## Summary
Discussion about applying rounding to tool damage numbers in Cubyz.

## Explanation
Discussion about applying rounding to tool damage numbers in Cubyz. The issue revolves around whether tool damage numbers should be integers or rounded to make gameplay more user-friendly. A maintainer suggests that even rounding up to one decimal would be beneficial, without specifying if it is for tooltips or actual game mechanics. Another maintainer asks if this rounding is intended for tooltips or actual game mechanics. Rounding could potentially improve the user-friendliness of the game by making tool damage numbers more intuitive and less prone to min-maxing. However, it could also affect the precision of block breaking calculations, as rounding might introduce small discrepancies in damage output. There are no existing issues with the current implementation of tool damage numbers, but there is a debate about whether rounding would be beneficial for gameplay balance. Rounding could introduce unintended side effects in game mechanics, such as making certain builds more advantageous than others. To ensure consistency across different parts of the game, any changes to tool damage numbers should be carefully implemented and thoroughly tested.

## Related Questions
- What are the potential impacts of rounding tool damage numbers on gameplay?
- How would rounding affect the precision of block breaking calculations?
- Are there any existing issues with the current implementation of tool damage numbers?
- What is the rationale behind keeping tool damage numbers as integers?
- Could rounding introduce any unintended side effects in the game mechanics?
- How would rounding be implemented to ensure consistency across different parts of the game?

*Source: unknown | chunk_id: github_issue_2696_discussion*
