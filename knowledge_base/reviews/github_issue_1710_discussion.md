# [issues/issue_1710.md] - Issue #1710 discussion

**Type:** review
**Keywords:** lava texture, inverted, back-face culling, debug mode, highest LOD, block determination
**Concepts:** LOD (Level of Detail), back-face culling, texture rendering

## Summary
The issue of inverted lava texture and back-face culling problems while inside lava blocks has been resolved.

## Explanation
The issue of inverted lava texture while inside lava blocks has been resolved by fixing an error in determining the block the player stands in when the highest LOD is set to 0. The maintainer noted that back-face culling was working as intended, meaning the backface of lava should be drawn since players can stick their heads inside it. Additionally, similar issues occur with water but only in debug mode. Sync points are unrelated to this bug and are caused by a different issue (#1708).

## Related Questions
- What was the original error causing the inverted lava texture?
- How did fixing the block determination error resolve the back-face culling issue?
- Are there any known issues with water rendering in debug mode?
- Was the fix for this issue specific to lava or applicable to other fluids as well?
- How does the LOD setting affect block determination in Cubyz?
- What is the significance of sync points in the game's thread main loop?
- Is back-face culling intended to be disabled for certain blocks like lava?

*Source: unknown | chunk_id: github_issue_1710_discussion*
