# [issues/issue_1365.md] - Issue #1365 discussion

**Type:** review
**Keywords:** thin ice, onTouch functions, velocity, fall damage translation, block breaking, lag concerns, issue #2938
**Concepts:** fall damage, block damage, lag

## Summary
Discussion on implementing thin ice in the game, focusing on how to handle fall damage translation to block damage.

## Explanation
The discussion centers around implementing thin ice in the game where it breaks when players fall onto it with enough velocity. The maintainers propose translating fall damage into block damage to simulate this behavior, similar to how falling from a great height would break dirt blocks. Additionally, the surface of water freezes into thin ice in freezing biomes and can be melted back into water using heat sources. Thin ice can also be crafted into regular ice which cannot melt for building purposes. The maintainers acknowledge that this could introduce lag but believe it is feasible with the implementation of another feature (issue #2938).

## Related Questions
- What are the specific conditions under which thin ice forms and melts?
- How can thin ice be crafted into regular ice, and what properties does regular ice have?

*Source: unknown | chunk_id: github_issue_1365_discussion*
