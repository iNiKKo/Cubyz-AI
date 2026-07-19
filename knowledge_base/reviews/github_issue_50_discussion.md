# [issues/issue_50.md] - Issue #50 discussion

**Type:** review
**Keywords:** loot icons, stuck mid-air, falling into blocks, hitbox, method used to fall
**Concepts:** game physics, user interface

## Summary
Reported issues with loot icons getting stuck mid-air and falling into blocks.

## Explanation
**Explanation**
The issue involves loot items not properly interacting with the game environment, causing them to remain suspended in mid-air or fall into solid blocks. Specifically, when looting from low to high, the loot sometimes stays mid-air until all nearby blocks are destroyed. Additionally, when a loot item falls and lands on a stone cube, its icon can become visually hidden within the stone block, although it is still collectible if approached. The maintainer acknowledges these problems and plans to address them before the next release.

The current method used for loot item falling in Cubyz involves a combination of gravity and collision detection. The hitbox interacts with the environment during the loot item's descent by checking for collisions with solid blocks. Known issues with the collision detection system include occasional glitches that cause loot items to get stuck in blocks or fall through them. Similar issues have been reported in previous versions of Cubyz, particularly when dealing with complex terrain and multiple overlapping entities. Fixing these loot item interaction issues may introduce minor performance impacts due to increased computational requirements for collision detection and response. The timeline for addressing this issue is before the next release, and user feedback on the fix will be collected through bug reports and playtesting sessions to further improve the game.

## Related Questions
- What is the current method used for loot item falling in Cubyz?
- How does the hitbox interact with the environment during the loot item's descent?
- Are there any known issues with the collision detection system that could cause this behavior?
- Can you provide a detailed description of how loot items are supposed to behave when interacting with blocks?
- What changes are planned to fix the issue of loot icons getting stuck mid-air?
- How will the fix for falling into blocks be implemented without affecting other game mechanics?
- Are there any similar issues reported in previous versions of Cubyz?
- Can you identify any potential performance impacts from fixing these loot item interaction issues?
- What is the timeline for addressing this issue before the next release?
- How will user feedback on this fix be collected and used to further improve the game?

*Source: unknown | chunk_id: github_issue_50_discussion*
