# [easy/docs_docs_development_addons_blocks.md] - Chunk 0

**Type:** documentation
**Keywords:** block properties, transparent, collide, blockHealth, blockResistance, replaceable, selectable, blockDrops, degradable, viewThrough, alwaysViewThrough, hasBackface, tags, cubyz blocks
**Symbols:** transparent, collide, blockHealth, blockResistance, replaceable, selectable, blockDrops, degradable, viewThrough, alwaysViewThrough, hasBackface, tags

## Summary
Cubyz block `zig.zon` fields covering solidity, interaction, and basic identity (part 1 of 3 -- see sibling chunks for lighting/rendering fields and physics/ore fields).

## Explanation
Each Cubyz block has a `zig.zon` file with properties defining its behavior.

| Property | Type | Description |
|----------|------|-------------|
| `transparent` | `bool` | Whether the block is transparent. |
| `collide` | `bool` | Whether entities collide with the block. |
| `blockHealth` | `f32` | Health of the block. |
| `blockResistance` | `f32` | Resistance to damage or explosions. |
| `replaceable` | `bool` | Whether the block can be replaced by another block without being broken. |
| `selectable` | `bool` | Whether the block can be targeted and selected. |
| `blockDrops` | `[]BlockDrops` | Items dropped when the block is broken. |
| `degradable` | `bool` | Whether the block can degrade over time. |
| `viewThrough` | `bool` | Whether the player can see through the block. |
| `alwaysViewThrough` | `bool` | Forces the block to always be rendered as view-through. |
| `hasBackface` | `bool` | Whether the block renders back faces. |
| `tags` | `[]Tag` | Tags assigned to the block. |

## Related Questions
- What are the properties of a block in Cubyz?
- How can I determine if a block is transparent or not?
- Can you explain the difference between 'replaceable' and 'selectable' blocks?
- What does a Cubyz block's blockDrops field contain?
- What does a Cubyz block's hasBackface field control?

*Source: unknown | chunk_id: docs_docs_development_addons_blocks.md_chunk_0*
