# [issues/issue_86.md] - Issue #86 discussion

**Type:** review
**Keywords:** Goal-Oriented Action Planning, ECS, AI, optimization, state graph, Layered GOAP
**Symbols:** GOAP, ECS, FEAR, Middle-earth: Shadow of Mordor
**Concepts:** AI system design, performance optimization, modularity

## Summary
Discussion about implementing an AI system using Goal-Oriented Action Planning (GOAP) for Cubyz. The maintainers are considering the feasibility and performance implications of such a system.

## Explanation
Discussion about implementing an AI system using Goal-Oriented Action Planning (GOAP) for Cubyz. The maintainers are considering the feasibility and performance implications of such a system, noting that GOAP is powerful but potentially intensive when computing plans for multiple entities. Users suggest setting up a good debug system to handle complex chains of actions and limiting the speed of executing actions or using timers to stall AI behavior. The maintainers express concern about handling 50-100+ entities efficiently and propose optimizing state graph traversal for better performance. There's also mention of Layered GOAP, where high-level plans make mid-level plans, which in turn make low-level plans, potentially reducing complexity and improving performance.

## Related Questions
- What are the potential performance implications of implementing GOAP for 50-100+ entities?
- How can the state graph traversal be optimized to handle a large number of entities efficiently?
- Can Layered GOAP be effectively integrated into Cubyz's existing architecture?

*Source: unknown | chunk_id: github_issue_86_discussion*
