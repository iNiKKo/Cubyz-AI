# [issues/issue_1525.md] - Issue #1525 discussion

**Type:** review
**Keywords:** desert dust, block dust, wind, particle behavior, acceleration, gravity, bouncing, disappearing
**Concepts:** particle physics, wind simulation, gravity

## Summary
The issue discusses the behavior of desert dust particles in windy conditions, including their acceleration, gravity effects, and bouncing mechanics.

## Explanation
The discussion revolves around how desert dust particles should behave when wind is implemented. The particles are described to start slow, accelerate to match the wind's speed, be affected by gravity, and have specific rules for disappearing or bouncing upon contact with the ground. The maintainer asks if bouncing results in spawning a new particle.

## Related Questions
- How does the particle's velocity change when it bounces?
- What is the probability of a particle disappearing after touching the ground?
- Is there any code that currently simulates wind effects on particles?
- How does gravity affect the particle's trajectory in windy conditions?
- Does the particle's behavior differ based on the strength of the wind?
- Are there any plans to implement additional environmental factors for particle interactions?

*Source: unknown | chunk_id: github_issue_1525_discussion*
