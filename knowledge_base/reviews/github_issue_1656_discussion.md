# [issues/issue_1656.md] - Issue #1656 discussion

**Type:** review
**Keywords:** leftover damage, speed boost, swing time, invisible mechanic, DPS metric, block breaking
**Concepts:** gameplay mechanics, swing time calculation, player experience

## Summary
Discussion on implementing a speed boost for block breaking based on leftover damage.

## Explanation
Discussion on implementing a speed boost for block breaking based on leftover damage. The proposed mechanism involves reducing the next swing's duration by a percentage of the leftover damage compared to the tool's full damage output. For example, if a tool deals 50 damage per second and breaks a block with 10 health, the remaining 40 damage would reduce the next swing time by 80% (from 1 second to 0.2 seconds). The main concern is whether this mechanic should be applied only to the next swing or if it could lead to unintended consequences such as infinite stacking of swing times. There are also considerations about player visibility and understanding of the mechanic, as well as its impact on gameplay rhythm and tool crafting metrics.

## Related Questions
- What is the proposed mechanism for reducing swing time based on leftover damage?
- Why was transferring leftover damage to the next swing considered problematic?
- How could the infinite stacking of swing times be prevented?
- What are the potential impacts on player experience and gameplay rhythm?
- How would this feature affect the accuracy of DPS metrics when crafting tools?
- Is there a plan to create a prototype for testing this mechanic?

*Source: unknown | chunk_id: github_issue_1656_discussion*
