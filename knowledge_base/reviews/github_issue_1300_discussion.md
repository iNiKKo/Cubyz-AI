# [issues/issue_1300.md] - Issue #1300 discussion

**Type:** review
**Keywords:** gemstone, double damage, drop chance, durability, balance breaking, modifiers, opportunity cost, renaming
**Symbols:** white opal, Critstone
**Concepts:** game balance, modifier stacking, exploration

## Summary
The proposal discusses adding a white opal gemstone with specific physical and in-game properties. Maintainers suggest renaming it to 'Critstone' and adjusting its modifiers to avoid being overpowered.

## Explanation
The proposal discusses adding a new gemstone called **white opal** with specific physical and in-game properties. The physical properties include:

- Hardness: ~6 on Mohs scale
- Density: 2 g/cm3 at 20°C

In the game, white opal provides special effects instead of stats. Initially proposed modifiers included a chance to do double damage or increase drop chances, but maintainers expressed concerns about these being overpowered (OP). The suggestion was made to rename it to **Critstone** and adjust its behavior to reduce tool durability slightly while retaining the double damage effect.

Maintainers also argued against stacking additional penalties on gems due to the opportunity cost of replacing high-durability metal with low-durability gemstones, emphasizing that gems should have diverse uses for gameplay variety. The discussion highlights balance considerations in game design, focusing on small impact modifiers that can be creatively combined.

**Modifiers:**
- `luck` - chance to do double damage to block/entity (specifically 10% chance), to not lose durability or possibly double drop chance for rare things (apples?) or generally to double drops (5% chance).

**Spawn Rules:**
- `-3000 < Z < -300`
- Never spawns in veins

The proposal also mentions the historical superstition of opals providing luck and suggests alternative uses for the lucky modifier, such as increasing mob drops by 10% or giving a chance to dodge incoming damage (5%).

## Related Questions
- What are the spawn rules for white opal?
- What is the historical superstition associated with opals?

*Source: unknown | chunk_id: github_issue_1300_discussion*
