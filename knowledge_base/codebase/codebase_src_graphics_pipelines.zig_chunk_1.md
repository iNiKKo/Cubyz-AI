# [hard/codebase_src_graphics_pipelines.zig] - Chunk 1

**Type:** api
**Keywords:** GLSL, SPIR-V, shader linking, uniforms, Vulkan API
**Symbols:** Shader, Shader.id, Shader.ShaderStage, Shader.compileToSpirV, Shader.addShader, Shader.link, Shader.init, Shader.initCompute, Shader.createShaderModule, Shader.bind, Shader.deinit
**Concepts:** shader management, GLSL compilation, SPIR-V generation, Vulkan shader modules

## Summary
The `Shader` struct manages shader compilation, linking, and usage in a graphics pipeline.

## Explanation
The `Shader` struct encapsulates the logic for handling shaders in the Cubyz engine. It includes methods for compiling GLSL source to SPIR-V, adding shaders to a program, linking programs, initializing vertex and compute shaders, creating Vulkan shader modules, binding shaders for use, and deinitializing resources. The `compileToSpirV` function handles the conversion of GLSL code into SPIR-V format using glslang. The `addShader` method compiles individual shaders and attaches them to a program. The `link` method links all added shaders into a complete shader program. The `init` and `initCompute` functions set up vertex and compute shaders, respectively, by adding and linking shaders and setting uniform locations. The `createShaderModule` function creates Vulkan shader modules from SPIR-V code. The `bind` method activates the shader program for rendering, and `deinit` cleans up resources.

## Code Example
```zig
fn bind(self: *const Shader) void {
	c.glUseProgram(self.id);
}
```

## Related Questions
- What is the purpose of the `ShaderStage` enum?
- How does the `compileToSpirV` function work?
- What steps are involved in initializing a vertex shader?
- How are errors handled during shader compilation and linking?
- What is the role of the `createShaderModule` function?
- How do you bind a shader for rendering?
- What does the `deinit` method clean up?
- How are uniform locations set for shaders?
- What Vulkan API functions are used in this code?
- How does the shader management system handle different shader stages?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_1*
