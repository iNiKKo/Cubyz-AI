# [src/particles.zig] - Chunk 3564114095

**Type:** review
**Keywords:** struct, memory usage, performance, optimization, type index, dynamic read
**Symbols:** DirectionMode, Emitter, ParticleTypeLocal, ParticleType
**Concepts:** memory optimization, data redundancy

## Summary
The Emitter struct now stores both `particleTypeLocal` and `particleType`, with a review suggesting to store only the type index for efficiency.

## Explanation
The reviewer points out that storing copies of large structs (`ParticleTypeLocal`) in the `Emitter` struct is inefficient. The suggestion is to store only the type index, allowing the rest of the data to be dynamically read from an array. This change aims to optimize memory usage and potentially improve performance by reducing redundant data storage.

## Related Questions
- Why is storing a copy of large structs in the Emitter struct considered inefficient?
- What are the potential benefits of storing only the type index instead of the full struct?
- How might dynamically reading from an array impact performance?
- Can you explain the trade-offs between memory usage and access speed in this context?
- What is the purpose of the `particleTypeLocal` field in the Emitter struct?
- How does the suggested change affect the overall architecture of the particles system?

*Source: unknown | chunk_id: github_pr_3297_comment_3564114095*
