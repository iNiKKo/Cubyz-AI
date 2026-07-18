# [issues/issue_819.md] - Issue #819 discussion

**Type:** review
**Keywords:** MTU, Path MTU Discovery, RFC 8899, probe messages, padding data, client hello, server hello, network capacity, endpoint processing, slow protocol
**Concepts:** Path MTU Discovery, RFC 8899, MTU reduction detection

## Summary
The discussion revolves around implementing Path MTU discovery in Cubyz, considering both temporary fixes and more robust solutions like RFC 8899. The main points include setting a minimum MTU, using padding for probe messages, and ensuring proper handling of MTU reductions.

## Explanation
The issue highlights the need for Path MTU discovery to handle varying network conditions without significantly impacting performance. The user proposes a temporary fix where the client dictates the MTU size through progressively smaller packets until a successful connection is established. This approach builds a foundation for variable MTUs, which is essential for constant MTU discovery. The maintainer considers this if implementing RFC 8899 takes too long. The discussion also explores different probe message variants from RFC 8899, focusing on the trade-offs between complexity and effectiveness. The main concern is detecting and reacting to MTU reductions, which could occur due to network changes.

## Related Questions
- How does the client determine the MTU size in the proposed temporary fix?
- What are the potential drawbacks of using padding data for probe messages?
- How does the server adjust packet sizes based on the detected MTU?
- What is the role of the `mtuEstimate` variable in the network implementation?
- How can we ensure that the cost of probe packets is less than the expected gains?
- What are the implications of using the slow protocol for sending probe messages?

*Source: unknown | chunk_id: github_issue_819_discussion*
