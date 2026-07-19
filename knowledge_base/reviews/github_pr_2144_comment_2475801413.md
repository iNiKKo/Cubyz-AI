# [src/zon.zig] - PR #2144 review diff

**Type:** review
**Keywords:** refactor, getChild, getChildOrNull, optional return, code duplication, readability
**Symbols:** ZonElement, object, get
**Concepts:** code refactoring, function simplification

## Summary
Refactored `getChild` and introduced `getChildOrNull` to improve clarity and reduce code duplication.

## Explanation
The refactoring simplifies the `getChild` function by leveraging a new `getChildOrNull` method, which returns an optional `ZonElement`. The `getChildOrNull` function checks if the current `ZonElement` is of type `.object` and then attempts to retrieve the element associated with the given key using `self.object.get(key)`. If the key exists, it returns the corresponding `ZonElement`; otherwise, it returns `null`. The original `getChild` function now uses `getChildOrNull` combined with `orelse .null` to return `.null` if `getChildOrNull` returns `null`. This change enhances readability and reduces redundancy in the code. The reviewer suggests that using `orelse .null` in both functions can further streamline the code while maintaining its functionality.

## Related Questions
- What is the purpose of the `getChildOrNull` function?
- How does the refactoring improve the clarity of the code?
- Why was it decided to use `orelse .null` in both functions?
- Does this change affect the performance of the ZonElement operations?
- Are there any potential regressions introduced by this refactoring?
- What is the impact on backward compatibility with existing code?

*Source: unknown | chunk_id: github_pr_2144_comment_2475801413*
