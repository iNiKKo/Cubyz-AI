# [issues/issue_172.md] - Issue #172 discussion

**Type:** review
**Keywords:** modifiers, tool customization, gameplay enhancement, balance, specialization, trade-offs, engagement
**Symbols:** binding, long, hard, brittle, thorny, poisonous, combustible, hot, cold, soluble, far-reaching, blunt, single-use, one-hit, unbreakable, self-repairing, explosive, non-newtonian, zanite, life-steal, energy-steal, soul-steal
**Concepts:** gameplay balance, modifier specialization, trade-offs in gameplay, player engagement

## Summary
The discussion revolves around various material modifiers for tools in Cubyz, including common and rare modifiers, their effects, and potential implementations. Maintainers suggest adding new modifiers like 'non-newtonian', 'life steal', and 'energy steal' while considering the balance of gameplay.

## Explanation
The discussion revolves around various material modifiers for tools in Cubyz, including common and rare modifiers, their effects, and potential implementations. Maintainers suggest adding new modifiers like 'non-newtonian', 'life steal', and 'energy steal' while considering the balance of gameplay.

## Common Modifiers
- **binding**: Adds durability when next to a junction of other materials (e.g., sticky materials, fibers).
- **long**: Stronger when multiple items of this type are in a straight/diagonal line (e.g., sticks/rods).
- **hard**: Increases speed when at the tip of a tool (e.g., diamond).
- **brittle**: Decreases durability depending on the number of neighbors surrounding it (e.g., diamond, glass/ceramic).
- **thorny**: Inflicts bleeding effect on the target and damages the player when on the handle (e.g., cactus).
- **poisonous**: Causes poison damage (e.g., from poisonous materials).
- **combustible**: Loses durability when the player is on fire.
- **hot**: Burns the player/enemies and interacts with combustible materials.
- **cold**: Protects neighboring combustible blocks from durability damage and loses durability when next to a hot material.
- **soluble**: Loses durability when the player is under water.
- **far-reaching**: Increases range of the tool.
- **blunt**: Damage decreases the longer you use it.

## Rare Modifiers
- **single-use**: Only one material with this modifier can be used per tool -- prevents overpowered tools by stopping the same (or multiple different) strong single-use materials from being stacked together.
- **one-hit**: Deals much higher damage than normal, but the tool's durability breaks after that single use.
- **unbreakable**: Prevents the tool from breaking, potentially leading to resource imbalance.
- **self-repairing**: Repairs itself over time, which might be less engaging in Cubyz's balanced material system.

## Proposed Modifiers and Their Mechanics
- **specialization against specific block types**: Encourages more creative crafting by allowing tools to be specialized for certain materials or blocks.
- **thorny modifier refined**: Inflicts a bleeding effect instead of direct damage, with implications for gameplay balance.
- **life steal**: Restores health at the cost of durability, potentially creating trade-offs in gameplay balance.
- **energy steal**: Restores energy at the cost of durability, adding another layer of strategy to tool usage.
- **soul stealer**: Transfers a portion of the target's life force to the player, with potential balance issues.

## Additional Suggestions and Comments
- **wide swing modifier**: Allows a tool to deal damage to multiple blocks at once, potentially useful for axes or pickaxes but less so for other tools.
- **sticky modifier**: Prevents dropped items from being placed into the inventory, changing block mining behavior in Cubyz.
- **edible tool modifier**: Restores energy but costs durability, with potential implications for gameplay balance.

Maintainers also discuss the impact of adding a 'non-newtonian' modifier to tools in Cubyz, the intended interaction of the 'ruby' modifier with player health, and the mechanics of the proposed 'electrocute' modifier. They express concerns about the impact of 'self-repairing' and 'unbreaking' modifiers on resource usage, suggesting they might be less engaging in Cubyz's balanced material system.

## Related Questions
-  What is the impact of adding a 'non-newtonian' modifier to tools in Cubyz?
-  How does the 'thorny' modifier's bleeding effect work, and what are its implications for gameplay?
-  Can you explain the proposed 'life steal' modifier and its potential balance issues?
-  What are the considerations for implementing the 'self-repairing' and 'unbreaking' modifiers in Cubyz?
-  How does the suggested 'wide swing' modifier affect tool usage, and is it useful for all tools?
-  What is the intended interaction of the 'ruby' modifier with player health, and how is it balanced?
-  Can you elaborate on the proposed 'electrocute' modifier and its mechanics?
-  How might the 'sticky' modifier change block mining behavior in Cubyz?
-  What are the potential benefits and drawbacks of adding a 'graceful' or 'cumbersome' movement speed modifier to tools?
-  How could the 'edible' tool modifier be implemented, and what are its implications for gameplay?

*Source: unknown | chunk_id: github_issue_172_discussion*
