# [easy/docs_docs_development_addons_models.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz, block models, GLB files, UV mapping, texture slots, Z up, model specification
**Symbols:** Cubyz, glb, Blockbench, Blender, Z up, UVs, 64x64 texture, 16 slots, zig.zon, model
**Concepts:** Modeling, UV Mapping, Texture Slots, Block Model Specification

## Summary
Cubyz loads `.glb` files for block models and provides guidelines on creating and using them.

## Explanation
Cubyz loads `.glb` files for block models and provides guidelines on creating and using them. Cubyz uses a coordinate system with Z up. Block model UVs are mapped to a 64x64 texture with 16 slots, which are specified in the `zig.zon` file under fields such as `texture`, `texture_top`, `texture_bottom`, `texture_front`, `texture_back`, `texture_right`, `texture_left`, and additional fields like `texture6` to `texture15`. Each field corresponds to a specific face of the block model. The texture fields are: `texture` (Applied to all faces), `texture_top` OR `texture0`, `texture_bottom` OR `texture1`, `texture_front` OR `texture2`, `texture_back` OR `texture3`, `texture_right` OR `texture4`, `texture_left` OR `texture5`, `texture6`, `texture7`, `texture8`, `texture9`, `texture10`, `texture11`, `texture12`, `texture13`, `texture14`, and `texture15`. To give a block your model, specify the file path of your model in the block's `zig.zon`'s `model` field.

## Related Questions
- What are the specific texture fields in the `zig.zon` file for specifying block models?

*Source: unknown | chunk_id: docs_docs_development_addons_models.md_chunk_0*
