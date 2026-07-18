# [issues/issue_419.md] - Issue #419 discussion

**Type:** review
**Keywords:** bandwidth, TCP, UDP, Cubyz, congestion control, reliable, unreliable, throughput, sliding window, acks
**Concepts:** network bandwidth, congestion control, reliable vs unreliable throughput

## Summary
The discussion revolves around the suboptimal network bandwidth in Cubyz compared to raw TCP and UDP. The maintainer explains that their custom protocol uses congestion control for reliable packets but does not throttle unreliable packets.

## Explanation
The issue highlights a performance discrepancy between Cubyz's custom network protocol and raw TCP/UDP, where the latter achieves significantly higher bandwidth on localhost. The maintainer clarifies that their protocol includes congestion control for reliable data transmission but lacks it for unreliable messages. This distinction could explain why the custom protocol is slower, as unreliable packets are not being throttled by any congestion control mechanism.

## Related Questions
- What is the current implementation of congestion control in Cubyz's custom protocol?
- How does Cubyz handle acknowledgments (acks) for unreliable packets?
- Is there a plan to implement congestion control for unreliable packets in Cubyz?
- What are the potential performance gains if congestion control is added to unreliable packets?
- How does the sliding window size affect the throughput of Cubyz's custom protocol?
- Are there any known limitations or bottlenecks in Cubyz's current network implementation?

*Source: unknown | chunk_id: github_issue_419_discussion*
