# [issues/issue_2643.md] - Issue #2643 discussion

**Type:** review
**Keywords:** structure tables, biomes, IDs, tags, desiredStructureTables, ZonElement, error handling, log messages, flexibility, control
**Symbols:** desiredStructureTables, ZonElement
**Concepts:** biome initialization, structure table referencing, ID-based referencing, tag-based referencing

## Summary
Proposes enhancing the biome initialization process to allow referencing structure tables by ID alongside existing tag-based referencing. The enhancement includes adding a loop that checks for IDs in the `desiredStructureTables` property of ZonElement, ensuring tags in the table exist in the biome's tags, and logging an error message if an ID does not match.

## Explanation
The issue discusses enhancing the biome initialization process to allow structures from specific tables to be added based on their IDs rather than tags. This change aims to provide more flexibility and control over which structures are included in a biome. The proposal suggests adding a loop after the existing tag-checking loop to iterate over a `desiredStructureTables` property in the biome's ZonElement, ensuring that all tags in the structure table exist in the biome's tags before adding structures that match the specified IDs. Error handling is proposed for cases where an ID does not exist, with only a log message being generated. Additionally, there is a mention of allowing structure tables to include other structure tables by ID, which could be considered as part of this enhancement.

## Related Questions
- What are the specific requirements for adding structure tables by ID in biomes?
- How does the proposed change ensure that tags in the structure table exist in the biome's tags before referencing them by ID?

*Source: unknown | chunk_id: github_issue_2643_discussion*
