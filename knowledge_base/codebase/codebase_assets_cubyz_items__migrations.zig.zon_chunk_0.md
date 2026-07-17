# [easy/codebase_assets_cubyz_items__migrations.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** migrations, renaming, legacy identifiers, string literals, comptime arrays
**Symbols:** .old, .new
**Concepts:** item name migrations, configuration data, static mappings

## Summary
This chunk defines a static list of item name migrations, mapping legacy identifiers to new ones for the Cubyz items system.

## Explanation
The chunk contains only a single top-level array literal with multiple struct entries. Each entry is an anonymous struct containing two fields: .old and .new, both of type comptime []const u8 (implied by the string literals). The entire collection represents a configuration data set used to rename items during migration or version upgrades; no executable logic, functions, or algorithms are present.

## Related Questions
- What is the new name for the item with old identifier 'stone'?
- How many items are listed in this migration table?
- Which legacy identifiers map to names under the 'leaves/' namespace?
- Are any of these migrations reversible by swapping .old and .new values?
- What type is used for the string fields in each migration entry?
- Does this chunk contain any executable logic or functions?

*Source: unknown | chunk_id: codebase_assets_cubyz_items__migrations.zig.zon_chunk_0*
