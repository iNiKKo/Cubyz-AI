# [src/particles.zig] - PR #3297 review diff

**Type:** review
**Keywords:** lifeRatio, loopTime, frameCount, currentFrame, frameRate, particle lifecycle, animation tracking
**Symbols:** ParticleSystem, addParticle, lifeTime, density, rot, rotVel, dragCoeff, loopTime, particles, particleCount, pos, typ, currentFrame, frameRate
**Concepts:** Particle System, Lifecycle Management, Animation Tracking

## Summary
Refactored particle system to introduce `currentFrame` and `frameRate` for better tracking of particle lifecycle.

## Explanation
The change renames the `lifeRatio` field to `currentFrame`, which now represents the loop time multiplied by the frame count. Additionally, a new field `frameRate` is introduced, calculated as the reciprocal of lifeTime multiplied by loopTime and frameCount. This refactoring aims to improve the clarity and precision in tracking particle lifecycles, potentially enhancing performance and correctness in particle animations.

## Related Questions
- What is the purpose of renaming `lifeRatio` to `currentFrame`?
- How does the introduction of `frameRate` enhance particle system performance?
- Can you explain the calculation for `loopTime` in the refactored code?
- Why was it necessary to update the field names and calculations in the particle system?
- What are the potential benefits of using `currentFrame` and `frameRate` in particle animations?
- How does this change affect the overall architecture of the particle system?

*Source: unknown | chunk_id: github_pr_3297_comment_3560914855*
