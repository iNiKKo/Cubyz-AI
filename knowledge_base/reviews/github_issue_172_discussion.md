# [issues/issue_172.md] - Issue #172 discussion

**Type:** review
**Keywords:** modifiers, tool customization, gameplay enhancement, balance, specialization, trade-offs, engagement
**Symbols:** binding, long, hard, brittle, thorny, poisonous, combustible, hot, cold, soluble, far-reaching, blunt, single-use, one-hit, unbreakable, self-repairing, explosive, non-newtonian, zanite, life-steal, energy-steal, soul-steal
**Concepts:** gameplay balance, modifier specialization, trade-offs in gameplay, player engagement

## Summary
The discussion revolves around various material modifiers for tools in Cubyz, including common and rare modifiers, their effects, and potential implementations. Maintainers suggest adding new modifiers like 'non-newtonian', 'life steal', and 'energy steal' while considering the balance of gameplay.

## Explanation
The issue discusses the addition of tool material modifiers to enhance gameplay in Cubyz. Common modifiers include 'binding', which adds durability when next to a junction of other materials; 'long', which is stronger when multiple items of this type are in a straight/diagonal line; 'hard', which increases speed when at the tip of a tool; 'brittle', which decreases durability depending on the number of neighbors surrounding it; 'thorny', which inflicts bleeding effect on the target and damages the player when on the handle; 'poisonous', which causes poison damage; 'combustible', which loses durability when the player is on fire; 'hot', which burns the player/enemies and interacts with combustible materials; 'cold', which protects neighboring combustible blocks from durability damage and loses durability when next to a hot material; 'soluble', which loses durability when the player is under water; 'far-reaching', which increases range of the tool; and 'blunt', where damage decreases the longer you use it. Rare modifiers like 'single-use' and 'one-hit' introduce unique effects that could prevent overpowered tools. Maintainers suggest adding a modifier for specialization against specific block types, which encourages more creative crafting. They also propose refining existing modifiers such as 'thorny' to inflict a bleeding effect instead of direct damage. The discussion includes ideas like 'life steal', 'energy steal', and 'soul stealer', each with potential trade-offs in gameplay balance. Maintainers express concerns about the impact of 'self-repairing' and 'unbreaking' modifiers on resource usage, suggesting they might be less engaging in Cubyz's balanced material system. The 'wide swing' modifier allows a tool to deal damage to multiple blocks at once, while the 'sticky' modifier prevents dropped items from being placed into the inventory. The 'edible' tool modifier restores energy but costs durability.

## Related Questions
- What is the impact of adding a 'non-newtonian' modifier to tools in Cubyz?
- How does the 'thorny' modifier's bleeding effect work, and what are its implications for gameplay?
- Can you explain the proposed 'life steal' modifier and its potential balance issues?
- What are the considerations for implementing the 'self-repairing' and 'unbreaking' modifiers in Cubyz?
- How does the suggested 'wide swing' modifier affect tool usage, and is it useful for all tools?
- What is the intended interaction of the 'ruby' modifier with player health, and how is it balanced?
- Can you elaborate on the proposed 'electrocute' modifier and its mechanics?
- How might the 'sticky' modifier change block mining behavior in Cubyz?
- What are the potential benefits and drawbacks of adding a 'graceful' or 'cumbersome' movement speed modifier to tools?
- How could the 'edible' tool modifier be implemented, and what are its implications for gameplay?

*Source: unknown | chunk_id: github_issue_172_discussion*
