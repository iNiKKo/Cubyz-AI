# [src/entityModel.zig] - Chunk 3053045857

**Type:** review
**Keywords:** EntityModel, VertexArray, Texture, texturePath, nullable, lazy loading, path-based, deferred, world-specific, streaming
**Symbols:** EntityModel, VertexArray, Texture, height, texturePath, id, defaultTexture, modelFile
**Concepts:** lazy loading, memory optimization, nullable fields, path-based asset references, deferred initialization, world-specific assets, streaming, allocation reduction

## Summary
Refactor EntityModel struct to replace direct texture/VAO storage with path-based references and nullable fields, enabling deferred loading from world-specific asset folders.

## Explanation
The original struct stored a concrete VertexArray (vao) and Texture directly, which forced immediate allocation and prevented lazy loading. The reviewer pointed out the file is large and suggested storing only paths to read assets into temporary memory on demand. Since an id field already exists, the logical step is to have the assets store per-world asset folders keyed by that id. This change introduces nullable fields (vao: ?graphics.VertexArray = null, defaultTexture: ?main.graphics.Texture) so they can be initialized later when needed, and adds a texturePath string to hold the path. The height field is also added, likely for model scaling or LOD handling. By moving from eager allocation to lazy loading via paths, we reduce peak memory usage at startup and allow streaming of large models. This aligns with the architectural goal of minimizing upfront allocations in a game engine where many entities may be present.

## Related Questions
- What are the implications of making vao and defaultTexture nullable in EntityModel?
- How does storing texturePath instead of Texture affect asset loading order?
- Where is the per-world asset folder stored relative to the id field?
- Does this change require updates to any entity instantiation code that previously assumed non-null textures?
- What memory savings are expected by deferring VertexArray creation until needed?
- Is there a risk of null pointer dereference if vao remains null after loading?
- How does adding height affect the rendering pipeline for EntityModel instances?
- Does modelFile replace texturePath or coexist with it in the struct layout?
- What validation is needed to ensure texturePath points to an existing file before loading?
- Could this refactor impact entity pooling strategies that rely on immediate resource availability?
- Are there any compatibility concerns with older code expecting a concrete Texture field?
- How does this change align with the overall architecture of deferring heavy allocations in Cubyz?

*Source: unknown | chunk_id: github_pr_2680_comment_3053045857*
