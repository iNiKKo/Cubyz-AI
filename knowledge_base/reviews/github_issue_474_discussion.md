# [issues/issue_474.md] - Issue #474 discussion

**Type:** review
**Keywords:** fogPersistance, fogEfficiency, percentage-based system, per-biome setting, visual effects
**Concepts:** day-night cycle, biome fog, user customization

## Summary
Discussion on making biome fog effects adjustable independently of the day-night cycle.

## Explanation
The discussion revolves around modifying the behavior of biome fog so that it is not uniformly affected by the day-night cycle. The maintainer suggests implementing a percentage-based system where users can specify how much the fog is influenced by the time of day, ranging from no effect (0.00) to full effect (1.00). This allows for fine-grained control over the visual effects based on the time of day. Additionally, another suggestion is to make this setting configurable on a per-biome basis, which could offer even more granular control over the visual effects in different environments.

## Related Questions
- What is the current implementation of fog effect in relation to the day-night cycle?
- How can we implement a percentage-based control for biome fog effects?
- What are the potential performance implications of adding per-biome fog settings?
- Can you provide examples of how other games handle biome-specific visual effects?
- How will this change affect backwards compatibility with existing biomes?
- What are the architectural considerations for making these changes in a multi-threaded environment?

*Source: unknown | chunk_id: github_issue_474_discussion*
