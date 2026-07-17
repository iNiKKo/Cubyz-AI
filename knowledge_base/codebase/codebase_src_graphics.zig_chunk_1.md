# [hard/codebase_src_graphics.zig] - Chunk 1

**Type:** implementation
**Keywords:** Vulkan, Pipeline, VertexArray, uniforms, scissor, viewport, alphaBlending, TriangleStrip, shader assets, deinit
**Symbols:** restoreClip, SimpleVertex2D, RectBorderVertex, rectUniforms, rectPipeline, rectVao, initRect, deinitRect, rect, rectBorderUniforms, rectBorderPipeline, rectBorderVao, initRectBorder, deinitRectBorder, rectBorder
**Concepts:** Vulkan rendering pipeline, vertex attribute descriptions, uniform buffer setup, scissor and viewport handling, alpha blending attachments, triangle strip drawing, shader asset loading, resource initialization/deinitialization

## Summary
This chunk defines the graphics rendering pipeline for drawing filled rectangles and rectangle borders using Vulkan shaders. It includes vertex structures (SimpleVertex2D, RectBorderVertex), uniform buffers, pipelines, VAOs, and public functions to render these shapes with proper viewport/scissor handling.

## Explanation
The chunk declares SimpleVertex2D struct with a pos field of type [2]f32 and its attributeDescriptions array exposing the vertex location/format/offset for Vulkan. It also defines RectBorderVertex struct with a pos field of type [4]f32 and corresponding attributeDescriptions. Both structs are used to initialize VertexArray objects (rectVao, rectBorderVao) via their respective init functions which call Pipeline.init with shader paths from assets/cubyz/shaders/graphics/, empty vertex bindings, cullMode none, depthTest false, depthWrite false, and alphaBlending attachments. The chunk contains pub fn restoreClip(previousClip: ?Vec4i) void that assigns clip = previousClip; to restore the old clip state when leaving render functions. It defines var rectUniforms struct with fields screen, start, size, rectColor initialized to undefined, and var rectPipeline of type Pipeline also undefined. The initRect() function populates rectPipeline by calling Pipeline.init with SimpleVertex2D and rawData array of four SimpleVertex2D instances at positions (0,0), (0,1), (1,0), (1,1). It then calls rectVao = .init(SimpleVertex2D, &rawData, null). The deinitRect() function calls rectPipeline.deinit() and rectVao.deinit(). The pub fn rect(_pos: Vec2f, _dim: Vec2f) void applies scale to pos and dim via @splat(scale), adds translation, binds the scissor via rectPipeline.bind(getScissor()), retrieves viewport with c.glGetIntegerv(c.GL_VIEWPORT, &viewport), sets uniforms for screen position, start position, size, and color (via @bitCast(getColor())), binds rectVao, and draws a GL_TRIANGLE_STRIP of 4 vertices. Similarly, the chunk defines var rectBorderUniforms struct with additional lineWidth field, var rectBorderPipeline, var rectBorderVao. The initRectBorder() function declares RectBorderVertex inline within its body (not at top level), then calls Pipeline.init with shader paths for RectBorder.vert and RectBorder.frag, empty vertex bindings, cullMode none, depthTest false, depthWrite false, alphaBlending attachments. It constructs rawData array of ten RectBorderVertex instances with specific pos values covering border geometry, then initializes rectBorderVao via .init(RectBorderVertex, &rawData, null). The deinitRectBorder() function calls rectBorderPipeline.deinit() and rectBorderVao.deinit(). The pub fn rectBorder(_pos: Vec2f, _dim: Vec2f, _width: f32) void applies scale to pos, dim, width (using @splat(scale) for pos/dim and scale alone for width), binds scissor, retrieves viewport, sets uniforms for screen position, start position, size, and omits color uniform (likely handled elsewhere). The chunk does not declare any top-level const or pub const imports; all struct definitions are local to this chunk. No other functions or symbols beyond those explicitly declared in this chunk appear.

## Related Questions
- What vertex structure is used for the filled rectangle rendering pipeline?
- How are viewport and scissor coordinates applied before drawing a rectangle?
- Which Vulkan attachment flags are enabled in both rect and rectBorder pipelines?
- What steps does initRect perform to set up the rectangle VAO and pipeline?
- How is the color uniform configured for the filled rectangle draw call?
- What vertex data layout does RectBorderVertex expect according to its attributeDescriptions?
- In what order are deinit functions called relative to their corresponding init functions?
- Does this chunk declare any public constants imported from other modules?
- How is translation applied to the rectangle position before uniform upload?
- What happens if a user calls rectBorder without providing a width argument?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_1*
