# [issues/issue_2741.md] - Issue #2741 discussion

**Type:** review
**Keywords:** CDN, assets, gameplay server, external sources, GitHub
**Concepts:** asset management, server-client architecture, content delivery networks

## Summary
Discussion about offloading asset serving from gameplay server to CDNs or external sources.

## Explanation
The issue discusses the current practice where servers send all assets to clients upon joining, which puts unnecessary load on the gameplay server. The suggestion is to allow servers to specify CDN links for clients to fetch assets directly, potentially even fetching addons from platforms like GitHub. The maintainer notes that asset sizes are generally small compared to chunk data.

## Related Questions
- What are the potential benefits of using CDNs for asset distribution in Cubyz?
- How would implementing CDN support impact the current server-client architecture?
- Are there any concerns about security or reliability when fetching assets from external sources like GitHub?
- How can we ensure compatibility with existing servers that do not use CDNs?
- What are the performance implications of offloading asset serving to CDNs?
- How would this change affect the maintenance and scalability of the server infrastructure?

*Source: unknown | chunk_id: github_issue_2741_discussion*
