# [issues/issue_438.md] - Issue #438 discussion

**Type:** review
**Keywords:** frame time graph, average frames, second line, refresh rate, lag spikes, benchmarking, optimization
**Concepts:** frame rate monitoring, graph visualization, performance optimization

## Summary
The discussion revolves around adding an average of x frames into the frame time graph, with suggestions for implementation details and user feedback.

## Explanation
The issue primarily focuses on enhancing the frame time graph by averaging a specified number of frames (initially suggested as 12) to provide a smoother representation. The maintainer suggests adding this average as a second line in the graph, possibly with a different color, to maintain visibility of small lag spikes while offering an overall trend. There is also discussion about the refresh rate of the graph updates and whether it should be based on time or frame count. The user proposes expanding the issue to encompass all benchmarks for optimization purposes but is advised that this would be better handled as a separate issue.

## Related Questions
- What is the suggested number of frames to average in the frame time graph?
- How should the average be represented on the graph?
- Why is it important to maintain visibility of small lag spikes?
- What are the considerations for the refresh rate of the graph updates?
- Is there any concern about the readability of the graph at high refresh rates?
- How does the maintainer view the usefulness of adding an average line to the frame time graph?

*Source: unknown | chunk_id: github_issue_438_discussion*
