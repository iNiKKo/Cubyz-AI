# [issues/issue_473.md] - Issue #473 discussion

**Type:** review
**Keywords:** fog blocks, volumetric fog, world generation, player interaction, thread, layer, fog machine, dehumidifying block
**Concepts:** world generation, player interaction

## Summary
Discussion about implementing fog blocks differently to improve world generation and player interaction.

## Explanation
The issue discusses the current janky behavior of treating fog blocks as regular blocks during world generation. The maintainer notes that this is already tracked in another issue (#62). Suggestions include making volumetric fog blocks operate on a different layer or thread, allowing them to generate inside other blocks, and proposing fog machines or dehumidifying blocks for player interaction with fog.

## Related Questions
- What are the current issues with treating fog blocks as regular blocks during world generation?
- How can volumetric fog blocks be implemented to operate on a different layer or thread?
- What are the proposed solutions for player interaction with fog in the game?
- Is there an existing issue tracking the problems with fog block implementation?
- How might fog machines or dehumidifying blocks improve player control over fog in the game world?
- Are there any architectural considerations for implementing volumetric fog on a different layer?

*Source: unknown | chunk_id: github_issue_473_discussion*
