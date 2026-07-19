# [issues/issue_1412.md] - Issue #1412 discussion

**Type:** review
**Keywords:** block substitution, masks, patterns, inheritance, substitution map, HashMap, SBBs, biomes, verbosity, caching
**Symbols:** cubyz:generator, cubyz:birch_log, cubyz:oak_log, inherit_substitutions, children, crimson, structure, chance
**Concepts:** block substitution, blueprint inheritance, data structure design, caching strategies, biome definitions

## Summary
The issue discusses allowing block substitution in blueprints using masks and patterns, with inheritance control and a specific data structure for substitutions. It also explores potential caching strategies and the impact on existing SBBs.

## Explanation
The issue discusses allowing block substitution in blueprints using masks and patterns, with inheritance control and a specific data structure for substitutions. Substitution mappings can be specified as part of SBB definitions, where each entry is a dictionary containing `new` and `old` keys to avoid ambiguity caused by plain hash maps. The feature allows for optional inheritance of substitutions to child structures unless explicitly disabled with the `inherit_substitutions = false` setting. The maintainers consider potential caching strategies to avoid duplicating identical blueprints but note concerns about verbosity and complexity in biome definitions. Specifically, they propose using a key structure like `struct { old: []const u8, new: []const u8 }` for caching purposes.

Here is an example of how substitutions are defined:
```zig
.{
	.blueprint = "cubyz:generator",
	.substitute = .{
		.{.old = "cubyz:birch_log", .new = "cubyz:oak_log"},
	}
	.inherit_substitutions = false,
	.children = .{
		.crimson = .{
			.{.structure = "cubyz:tree/birch/1/tree/1", .chance = 0.2},
			.{.structure = "cubyz:tree/birch/1/tree/2", .chance = 0.2},
			.{.structure = "cubyz:tree/birch/1/tree/3", .chance = 0.2},
			.{.structure = "cubyz:tree/birch/1/tree/4", .chance = 0.4},
		},
	},
}
```
The maintainers also discuss whether children structures should be allowed to define substitution maps if parent structures contain one, noting that this could increase verbosity in biome definitions.

**How does the substitution mapping avoid ambiguity?**
Substitution mappings use a list of dictionaries containing `new` and `old` keys to clearly specify which blocks are being substituted for others, avoiding any potential confusion or errors that might arise from using plain hash maps.

**What are the potential performance implications of caching blueprints?**
Caching blueprints in a HashMap could significantly improve performance by reducing the need to duplicate identical blueprints multiple times. However, it also introduces complexity and verbosity in biome definitions, which is a concern for maintainers like @ikabod-kee.

**How would allowing children to define substitution maps impact existing SBBs?**
Allowing children structures to define their own substitution maps could increase the verbosity of biome definitions, making them more complex and harder to manage. This is why the maintainers are considering restricting substitution maps only to special SBB 'generators'.

**What is the proposed key structure for caching blueprints?**
The maintainers propose using a key structure like `struct { old: []const u8, new: []const u8 }` for caching purposes. This would allow for efficient lookups and management of cached blueprints.

**Why might @ikabod-kee be unhappy with the current proposal?**
@ikabod-kee is not keen on copying SBBs multiple times in biome definitions, even when using dedicated generator SBBs that aggregate multiple tree models. The verbosity and complexity introduced by substitution maps are also a concern for them.

**How could special SBB 'generators' address the verbosity concern?**
By restricting substitution maps only to special SBB 'generators', alongside other parameters like `snap`, the maintainers aim to reduce verbosity in biome definitions, making it easier and more efficient to manage complex structures.

## Related Questions
- How does the substitution mapping avoid ambiguity?
- What are the potential performance implications of caching blueprints?
- How would allowing children to define substitution maps impact existing SBBs?
- What is the proposed key structure for caching blueprints?
- Why might @ikabod-kee be unhappy with the current proposal?
- How could special SBB 'generators' address the verbosity concern?

*Source: unknown | chunk_id: github_issue_1412_discussion*
