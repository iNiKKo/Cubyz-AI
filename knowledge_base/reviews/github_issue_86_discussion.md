# [issues/issue_86.md] - Issue #86 discussion

**Type:** review
**Keywords:** Goal-Oriented Action Planning, ECS, AI, optimization, state graph, Layered GOAP
**Symbols:** GOAP, ECS, FEAR, Middle-earth: Shadow of Mordor
**Concepts:** AI system design, performance optimization, modularity

## Summary
Discussion about implementing an AI system using Goal-Oriented Action Planning (GOAP) for Cubyz. The maintainers are considering the feasibility and performance implications of such a system.

## Explanation
The discussion revolves around integrating GOAP into Cubyz, which is described as a powerful but potentially intensive system. Users suggest that while it may require significant initial setup, it offers flexibility and depth in AI behavior. The maintainers express concern about the performance impact on handling multiple entities (50-100+) and propose optimizing the state graph traversal for better efficiency. There's also mention of Layered GOAP as a potential solution to reduce complexity and improve performance.

## Related Questions
- What are the potential performance implications of implementing GOAP for 10k+ entities?
- How can the state graph traversal be optimized to handle a large number of entities efficiently?
- Can Layered GOAP be effectively integrated into Cubyz's existing architecture?
- What are the benefits and drawbacks of using GOAP in game development compared to other AI systems?
- How does the initial setup cost of GOAP compare to its long-term maintainability and flexibility?
- Are there any specific tools or libraries available for implementing GOAP in Zig that could be beneficial?

*Source: unknown | chunk_id: github_issue_86_discussion*
