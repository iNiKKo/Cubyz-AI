# [issues/issue_2158.md] - Issue #2158 discussion

**Type:** review
**Keywords:** tooltip, GUI components, manual assignment, optional arguments, Zig language, code clarity
**Symbols:** Label, Checkbox, Button
**Concepts:** GUI design, optional arguments, code clarity

## Summary
Discussion on adding a tooltip feature to GUI components, with consideration for manual assignment versus optional arguments.

## Explanation
The discussion revolves around the addition of tooltips to GUI components in Cubyz. The user suggests manually assigning tooltips after component initialization to avoid cluttering code with unnecessary null values. The maintainer proposes using Zig's optional argument functionality, either through struct field initialization or empty struct syntax, to provide flexibility without mandatory tooltip assignment.

## Related Questions
- How can tooltips be added to GUI components in Cubyz?
- What are the advantages of manually assigning tooltips after initialization?
- How does Zig's optional argument functionality apply to GUI component properties?
- Is there a preferred method for adding tooltips to avoid code clutter?
- Can tooltips be conditionally applied to specific GUI components?
- What is the impact on performance when using optional arguments in GUI components?

*Source: unknown | chunk_id: github_issue_2158_discussion*
