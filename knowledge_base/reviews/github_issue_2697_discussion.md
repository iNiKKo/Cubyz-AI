# [issues/issue_2697.md] - Issue #2697 discussion

**Type:** review
**Keywords:** wall placement mode, mushrooms, spikes, floor, ceiling, solid points, implementation complexity
**Concepts:** engine architecture, structure placement

## Summary
Discussion on adding a wall placement mode for structures like mushrooms and spikes.

## Explanation
Discussion on adding a wall placement mode for structures like mushrooms and spikes. The maintainers note that while floor and ceiling modes are relatively straightforward to implement due to the ease of finding solid points above or below, wall placement is more challenging because identifying the next solid point to the left or right is difficult. Specifically, the maintainers hope that existing floor/ceiling modes could adequately cover wall placements despite these challenges.

## Related Questions
- What are the current challenges in implementing wall placement mode?
- How does the maintainers' hope for floor/ceiling modes cover wall placements?
- Can you explain the difficulty in finding solid points to the left or right?
- Are there any potential performance implications of adding wall placement mode?
- What other structure types might benefit from wall placement mode?
- How could existing modes be adapted to support wall placements?
- Is there a plan to prioritize the implementation of wall placement mode?
- What are the expected benefits of adding wall placement mode?
- Are there any architectural considerations for implementing this feature?
- How will the addition of wall placement mode affect user experience?

*Source: unknown | chunk_id: github_issue_2697_discussion*
