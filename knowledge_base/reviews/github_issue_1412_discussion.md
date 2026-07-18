# [issues/issue_1412.md] - Issue #1412 discussion

**Type:** review
**Keywords:** block substitution, masks, patterns, inheritance, substitution map, HashMap, SBBs, biomes, verbosity, caching
**Symbols:** cubyz:generator, cubyz:birch_log, cubyz:oak_log, inherit_substitutions, children, crimson, structure, chance
**Concepts:** block substitution, blueprint inheritance, data structure design, caching strategies, biome definitions

## Summary
The issue discusses allowing block substitution in blueprints using masks and patterns, with inheritance control and a specific data structure for substitutions. It also explores potential caching strategies and the impact on existing SBBs.

## Explanation
The discussion centers around implementing block substitution in blueprints, where blocks can be replaced based on specified mappings. The feature allows for optional inheritance of substitutions to child structures unless explicitly disabled. The use of a list of dictionaries with `new` and `old` keys is proposed to prevent ambiguity. The maintainers consider the implications for existing SBBs and suggest potential caching strategies to avoid duplication, but also note concerns about verbosity and complexity in biome definitions.

## Related Questions
- How does the substitution mapping avoid ambiguity?
- What are the potential performance implications of caching blueprints?
- How would allowing children to define substitution maps impact existing SBBs?
- What is the proposed key structure for caching blueprints?
- Why might @ikabod-kee be unhappy with the current proposal?
- How could special SBB 'generators' address the verbosity concern?

*Source: unknown | chunk_id: github_issue_1412_discussion*
