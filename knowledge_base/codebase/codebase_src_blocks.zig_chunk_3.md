# [hard/codebase_src_blocks.zig] - Chunk 3

**Type:** implementation
**Keywords:** packed struct, inline functions, static arrays, callbacks, block transformations
**Symbols:** Block, Block.typ, Block.data, Block.air, Block.toInt, Block.fromInt, Block.transparent, Block.collide, Block.id, Block.idAndData, Block.blockHealth, Block.blockResistance, Block.replaceable, Block.selectionCapabilities, Block.blockDrops, Block.degradable, Block.viewThrough, Block.alwaysViewThrough, Block.hasBackFace, Block.tags, Block.hasTag, Block.light, Block.absorption, Block.onInteract, Block.onBreak, Block.onUpdate, Block.mode, Block.modeData, Block.rotateZ, Block.lodReplacement, Block.opaqueVariant, Block.friction, Block.bounciness, Block.density, Block.terminalVelocity, Block.mobility, Block.allowOres, Block.onTick, Block.onTouch, Block.blockEntity, Block.canBeChangedInto, Block.isSelectableByItem
**Concepts:** block properties, block interactions, voxel engine blocks

## Summary
The `Block` struct defines the properties and behaviors of blocks in the Cubyz voxel engine, including type, data, transparency, collision, health, resistance, and various callbacks for interactions.

## Explanation
The `Block` struct is a packed structure containing two fields: `typ` (type) and `data`. It provides methods to convert between block instances and integer representations. The struct includes numerous inline functions that return properties of the block based on its type, such as transparency, collision capabilities, health, resistance, and more. These properties are accessed through static arrays like `_transparent`, `_collide`, `_blockHealth`, etc., which map block types to their respective attributes. Additionally, the struct defines methods for handling interactions, such as `onInteract`, `onBreak`, and `onUpdate`, returning callbacks that define how blocks respond to player actions or environmental changes. The `canBeChangedInto` method checks if a block can be transformed into another type based on certain conditions.

## Code Example
```zig
pub inline fn transparent(self: Block) bool {
	return _transparent[self.typ];
}
```

## Related Questions
- What is the purpose of the `Block` struct in Cubyz?
- How does a block's type and data relate to its properties?
- What methods are available for checking block transparency?
- How are block interactions handled through callbacks?
- What static arrays are used to store block properties?
- How can blocks be transformed into other types?
- What is the role of the `mode` method in block behavior?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_3*
