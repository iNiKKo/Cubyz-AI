# [src/items.zig] - Chunk 2054623602

**Type:** review
**Keywords:** MaterialProperty, density, strength, elasticity, hardness, fromString, std.meta.stringToEnum, enum variant, ignored, fallback, default, scale, invalid input
**Symbols:** Modifier, MaterialProperty, density, elasticity, hardness, fromString
**Concepts:** enum parsing, fallback default behavior, data integrity, scale mismatch, invalid input handling, type safety

## Summary
Replaced the fallback default material property from strength to density when an unknown string is parsed, addressing a reviewer's concern that invalid values should be ignored rather than mapped to an arbitrary default.

## Explanation
The original code used std.meta.stringToEnum on MaterialProperty and, upon failure, logged an error and returned .strength as the fallback. The reviewer argued that any unknown property value is likely out of scale with density (the chosen default) and therefore mapping to strength is equally arbitrary; they suggested introducing a dedicated enum variant `ignored` so that invalid inputs are dropped rather than silently substituted. This change aligns with the architectural principle of preserving data integrity: when an asset designer provides a property name that does not exist, the system should not assume a default magnitude for it. By switching the fallback to .density (or eventually to a new .ignored variant), we reduce the risk of unintended physics behavior caused by mismatched scales. The diff also removes the now‑unused .strength and .grip entries from the enum definition, simplifying the type surface.

## Related Questions
- What enum variants are currently defined in MaterialProperty?
- How does fromString handle an unknown string value today?
- Why was .strength chosen as the original fallback default?
- Does the current code log any error when parsing fails?
- Is there a plan to introduce an `ignored` variant for invalid inputs?
- What happens to asset data if a designer provides a property name that does not exist in MaterialProperty?
- Are .grip and .strength still referenced elsewhere after the enum definition change?
- How would changing the fallback from strength to density affect physics calculations?
- Is there any test coverage for the stringToEnum failure path in items.zig?
- What is the impact of removing unused enum variants on binary size or API compatibility?

*Source: unknown | chunk_id: github_pr_1332_comment_2054623602*
