# [hard/codebase_src_items.zig] - Chunk 6

**Type:** gameplay
**Keywords:** ProceduralItem, crafting grid, durability, seed, type, material grid, properties, texture, tooltip, modifiers, tags, initialization, cloning, saving, loading
**Symbols:** ProceduralItem, init, clone, save, fromBytes, toBytes, hashCode, getItemAt, getProperty, setProperty, getTexture, getTooltip, hasTag, isEffectiveOn, getBlockDamage, onUseReturnBroken, canPutIntoWorkbenchCallback
**Concepts:** Procedural generation, Item management, Serialization, Deserialization, Property handling, Game mechanics

## Summary
Defines the ProceduralItem struct and its methods for initialization, cloning, saving, loading, property management, and interaction with other game components.

## Explanation
The ProceduralItem struct represents a procedurally generated item in the game. It includes various fields such as crafting grid, durability, seed, type, material grid, properties, texture, tooltip, modifiers, and tags. The struct provides methods for initializing items from different sources (crafting grid, inventory, Zon file), cloning items, saving and loading items to/from binary format, managing item properties, retrieving textures and tooltips, checking tags and effectiveness on blocks, calculating block damage, handling durability, and determining if an item can be placed in a workbench.

## Code Example
```zig
pub fn getProperty(self: *ProceduralItem, prop: ProceduralItemProperty) f32 {
		return self.properties[@intFromEnum(prop)];
	}
```

## Related Questions
- How does ProceduralItem handle durability changes?
- What methods are available for managing item properties in ProceduralItem?
- Can you explain how ProceduralItem initializes from a Zon file?
- How does ProceduralItem generate its texture and tooltip?
- What is the purpose of the `canPutIntoWorkbenchCallback` method in ProceduralItem?
- How does ProceduralItem handle block damage calculations?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_6*
