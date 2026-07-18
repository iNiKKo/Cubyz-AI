# [issues/issue_1365.md] - Issue #1365 discussion

**Type:** review
**Keywords:** thin ice, onTouch functions, velocity, fall damage translation, block breaking, lag concerns, issue #2938
**Concepts:** fall damage, block damage, lag

## Summary
Discussion on implementing thin ice in the game, focusing on how to handle fall damage translation to block damage.

## Explanation
The discussion revolves around addressing an issue where thin ice breaks when characters fall onto it with sufficient velocity. The maintainers propose translating fall damage into block damage to simulate this behavior, similar to how falling from a great height would break dirt blocks. They acknowledge that this could introduce lag but believe it is feasible with the implementation of another feature (issue #2938).

## Related Questions
- What is the proposed method for translating fall damage to block damage?
- How does the maintainers' idea address the issue of thin ice breaking under high velocity falls?
- What potential performance issues are mentioned in the discussion?
- Which other feature (issue) is required for implementing this solution?
- How does the proposed implementation compare to existing mechanics in the game?
- Are there any alternative methods suggested for handling thin ice breakage?

*Source: unknown | chunk_id: github_issue_1365_discussion*
