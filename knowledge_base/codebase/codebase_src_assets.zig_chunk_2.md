# [hard/codebase_src_assets.zig] - Chunk 2

**Type:** api
**Keywords:** readAllBlueprints, readAllModels, createAssetStringID, addon directory, file filtering, path normalization, asset ID generation, NeverFailingAllocator
**Symbols:** readAllBlueprints, readAllModels
**Concepts:** asset loading, addon directory iteration, file filtering by extension and prefix, ID generation for assets, Windows path separator normalization, error logging with std.log.err, NeverFailingAllocator usage

## Summary
This chunk defines public functions for reading assets from addon directories (defaults, blueprints, models) and a utility to generate unique string IDs for assets.

## Explanation
The chunk declares three public functions: readAllBlueprints, readAllModels, and an implicit function handling defaults (likely readAllDefaults). Each follows the same pattern: open an addon directory at subPath, walk it with a stack allocator, filter entries by kind (.file), basename prefixes/suffixes (_defaults, _migrations, .blp, .zon, or user-provided fileEnding), and then either read to Zon (for defaults) or raw bytes (for blueprints/models). For defaults, the code loads a Defaults struct from main.stackAllocator, iterates entries skipping those starting with '_defaults', reads each .zon file via assetsDirectory.readToZon, optionally joins with stored defaults using zon.join(.preferLeft, ...), and puts into output. Blueprints skip _migrations prefix, require .blp suffix, read raw bytes, create an ID with assetType 'blueprint', and put into output. Models are similar but accept a fileEnding argument (defaulting to '.zon' in the caller context) and use assetType 'model'. All three functions catch errors from directory opening or walking; they log errors via std.log.err with formatted messages, break out of loops on non-file entries or _migrations prefix, and continue processing other files. The chunk also defines createAssetStringID: it takes an external allocator, addon name, asset type string, and relative file path; it computes a base name end index (subtracting '.zig.zon' if present, else finding last '.'), strips the extension to get pathNoExtension, finds the start of the filename after the last '/', checks that the filename does not start with '_' (logging an error and returning InvalidId if so), allocates a buffer sized addonName.len + 1 + pathNoExtension.len, copies addonName then ':' then the converted path (replacing '\', converting Windows separators to '/'), validates each character allowing only '_', 'a'-'z', '0'-'9', '/' (logging an error and returning InvalidId for any other char), and returns the resulting []u8. The chunk uses NeverFailingAllocator type for allocator arguments, implying callers guarantee no allocation failures; output is a pointer to BytesHashMap where put is called with allocator.allocator as first arg. Error handling includes std.log.err calls that format messages with @errorName(err) or literal strings, and unreachable branches after successful puts (indicating the code assumes put never fails given NeverFailingAllocator). The chunk does not define any structs or enums itself; it only references external types like Defaults, BytesHashMap, Addon, etc. No networking, serialization beyond reading Zon files, concurrency primitives, or world generation logic is present here.

## Related Questions
- How does readAllBlueprints filter blueprint files?
- What happens when an addon directory cannot be opened in readAllModels?
- Which file extensions are accepted for model assets by default?
- How is the asset ID constructed inside createAssetStringID?
- Why does createAssetStringID reject filenames starting with underscore?
- What error is logged if a path contains invalid characters after normalization?
- Does readAllBlueprints handle _migrations files differently from other blueprints?
- How are defaults merged when reading addon assets in the implicit function?
- Is there any concurrency protection around the walker loop in these functions?
- What does unreachable mean after output.put calls in this chunk?

*Source: unknown | chunk_id: codebase_src_assets.zig_chunk_2*
