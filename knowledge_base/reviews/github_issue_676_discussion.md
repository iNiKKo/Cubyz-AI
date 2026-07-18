# [issues/issue_676.md] - Issue #676 discussion

**Type:** review
**Keywords:** issue_676.md, player momentum, sliding against block, intended behavior, refactoring #663
**Concepts:** refactoring, physics engine, player movement

## Summary
The player maintains forward momentum when sliding against a block, which was not intended.

## Explanation
The issue arises from the player's unexpected behavior while sliding against blocks. The maintainer suspects it might be an unintended side-effect of recent refactoring in pull request #663, suggesting that changes made during this refactoring could have altered the physics or movement logic related to player interactions with blocks.

## Related Questions
- What changes were made in pull request #663 that could affect player movement?
- Is there a specific part of the physics engine code that controls sliding against blocks?
- How does the current implementation handle player momentum during sliding actions?
- Are there any unit tests that cover this behavior, and if so, what are their results?
- Can we revert changes from #663 to see if it resolves the issue?
- Is there a configuration option that might control this behavior without code changes?

*Source: unknown | chunk_id: github_issue_676_discussion*
