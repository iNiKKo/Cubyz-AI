# [issues/issue_62.md] - Issue #62 discussion

**Type:** review
**Keywords:** fluids, gases, simulation, performance, rendering, exponential growth, gas types, vector representation, globules, hierarchical node approach
**Concepts:** fluid dynamics, gas simulation, performance optimization, rendering efficiency

## Summary
The discussion revolves around designing a fluid/gas system for Cubyz, focusing on how to handle multiple gas types and fluid dynamics without causing performance issues.

## Explanation
The main concern is the efficient simulation of fluids and gases while preventing excessive computational load. The maintainers highlight that mixing gases can lead to an exponential increase in gas types and complex rendering requirements. Users propose various solutions, such as treating gases as vectors, grouping fluids into globules, and using a hierarchical node approach. There's also mention of fluid simulation articles for further research. The issue remains open until a viable solution is implemented.

## Related Questions
- What are the potential performance impacts of mixing gases in the fluid/gas system?
- How can fluids be grouped to reduce rendering complexity without losing dynamics?
- Are there any existing games that use a similar constrained gas system as Cubyz?
- What is the proposed approach for controlling gas proliferation in the simulation?
- How does the hierarchical node approach address performance concerns in fluid/gas simulations?
- Can you provide more details on the chess game analogy for fluid dynamics in Cubyz?

*Source: unknown | chunk_id: github_issue_62_discussion*
