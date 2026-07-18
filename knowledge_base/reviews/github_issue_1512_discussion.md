# [issues/issue_1512.md] - Issue #1512 discussion

**Type:** review
**Keywords:** torch flame particle, animation adjustment, upwards velocity, block textures, frame consistency, LOD rendering
**Concepts:** animation, particle system, visual effects

## Summary
The discussion revolves around refining the torch flame particle's animation and appearance to improve its visual appeal and consistency with block textures.

## Explanation
The issue focuses on enhancing the torch flame particle by adjusting its animation, velocity, and texture properties. The user suggests that the flame should have a tiny upwards velocity and that the animation frames should be consistent in size (4x4 pixels). The maintainer agrees to adjust the animation accordingly. The discussion also touches on making the particles rarer as the player moves further away from the torch and ensuring they do not spawn during Level of Detail (LOD) rendering.

## Related Questions
- What is the current animation speed of the torch flame particle?
- How does the flame particle's appearance change with distance from the player?
- Is there a specific reason for making the particle frames 4x4 pixels in size?
- Does the updated animation maintain consistency with other block textures?
- How does the LOD rendering affect the visibility of the torch flame particles?
- What are the performance implications of adjusting the particle's upwards velocity?

*Source: unknown | chunk_id: github_issue_1512_discussion*
