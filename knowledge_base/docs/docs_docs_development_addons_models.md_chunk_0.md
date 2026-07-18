# [easy/docs_docs_development_addons_models.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz, block models, GLB files, UV mapping, texture slots, Z up, model specification
**Symbols:** Cubyz, glb, Blockbench, Blender, Z up, UVs, 64x64 texture, 16 slots, zig.zon, model
**Concepts:** Modeling, UV Mapping, Texture Slots, Block Model Specification

## Summary
Cubyz loads `.glb` files for block models and provides guidelines on creating and using them.

## Explanation
Cubyz uses Z up for its coordinate system. Block model UVs are mapped to a 64x64 texture with 16 slots, which are specified in the `zig.zon` file under fields like `texture`, `texture_top`, etc., based on the block's faces.

## Related Questions
- What is the coordinate system used by Cubyz?
- How many texture slots are available for block models in Cubyz?
- Where can I find more information about creating and using block models in Cubyz?
- What are some common mistakes to avoid when modeling for Cubyz?
- How do I specify the file path of my model in the `zig.zon` file?
- What is the purpose of each texture field in the `zig.zon` file?
- How does Cubyz handle block models with multiple faces?
- Can I use a different 3D modeling software to create block models for Cubyz?
- What are some best practices for creating high-quality block models for Cubyz?
- How do I troubleshoot issues with loading block models in Cubyz?
- What is the maximum size of a texture that can be used in Cubyz?
- Can I use a 3D modeling software other than Blockbench or Blender to create block models for Cubyz?

*Source: unknown | chunk_id: docs_docs_development_addons_models.md_chunk_0*
