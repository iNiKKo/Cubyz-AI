# [hard/codebase_src_graphics_pipelines.zig] - Chunk 1

**Type:** api
**Keywords:** GLSL, SPIR-V, shader linking, uniforms, Vulkan API
**Symbols:** Shader, Shader.id, Shader.ShaderStage, Shader.compileToSpirV, Shader.addShader, Shader.link, Shader.init, Shader.initCompute, Shader.createShaderModule, Shader.bind, Shader.deinit
**Concepts:** shader management, GLSL compilation, SPIR-V generation, Vulkan shader modules

## Summary
The `Shader` struct manages shader compilation, linking, and usage in a graphics pipeline.

## Explanation
The `Shader` struct manages shader compilation, linking, and usage in a graphics pipeline. It includes methods for compiling GLSL source to SPIR-V, adding shaders to a program, linking programs, initializing vertex and compute shaders, creating Vulkan shader modules, binding shaders for use, and deinitializing resources. The `compileToSpirV` function handles the conversion of GLSL code into SPIR-V format using glslang. It takes parameters such as allocator, source, filename, defines, and shaderStage, and returns a slice of c_uint representing the compiled SPIR-V code. The `addShader` method compiles individual shaders and attaches them to a program. It reads the shader file, sets up the shader source with defines, compiles the shader, and attaches it to the program. The `link` method links all added shaders into a complete shader program. If linking fails, it logs an error message. The `init` and `initCompute` functions set up vertex and compute shaders, respectively, by adding and linking shaders and setting uniform locations. They take parameters such as filenames, defines, and a uniform struct, and return a Shader instance. The `createShaderModule` function creates Vulkan shader modules from SPIR-V code. It reads the shader file, compiles it to SPIR-V, and then creates a Vulkan shader module using vkCreateShaderModule. The `bind` method activates the shader program for rendering by calling glUseProgram. The `deinit` method cleans up resources by deleting the shader program with glDeleteProgram. The `ShaderStage` enum defines different shader stages such as vert (vertex), frag (fragment), and comp (compute).

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
