# [issues/issue_2848.md] - Issue #2848 discussion

**Type:** review
**Keywords:** unlimited chunk requests, high memory usage, chunkRequest.serverReceive, queueChunkAndDecreaseRefCount, isStillNeeded, render distance, RAM spikes, memory footprint, task allocation, caches
**Symbols:** chunkRequest.serverReceive, queueChunkAndDecreaseRefCount, isStillNeeded
**Concepts:** memory management, task creation, caching

## Summary
The server accepts unlimited chunk requests, leading to high memory usage due to task creation and caching.

## Explanation
The issue arises from the **chunkRequest.serverReceive()** function in **src/network/protocols.zig**, which processes chunk requests without any limit. Although **queueChunkAndDecreaseRefCount** uses **isStillNeeded()** for filtering, all tasks are created and allocated before this filter is applied, resulting in significant memory usage. The maintainer notes that the memory footprint of these tasks is around 1 megabyte each, but the observed high memory usage is due to growing caches. Beyond a certain point (around ~8 GB), additional memory usage increases are minimal with more users joining.

## Related Questions
- How does the server handle chunk requests with varying render distances?
- What is the impact of task creation and caching on memory usage in Cubyz?
- Why are all tasks created before filtering in **queueChunkAndDecreaseRefCount**?
- How can the server be modified to limit the number of chunk requests accepted?
- What measures can be taken to prevent excessive memory usage due to chunk requests?
- How does the current implementation affect performance with high render distances?
- Is there a way to optimize task creation and allocation in **chunkRequest.serverReceive**?
- What are the potential consequences of unlimited chunk requests on server stability?
- How can the maintainer's comment about memory footprint be verified?
- Are there any existing mechanisms to control the number of concurrent tasks?

*Source: unknown | chunk_id: github_issue_2848_discussion*
