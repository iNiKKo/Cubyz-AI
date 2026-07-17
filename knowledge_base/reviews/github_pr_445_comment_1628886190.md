# [src/renderer/chunk_meshing.zig] - Chunk 1628886190

**Type:** review
**Keywords:** ChunkMesh, taskType, .lighting, LightRefreshTask, performance, masking, aggregation, profiling, heterogeneous, workload
**Symbols:** ChunkMesh, taskType, .lighting, LightRefreshTask
**Concepts:** task tagging, performance masking, architectural grouping, profiling accuracy, heterogeneous workload aggregation

## Summary
The diff adds a `taskType = .lighting` field to the ChunkMesh struct's task list, but the reviewer warns that multiple tasks sharing the same `.lighting` tag can mask performance issues because they perform different operations.

## Explanation
Architecturally, the code introduces a new entry in the ChunkMesh's task array with `taskType = .lighting`. The reviewer’s concern is that this tagging scheme groups heterogeneous workloads under a single label. Since each `.lighting` task may have vastly different execution times (e.g., LightRefreshTask being fast), aggregating them can skew measured averages and hide bottlenecks in slower lighting tasks. This design choice risks obscuring performance regressions during profiling or benchmarking, making it harder to identify which specific lighting operation is consuming time.

## Related Questions
- What other tasks are currently tagged with `.lighting` in ChunkMesh?
- How does the current task execution order affect performance measurement for lighting tasks?
- Is there a way to differentiate between fast and slow lighting tasks without changing their tag?
- Could introducing separate tags (e.g., `.lighting_refresh`, `.lighting_compute`) resolve the masking issue?
- What metrics are used to evaluate mesh generation time, and how does task tagging influence them?
- Are there any existing profiling tools in the codebase that aggregate tasks by type?
- How might this change impact backward compatibility with older versions of ChunkMesh?
- Is there a risk that future lighting tasks will be added under `.lighting` without proper performance analysis?
- What is the expected distribution of execution times among all `.lighting` tasks?
- Could lazy evaluation or batching help mitigate the skew caused by fast tasks?

*Source: unknown | chunk_id: github_pr_445_comment_1628886190*
