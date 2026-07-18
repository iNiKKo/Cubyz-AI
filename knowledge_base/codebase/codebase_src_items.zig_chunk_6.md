# [hard/codebase_src_items.zig] - Chunk 6

**Type:** gameplay
**Keywords:** ProceduralItem, crafting grid, durability, seed, type, material grid, properties, texture, tooltip, modifiers, tags, initialization, cloning, saving, loading
**Symbols:** ProceduralItem, init, clone, save, fromBytes, toBytes, hashCode, getItemAt, getProperty, setProperty, getTexture, getTooltip, hasTag, isEffectiveOn, getBlockDamage, onUseReturnBroken, canPutIntoWorkbenchCallback
**Concepts:** Procedural generation, Item management, Serialization, Deserialization, Property handling, Game mechanics

## Summary
Defines the ProceduralItem struct with fields such as crafting grid (size 25), durability, seed, type, material grid (16x16), properties array initialized to zero values, texture, tooltip, modifiers, and tags. Provides methods for initialization from various sources including `initFromZon` using a hash of available items in the crafting grid, cloning while copying image data, saving/loading binary format with detailed serialization logic, property management with exact property values, generating textures and tooltips with formatted strings, checking tags and effectiveness on blocks, calculating block damage considering modifiers, handling durability changes decrementing by 1 per use, and determining workbench placement based on slot availability and material presence.

## Explanation
The ProceduralItem struct represents a procedurally generated item in the game. It includes fields such as crafting grid (size of 25), durability, seed, type, material grid (16x16), properties array initialized to zero values, texture, tooltip, modifiers, and tags. The struct provides methods for initializing items from different sources (crafting grid, inventory, Zon file) with specific details like `initFromZon` using a hash of available items in the crafting grid rather than CRC32. Cloning involves copying image data to ensure uniqueness. Saving and loading involve detailed serialization logic including durability, seed, type, and crafting grid contents. Property management includes setting properties via `setProperty`, which updates specific property values without recalculating all properties. Generating textures uses a method that creates or retrieves an existing texture based on the item's material composition. Tooltips are generated with formatted strings detailing swing speed, damage, durability, and modifiers if applicable. Checking tags involves iterating through predefined tags to determine effectiveness on blocks. Block damage calculation considers both base damage and any applied modifiers. Durability is managed by decrementing it per use until reaching zero. Workbench placement checks slot availability and material presence in the crafting grid.

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
