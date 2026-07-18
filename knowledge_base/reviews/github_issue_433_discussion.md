# [issues/issue_433.md] - Issue #433 discussion

**Type:** review
**Keywords:** performance metrics, threadpool tasks, average time per task, total execution time, getTaskId, VTable, chunk generation, lighting, task differentiation, new tasks
**Symbols:** chunkgen, lighting, VTable, getTaskId
**Concepts:** thread safety, performance optimization, task management

## Summary
Discussion on adding performance metrics for threadpool tasks, focusing on average time per task and total execution time.

## Explanation
Discussion on adding performance metrics for threadpool tasks within Cubyz. The goal is to optimize these tasks by understanding their execution times, specifically focusing on average time per task and total execution time. Users propose splitting the tasks into categories such as chunk generation (chunkgen) and lighting. Maintainers suggest adding a `getTaskId` method to the VTable to differentiate between tasks for better performance analysis. However, there is concern that this might complicate the addition of new tasks in the future. The maintainer notes that each chunk has two tasks: one for lighting/meshing and another for generation, with lighting taking a significant portion of the combined time.

## Related Questions
- How can we implement the `getTaskId` method in the VTable to differentiate between threadpool tasks?
- What are the potential impacts on adding new tasks if we introduce a `getTaskId` method?
- How can we ensure that the performance metrics for threadpool tasks remain stable and useful over time?
- What other methods could be used to optimize the execution of chunk generation and lighting tasks in Cubyz?
- Can you provide a detailed breakdown of how the `getTaskId` method would interact with existing task management systems in Cubyz?

*Source: unknown | chunk_id: github_issue_433_discussion*
