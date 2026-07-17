# [easy/codebase_assets_cubyz_blocks_marble__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** stone tag, mineable block, marble material, auto drop, durability value, mass damage, hardness damage, swing speed, texture roughness, color palette, modifier strength, encased restriction
**Symbols:** .tags, .blockHealth, .drops, .items, .auto, .material, .durability, .massDamage, .hardnessDamage, .swingSpeed, .textureRoughness, .colors, .modifiers, .id, .strength, .tag, .restriction, .encased, .precious, .amount
**Concepts:** block configuration, material properties, item drops, modifier restrictions

## Summary
Defines the marble block configuration with its tags, health, drops, and item properties including durability, damage values, texture roughness, color palette, and modifiers.

## Explanation
This chunk declares a single top-level struct instance (implicitly named by its field references) containing .tags = {.stone, .mineable, .marble}, blockHealth = 28, drops array with one entry having items set to the auto flag, and an item object. The item object includes a material subobject with durability = 55, massDamage = 1.0, hardnessDamage = 3.7, swingSpeed = 3.0, textureRoughness = 1.0, colors array of five hex values (0xffA89B94, 0xffC9C0BB, 0xffECE9E3, 0xffFBF8F1, 0xffECE9E3), and modifiers array containing one modifier with id = good_at, strength = 0.5, tag = .marble, and restriction object specifying id = .encased, tag = .precious, amount = 2.

## Related Questions
- What tags are assigned to the marble block in this configuration?
- How much health does the marble block have according to this file?
- Which item is dropped when the marble block breaks and what flag controls it?
- What is the durability value of the material associated with the marble drop?
- What are the mass damage, hardness damage, and swing speed values for the marble material?
- How many colors are defined in the marble material's color array and what are their hex values?
- What modifier ID is present in the marble item configuration and what strength does it have?
- Which tag does the modifier apply to and what restriction does it enforce?
- What restriction ID, tag, and amount are specified for the marble modifier?
- Is there any additional data beyond tags, health, drops, material properties, modifiers in this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_marble__defaults.zig.zon_chunk_0*
