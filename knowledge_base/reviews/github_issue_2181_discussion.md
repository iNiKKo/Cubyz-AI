# [issues/issue_2181.md] - Issue #2181 discussion

**Type:** review
**Keywords:** CI compile targets, baseline x86_64, Sandybridge, Alderlake, chunk loading, opaque faces counter, real optimizations, render thread performance
**Concepts:** CPU optimization, compilation targets, performance benchmarking

## Summary
The issue discusses changing the CI compile target from `baseline` x86_64 to Sandybridge or building a legacy package for older CPUs, based on performance comparisons.

## Explanation
The discussion revolves around optimizing Cubyz's compilation targets to leverage newer CPU features, which could potentially improve performance. The user provides benchmarks showing that targeting Sandybridge or native (Alderlake) processors results in faster chunk loading and less fluctuation in opaque faces counter compared to the baseline target. The maintainer suggests focusing on real optimizations like improving render thread performance instead of changing compilation targets, emphasizing that users can compile for their specific hardware with a mod loader.

## Related Questions
- What are the potential benefits of changing the CI compile target to Sandybridge?
- How does targeting native (Alderlake) processors compare to Sandybridge in terms of performance?
- Why does the maintainer suggest focusing on real optimizations instead of changing compilation targets?
- Can users currently compile Cubyz for their specific hardware, and how?
- What are the implications of building a legacy package for older CPUs?
- How do the performance benchmarks provided by the user support the argument for changing compilation targets?

*Source: unknown | chunk_id: github_issue_2181_discussion*
