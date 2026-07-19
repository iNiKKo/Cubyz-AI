# [issues/issue_2154.md] - Issue #2154 discussion

**Type:** review
**Keywords:** grappling hook, propulsion, charge mode, attack mode, ropes, ammunition, crafting pattern
**Symbols:** grappling hook, rope
**Concepts:** player movement, mechanics integration, crafting recipe

## Summary
The grappling hook proposal introduces a hybrid tool and weapon for player movement in Cubyz, with modes for attacking and propelling. The discussion suggests integrating ropes as ammunition to address potential conflicts with existing mechanics and simplify the crafting recipe.

## Explanation
The grappling hook is a hybrid tool and weapon designed to enhance player mobility in Cubyz by allowing them to attach to walls or entities and propel themselves. The proposal outlines two main modes: a left-click attack mode that deals damage (1-5) and returns immediately, and a right-click charge mode that propels the player towards targets with a charge speed of 0.2 seconds. When the grappling hook reaches its maximum charge, releasing the right click throws it in the direction the player is facing, dealing damage to whatever it hits (be it a mob or block) and initiating propulsion power of 10. If the grappling hook hooks a mob, the player can right-click to propel themselves toward the grappling mob or left-click to pull the mob toward the player. If it hooks a block, right-clicking pulls the player toward the block and releases the grappling hook; if left-clicking the block is enough, the block is mined if the grappling hook has enough 'mining power.' The grappling hook's cooldown lasts until the player touches the grappling hook and is able to use it again. If the grappling hook is attached to something while switching to another item, it is released and the cooldown remains in effect until the grappling hook returns to the player. The discussion suggests integrating ropes as ammunition for propulsion, reducing crafting complexity and unifying mechanics. The specific stats for the grappling hook are: range distance (not specified), impact damage (1-5), charge speed (0.2 seconds), propulsion power (10), and reload speed (0.4 seconds).

## Related Questions
- How does the grappling hook handle different types of targets (blocks, mobs)?
- What is the impact of integrating ropes as ammunition on gameplay balance?
- How does the grappling hook's cooldown mechanism work?
- Can the grappling hook be used while holding other items?
- What are the specific stats for the grappling hook (range distance, impact damage, etc.)?
- How does the grappling hook interact with existing mechanics like ropes?

*Source: unknown | chunk_id: github_issue_2154_discussion*
