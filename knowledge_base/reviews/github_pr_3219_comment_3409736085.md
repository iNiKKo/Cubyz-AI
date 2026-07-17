# [src/server/server.zig] - Chunk 3409736085

**Type:** review
**Keywords:** deinit, threadPool, clear, race condition, connectionManager, players, disconnected, playerJobQueue, wait, threads, cleanup
**Symbols:** init, deinit, main.threadPool.clear, connectionManager.deinit
**Concepts:** race condition, thread pool lifecycle, resource cleanup order, player job queue draining, concurrent task execution

## Summary
The deinit function now clears main.threadPool, but a reviewer flags a race condition where clients may start new tasks before connectionManager.deinit completes.

## Explanation
The original deinit unconditionally cleared the entire thread pool. This is unsafe because other threads (e.g., client handling) might still be enqueuing jobs or executing them when deinit runs, leading to use-after-free or lost work. The reviewer points out that the safer approach is to only drain tasks associated with disconnected players—clearing playerJobQueue and waiting for in-flight tasks to finish—rather than nuking the whole pool. This preserves correctness under concurrent client activity and avoids unnecessary shutdown of threads that may still be needed for cleanup.

## Related Questions
- What is the exact sequence of calls that leads to the race condition in deinit?
- Which threads are allowed to enqueue jobs after connectionManager.deinit starts?
- How does clearing playerJobQueue differ from clearing main.threadPool.clear?
- Is there a guarantee that all client tasks finish before deinit runs?
- What happens if a new task is submitted while the thread pool is being cleared?
- Does the current implementation wait for in-flight tasks to complete before returning from deinit?
- Are there any other places where main.threadPool.clear is called besides deinit?
- How does the reviewer propose to handle tasks that are currently running on disconnected players?
- What synchronization primitives protect playerJobQueue and main.threadPool?
- Is there a possibility of memory leaks if we only clear playerJobQueue without draining the pool?

*Source: unknown | chunk_id: github_pr_3219_comment_3409736085*
