# [issues/issue_3274.md] - Issue #3274 discussion

**Type:** review
**Keywords:** Hide Wand, Creative Mode, Ghost Mode, block hiding, server-side physics, collision detection
**Concepts:** client-server architecture, user interface design, game mechanics

## Summary
Discussion about adding a 'Hide Wand' feature in Creative Mode, which allows hiding blocks without breaking them.

## Explanation
Discussion about adding a 'Hide Wand' feature in Creative Mode, which allows players to hide blocks temporarily for easier navigation within structures without breaking them. The Hide Wand has the following functions:
- **Left-Click:** Use wand
- **Right-Click:** Cycle function
The specific cycle includes: 
- **Hide 1x1:** Hides the selected block.
- **Hide 3x3:** Hides a 3³ volume around the selected block.
- **Hide Connected:** Hides the selected block and all touching blocks of its type, up to 16 blocks at a time.
- **Unhide All:** Unhides all hidden blocks.
The primary concern raised is the potential conflict with existing features like Ghost Mode and how it interacts with server-side physics, particularly block hitboxes. Hidden blocks are treated exactly like air blocks and leave persistent emissive particles in their place. Additionally, they can be replaced by other blocks without breaking them. There's also a suggestion to consider adding more functionality to Ghost Mode instead of implementing the Hide Wand.

## Related Questions
- How does the Hide Wand interact with server-side block hitboxes?
- What are the potential use cases for the Hide Wand in Creative Mode?
- How could Ghost Mode be enhanced to address similar needs as the Hide Wand?
- What are the implications of adding client-side tools like the Hide Wand on multiplayer gameplay?
- Can the Hide Wand feature be extended to Survival Mode, and if so, how?
- How does the Hide Wand affect block replacement mechanics in the game?

*Source: unknown | chunk_id: github_issue_3274_discussion*
