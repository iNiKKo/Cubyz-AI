# [src/game.zig] - PR #2381 review diff

**Type:** review
**Keywords:** refactor, rename, functions, secondary action, separate PR, contributing guidelines
**Symbols:** pressPlace, releasePlace, pressSecondary, releaseSecondary, Player.useItem, Player.placeBlock
**Concepts:** refactoring, naming conventions, consistency

## Summary
Refactored 'pressPlace' and 'releasePlace' functions to 'pressSecondary' and 'releaseSecondary'.

## Explanation
The change renames the existing block placement functions to more generic secondary action names. The reviewer emphasizes that this refactoring should be applied consistently across other similar functions, such as those related to breaking blocks, and suggests doing so in a separate pull request to maintain clear separation of changes.

## Related Questions
- What is the purpose of renaming 'pressPlace' to 'pressSecondary'?
- Why should the refactoring be applied consistently across other functions?
- How does this change affect the game's functionality?
- Are there any potential side effects from renaming these functions?
- What are the guidelines for submitting separate pull requests?
- How does this refactor align with the overall architecture of the game?

*Source: unknown | chunk_id: github_pr_2381_comment_2599274116*
