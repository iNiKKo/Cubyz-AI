# [hard/codebase_src_assets.zig] - Chunk 3

**Type:** implementation
**Keywords:** registerItem, Palette, loadFromZonLegacy, SparsePaletteNotAllowed, BaseItemIndex, blocks.register, biomes.register, items.registerRecipes, allocator.create, errdefer
**Symbols:** init, registerItem, registerProceduralItem, registerBlock, assignBlockItem, registerBiome, registerRecipesFromZon, Palette, Palette.init, Palette.loadFromZon, Palette.loadFromZonLegacy, Palette.deinit
**Concepts:** asset registration, palette loading, sparse palette handling, ZON file parsing, error propagation, memory allocation, defer cleanup

## Summary
This chunk defines asset registration utilities and a Palette data structure for loading color/texture palettes from ZON files, including legacy sparse palette handling.

## Explanation
The chunk declares the function `init()` which initializes a global `common` object by calling its init method with the main arena and reading assets from the cwd under 'assets/'. It then defines several registration helpers: `registerItem(assetFolder, id, zon)` splits an asset ID on ':' to extract a module name, allocates paths for texture lookups (both addon-relative and global), and delegates to `items.register`. `registerProceduralItem` simply forwards to `items.registerProceduralItem`. `registerBlock(assetFolder, id, zon)` logs if the ZON element is null, then registers with both `blocks.register` and `blocks.meshes.register`. `assignBlockItem(stringId)` retrieves a block by ID, converts the string ID to an index via `items.BaseItemIndex.fromId`, and assigns it to the item's `.block` field. `registerBiome(numericId, stringId, zon)` logs missing biomes and registers with `biomes.register`. `registerRecipesFromZon(zon)` forwards to `items.registerRecipes`. The chunk also defines a public struct `Palette` containing an allocator and a list of strings. Its `init` method dispatches based on the ZON element type: `.object` uses `loadFromZonLegacy`, while `.array` or `.null` use `loadFromZon`; any other type returns `error.InvalidPaletteFormat`. If a firstElement is provided, it validates that the palette list is empty before appending and checks for mismatch with the first item. `loadFromZon` converts the ZON element to a slice, creates a Palette instance, appends each name (converted from ?[]const u8), and returns on invalid entries. `loadFromZonLegacy` handles sparse palettes by iterating over an object iterator, mapping numeric IDs to names in a translation buffer, validating that IDs are within range (returning `error.SparsePaletteNotAllowed` if not), then constructing the Palette with those names; it logs each entry and returns on missing keys. The chunk ends mid-definition of `deinit(self: *Palette) void`, indicating cleanup logic is present but incomplete in this excerpt.

## Code Example
```zig
pub fn init() void {
	common = .init();
	common.read(main.globalArena, main.files.cwd(), "assets/");
	common.log(.common);
}
```

## Related Questions
- What error is returned when a Palette ZON element type is neither .object nor .array?
- How does the chunk handle missing biome or block entries in their respective registration functions?
- Which global object is initialized by calling init() and what arguments are passed to it?
- In loadFromZonLegacy, how is a sparse palette detected and what error code is used for out-of-range IDs?
- What validation is performed on the firstElement argument in Palette.init before appending to the list?
- How does registerItem split an asset ID and where are the resulting module and texture paths stored?
- What happens inside assignBlockItem when items.BaseItemIndex.fromId returns a null value?
- Which two functions are called by registerBlock after handling a missing ZON element?
- In loadFromZon, how is each name converted from ?[]const u8 to []const u8 and what error occurs on failure?
- What does the Palette struct contain as its public fields and which allocator type is required?
- How does the chunk ensure cleanup of allocated memory for texture paths in registerItem?
- What logging behavior is present when a palette entry has an invalid numeric ID in loadFromZonLegacy?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_3*
