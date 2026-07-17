# [src/renderer.zig] - PR #950 review diff

**Type:** review
**Keywords:** skybox, shader, vertex array, buffer, rendering, performance measuring, debug menu
**Symbols:** Skybox, Shader, uniforms, vao, vbos, init, deinit, render
**Concepts:** OpenGL rendering, resource management, GPU performance monitoring

## Summary
Added Skybox struct with initialization, deinitialization, and rendering functions. Encapsulated render function within GPU performance measuring.

## Explanation
The change introduces a new `Skybox` struct to handle skybox rendering in the Cubyz game engine. The struct includes methods for initializing resources (shaders, vertex array objects, and buffers), deinitializing them, and rendering the skybox. The reviewer suggests encapsulating the render function within GPU performance measuring functions (`start/stopQuery`) of a new type to integrate it into the GPU performance debug menu accessible via F5.

## Related Questions
- What is the purpose of the `Skybox` struct in the Cubyz engine?
- How does the `init` function initialize the skybox resources?
- Why are the `glDisable` and `glEnable` calls used in the `render` function?
- What changes were made to integrate the render function into GPU performance measuring?
- How is the time uniform calculated for the skybox shader?
- What is the role of the `viewMatrix` and `projectionMatrix` in rendering the skybox?
- How does the skybox handle lighting direction calculations?
- What are the implications of disabling culling and depth testing during skybox rendering?
- How are the vertex and index data structured for the skybox?
- What is the significance of using `@mod` to calculate time in the shader?

*Source: unknown | chunk_id: github_pr_950_comment_1949897465*
