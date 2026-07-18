# [issues/issue_3202.md] - Issue #3202 discussion

**Type:** review
**Keywords:** replacement syntax, zon parsing, get method, optional type, null, hashmaps, _type, T, innerType, InnerType, Java
**Symbols:** ZonElement, get
**Concepts:** optional types, readability, backwards compatibility

## Summary
Proposes removing the 'replacement' syntax from zon parsing and changing the `get` method to return an optional type instead.

## Explanation
The proposal aims to simplify the `get` method by returning an optional type (`?_type`) instead of using a replacement parameter. This change aligns with the behavior of standard library functions like hashmaps, which return `null` if nothing is found. The reviewer suggests renaming `_type` to `T` and `innerType` in `.as` to `InnerType`. The maintainer notes that this pattern originates from Java, which lacks optional types.

## Related Questions
- What is the purpose of changing the `get` method to return an optional type?
- Why was the `_type` parameter renamed to `T`?
- How does this change align with standard library behavior?
- What are the potential implications for backwards compatibility?
- Is there a specific reason why the pattern originates from Java?
- How might this change affect code readability and maintainability?

*Source: unknown | chunk_id: github_issue_3202_discussion*
