# [issues/issue_1512.md] - Issue #1512 discussion

**Type:** review
**Keywords:** torch flame particle, animation adjustment, upwards velocity, block textures, frame consistency, LOD rendering
**Concepts:** animation, particle system, visual effects

## Summary
The discussion revolves around refining the torch flame particle's animation and appearance to improve its visual appeal and consistency with block textures.

## Explanation
The discussion revolves around refining the torch flame particle's animation and appearance to improve its visual appeal. The user suggests that the flame should have a tiny upwards velocity and that each frame of the animation should be consistent in size at 4x4 pixels, matching block textures. The maintainer agrees to adjust the animation accordingly. Additionally, the flame particles become rarer as the player moves further away from the torch and do not spawn during Level of Detail (LOD) rendering. The user also suggests that the texture should go up instead of sideways, and that each frame goes down vertically.

## Related Questions
- What is the exact size of each frame in the torch flame particle's animation?
- How does the flame particle's appearance change with distance from the player?
- Does the updated animation maintain consistency with other block textures?
- How does LOD rendering affect the visibility of the torch flame particles?

*Source: unknown | chunk_id: github_issue_1512_discussion*
