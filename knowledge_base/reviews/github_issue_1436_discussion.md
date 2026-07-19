# [issues/issue_1436.md] - Issue #1436 discussion

**Type:** review
**Keywords:** rename, collision detection, parameter naming, adjective consistency, verb inconsistency
**Symbols:** collide, solid, hasCollision
**Concepts:** naming conventions, consistency

## Summary
Discussion about renaming the `collide` parameter to `solid` or `hasCollision` in Cubyz.

## Explanation
Discussion about renaming the `collide` parameter to `solid` or `hasCollision` in Cubyz. The maintainers initially suggest renaming from `collide` to `solid`, but they are concerned that 'solid' could be ambiguous as it can refer to the state of matter, not just the ability to collide (e.g., mushrooms are solid as a matter state but do not collide). Another maintainer points out that `collide` is a verb while other properties are adjectives, suggesting inconsistency. A user proposes `hasCollision` as an alternative, which aligns with using adjectives for all properties.

## Related Questions
- What are the potential implications of renaming `collide` to `solid` in Cubyz?
- Why is there a concern about the ambiguity of the term 'solid' in this context?
- How does the use of verbs and adjectives for parameter names affect code readability?
- What alternative naming suggestions have been made for the collision detection parameter?
- Can you explain the reasoning behind maintaining consistency in property naming conventions?
- How might renaming parameters impact existing codebase compatibility?

*Source: unknown | chunk_id: github_issue_1436_discussion*
