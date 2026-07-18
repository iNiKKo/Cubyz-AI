# [issues/issue_180.md] - Issue #180 discussion

**Type:** review
**Keywords:** fog, density, cubemap, screenspace, noise map, player movement, overlay, shader, scrolling texture
**Concepts:** fog rendering, pixel density consistency, screenspace effects

## Summary
The issue discusses the challenge of making fog density consistent across front and back faces for each pixel, exploring potential solutions like density cubemaps or screenspace effects with noise maps.

## Explanation
The main problem is ensuring that the fog density remains uniform between front and back faces for a single pixel. This constraint limits the options to either using a density cubemap or implementing a screenspace effect. The reviewer suggests that while these methods might not look ideal due to their inability to respond correctly to player movement, a low-frequency noise map could be an acceptable compromise if updated every frame based on wind and player position. The maintainer proposes adding an overlay or shader with a scrolling texture as an alternative solution.

## Related Questions
- What are the limitations of using a density cubemap for fog rendering?
- How can screenspace effects with noise maps be updated every frame?
- What is the impact of player movement on fog density consistency?
- Can an overlay or shader with a scrolling texture improve fog rendering?
- What are the potential drawbacks of implementing a low-frequency noise map for fog density?
- How does the proposed solution in issue #193 address the fog rendering challenge?

*Source: unknown | chunk_id: github_issue_180_discussion*
