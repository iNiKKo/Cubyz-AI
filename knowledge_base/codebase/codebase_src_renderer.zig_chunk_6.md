# [hard/codebase_src_renderer.zig] - Chunk 6

**Type:** implementation
**Keywords:** graphics pipeline, vertex array object, shader storage buffer, uniform binding, AABB intersection, camera frustum, random star generation, lighting threshold
**Symbols:** init, deinit, render, Frustum, Frustum.Plane
**Concepts:** skybox rendering, frustum culling, SSBO usage, day-night cycle integration

## Summary
This chunk defines the star rendering pipeline and a frustum culling utility.

## Explanation
The init() function loads a star texture, builds a graphics.Pipeline with vertex/fragment shaders for skybox stars, initializes an SSBO holding per-star data (position, color), and populates it by generating random positions, radii, temperatures, and lighting values until each star reaches a minimum light threshold. It then transforms three fixed triangle vertices into world space using rotation matrices derived from latitude/longitude computed from the normalized position, writes those transformed vertices plus the center point and color into the SSBO buffer, and finally creates an empty vertex array object. The deinit() function cleans up pipeline, SSBO, and VAO resources. render() checks star opacity via game.world.dayTime.getStarOpacity(), binds the pipeline with null shader (skybox), computes a combined MVP matrix using projection, view, and a rotation around X based on day progress, binds the SSBO at slot 12, sets uniforms for opacity and MVP, draws numStars*3 triangles as GL_TRIANGLES, then unbinds the SSBO. The Frustum struct defines four planes (right/left/top/bottom) computed from camera position, inverse rotation matrix, field of view, and viewport aspect; testAAB() checks whether an AABB intersects all frustum planes by computing dot distances to each plane and adding the most positive corner offset.

## Code Example
```zig
pub fn deinit() void {
	starPipeline.deinit();
	starSsbo.deinit();
	starVao.deinit();
}
```

## Related Questions
- How does the star rendering pipeline handle day-night opacity changes?
- What is the purpose of binding null shaders in render()?
- Why are three triangle vertices transformed per star instead of one?
- How is the SSBO populated with star data during init()?
- What determines whether a star reaches its minimum light threshold?
- How are latitude and longitude derived from normalized position vectors?
- What role does the Frustum testAAB function play in rendering?
- Why is the rotation applied around X axis based on day progress?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_6*
