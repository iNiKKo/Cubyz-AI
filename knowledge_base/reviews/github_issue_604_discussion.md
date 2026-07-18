# [issues/issue_604.md] - Issue #604 discussion

**Type:** review
**Keywords:** armor, accessories, procedural generation, customization, item types, modding, callbacks, stats, balancing, metadata, player models
**Symbols:** Item Type, Proceduraltem, Tool struct, Data packed struct, Modifiers, BaseItem, ProceduralItem, onHit, onInteract, onUse, printTooltip
**Concepts:** Moddability, Procedural generation, Customization, Item interaction callbacks, Stat balancing

## Summary
Discussion and planning for adding armor and accessory slots in Cubyz, focusing on procedural generation and customization options.

## Explanation
The discussion revolves around how to implement armor and accessories in Cubyz. The maintainers suggest using metadata for player models to determine where armor should be displayed and propose procedural generation of armor textures based on materials. There is a suggestion to treat armor and accessories similarly internally, with specific slots like rings, helmets, etc., and the possibility of using orbs or chakra-like effects instead of traditional armor plates. The user proposes creating a new item type for armor and accessories, separating it from tools, and implementing a callback system for interactions. There are also discussions about moddability, balancing stats, and ensuring that modifiers can work across different types of items without crashing.

## Related Questions
- How does Cubyz plan to handle the procedural generation of armor textures?
- What are the proposed slots for accessories in Cubyz?
- How will modders be able to add new types of Proceduraltems?
- What is the suggested approach for handling item interaction callbacks in Cubyz?
- How will stats and balancing be managed for different types of items in Cubyz?
- What are the potential issues with using unions for item data structures in Cubyz?
- How does Cubyz plan to ensure that modifiers can work across different item types without crashing?
- What is the proposed system for handling syntax highlighting when using unions in Cubyz?
- How will armor be displayed on players with custom models in Cubyz?
- What are the considerations for balancing stats and ensuring player understanding of item effects in Cubyz?

*Source: unknown | chunk_id: github_issue_604_discussion*
