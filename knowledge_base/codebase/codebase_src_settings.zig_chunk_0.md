# [medium/codebase_src_settings.zig] - Chunk 0

**Type:** configuration
**Keywords:** ZonElement, settings file, resolutionScale, defaultPort, entityLookback, highestSupportedLod, fpsCap, mouseSensitivity, controllerAxisDeadzone, keyboard bindings
**Symbols:** What happens if the settings file cannot be read?, How are optional fields handled during initialization?, Which default values are applied when a setting is missing from the file?, What occurs when resolutionScale is outside its allowed set of values?, How does init() handle non-const struct fields that have nested children?, What is the purpose of the pub const version field imported from utils/version.zig?, Which error condition causes a log message in init() and what does it return instead?, version
**Concepts:** settings persistence, runtime configuration, default value application, file I/O with ZON format, optional type handling, struct field iteration, keyboard binding parsing

## Summary
Loads and saves runtime settings from a ZON file, applying defaults for missing or invalid values; exposes public configuration fields (graphics, networking, gameplay) and provides init/deinit lifecycle hooks.

## Explanation
The chunk defines a Settings struct with many pub const/pub var fields representing default graphics (resolutionScale, bloom, vsync), networking (defaultPort, connectionTimeout, entityLookback, highestSupportedLod), gameplay (fpsCap, fov, mouseSensitivity, controllerSensitivity, invertMouseY, playerName, streamerMode, showPlayerIndexWithName), and other runtime values (lastVersionString, storedAccount). It imports ZonElement from main and Window.Key.IsToggling from graphics/Window.zig. The init() function reads a settings file whose name is chosen at compile time via builtin.mode: in Debug builds it loads debug_settings.zig.zon, otherwise settings.zig.zon; on error other than FileNotFound it logs and returns null. After reading, it deinit's the ZonElement. Then it iterates over all struct fields (decls) to apply defaults: for non-const fields it checks if the type is optional and unwraps the child; for std.Io.Duration types it converts from nanoseconds in the file to a Duration via truncation, otherwise it calls DeclType.fromZon on nested structs or zon.get for scalar/pointer types (slice pointers are duplicated with globalAllocator). If resolutionScale is not 1, 0.5, or 0.25 it resets to 1. It then processes keyboard bindings by reading the 

## Related Questions
- What happens if the settings file cannot be read?
- How are optional fields handled during initialization?
- Which default values are applied when a setting is missing from the file?
- What occurs when resolutionScale is outside its allowed set of values?
- How does init() handle non-const struct fields that have nested children?
- What is the purpose of the pub const version field imported from utils/version.zig?
- Which error condition causes a log message in init() and what does it return instead?

*Source: unknown | chunk_id: codebase_src_settings.zig_chunk_0*
