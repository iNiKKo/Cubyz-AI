# [issues/issue_1678.md] - Issue #1678 discussion

**Type:** review
**Keywords:** Attack The Block!, ATB, damage split, hitbox, block intersection, size stat, optional slots, particles, crosshair highlighting, desynchronization, cursor mode switching
**Concepts:** damage distribution, hitbox, block intersection, tool radius, player control

## Summary
The discussion revolves around the implementation of an 'Attack The Block!' (ATB) feature that allows players to distribute damage across multiple blocks by aiming at their intersections. This system aims to provide more control and satisfaction in mining and tunneling.

## Explanation
The ATB feature introduces a new mechanic where player tools cast a 1.5x1.5x1.5 pixel hitbox when swung, distributing damage evenly across all blocks within this area. The main concern is ensuring that players can control their swings effectively without accidentally damaging unintended blocks. The maintainers propose adding a 'size' stat to tools, determined by the number of optional slots filled, which would affect the radius of attack. This feature is intended to balance precision and mining efficiency, with different tool sizes catering to various use cases. Additionally, visual aids like particles and crosshair highlighting are suggested to help players understand the area of effect. The maintainers also discuss potential issues such as desynchronization in block breaking due to grid size constraints and propose solutions like cursor mode switching for precision tools.

## Related Questions
- How does the damage distribution work in the ATB feature?
- What is the impact of the 'size' stat on tool behavior?
- How are players expected to control their swings with the new system?
- What visual aids are proposed to help players understand the area of effect?
- What potential issues arise from desynchronization in block breaking, and how are they addressed?
- How does the ATB feature balance precision and mining efficiency?

*Source: unknown | chunk_id: github_issue_1678_discussion*
