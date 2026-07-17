# [easy/docs_docs_development_addons_models.md] - Chunk 0

**Type:** configuration
**Keywords:** models, .glb, UV, texture slots, Z up, zig.zon, configuration, block models, texture mapping, model field, texture_top, texture_bottom, texture_front, texture_back, texture_right
**Symbols:** .glb, Z up, 64x64, texture, texture_top, texture0, texture_bottom, texture1, texture_front, texture2, texture_back, texture3, texture_right, texture4, texture_left, texture5, texture6, texture7, texture8, texture9, texture10, texture11, texture12, texture13, texture14, texture15, zig.zon, model
**Concepts:** .glb model loading, Z up orientation, 64x64 UV texture mapping, texture slot indexing, zig.zon configuration fields, block model assignment workflow

## Summary
Models are loaded as .glb files with Z up orientation and mapped to a 64x64 UV grid using 16 texture slots; individual textures are referenced via zig.zon fields (texture, texture_top/0 through texture15).

## Explanation
Cubyz requires block models in .glb format created with Z up. The model's UV map is split across a 64x64 texture sheet containing 16 slots; the first slot corresponds to the generic 'texture' field applied to all faces, while subsequent slots (0–15) are exposed as either named fields (top, bottom, front, back, right, left plus six additional textures) or numeric indices. To assign a model to a block, set the block's zig.zon model field to the path of the .glb file; then populate the corresponding texture fields in that same zig.zon with paths to the individual texture files.

## Related Questions
- What file format does Cubyz require for block models?
- How is the Z axis oriented in Cubyz model loading?
- What are the dimensions of the UV texture grid used for blocks?
- How many texture slots are available on the 64x64 UV map?
- Which zig.zon field applies a single texture to all faces of a block?
- What is the naming convention for the top face texture in zig.zon?
- How do you reference the back face texture using both name and index fields?
- Where should the path to a .glb model be specified in a block's configuration?
- Are there any additional texture slots beyond the six named faces (top, bottom, front, back, right, left)?
- What happens if you omit the zig.zon model field when assigning a custom model?

*Source: unknown | chunk_id: docs_docs_development_addons_models.md_chunk_0*
