# [issues/issue_1678.md] - Issue #1678 discussion

**Type:** review
**Keywords:** Attack The Block!, ATB, damage split, hitbox, block intersection, size stat, optional slots, particles, crosshair highlighting, desynchronization, cursor mode switching
**Concepts:** damage distribution, hitbox, block intersection, tool radius, player control

## Summary
The discussion revolves around the implementation of an 'Attack The Block!' (ATB) feature that allows players to distribute damage across multiple blocks by aiming at their intersections. This system aims to provide more control and satisfaction in mining and tunneling.

## Explanation
The discussion revolves around implementing an 'Attack The Block!' (ATB) feature that allows players to distribute damage across multiple blocks by aiming at their intersections. This system introduces a new mechanic where player tools cast a 1.5x1.5x1.5 pixel hitbox when swung, distributing damage evenly across all blocks within this area. If one of the blocks is going to be destroyed, the leftover damage is automatically distributed to other blocks in the hitbox.

The main concern is ensuring that players can control their swings effectively without accidentally damaging unintended blocks. The maintainers propose adding a 'size' stat to tools, which determines the radius of attack based on how many optional slots are filled in the tool. Each additional slot adds 0.5 to the size count, with default size being 1x (4 pixels). Larger sizes like x2 or x3 can be achieved by filling more slots.

The 'size' stat is displayed as a multiplier in the tooltip when hovering over the crafting menu icons, e.g., "Size: x1" for default size. Players can change the tool's radius using this stat and are provided with visual aids like particles to indicate where block damage occurs. Puff particles show the area of the hitbox while sparkle or slash particles display normal damage.

To help players understand the mechanic, a box around the crosshair highlights every block that will be affected when wielding a tool. This system aims to balance precision and mining efficiency by allowing different sizes for various use cases (e.g., 0.25x for precise work, 1x for standard tools, and 2.5x for tunnelling). Additionally, cursor mode switching is proposed to switch between single-target damage and area-of-effect modes.

Potential issues such as desynchronization in block breaking due to grid size constraints are addressed by visual aids like crosshair highlighting and particle effects.

## Related Questions
- How does the damage distribution work in the ATB feature?
- What is the exact size of the hitbox cast when swinging a tool?
- How is the 'size' stat calculated based on optional slots filled?
- How are players expected to control their swings with the new system?
- What visual aids are proposed to help players understand the area of effect?
- What potential issues arise from desynchronization in block breaking, and how are they addressed?
- How does the ATB feature balance precision and mining efficiency?

*Source: unknown | chunk_id: github_issue_1678_discussion*
