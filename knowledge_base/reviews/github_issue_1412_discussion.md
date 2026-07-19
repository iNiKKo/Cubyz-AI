# [issues/issue_1412.md] - Issue #1412 discussion

**Type:** review
**Keywords:** block substitution, masks, patterns, inheritance, substitution map, HashMap, SBBs, biomes, verbosity, caching
**Symbols:** cubyz:generator, cubyz:birch_log, cubyz:oak_log, inherit_substitutions, children, crimson, structure, chance
**Concepts:** block substitution, blueprint inheritance, data structure design, caching strategies, biome definitions

## Summary
The issue discusses allowing block substitution in blueprints using masks and patterns, with inheritance control and a specific data structure for substitutions. It also explores potential caching strategies and the impact on existing SBBs.

## Explanation
The issue discusses allowing block substitution in blueprints using masks and patterns. Substitution mappings can be specified as part of SBB definitions, where each entry is a dictionary containing `new` and `old` keys to avoid ambiguity caused by plain hash maps. The feature allows for optional inheritance of substitutions to child structures unless explicitly disabled with the `inherit_substitutions = false` setting. The maintainers consider potential caching strategies to avoid duplicating identical blueprints but note concerns about verbosity and complexity in biome definitions. Specifically, they propose using a key structure like `struct { old: []const u8, new: []const u8 }` for caching purposes.

## Related Questions
- How does the substitution mapping avoid ambiguity?
- What are the potential performance implications of caching blueprints?
- How would allowing children to define substitution maps impact existing SBBs?
- What is the proposed key structure for caching blueprints?
- Why might @ikabod-kee be unhappy with the current proposal?
- How could special SBB 'generators' address the verbosity concern?

*Source: unknown | chunk_id: github_issue_1412_discussion*
