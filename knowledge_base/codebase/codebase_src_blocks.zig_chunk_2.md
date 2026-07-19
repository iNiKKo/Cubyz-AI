# [hard/codebase_src_blocks.zig] - Chunk 2

**Type:** implementation
**Keywords:** block registration, callback initialization, data parsing, error handling, type retrieval
**Symbols:** registerOpaqueVariant, registerCallbacks, finishBlocks, reset, getTypeById, ParseBlockConfig, parseBlockData, parseBlock, parseBlockWithOptions, getBlockById, getBlockData, hasRegistered
**Concepts:** block registration, callback handling, data parsing, error logging, type mapping

## Summary
Handles block registration and parsing from configuration data.

## Explanation
This chunk manages the registration of blocks with various properties such as opaque variants, callbacks for interactions, drops, LOD replacements, and type mappings. It also includes functions to parse block data from strings, reset block states, and retrieve block information by ID or name. The primary responsibility is to ensure that all block configurations are correctly loaded and accessible within the engine.

### Functions:
- **registerOpaqueVariant**: Registers an opaque variant for a block type. If the `zon` element has an `opaqueVariant`, it uses that; otherwise, it defaults to the original type.
  ```zig
  fn registerOpaqueVariant(typ: u16, zon: ZonElement) void {
      if (zon.get([]const u8, "opaqueVariant")) |replacement| {
          _opaqueVariant[typ] = getTypeById(replacement);
      } else {
          _opaqueVariant[typ] = typ;
      }
  }
  ```
- **registerCallbacks**: Registers callbacks for various block events (`onInteract`, `onBreak`, `onUpdate`, `onTick`, `onTouch`). If the event is not found, it logs an error and sets the callback to `.noop`.
  ```zig
  fn registerCallbacks(typ: u16, zon: ZonElement) void {
      _onInteract[typ] = blk: {
          break :blk ClientBlockCallback.init(zon.getChildOrNull("onInteract") orelse break :blk .noop, .{.block = .{.typ = typ, .data = 0}}) orelse {
              std.log.err("Failed to load onInteract event for block {s}", .{_id[typ]});
              break :blk .noop;
          };
      };
      // Similar blocks for other events...
  }
  ```
- **finishBlocks**: Iterates through all registered blocks and calls functions to register drops, LOD replacements, opaque variants, and callbacks. It also registers a void block and finishes texture loading.
  ```zig
  pub fn finishBlocks(zonElements: Assets.ZonHashMap) void {
      var i: u16 = 0;
      while (i < size) : (i += 1) {
          registerBlockDrop(i, zonElements.get(_id[i]) orelse continue);
          registerLodReplacement(i, zonElements.get(_id[i]) orelse continue);
          registerOpaqueVariant(i, zonElements.get(_id[i]) orelse continue);
          registerCallbacks(i, zonElements.get(_id[i]) orelse continue);
      }
      blueprint.registerVoidBlock(parseBlock("cubyz:void"));
      meshes.finishTextureLoading();
  }
  ```
- **reset**: Resets the block system by setting size to 0, clearing ores and reverse indices, and resetting meshes.
  ```zig
  pub fn reset() void {
      size = 0;
      ores = .empty;
      reverseIndices = .{};
      meshes.reset();
  }
  ```
- **getTypeById**: Retrieves the block type by ID. If the ID is not found, it logs an error and returns 0 (air).
  ```zig
  pub fn getTypeById(id: []const u8) u16 {
      if (reverseIndices.get(id)) |result| {
          return result;
      } else {
          std.log.err("Couldn't find block {s}. Replacing it with air...", .{id});
          return 0;
      }
  }
  ```
- **parseBlockData**: Parses block data from a string. If the data contains a colon, it treats it as an ore block and logs a warning if the parent block data is not 0. It returns the parsed type or null if parsing fails.
  ```zig
  fn parseBlockData(fullBlockId: []const u8, data: []const u8, comptime config: ParseBlockConfig) ?u16 {
      if (std.mem.containsAtLeastScalar(u8, data, 1, ':')) {
          const oreChild = parseBlockWithOptions(data, config);
          if (oreChild.data != 0) {
              std.log.warn("Error while parsing ore block data of '{s}': Parent block data must be 0.", .{fullBlockId});
          }
          return oreChild.typ;
      }
      return std.fmt.parseInt(u16, data, 0) catch |err| {
          std.log.err("Error while parsing block data of '{s}': {s}", .{fullBlockId, @errorName(err)});
          return null;
      };
  }
  ```
- **parseBlock**: Parses a block from a string using default configuration.
  ```zig
  pub fn parseBlock(data: []const u8) Block {
      return parseBlockWithOptions(data, .{});
  }
  ```
- **parseBlockWithOptions**: Parses a block from a string with optional migration support. It splits the ID and data, applies migrations if configured, and returns the parsed block.
  ```zig
  pub fn parseBlockWithOptions(data: []const u8, comptime config: ParseBlockConfig) Block {
      var id: []const u8 = data;
      var blockData: ?u16 = null;
      if (std.mem.indexOfScalarPos(u8, data, 1 + (std.mem.indexOfScalar(u8, data, ':') orelse 0), ':')) |pos| {
          id = data[0..pos];
          blockData = parseBlockData(data, data[pos + 1 ..], config);
      }
      if (config.applyMigrations) {
          id = main.migrations.applySingle(.block, id);
      }
      if (reverseIndices.get(id)) |resultType| {
          var result: Block = .{.typ = resultType, .data = 0};
          result.data = blockData orelse result.mode().naturalStandard;
          return result;
      } else {
          std.log.err("Couldn't find block {s}. Replacing it with air...", .{id});
          return Block.init(0, 0);
      }
  }
  ```
- **getBlockById**: Retrieves the block type by ID. If the ID is not found, it returns an error.
  ```zig
  pub fn getBlockById(idLikeString: []const u8) !u16 {
      const addonNameSeparatorIndex = std.mem.indexOfScalar(u8, idLikeString, ':') orelse return error.MissingAddonNameSeparator;
      const blockIdEndIndex = std.mem.indexOfScalarPos(u8, idLikeString, 1 + addonNameSeparatorIndex, ':') orelse idLikeString.len;
      const id = idLikeString[0..blockIdEndIndex];
      return reverseIndices.get(id) orelse return error.NotFound;
  }
  ```
- **getBlockData**: Retrieves the block data from a string. If the data is empty or invalid, it returns an error.
  ```zig
  pub fn getBlockData(idLikeString: []const u8) !?u16 {
      const addonNameSeparatorIndex = std.mem.indexOfScalar(u8, idLikeString, ':') orelse return error.MissingAddonNameSeparator;
      const blockIdEndIndex = std.mem.indexOfScalarPos(u8, idLikeString, 1 + addonNameSeparatorIndex, ':') orelse return null;
      const dataString = idLikeString[blockIdEndIndex + 1 ..];
      if (dataString.len == 0) return error.EmptyDataString;
      return std.fmt.parseInt(u16, dataString, 0) catch return error.InvalidData;
  }
  ```
- **hasRegistered**: Checks if a block ID is registered.
  ```zig
  pub fn hasRegistered(id: []const u8) bool {
      return reverseIndices.contains(id);
  }
  ```

## Code Example
```zig
fn reset() void {
	size = 0;
	ores = .empty;
	reverseIndices = .{};
	meshes.reset();
}
```

## Related Questions
-  How does the `registerOpaqueVariant` function work?
-  What is the purpose of the `finishBlocks` function?
-  How are block callbacks registered in this chunk?
-  What error handling is implemented for parsing block data?
-  How does the `getTypeById` function handle missing block IDs?
-  What is the role of the `ParseBlockConfig` struct?
-  How does the `parseBlockWithOptions` function differ from `parseBlock`?
-  What kind of errors can be returned by `getBlockById`?
-  How is block data parsed from a string in this chunk?
-  What does the `reset` function do to the block system?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_2*
