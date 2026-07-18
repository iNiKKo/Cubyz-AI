# [src/particles.zig] - PR #1367 review diff

**Type:** review
**Keywords:** particles, particle management, heap allocation, static array, performance, memory optimization, resource initialization, deinitialization, texture handling, shader integration
**Symbols:** ParticleManager, SSBO, TextureArray, Shader, Image, ZonElement, ParticleSystem, ParticleType, ColorRGB, Mat4f, Vec3d, Vec3f, Vec3i
**Concepts:** Memory Management, Performance Optimization, Resource Management

## Summary
Added a new `particles.zig` file with a `ParticleManager` struct for managing particle systems. The review suggests changing the dynamic allocation of particles to a static array.

## Explanation
The added `particles.zig` file introduces a comprehensive system for managing particles in Cubyz, including initialization, deinitialization, registration of particle types, and rendering. The reviewer points out that the current implementation heap-allocates the `particles` array, which could lead to performance overhead and potential memory fragmentation. The suggestion is to replace this with a static array to improve performance and reduce allocation costs.

## Related Questions
- What is the purpose of the `ParticleManager` struct in Cubyz?
- How does the `register` function handle particle type registration?
- Why is there a suggestion to change the dynamic allocation of particles to a static array?
- What are the benefits of using a static array for particle storage?
- How does the `readTextureData` function process texture files for animation frames?
- What role does the `generateTextureArray` function play in the particle system?
- How is the `update` function used to update particle states over time?
- What is the purpose of the `render` function in the particle system?
- How are textures and emission textures managed within the `ParticleManager`?
- What is the significance of the `ParticleSystem` struct in the overall particle management system?

*Source: unknown | chunk_id: github_pr_1367_comment_2068705882*
