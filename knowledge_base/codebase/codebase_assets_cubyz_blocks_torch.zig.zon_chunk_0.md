# [easy/codebase_assets_cubyz_blocks_torch.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** choppable, blockHealth, drops, replaceable, emittedLight, viewThrough, absorbedLight, collide, rotation, check_support_blocks, model, texture, item
**Symbols:** tags, blockHealth, drops, replaceable, emittedLight, viewThrough, absorbedLight, collide, rotation, onUpdate, model, texture, item, lodReplacement
**Concepts:** block definition, light emission, support checking, choppable tags, auto drops, replaceable blocks, model textures, item linking

## Summary
Defines the torch block configuration with choppable tags, light emission properties, support-checking update logic, and model/texture references.

## Explanation
This chunk declares a single block definition object containing metadata for the torch. The .tags field lists {.choppable}, indicating the block can be chopped by tools. The .blockHealth is set to 0.5, defining its durability. The .drops field contains an array with one element specifying that drops are handled via the .auto policy (no explicit drop items defined here). The .replaceable flag is true, meaning this block can be replaced by other blocks during world generation or player interaction. Light properties include .emittedLight set to 0xa58d73 and .absorbedLight set to 0x010101, defining how the torch affects surrounding lighting. The .viewThrough is true, allowing line-of-sight through the block for rendering purposes. The .collide field is false, meaning players or entities do not collide with this block. The .rotation specifies the rotation identifier as cubyz:torch. The .onUpdate field contains a single entry with type .check_support_blocks, indicating that on each update tick the engine will verify whether the torch has supporting blocks beneath it (likely to prevent falling when unsupported). The .model object defines two texture references: .base pointing to cubyz:torch and .side pointing to cubyz:torch_side, used for rendering different faces. The .texture field directly references cubyz:torch as the primary texture. Finally, the .item field contains a subobject with .texture set to torch.png, linking the block to its corresponding item asset.

## Related Questions
- What tags are assigned to the torch block?
- How is the durability of the torch defined in this configuration?
- Does the torch drop items when broken, and how are those drops handled?
- Can other blocks replace the torch during world generation or player interaction?
- What light values does the torch emit and absorb?
- Is the torch transparent to line-of-sight rendering?
- Does the torch collide with entities or players?
- What rotation identifier is used for the torch block?
- What update logic runs on each tick for the torch, and what does it check?
- Which textures are referenced in the model definition for the torch?
- What texture is linked to the item representation of the torch?
- What LOD replacement value is specified for the torch?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_torch.zig.zon_chunk_0*
