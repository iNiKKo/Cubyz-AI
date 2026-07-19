# [issues/issue_1710.md] - Issue #1710 discussion

**Type:** review
**Keywords:** lava texture, inverted, back-face culling, debug mode, highest LOD, block determination
**Concepts:** LOD (Level of Detail), back-face culling, texture rendering

## Summary
The issue of inverted lava texture and back-face culling problems while inside lava blocks has been resolved.

## Explanation
The issue of inverted lava texture and back-face culling problems while inside lava blocks has been resolved by fixing an error in determining the block the player stands in when the highest LOD is set to 0. The original error causing the inverted lava texture was that the block you stand in was incorrectly determined, leading to the texture appearing inverted. Fixing this error resolved the back-face culling issue because it ensured that the correct block was identified, allowing for proper rendering of the lava's front and back faces. Additionally, similar issues occur with water but only in debug mode. Sync points are unrelated to this bug and are caused by a different issue (#1708). The LOD setting affects block determination by influencing how detailed the blocks are rendered; when set to 0, it can lead to errors in determining which block the player is standing in. Back-face culling is intended to be enabled for all blocks, including lava, to prevent rendering of faces that are not visible to the player.

## Related Questions
- What was the original error causing the inverted lava texture?
- How did fixing the block determination error resolve the back-face culling issue?
- Are there any known issues with water rendering in debug mode?
- Was the fix for this issue specific to lava or applicable to other fluids as well?
- How does the LOD setting affect block determination in Cubyz?
- What is the significance of sync points in the game's thread main loop?
- Is back-face culling intended to be disabled for certain blocks like lava?

*Source: unknown | chunk_id: github_issue_1710_discussion*
