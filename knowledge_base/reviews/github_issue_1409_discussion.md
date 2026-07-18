# [issues/issue_1409.md] - Issue #1409 discussion

**Type:** review
**Keywords:** grass heights, texture_pile rotation, two-tall grass, collision, block size, model pile, gras_vegetation
**Concepts:** texture_pile, collision assumptions, model pile

## Summary
Discussion on implementing varying grass heights and two-tall grass in Cubyz, focusing on texture_pile rotation and potential architectural changes.

## Explanation
The discussion revolves around the implementation of varying grass heights using texture_pile rotation. The user suggests having two distinct heights within a single block space and two heights spanning two blocks. Maintainers express concerns about collision assumptions and the complexity of extending blocks beyond their standard size. The user proposes treating the first two stages like texture_pile and introducing a third stage that changes to a separate block/model for two-tall grass, which would drop three grass_vegetation items when broken. Maintainers suggest revisiting the idea of a model pile, which is planned but not yet implemented.

## Related Questions
- How does the current implementation of texture_pile handle varying heights?
- What are the potential architectural changes needed for two-tall grass?
- Are there any existing plans or implementations for a model pile in Cubyz?
- How would collision detection be affected by extending blocks beyond their size?
- What is the impact on performance when implementing multiple states for grass?
- How can the third stage of grass be designed to drop three items upon breaking?
- Are there any backward compatibility concerns with introducing new grass states?
- What are the potential user benefits of having varying grass heights and two-tall grass?
- How would the current collision system need to be modified for this feature?
- Is there a way to optimize the rendering of multiple grass states within a single block?

*Source: unknown | chunk_id: github_issue_1409_discussion*
