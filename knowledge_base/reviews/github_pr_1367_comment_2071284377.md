# [src/particles.zig] - PR #1367 review diff

**Type:** review
**Keywords:** particles.zig, ParticleManager, ParticleSystem, SSBO, TextureArray, Shader, Image, ZonElement, ColorRGB, Mat4f, Vec3d, Vec3f, Vec3i
**Symbols:** ParticleManager, ParticleSystem, SSBO, TextureArray, Shader, Image, ZonElement, ColorRGB, Mat4f, Vec3d, Vec3f, Vec3i
**Concepts:** Memory Management, Graphics Rendering, Particle System, Shader Programming, Texture Handling

## Summary
The `particles.zig` file introduces a new module for managing and rendering particles in the Cubyz game engine. It defines structures like `ParticleManager` and `ParticleSystem`, handles texture loading, SSBO initialization, and particle updates and rendering.

## Explanation
This code snippet is part of the Cubyz game engine's particle system implementation. The `ParticleManager` struct manages different types of particles, including their textures and properties. It initializes various lists and allocators to handle memory efficiently. The `ParticleSystem` struct handles the actual particles, managing their lifecycle, updating their positions based on physics, and rendering them using shaders.

The `ParticleManager` struct includes methods for registering particle types, reading texture data, generating texture arrays, and handling particle updates and rendering. It uses an SSBO to store particle types and a TextureArray to manage textures efficiently.

The `ParticleSystem` struct has a maximum capacity of 65536 particles. It manages the lifecycle of particles, updating their positions based on physics properties such as gravity (0, 0, 4), drag (2), lifeTimeMin (5), lifeTimeMax (5), velMin (5), and velMax (10). The struct uses a shader for rendering particles, with uniforms for projection matrix, view matrix, billboard matrix, player position, ambient light, texture sampler, and emission texture sampler.

The code includes functions for reading texture data, generating texture arrays, and handling particle updates and rendering. It also mentions a potential optimization opportunity regarding collision detection and suggests allocating different buffers for particles with different behaviors.

## Related Questions
- What is the purpose of the `ParticleManager` struct in Cubyz?
- How does the `ParticleSystem` handle particle updates and rendering?
- What optimization opportunity is mentioned regarding collision detection?
- How are textures managed in the particle system?
- What role do SSBOs play in this implementation?
- How are shaders used for rendering particles?
- What is the maximum capacity of particles in Cubyz?
- How does the code handle memory allocation and deallocation for particles?
- What is the structure of the `UniformStruct` used in particle rendering?
- How are textures loaded and sliced for animation frames?

*Source: unknown | chunk_id: github_pr_1367_comment_2071284377*
