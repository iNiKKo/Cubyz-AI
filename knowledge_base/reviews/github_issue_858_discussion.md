# [issues/issue_858.md] - Issue #858 discussion

**Type:** review
**Keywords:** lava, blue, green, transparent blocks, volumetric fog, unfixable, side effect, normal gameplay, Intel hardware, NVIDIA hardware
**Concepts:** volumetric fog, visual rendering

## Summary
The issue describes a visual anomaly where lava appears blue and green from inside when the player is inside of a block. The maintainer suggests that this is an unfixable side effect of volumetric fog calculation.

## Explanation
The discussion revolves around a visual bug in Cubyz, where the appearance of lava changes to blue and green when viewed from inside a block. The maintainer explains that this issue arises due to how volumetric fog is calculated within the game engine. They note that while it might not be addressed for normal gameplay, there are potential fixes for specific cases: #801 addresses the issue for lava, and #817 could resolve similar issues on Intel and NVIDIA hardware for other transparent blocks.

## Related Questions
- What is the cause of the blue and green appearance of lava from inside a block?
- How does volumetric fog calculation contribute to this visual anomaly?
- Are there any plans to fix this issue for normal gameplay?
- Which pull request addresses the issue for lava specifically?
- Can #817 resolve similar issues on other hardware platforms?
- What are the potential implications of leaving this issue unaddressed in normal gameplay?

*Source: unknown | chunk_id: github_issue_858_discussion*
