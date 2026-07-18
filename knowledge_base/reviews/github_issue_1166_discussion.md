# [issues/issue_1166.md] - Issue #1166 discussion

**Type:** review
**Keywords:** Hammer, original form, tool configuration, block reversion, crafting
**Concepts:** tool design, block interaction, configuration

## Summary
Discussion about implementing a 'Hammer' tool that reverts broken blocks to their original form.

## Explanation
The discussion centers around the implementation of a 'Hammer' tool in Cubyz that reverts blocks to their original form when broken. The maintainers are concerned about defining what constitutes the 'original form' and how the tool should determine this. For example, breaking stone bricks with a hammer would revert them back to stone. There is also a suggestion that the tool could be configured to allow different block drops based on the tools used, specifically for stone blocks. The maintainers are considering whether the hammer can convert planks back to wood logs and how it should determine the original form of each block.

## Related Questions
- How does the Hammer tool revert stone bricks back to stone?
- Can the Hammer tool be configured to revert different types of blocks (e.g., stone, wood) to their specific forms?
- What are the potential implications of allowing configurable block drops based on tools used?

*Source: unknown | chunk_id: github_issue_1166_discussion*
