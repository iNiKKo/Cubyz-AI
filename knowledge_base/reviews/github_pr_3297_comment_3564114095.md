# [src/particles.zig] - PR #3297 review diff

**Type:** review
**Keywords:** architectural review, memory efficiency, struct storage, type index, dynamic data access
**Symbols:** DirectionMode, Emitter, particleTypeLocal, ParticleTypeLocal, particleType, ParticleType
**Concepts:** memory optimization, data structure design

## Summary
The `Emitter` struct now stores both `particleTypeLocal` and `particleType`, with a critical architectural review suggesting to store only the type index for efficiency.

## Explanation
The reviewer points out that storing copies of large structs (`ParticleTypeLocal`) in the `Emitter` struct is inefficient. The suggestion is to store only the type index, allowing the rest of the data to be dynamically read from an array. This change aims to optimize memory usage and potentially improve performance by reducing redundancy.

## Related Questions
- Why is storing a copy of large structs in the Emitter struct considered inefficient?
- What is the suggested alternative to storing copies of large structs in the Emitter struct?
- How does storing only the type index and dynamically accessing data from an array improve memory usage?
- What potential performance benefits could come from reducing redundancy in the Emitter struct?
- Can you explain the architectural reasoning behind the reviewer's suggestion for optimizing the Emitter struct?
- How might this change impact the overall design of the particles system in Cubyz?

*Source: unknown | chunk_id: github_pr_3297_comment_3564114095*
