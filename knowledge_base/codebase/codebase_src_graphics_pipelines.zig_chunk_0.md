# [hard/codebase_src_graphics_pipelines.zig] - Chunk 0

**Type:** implementation
**Keywords:** glslang, SPIR-V, vertex shader, fragment shader, compute shader, link program, compile status, uniform location, error handling
**Symbols:** Shader, ShaderStage
**Concepts:** shader compilation, SPIR-V generation, GLSL preprocessing, uniform location binding, error logging

## Summary
This chunk defines the Shader struct and its methods for compiling GLSL to SPIR-V (via glslang) and linking OpenGL shaders, including helper functions addShader, link, init, and initCompute.

## Explanation
The chunk declares a top-level const Shader struct with an id field of type c_uint. It defines an enum ShaderStage mapping GLSLANG_* constants to vert, frag, comp. The compileToSpirV function takes an allocator, source string, filename, defines, and shaderStage; it extracts the version line, builds a main.ListManaged(u8) buffer with version+defines+source+null terminator, constructs a c.glslang_input_t struct (language GLSL, stage from enum, client VULKAN, target SPV 1.0), calls glslang_shader_create, preprocesses and parses the shader, logs errors via std.log.err if preprocessing or parsing fails returning error.FailedCompiling, creates a program, adds the shader, links with GLSLANG_MSG_SPV_RULES_BIT | GLSLANG_MSG_VULKAN_RULES_BIT (logging on failure), generates SPIR-V, allocates output bytes via allocator.alloc(c_uint, ...) and copies them using glslang_program_SPIRV_get. The addShader method reads a file from main.files.cwd(), extracts version line similarly, creates an OpenGL shader with c.glCreateShader(shaderStage), sets source with glShaderSource (3 parts: version, defines, source), compiles, checks GL_COMPILE_STATUS, logs error and returns error.FailedCompiling on failure, then attaches the compiled shader to self.id. The link method calls glLinkProgram(self.id), checks GL_LINK_STATUS, logs error and returns error.FailedLinking if bad. The init function creates a Shader with id from c.glCreateProgram(), adds vertex and fragment shaders via addShader (catch return shader on failure), links via link (catch return shader), then optionally populates uniform locations by iterating struct fields of type c_int and calling glGetUniformLocation, returning the initialized Shader. The initCompute function mirrors init but only adds a compute shader and does not attach it to any existing program; it also handles optional uniform structs similarly.

## Related Questions
- How does compileToSpirV handle shader preprocessing errors?
- What happens if glslang_shader_preprocess returns zero in compileToSpirV?
- Which GLSLANG_* constants are used to configure the input struct for Vulkan SPIR-V generation?
- Does addShader attach its compiled shader to an existing program or create a new one?
- How does init populate uniform locations when a non-null uniformStruct is provided?
- What error type is returned if glLinkProgram fails in the link method?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_0*
