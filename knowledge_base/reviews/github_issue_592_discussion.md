# [issues/issue_592.md] - Issue #592 discussion

**Type:** review
**Keywords:** fog occlusion, biome fog, feasibility, heuristic, transparent rendering, culling
**Concepts:** fog occlusion, biome fog, rendering pipeline

## Summary
The maintainer discusses the feasibility of adding fog occlusion for biome fog, concluding it is not feasible due to the complexity of determining fog density accurately.

## Explanation
The maintainer explains that a simple heuristic, such as assuming the highest biome fog density, would not be accurate because placed blocks can have less dense fog. This makes it impossible to cull objects behind the fog during rendering stages, as the fog density is only known after transparent rendering, which is the last stage.

## Related Questions
- What is the main reason given for not implementing fog occlusion?
- How does the maintainer suggest determining fog density?
- Why is it impossible to cull objects behind the fog during rendering stages?
- What stage of rendering is fog density determined in?
- Can a simple heuristic be used to determine fog density accurately?
- What are the implications of not being able to cull objects based on fog density?

*Source: unknown | chunk_id: github_issue_592_discussion*
