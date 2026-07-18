# [issues/issue_133.md] - Issue #133 discussion

**Type:** review
**Keywords:** greedy meshing, transparent blocks, triangle counts, fragment shader cost, speedup, laptop performance, light data resampling, internal leaf culling, mesh memory usage, data per face
**Symbols:** greedy_meshing, fragment_shader, light_data_resampling, internal_leaf_culling
**Concepts:** mesh optimization, rendering performance, CPU-side storage, face count reduction, memory usage

## Summary
The discussion revolves around the feasibility of implementing greedy meshing to optimize block updates and reduce rendering costs, but ultimately concludes that it may not provide significant benefits due to increased meshing cost and reduced face count reduction.

## Explanation
The maintainers initially considered implementing greedy meshing to optimize block updates and reduce rendering costs for transparent blocks like water or fog. However, they found that the fragment shader cost of greedy meshing was high, resulting in only a minimal speedup (0-20%) on their GPU and even slower performance on laptops. They also explored other solutions for performance and memory usage optimization. A reconsideration suggested using greedy meshing to improve CPU-side mesh storage by better caching light data samples, but testing showed no significant reduction in the number of samples needed. The main issue was that greedy meshing did not effectively reduce face counts; it only halved them at best, duplicating 2/6th of the corners. Additionally, there were some more rendering improvements (internal leaf culling), making greedy meshing even less viable for actual rendering due to increased data per face and higher mesh memory usage.

## Related Questions
- What was the primary reason for deprioritizing greedy meshing?
- How did greedy meshing affect the number of light data samples needed?
- What were the additional rendering improvements that made greedy meshing less viable?
- How did optimized mesh memory usage impact the effectiveness of greedy meshing?
- What is the current bottleneck in block updates regarding light data resampling?

*Source: unknown | chunk_id: github_issue_133_discussion*
