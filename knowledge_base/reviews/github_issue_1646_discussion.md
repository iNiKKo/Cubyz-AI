# [issues/issue_1646.md] - Issue #1646 discussion

**Type:** review
**Keywords:** black squares, distance, looking around, FPS limit, Render Distance, Highest LOD, Leaves Quality, Opaque leaves, FOV, bloom, V-sync, Anisotropic filtering, resolution scale
**Concepts:** bloom, pixel error, rendering artifact

## Summary
The issue involves black squares briefly appearing in the distance when looking around, which are attributed to pixel errors amplified by bloom.

## Explanation
The issue involves black squares briefly appearing in the distance when looking around, which are attributed to pixel errors amplified by bloom. The user reports experiencing this issue with the following settings: FPS limit set to 80, Render Distance set to 24, Highest LOD set to 5, Leaves Quality set to 4, Opaque leaves set to 200, FOV set to 120, bloom and V-sync enabled, 4x Anisotropic filtering, and a resolution scale of 100%. The maintainer notes that these black squares are a result of pixel errors being exacerbated by the bloom effect. The discussion highlights the distinction between single-pixel errors and this more pronounced issue, suggesting that the problem is related to how bloom interacts with rendering artifacts.

## Related Questions
- What specific settings (FPS limit, Render Distance, Highest LOD, Leaves Quality, Opaque leaves, FOV, V-sync, Anisotropic filtering, resolution scale) are most likely to cause pixel errors in Cubyz?
- How does bloom interact with rendering artifacts in Cubyz given the user's reported settings?

*Source: unknown | chunk_id: github_issue_1646_discussion*
