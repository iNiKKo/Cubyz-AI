# [issues/issue_133.md] - Issue #133 discussion

**Type:** review
**Keywords:** greedy meshing, transparent blocks, triangle counts, fragment shader cost, speedup, laptop performance, light data resampling, internal leaf culling, mesh memory usage, data per face
**Symbols:** greedy_meshing, fragment_shader, light_data_resampling, internal_leaf_culling
**Concepts:** mesh optimization, rendering performance, CPU-side storage, face count reduction, memory usage

## Summary
The discussion revolves around the feasibility of implementing greedy meshing to optimize block updates and reduce rendering costs, but ultimately concludes that it may not provide significant benefits due to increased meshing cost and reduced face count reduction.

## Explanation
The maintainers initially considered greedy meshing for its potential to reduce triangle counts in transparent blocks like water or fog. However, they found that the fragment shader cost of greedy meshing was high, resulting in only a minimal speedup (0-20%) and even slower performance on laptops. They also explored other solutions for performance and memory usage optimization. A reconsideration suggested using greedy meshing to improve CPU-side mesh storage by better caching light data samples, but testing showed no significant reduction in the number of samples needed. The main issue was that greedy meshing did not effectively reduce face counts, and additional rendering improvements further reduced its viability. Furthermore, optimized mesh memory usage made greedy meshing result in more data per face.

## Related Questions
- What was the primary reason for deprioritizing greedy meshing?
- How did greedy meshing affect the number of light data samples needed?
- What were the additional rendering improvements that made greedy meshing less viable?
- How did optimized mesh memory usage impact the effectiveness of greedy meshing?
- What is the current bottleneck in block updates regarding light data resampling?
- How does greedy meshing compare to other approaches for performance optimization?
- What are the potential benefits of using greedy meshing for CPU-side mesh storage?
- What was the observed speedup with greedy meshing on different hardware configurations?
- How did the depth prepass contribute to offsetting the cost of greedy meshing?
- What is the relationship between face count reduction and rendering performance in greedy meshing?

*Source: unknown | chunk_id: github_issue_133_discussion*
