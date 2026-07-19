# [issues/issue_748.md] - Issue #748 discussion

**Type:** review
**Keywords:** render distance limit, server-side, stability, resources, network protocol
**Concepts:** server stability, resource usage, network speed

## Summary
Discussion on server-side render distance limit to improve stability and resource usage.

## Explanation
Discussion on server-side render distance limit to improve stability and resource usage, particularly addressing network speed issues when sending chunks to newly joined players. The maintainer notes that with improvements to the network protocol, such as more efficient data compression and reduced packet size, this issue is less of a concern now.

## Related Questions
- What are the current improvements in the network protocol that have reduced the issue?
- How does the server-side render distance limit improve stability?
- What specific resources are being targeted for optimization with this change?
- Are there any potential regressions to consider when implementing the render distance limit?
- How does the network speed benefit from limiting the render distance?
- What is the impact of the render distance limit on newly joined players?

*Source: unknown | chunk_id: github_issue_748_discussion*
