# [issues/issue_272.md] - Issue #272 discussion

**Type:** review
**Keywords:** up direction, z-axis, y-axis, terrain generation, intuitive, common standard
**Concepts:** coordinate system, terrain generation

## Summary
Discussion about changing the up direction from y to z in Cubyz.

## Explanation
The discussion revolves around whether the 'up' direction should be represented by the z-axis instead of the current y-axis. The user suggests that using z as the up/down axis could make terrain generation more intuitive, aligning with common standards where z is typically used for vertical movement. This change would involve iterating over x and z rather than x and y, which might simplify certain aspects of terrain generation. However, there are potential impacts on existing terrain generation code, user experience, and gameplay that need to be considered. The benefits and drawbacks of this change should also be thoroughly evaluated to ensure compatibility with existing plugins or mods.

## Related Questions
- What are the potential impacts on existing terrain generation code if z is made the up axis?
- How would changing the up direction affect user experience and gameplay?
- Are there any other parts of the codebase that might need to be updated to accommodate this change?
- What are the benefits and drawbacks of using z as the up axis in Cubyz?
- How does this change align with industry standards for 3D coordinate systems?
- Would changing the up direction introduce any compatibility issues with existing plugins or mods?

*Source: unknown | chunk_id: github_issue_272_discussion*
