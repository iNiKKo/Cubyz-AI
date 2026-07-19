# [issues/issue_546.md] - Issue #546 discussion

**Type:** review
**Keywords:** saplings, seeds, trees, composting, sulfur, resource management, game design, exploration, grind, recipes
**Symbols:** acorn, pinecone, coconut, baobab fruit, sapling, seed, tree, compost, sulfur
**Concepts:** gameplay balance, resource management, exploration vs. grind, inventory recipes

## Summary
The discussion revolves around implementing sapling mechanics in Cubyz, considering different approaches like seeds vs. saplings, and exploring resource management systems such as composting.

## Explanation
The discussion revolves around implementing sapling mechanics in Cubyz, considering different approaches like seeds vs. saplings, and exploring resource management systems such as composting. The maintainers and users explore different approaches for sapling mechanics, including the Terraria-style seed system versus the Minecraft-style sapling item. They also discuss methods to prevent infinite wood farming by introducing complexity such as composting or requiring specific resources like sulfur. The discussion touches on game design principles, such as avoiding grindy gameplay and encouraging exploration. Specifically, it is proposed that saplings should be able to turn into structures, but the exact mechanism for this transformation is not explicitly stated in the raw content.

The Terraria-style seed system involves seeds represented by items like acorns or pinecones, which only turn into a little bush when planted. The Minecraft-style sapling item is another option. Users suggest having seeds as blocks hanging from trees that can be harvested with a sickle, with a chance of not getting any seeds at all. For fruit-bearing trees, the fruits could grow on trees like crops for food prep but would limit infinite wood farming if they are also the sapling item.

To prevent infinite wood farming, maintainers propose making saplings a separate step from seeds, requiring a pot, soil, and 10 seeds to make one sapling or using an external resource like a 'growth crystal.' Another idea is to have a seed grow into a tree with an X% chance of disappearing. Users suggest having the crystal force seeds to always sprout into a tree while having the option to gamble if the seed sprouts or not.

Another proposal is that saplings will only grow into a tree if they are placed on rich soil/compost blocks, consuming nutrients and converting them back into regular soil. This limits the number of trees you can grow based on the amount of compost available. Compost could be crafted using a composter where players input unwanted plant matter to get compost out, or it could be made with 120 grass vegetation, 10 mushrooms, and 10 sulfur. Sulfur ore is large crystalline chunks that need to be processed first.

Maintainers suggest requiring different plants for composting to encourage exploration rather than grindy gameplay. They also propose adjusting the seed system to make it more balanced by allowing edible seeds like coconuts and baobab fruits to be cut into many servings.

## Related Questions
- How does the current sapling system in Cubyz work?
- What are the proposed changes to the sapling mechanics?
- Why is composting being considered as a solution for resource management?
- How would the sulfur processing fit into the composting system?
- What are the potential issues with requiring large quantities of resources for composting?
- How does the discussion address the balance between exploration and grind in gameplay?
- What alternative solutions were proposed to prevent infinite wood farming?
- How might the multi-ingredient inventory recipes be implemented?
- What is the current status of the composter feature in Cubyz development?
- How could the seed system be adjusted to make it more balanced?

*Source: unknown | chunk_id: github_issue_546_discussion*
