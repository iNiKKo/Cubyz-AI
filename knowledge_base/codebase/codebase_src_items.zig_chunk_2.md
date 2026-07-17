# [hard/codebase_src_items.zig] - Chunk 2

**Type:** implementation
**Keywords:** item attributes, texture map, material information, height map, randomness
**Symbols:** BaseItem, BaseItem.image, BaseItem.texture, BaseItem.id, BaseItem.name, BaseItem.tags, BaseItem.tooltip, BaseItem.stackSize, BaseItem.material, BaseItem.block, BaseItem.foodValue, BaseItem.init, BaseItem.hashCode, BaseItem.getTexture, BaseItem.getTooltip, BaseItem.hasTag, TextureGenerator, TextureGenerator.generateHeightMap
**Concepts:** item properties, texture generation

## Summary
Defines item properties and texture generation logic.

## Explanation
This chunk defines the `BaseItem` struct, which represents basic item attributes such as image, texture, ID, name, tags, stack size, material, block type, food value, and tooltip. It includes methods to retrieve these properties. Additionally, it provides a `TextureGenerator` struct with a method to generate a height map for procedural items based on their material information.

## Code Example
```zig
pub fn stackSize(self: BaseItemIndex) u16 {
	return itemList[@intFromEnum(self)].stackSize;
}
```

## Related Questions
- What is the purpose of the `BaseItem` struct?
- How does the `init` method initialize a `BaseItem` instance?
- What does the `generateHeightMap` function do in the `TextureGenerator` struct?
- How are item tags managed within the `BaseItem` struct?
- What is the role of the `hashCode` method in the `BaseItem` struct?
- How is the texture for a `BaseItem` generated if no texture path is provided?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_2*
