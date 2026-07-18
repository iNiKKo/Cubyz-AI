# [issues/issue_3302.md] - Issue #3302 discussion

**Type:** review
**Keywords:** biome tags, stone types, structure tables, auto-generation, blocks, inheritance, probability, structures
**Concepts:** biome tags, structure tables, auto-generation

## Summary
Discussion on adding biome tags for specific stone types to improve structure table usage.

## Explanation
The issue proposes adding biome-specific tags for various stone types to enhance their usability in structure tables. The maintainer suggests an auto-generation approach where biomes inherit tags from blocks within them, considering the probability of structures to avoid false triggers.

## Related Questions
- How would the auto-generation of biome tags affect performance?
- What are the potential issues with inheriting block tags in biomes?
- Can you provide examples of how the probability factor would be implemented?
- How does this feature impact backwards compatibility?
- What is the expected maintenance overhead for managing these tags manually versus automatically?
- How will the auto-generation system handle cases where multiple blocks have conflicting tags?
- Are there any potential memory implications from adding more tags to biomes?
- Can you explain how the chance factor would be calculated and applied?
- What are the architectural considerations for integrating this feature with existing biome systems?
- How does this change affect the design of structure tables in Cubyz?

*Source: unknown | chunk_id: github_issue_3302_discussion*
