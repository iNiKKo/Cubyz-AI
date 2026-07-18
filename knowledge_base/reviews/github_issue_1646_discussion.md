# [issues/issue_1646.md] - Issue #1646 discussion

**Type:** review
**Keywords:** black squares, distance, looking around, FPS limit, Render Distance, Highest LOD, Leaves Quality, Opaque leaves, FOV, bloom, V-sync, Anisotropic filtering, resolution scale
**Concepts:** bloom, pixel error, rendering artifact

## Summary
The issue involves black squares briefly appearing in the distance when looking around, which are attributed to pixel errors amplified by bloom.

## Explanation
The user reports experiencing black squares that appear briefly in the distance while playing Cubyz. The maintainer notes that these black squares are a result of pixel errors being exacerbated by the bloom effect. The discussion highlights the distinction between single-pixel errors and this more pronounced issue, suggesting that the problem is related to how bloom interacts with rendering artifacts.

## Related Questions
- What settings are most likely to cause pixel errors in Cubyz?
- How does bloom interact with rendering artifacts in Cubyz?
- Are there any known issues with the bloom effect in Cubyz that could cause this behavior?
- Can adjusting the render distance or LOD settings mitigate the appearance of black squares?
- What is the impact of V-sync on pixel errors and rendering artifacts in Cubyz?
- How does anisotropic filtering affect the visibility of pixel errors in Cubyz?
- Are there any other visual effects in Cubyz that could amplify pixel errors like bloom?
- What are the potential causes of black squares appearing briefly in the distance when looking around in Cubyz?
- Is this issue related to any specific hardware or driver configurations?
- How can developers debug and fix issues related to pixel errors and rendering artifacts in Cubyz?

*Source: unknown | chunk_id: github_issue_1646_discussion*
