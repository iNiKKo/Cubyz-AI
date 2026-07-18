# [easy/codebase_assets_cubyz_blocks_branch_glimmergill.zig.zon] - Chunk 0

**Type:** implementation
**Keywords:** block properties, item durability, texture mapping, decay prevention, material properties
**Symbols:** blockHealth, texture0, texture1, texture2, texture3, texture4, texture5, item, material, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, colors, modifiers
**Concepts:** block definition, item material, decay prohibition

## Summary
Block definition for Glimmergill branch in Cubyz

## Explanation
This chunk defines a block named 'Glimmergill branch' with the following attributes:

- **Tags:** `.choppable`, `.cuttable`, `.sliceable`, `.mushroom`
- **Block Health:** 2
- **Textures:**
  - `texture0`: `cubyz:branch/glimmergill/dot`
  - `texture1`: `cubyz:branch/glimmergill/half_line`
  - `texture2`: `cubyz:branch/glimmergill/line`
  - `texture3`: `cubyz:branch/glimmergill/bend`
  - `texture4`: `cubyz:branch/glimmergill/intersection`
  - `texture5`: `cubyz:branch/glimmergill/cross`
- **Item Material:**
  - **Durability:** 260
  - **Mass Damage:** 1.5
  - **Hardness Damage:** 0.5
  - **Swing Speed:** 4.2
  - **Texture Roughness:** 0.5
  - **Colors:** `0xff4a3570`, `0xff564085`, `0xff684a97`, `0xff7555b2`, `0xff7555b2` (5 entries, the last repeated)
  - **Modifiers:** one modifier, `.id = "durable"`, `.strength = 0.50`
  - **Item texture:** `branch/glimmergill.png`
- **Decay Prohibitor:** `true` (this block prevents decay)

## Related Questions
- What tags are assigned to the Glimmergill branch block?
- What is the block health of the Glimmergill branch?
- What durability does the Glimmergill branch item material have?
- What modifier is applied to the Glimmergill branch, and what is its strength?
- Does the Glimmergill branch prevent decay?
- How many colors are defined for the Glimmergill branch's item material?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_glimmergill.zig.zon_chunk_0*
