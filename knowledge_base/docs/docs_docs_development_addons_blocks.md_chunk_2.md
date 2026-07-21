# [easy/docs_docs_development_addons_blocks.md] - Chunk 2

**Type:** documentation
**Keywords:** friction, bounciness, density, terminalVelocity, mobility, allowOres, ore fields, size, veins, maxHeight, minHeight, item property
**Symbols:** friction, bounciness, density, terminalVelocity, mobility, allowOres, ore, item

## Summary
Cubyz block `zig.zon` fields covering physics and ore generation (part 3 of 3).

## Explanation
| Property | Type | Description |
|----------|------|-------------|
| `friction` | `f32` | Surface friction of the block. |
| `bounciness` | `f32` | Bounce factor applied to entities. |
| `density` | `f32` | Physical density of the block. |
| `terminalVelocity` | `f32` | Maximum falling velocity through the block. |
| `mobility` | `f32` | Mobility value used by the physics system. |
| `allowOres` | `bool` | Whether ores can generate inside this block. |
| `ore` | `struct` | Ore generation settings (size, density, veins, maxHeight, minHeight -- see Ore Fields below). |
| `item` | `struct` | Item properties that can also be applied to blocks, such as textures and material values. |

### Ore Fields
| Property | Type | Description |
|----------|------|-------------|
| `size` | `f32` | Average vein size in blocks. |
| `density` | `f32` | Average density of each vein. |
| `veins` | `f32` | Average number of veins per chunk. |
| `maxHeight` | `f32` | Highest point the ore can generate. |
| `minHeight` | `f32` | Lowest point the ore can generate. |

## Related Questions
- Can you explain the impact of friction on block physics in Cubyz?
- What are some common use cases for setting `allowOres` to true?
- How does the terminal velocity affect falling through blocks in Cubyz?
- How does the `ore` field work in Cubyz, and what are its properties?
- Can you provide an example of a block's `item` property?

*Source: unknown | chunk_id: docs_docs_development_addons_blocks.md_chunk_2*
