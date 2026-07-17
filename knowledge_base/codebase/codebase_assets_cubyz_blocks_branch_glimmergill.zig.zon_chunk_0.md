# [easy/codebase_assets_cubyz_blocks_branch_glimmergill.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** choppable, cuttable, sliceable, mushroom, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, decayProhibitor
**Symbols:** tags, blockHealth, texture0, texture1, texture2, texture3, texture4, texture5, item, material, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, colors, modifiers, id, strength, texture, decayProhibitor
**Concepts:** block configuration, item properties, texture mapping, damage modifiers, durability scaling, decay prevention

## Summary
Configuration data defining the Glimmergill branch block with its texture assets, item properties including durability and damage modifiers, and decay prohibition settings.

## Explanation
This chunk contains a single configuration object for the Glimmergill branch block. The tags field lists .choppable, .cuttable, .sliceable, and .mushroom as its interaction categories. Block health is set to 2. Texture assets are specified across six slots: texture0 through texture5 map to cubyz:branch/glimmergill/dot, half_line, line, bend, intersection, and cross respectively. The item subobject defines material properties with durability of 260, massDamage of 1.5, hardnessDamage of 0.5, swingSpeed of 4.2, textureRoughness of 0.5, and a colors array containing five hex values (0xff4a3570, 0xff564085, 0xff684a97, 0xff7555b2 repeated). A modifiers array includes one entry with id durable and strength 0.50. The texture field points to branch/glimmergill.png. DecayProhibitor is set to true.

## Related Questions
- What tags are assigned to the Glimmergill branch block?
- How much health does the Glimmergill branch block have?
- Which texture is used for the dot face of the Glimmergill branch?
- What is the durability value of the Glimmergill branch item material?
- Does the Glimmergill branch block decay over time?
- What damage does the Glimmergill branch item deal with mass attacks?
- How many colors are defined for the Glimmergill branch texture?
- Is there a durability modifier applied to the Glimmergill branch item?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_branch_glimmergill.zig.zon_chunk_0*
