# [issues/issue_1023.md] - Issue #1023 discussion

**Type:** review
**Keywords:** sickle, durability, blocks, breaking, clarification
**Concepts:** tool durability, block interaction

## Summary
Discussion about whether tools like a sickle should have durability when breaking certain blocks.

## Explanation
The discussion revolves around the issue of tool durability, specifically regarding tools like a sickle. The maintainer asks if this means that such tools will never break when used on blocks where they are not typically needed. The user clarifies that the intention is to avoid using tool durability for breaking blocks that do not require it, suggesting that tools should only lose durability when used on appropriate blocks.

## Related Questions
- What is the intended behavior of tools like a sickle when breaking blocks that do not require them?
- How does the current implementation handle tool durability for different types of blocks?
- Are there any specific scenarios where tool durability should be applied or ignored?
- What are the potential consequences if tool durability is incorrectly applied to certain blocks?
- How can we ensure that tools only lose durability when used on appropriate blocks?
- Is there a need for additional configuration options to control tool durability behavior?

*Source: unknown | chunk_id: github_issue_1023_discussion*
