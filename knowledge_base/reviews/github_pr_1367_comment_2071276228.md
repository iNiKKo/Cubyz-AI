# [src/particles.zig] - PR #1367 review diff

**Type:** review
**Keywords:** particle system, SSBO, texture array, shader, memory allocation, collision detection, rendering, ZonElement, animation frames, branch mispredicts
**Symbols:** ParticleManager, ParticleSystem, SSBO, TextureArray, Shader, Image, ZonElement, ColorRGB, Mat4f, Vec3d, Vec3f, Vec3i
**Concepts:** Memory Management, Resource Initialization, Rendering Pipeline, Shader Programming, Particle Simulation

## Summary
The `particles.zig` file introduces a new module for managing particle systems and their rendering in Cubyz. It defines structures like `ParticleManager` and `ParticleSystem`, handles texture loading, SSBO initialization, and updates/rendering logic.

## Explanation
This code snippet is part of the Cubyz game engine's particle system implementation. The `ParticleManager` struct manages various aspects of particles, including their types, textures, and registration from ZonElement configurations. It initializes and deinitializes resources such as SSBOs, texture arrays, and lists for storing particle data. The `ParticleSystem` struct handles the dynamic behavior of particles, including their movement, collision detection, and rendering using shaders. The code includes functions for reading texture data, generating texture arrays, updating particle states, and rendering them. The reviewer notes a potential optimization opportunity by separating colliding particles into a separate array to reduce branch mispredicts.

The `ParticleType` struct contains fields such as `isBlockTexture`, `animationFrames`, `startFrame`, and others that define the properties of each particle type. The default texture for particles is set to 'cubyz:spark', and animation frames are handled by splitting the texture into multiple frames based on the specified number of frames.

Textures are loaded from paths constructed using the module name and texture ID, with both base textures and emission textures being read and stored in separate lists. The shader program for particle rendering is initialized with vertex and fragment shaders located at 'assets/cubyz/shaders/particles/particles.vs' and 'assets/cubyz/shaders/particles/particles.fs', respectively.

The maximum capacity of particles in a single system is set to 65,536. Memory allocation for particle data is handled using the global allocator, with dynamic buffers created for SSBOs to store particle properties. The rendering process involves binding textures and shaders, setting uniform values, and drawing particles using OpenGL commands.

## Related Questions
- What is the purpose of the `ParticleManager` struct in Cubyz?
- How does the `ParticleSystem` handle particle collisions?
- What optimization is suggested for handling colliding particles?
- How are textures loaded and managed in the particle system?
- What role do SSBOs play in the particle rendering process?
- How is the shader program initialized for particle rendering?
- What is the maximum capacity of particles in a single system?
- How does the code handle memory allocation for particle data?
- What are the key components of the `ParticleType` struct?
- How are texture paths constructed and used in the particle system?

*Source: unknown | chunk_id: github_pr_1367_comment_2071276228*
