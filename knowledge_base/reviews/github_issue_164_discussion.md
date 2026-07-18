# [issues/issue_164.md] - Issue #164 discussion

**Type:** review
**Keywords:** lighting issue, 3×3 surrounding region, GPU, AO effect, 3D texture interpolation, VRAM usage
**Concepts:** lighting, voxel models, GPU, Ambient Occlusion

## Summary
The lighting issue on voxel models is addressed by supplying a full 3×3 surrounding region of lights to the GPU. A previous solution involving 3D texture interpolation was explored but found unsatisfactory due to the AO effect being too thin.

## Explanation
The original problem stems from the lack of comprehensive light data supplied to the GPU, which results in incorrect lighting calculations for voxel models. The proposed solution involves sending a larger volume of light data (3×3 surrounding region) to ensure accurate lighting. However, an earlier attempt using 3D texture interpolation was deemed inadequate because it failed to produce satisfactory Ambient Occlusion (AO) effects, leading to visually thin AO boundaries.

## Related Questions
- What is the current method for supplying light data to the GPU?
- Why was the 3×3×3 surrounding light data approach chosen over other methods?
- How does the AO effect impact the visual quality of the lighting?
- What are the potential performance implications of sending a larger volume of light data to the GPU?
- Is there an alternative solution that balances between VRAM usage and visual quality?
- How can the 3D texture interpolation method be improved to achieve better AO effects?

*Source: unknown | chunk_id: github_issue_164_discussion*
