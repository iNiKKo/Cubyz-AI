# [issues/issue_2643.md] - Issue #2643 discussion

**Type:** review
**Keywords:** structure tables, biomes, IDs, tags, desiredStructureTables, ZonElement, error handling, log messages, flexibility, control
**Symbols:** desiredStructureTables, ZonElement
**Concepts:** biome initialization, structure table referencing, ID-based referencing, tag-based referencing

## Summary
Proposes adding the ability to reference structure tables by ID in biomes, alongside existing tag-based referencing.

## Explanation
The issue discusses enhancing the biome initialization process to allow structures from specific tables to be added based on their IDs rather than tags. This change aims to provide more flexibility and control over which structures are included in a biome. The proposal suggests adding a loop after the existing tag-checking loop to iterate over a `desiredStructureTables` property in the biome's ZonElement, adding structures that match the specified IDs. Error handling is proposed for cases where an ID does not exist, with only a log message being generated. Additionally, there is a mention of allowing structure tables to include other structure tables by ID, which could be considered as part of this enhancement.

## Related Questions
- What is the purpose of the `desiredStructureTables` property in the biome's ZonElement?
- How does the proposed change affect the existing tag-based structure table referencing?
- What are the potential benefits and drawbacks of using ID-based referencing for structure tables?
- How will error handling be implemented if an ID does not exist in a structure table?
- Can you explain how allowing structure tables to include other structure tables by ID might be beneficial?
- What is the current status of the PR that this issue is split from (#2129)?
- Are there any potential performance implications of adding this new loop for ID-based referencing?
- How will this change impact backwards compatibility with existing biome definitions?
- Is there a plan to implement the additional feature of structure tables including other tables by ID in this PR, or will it be addressed separately?
- What are the next steps for implementing and testing this proposed enhancement?

*Source: unknown | chunk_id: github_issue_2643_discussion*
