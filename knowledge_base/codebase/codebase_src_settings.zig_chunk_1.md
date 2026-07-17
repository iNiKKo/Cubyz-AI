# [medium/codebase_src_settings.zig] - Chunk 1

**Type:** configuration
**Keywords:** readToZon, writeZon, join, preferLeft, getAlloc, dupe, fallback defaults, globalArena, pub var, struct fields
**Symbols:** launchConfig, environment
**Concepts:** configuration loading, file I/O, ZonElement serialization, arena allocation, settings merging

## Summary
This chunk defines the public API for loading and saving Cubyz configuration files (launchConfig.zon) and environment variables, including merging old settings while preserving unknown fields.

## Explanation
The chunk declares two top-level structs: launchConfig and environment. launchConfig contains pub var fields cubyzDir, autoEnterWorld, headlessServer, preferredAuthenticationAlgorithm, vulkanTestingMode, and a pub fn init() that reads launchConfig.zon from the current working directory using main.files.cwd().readToZon(), then populates each field by calling zon.get() with fallbacks to defaults. It also dupe()-s string fields into main.globalArena for ownership transfer. environment contains pub var SDL_GAMECONTROLLERCONFIG and env, plus a pub fn init(_env: std.process.Environ) that copies the environ and allocates SDL_GAMECONTROLLERCONFIG via env.getAlloc(main.globalArena.allocator, 

## Related Questions
- What are the default values used when launchConfig.zon is missing or a field cannot be read?
- How does the chunk ensure that unknown settings from an old configuration file are not lost during merging?
- Which allocator is used to store string fields copied from launchConfig.zon, and why is this choice made?
- What happens if reading launchConfig.zon fails with an error other than FileNotFound?
- Does the chunk write any data back to disk when init() runs, or only read?
- How are boolean flags like headlessServer and vulkanTestingMode initialized in launchConfig?

*Source: unknown | chunk_id: codebase_src_settings.zig_chunk_1*
