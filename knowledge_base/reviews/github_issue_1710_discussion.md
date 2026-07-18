# [issues/issue_1710.md] - Issue #1710 discussion

**Type:** review
**Keywords:** lava texture, inverted, back-face culling, debug mode, highest LOD, block determination
**Concepts:** LOD (Level of Detail), back-face culling, texture rendering

## Summary
The issue of inverted lava texture and back-face culling problems while inside lava blocks has been resolved.

## Explanation
The problem was caused by an error in determining the block the player stands in when the highest LOD is set to 0. This error has been fixed, which resolves both the inverted lava texture issue and the back-face culling problem. The maintainer also noted that similar issues occur with water but only in debug mode.

## Related Questions
- What was the original error causing the inverted lava texture?
- How did fixing the block determination error resolve the back-face culling issue?
- Are there any known issues with water rendering in debug mode?
- Was the fix for this issue specific to lava or applicable to other fluids as well?
- How does the LOD setting affect block determination in Cubyz?
- What is the significance of sync points in the game's thread main loop?
- Is back-face culling intended to be disabled for certain blocks like lava?
- Can the fix for this issue be applied to similar rendering problems in other parts of the game?
- How does updating to the latest commit resolve the reported issues?
- Are there any performance implications from fixing the block determination error?

*Source: unknown | chunk_id: github_issue_1710_discussion*
