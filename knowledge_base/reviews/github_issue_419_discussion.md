# [issues/issue_419.md] - Issue #419 discussion

**Type:** review
**Keywords:** bandwidth, TCP, UDP, Cubyz, congestion control, reliable, unreliable, throughput, sliding window, acks
**Concepts:** network bandwidth, congestion control, reliable vs unreliable throughput

## Summary
The discussion revolves around the suboptimal network bandwidth in Cubyz compared to raw TCP and UDP. The maintainer explains that their custom protocol uses congestion control for reliable packets but does not throttle unreliable packets.

## Explanation
Raw TCP and raw UDP have a bandwidth of 1 GB/s or more on localhost when sending 60 MB worth of data, whereas Cubyz takes around 4 seconds to send the same amount of data, resulting in a throughput of 15 MB/s. The maintainer explains that their custom protocol uses congestion control for reliable packets but does not throttle unreliable packets, leading to a significant performance discrepancy on localhost. Specifically, the sliding window size is set to up to 65536 packets of slightly less than 1500 bytes each, which should theoretically not be a bottleneck here. The maintainer also mentions that they send bulk acks once every 100 ms for unreliable packets.

## Related Questions
- What is the current implementation of congestion control in Cubyz's custom protocol?
- How does Cubyz handle acknowledgments (acks) for unreliable packets?
- Is there a plan to implement congestion control for unreliable packets in Cubyz?
- What are the potential performance gains if congestion control is added to unreliable packets?
- How does the sliding window size of up to 65536 packets affect the throughput of Cubyz's custom protocol?
- Are there any known limitations or bottlenecks in Cubyz's current network implementation?

*Source: unknown | chunk_id: github_issue_419_discussion*
