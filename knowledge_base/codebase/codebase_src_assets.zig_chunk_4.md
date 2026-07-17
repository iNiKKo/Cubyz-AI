# [hard/codebase_src_assets.zig] - Chunk 4

**Type:** api
**Keywords:** Palette, deinit, add, size, replaceEntry, loadWorldAssets, refCount, migrations, registerModel, entityModelPalette, blockPalette, itemPalette
**Symbols:** Palette, worldAssetFolder, refCount, loadWorldAssets
**Concepts:** palette management, migration application, model registration, reference counting, stack arena allocation, file reading, entity component system

## Summary
This chunk defines the Palette struct for managing block/item name-to-ID mappings, implements world asset loading with migration application and model registration, and exposes public API functions for palette operations.

## Explanation
The chunk declares a Palette struct containing an allocator-owned array of u8 strings (palette) and provides deinit, add, size, replaceEntry methods. It also defines loadWorldAssets which atomically increments refCount to ensure assets are loaded only once by the server; it duplicates assetFolder into worldAssetFolder, initializes main.Tag tags, creates a stack arena, clones common.worldAssets from that arena, reads files via main.files.cubyzDir(), then registers all migrations for block/item/biome/entityModel/entityComponent palettes. After migrations, it iterates worldAssets.blockModelsZon to register optimized block models, then handles entityModelPalette: first registers entries present in the palette (enforcing ID values), then iterates missing entity model descriptions from worldAssets.entityModelDescriptions and registers them while adding their IDs to entityModelPalette. If headlessServer is false it calls blocks.meshes.registerBlockBreakingAnimation. For blocks it first loops blockPalette.palette.items calling registerBlock, then iterates remaining entries in worldAssets.blocks that are not yet registered (blocks.hasRegistered) and adds them plus their stringId to blockPalette. The same pattern applies for items: loop itemPalette.palette.items, then iterate remaining entries in worldAssets.items.

## Related Questions
- What does the Palette struct contain and how is its memory managed?
- How does loadWorldAssets ensure assets are loaded only once by the server?
- Which migration types are applied during world asset loading?
- How are block models registered from worldAssets.blockModelsZon?
- What happens to entity model IDs that are missing in the palette but present in game files?
- Under what condition is registerBlockBreakingAnimation called?
- How does loadWorldAssets handle blocks that were not listed in blockPalette?
- What is the role of main.Tag.initTags() during asset loading?
- Does loadWorldAssets use a stack arena or heap allocator for temporary storage?
- Are there any error returns from loadWorldAssets besides those delegated to migrations?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_4*
