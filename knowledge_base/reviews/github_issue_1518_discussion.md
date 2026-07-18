# [issues/issue_1518.md] - Issue #1518 discussion

**Type:** review
**Keywords:** block hitting particles, crosshair, texture, swing speed, cone shape, bounce, disappear, center breaking, ID space, ticking bomb, u32, u24, multiple particles
**Concepts:** ID space management, particle system

## Summary
The discussion revolves around the implementation of block hitting particles and potential issues with the current ID system for particles.

## Explanation
The issue describes the spawning of particles when a block is hit, which are derived from the block's texture. The number and speed of these particles depend on the strength and swing speed of the tool used. The particles move towards the player in a cone shape, bounce once or twice based on the block type, and disappear shortly after landing. The maintainer points out that other players breaking blocks appear to break them from the center, suggesting a potential issue with particle emission direction. Additionally, there is a concern about the ID space for particles being similar to that of blocks, which could lead to running out of particle IDs before block IDs, creating a 'ticking bomb' in the ID system. The maintainer suggests increasing the integer type used for particle types to u32 or u24 to prevent this issue and warns that adding multiple particles per block exacerbates the problem of exhausting particle ID space.

## Related Questions
- What is the current implementation of particle emission direction when a block is hit?
- How does the number and speed of particles depend on the tool used?
- What is the potential issue with other players breaking blocks from the center?
- Why is there a concern about the ID space for particles being similar to that of blocks?
- What solution is suggested to prevent running out of particle IDs before block IDs?
- How does adding multiple particles per block exacerbate the problem of exhausting particle ID space?

*Source: unknown | chunk_id: github_issue_1518_discussion*
