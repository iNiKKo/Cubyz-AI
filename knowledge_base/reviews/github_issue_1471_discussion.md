# [issues/issue_1471.md] - Issue #1471 discussion

**Type:** review
**Keywords:** particle collisions, lighting, optimization, AABB collision, physics checks, interpolation
**Concepts:** collision detection, lighting optimization, performance improvement

## Summary
The discussion revolves around optimizing particle collision detection and lighting, aiming to improve performance from handling up to 30k particles at 60fps to potentially 1 million particles. The maintainer suggests simplifying collision detection by using a single swept AABB collision instead of iterating through blocks three times.

## Explanation
The discussion revolves around optimizing particle collision detection and lighting to improve performance from handling up to 30k particles at 60fps to potentially 1 million particles. The maintainer has measured performance and found that without collisions, the system can handle up to 500k particles at 30ms, but with collisions, it drops to around 400k particles at 60-70ms. Profiling indicates that collision detection and lighting consume the majority of processing time. The maintainer suggests simplifying collision detection by using a single swept AABB collision instead of iterating through blocks three times. Additionally, they propose optimizing physics checks by performing them only every x frames and interpolating in-between, similar to Vintage Story's approach. This could help reduce overhead and improve performance. Furthermore, the maintainer mentions storing previous block positions to determine if particles should change blocks.

## Related Questions
- What is the current maximum number of particles that can be handled with collision detection enabled?
- How does simplifying collision detection to a single swept AABB collision improve performance?
- What is the maintainer's proposed method for optimizing physics checks in particle systems?
- How does interpolating physics checks between frames benefit performance?
- What are the potential drawbacks of reducing the frequency of physics and lighting updates?
- How can storing previous block positions help determine if a particle should change blocks?

*Source: unknown | chunk_id: github_issue_1471_discussion*
