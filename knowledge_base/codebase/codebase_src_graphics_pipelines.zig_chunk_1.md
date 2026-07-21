# [hard/codebase_src_graphics_pipelines.zig] - Chunk 1

**Type:** api
**Keywords:** GLSL, SPIR-V, shader linking, uniforms, Vulkan API
**Symbols:** Shader, Shader.id, Shader.ShaderStage, Shader.compileToSpirV, Shader.addShader, Shader.link, Shader.init, Shader.initCompute, Shader.createShaderModule, Shader.bind, Shader.deinit
**Concepts:** shader management, GLSL compilation, SPIR-V generation, Vulkan shader modules

## Summary
The `Shader` struct manages shader compilation, linking, and usage in a graphics pipeline. It includes methods for compiling GLSL source to SPIR-V, adding shaders to a program, linking programs, initializing vertex and compute shaders, creating Vulkan shader modules, binding shaders for use, and deinitializing resources.

## Explanation
The `Shader` struct manages shader compilation, linking, and usage in a graphics pipeline. It includes methods for compiling GLSL source to SPIR-V, adding shaders to a program, linking programs, initializing vertex and compute shaders, creating Vulkan shader modules, binding shaders for use, and deinitializing resources.

The `loadShaderFile` function reads shader files, processes them with defines, and handles nested includes. It takes parameters such as allocator (a NeverFailingAllocator), filename (the name of the shader file), and defines (additional preprocessor definitions as a slice of u8). The function returns a slice of u8 representing the processed shader source code.

The `compileToSpirV` function handles the conversion of GLSL code into SPIR-V format using glslang. It takes parameters such as allocator (a NeverFailingAllocator), source (the GLSL source code as a slice of u8), filename (the name of the shader file), defines (additional preprocessor definitions as a slice of u8), and shaderStage (an enum value specifying the shader stage). The function returns a slice of c_uint representing the compiled SPIR-V code.

The `addShader` method compiles individual shaders and attaches them to a program. It reads the shader file, sets up the shader source with defines, compiles the shader using glCompileShader, and attaches it to the program using glAttachShader. The method takes parameters such as filename (the name of the shader file), defines (additional preprocessor definitions), and shaderStage (an enum value specifying the shader stage).

The `link` method links all added shaders into a complete shader program. If linking fails, it logs an error message detailing the issue.

The `init` and `initCompute` functions set up vertex and compute shaders, respectively, by adding and linking shaders and setting uniform locations. They take parameters such as filenames (the names of the shader files), defines (additional preprocessor definitions), and a uniform struct (a struct containing uniform variable locations). These functions return a Shader instance.

The `createShaderModule` function creates Vulkan shader modules from SPIR-V code. It reads the shader file, compiles it to SPIR-V using compileToSpirV, and then creates a Vulkan shader module using vkCreateShaderModule. The method takes parameters such as path (the path to the shader file), defines (additional preprocessor definitions), and stage (an enum value specifying the shader stage). It returns a c.VkShaderModule.

The `bind` method activates the shader program for rendering by calling glUseProgram with the shader's ID.

The `deinit` method cleans up resources by deleting the shader program with glDeleteProgram.

The `ShaderStage` enum defines different shader stages such as vert (vertex), frag (fragment), and comp (compute).

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
