# [issues/issue_1525.md] - Issue #1525 discussion

**Type:** review
**Keywords:** desert dust, block dust, wind, particle behavior, acceleration, gravity, bouncing, disappearing
**Concepts:** particle physics, wind simulation, gravity

## Summary
The issue discusses the behavior of desert dust particles in windy conditions, including their acceleration, gravity effects, and bouncing mechanics.

## Explanation
The issue discusses the behavior of desert dust particles in windy conditions. Specifically, on windy days, sand will produce a 1x1 pixel particle that starts slow and accelerates to match the wind's speed. The particle is affected by gravity and has specific rules for disappearing or bouncing upon contact with the ground: it has a 50% chance of disappearing or bouncing when touching the ground, and after two bounces, it will have a 100% chance of disappearing. When the particle bounces, it loses some velocity but quickly regains speed from the wind.

## Related Questions
- What is the probability of a particle disappearing after touching the ground?
- How many times can a particle bounce before it disappears completely?
- Does the particle lose any velocity when it bounces and how does it regain speed?

*Source: unknown | chunk_id: github_issue_1525_discussion*
