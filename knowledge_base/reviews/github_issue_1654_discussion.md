# [issues/issue_1654.md] - Issue #1654 discussion

**Type:** review
**Keywords:** tooltip, damage calculation, good at modifier, percentage boost, total damage, function signature, Tool object
**Symbols:** printTooltip, Tool
**Concepts:** User Interface, Code Refactoring, Function Signature Modification

## Summary
The issue requests modifying the `printTooltip()` function to display both percentage boost and total damage for 'good at' modifiers in tooltips.

## Explanation
The current implementation of the `printTooltip()` function only shows the percentage boost provided by 'good at' modifiers. The user suggests enhancing this tooltip to include the actual damage value, making it easier to understand the impact without needing a calculator. This change involves modifying the function signature to accept a Tool object as a parameter, allowing access to necessary attributes for calculating and displaying the total damage.

## Related Questions
- What is the current behavior of the `printTooltip()` function?
- How will modifying the function signature impact existing code?
- What attributes of the Tool object are necessary for calculating total damage?
- How should the tooltip be formatted to include both percentage and total damage?
- Are there any potential performance implications of this change?
- How can we ensure that the new implementation maintains backwards compatibility?

*Source: unknown | chunk_id: github_issue_1654_discussion*
