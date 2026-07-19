# [issues/issue_604.md] - Issue #604 discussion

**Type:** review
**Keywords:** armor, accessories, procedural generation, customization, item types, modding, callbacks, stats, balancing, metadata, player models
**Symbols:** Item Type, Proceduraltem, Tool struct, Data packed struct, Modifiers, BaseItem, ProceduralItem, onHit, onInteract, onUse, printTooltip
**Concepts:** Moddability, Procedural generation, Customization, Item interaction callbacks, Stat balancing

## Summary
Discussion and planning for adding armor and accessory slots in Cubyz, focusing on procedural generation and customization options. The maintainers suggest using metadata to determine where armor should be displayed and propose procedural generation of textures based on materials. Specific accessory slots like rings, helmets, etc., are proposed, with the possibility of orbs or chakra-like effects instead of traditional plates.

## Explanation
Discussion and planning for adding armor and accessory slots in Cubyz, focusing on procedural generation and customization options. The maintainers suggest using metadata for player models to determine where armor should be displayed and propose procedural generation of armor textures based on materials. Specific accessory slots like rings, helmets, goggles, chest, arms, legs, etc., are proposed, with the possibility of orbs or chakra-like effects instead of traditional plates. The user proposes creating a new item type for armor and accessories, separating it from tools, and implementing a callback system for interactions. There are also discussions about moddability, balancing stats, and ensuring that modifiers can work across different types of items without crashing. Specific slots proposed include 2 ring slots, boots slot, necklace slot, etc., with each category having different accessory blueprints/shapes.

## Related Questions
- How does Cubyz plan to handle the procedural generation of armor textures?
- What are the proposed slots for accessories in Cubyz (e.g., rings, helmets, goggles)?
- How will modders be able to add new types of Proceduraltems using the Tool struct and Data packed struct?
- What is the suggested approach for handling item interaction callbacks in Cubyz?
- How will stats and balancing be managed for different types of items in Cubyz?
- What are the potential issues with using unions for item data structures in Cubyz?
- How does Cubyz plan to ensure that modifiers can work across different item types without crashing?

*Source: unknown | chunk_id: github_issue_604_discussion*
