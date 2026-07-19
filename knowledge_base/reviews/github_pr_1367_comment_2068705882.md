# [src/particles.zig] - PR #1367 review diff

**Type:** review
**Keywords:** particles, particle management, heap allocation, static array, performance, memory optimization, resource initialization, deinitialization, texture handling, shader integration
**Symbols:** ParticleManager, SSBO, TextureArray, Shader, Image, ZonElement, ParticleSystem, ParticleType, ColorRGB, Mat4f, Vec3d, Vec3f, Vec3i
**Concepts:** Memory Management, Performance Optimization, Resource Management

## Summary
Added a new `particles.zig` file with a `ParticleManager` struct for managing particle systems. The review suggests changing the dynamic allocation of particles to a static array.

## Explanation
The added `particles.zig` file introduces a comprehensive system for managing particles in Cubyz, including initialization, deinitialization, registration of particle types, and rendering. The reviewer points out that the current implementation heap-allocates the `particles` array, which could lead to performance overhead and potential memory fragmentation. The suggestion is to replace this with a static array to improve performance and reduce allocation costs.

The `ParticleManager` struct manages various aspects of particle systems, including:
- Initialization and deinitialization of resources such as SSBOs, texture arrays, and lists for textures and emission textures.
- Registration of particle types using the `register` function, which reads configuration from a `ZonElement` and loads textures accordingly.
- Processing of texture files for animation frames in the `readTextureData` function.
- Generation of texture arrays in the `generateTextureArray` function to optimize rendering.
- Updating particle states over time with the `update` function.
- Rendering particles with the `render` function, taking into account player position and ambient light.

The `register` function handles particle type registration by:
- Extracting configuration values such as `isBlockTexture`, `animationFrames`, and texture paths from a `ZonElement`.
- Loading base and emission textures based on the provided path and handling animation frames.

The `readTextureData` function processes texture files for animation frames by:
- Reading base and emission textures using the `readTextureFile` function.
- Extracting individual animation slices from the loaded images using the `extractAnimationSlice` function.

The `generateTextureArray` function plays a crucial role in the particle system by:
- Generating texture arrays for both regular and emission textures.
- Setting texture parameters such as anisotropic filtering.

The `update` function is used to update particle states over time by:
- Converting the `deltaTime` parameter to a `f32` value.
- Updating the particle system with the calculated delta time.

The `render` function in the particle system is responsible for:
- Rendering particles based on the player's position and ambient light conditions.

Textures and emission textures are managed within the `ParticleManager` by:
- Storing texture IDs, images, and emission images in respective lists.
- Generating texture arrays from these lists to optimize rendering performance.

The `ParticleSystem` struct is significant in the overall particle management system as it handles the actual particles, including their storage, update, and rendering processes.

## Related Questions
-  What is the purpose of the `ParticleManager` struct in Cubyz?
-  How does the `register` function handle particle type registration?
-  Why is there a suggestion to change the dynamic allocation of particles to a static array?
-  What are the benefits of using a static array for particle storage?
-  How does the `readTextureData` function process texture files for animation frames?
-  What role does the `generateTextureArray` function play in the particle system?
-  How is the `update` function used to update particle states over time?
-  What is the purpose of the `render` function in the particle system?
-  How are textures and emission textures managed within the `ParticleManager`?
-  What is the significance of the `ParticleSystem` struct in the overall particle management system?

*Source: unknown | chunk_id: github_pr_1367_comment_2068705882*
