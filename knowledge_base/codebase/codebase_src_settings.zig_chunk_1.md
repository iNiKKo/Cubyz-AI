# [medium/codebase_src_settings.zig] - Chunk 1

**Type:** serialization
**Keywords:** deinitialization, serialization, ZonElement, keyboard configuration, file reading/writing, environment variables
**Symbols:** deinit, save, launchConfig, launchConfig.cubyzDir, launchConfig.autoEnterWorld, launchConfig.headlessServer, launchConfig.preferredAuthenticationAlgorithm, launchConfig.vulkanTestingMode, launchConfig.init, environment, environment.SDL_GAMECONTROLLERCONFIG, environment.env, environment.init
**Concepts:** settings management, configuration loading, keyboard settings, file I/O

## Summary
Handles settings deinitialization and saving, including keyboard settings.

## Explanation
This chunk defines functions for deinitializing and saving settings. The `deinit` function saves the current settings and then deallocates non-const fields, handling both structs and slices. Specifically, it checks if a field is const using `@typeInfo(@TypeOf(&@field(@This(), decl.name))).pointer.is_const`, and if not, it deinitializes or frees the memory accordingly. The `save` function serializes settings into a ZonElement object, preserving unknown settings from an old file if it exists. It also handles keyboard settings specifically by iterating through `main.KeyBoard.keys` and creating a ZonElement for each key setting with fields like `key`, `mouseButton`, `scancode`, and `isToggling`. The `launchConfig` struct initializes configuration settings from a launch config file located at `main.files.cwd().readToZon(main.stackAllocator, "launchConfig.zon")`. It reads the following values: `cubyzDir` (a string path), `autoEnterWorld` (a string path), `headlessServer` (a boolean value), `preferredAuthenticationAlgorithm` (an enum of type `main.network.authentication.KeyTypeEnum`, defaulting to `.ed25519`), and `vulkanTestingMode` (a boolean value). The `environment` struct captures SDL-related environment variables using `env.getAlloc(main.globalArena.allocator, "SDL_GAMECONTROLLERCONFIG")`. This function retrieves the value of the `SDL_GAMECONTROLLERCONFIG` environment variable.

## Code Example
```zig
pub fn deinit() void {
	save();
	inline for (@typeInfo(@This()).@"struct".decls) |decl| {
		const is_const = @typeInfo(@TypeOf(&@field(@This(), decl.name))).pointer.is_const; // Sadly there is no direct way to check if a declaration is const.
		if (!is_const) {
			const DeclType = @TypeOf(@field(@This(), decl.name));
			if (@typeInfo(DeclType) == .@"struct") {
				if (DeclType == std.Io.Duration) continue;
				@field(@This(), decl.name).deinit(main.globalAllocator);
				continue;
			}
			if (@typeInfo(DeclType) == .pointer) {
				if (@typeInfo(DeclType).pointer.size == .slice) {
					main.globalAllocator.free(@field(@This(), decl.name));
				} else {
					@compileError("Not implemented yet.");
				}
			}
		}
	}
}
```

## Related Questions
- How does the `deinit` function handle non-const fields?
- What is the purpose of the `save` function in this chunk?
- How are keyboard settings serialized in the `save` function?
- What file is read during the initialization of `launchConfig`?
- How does the `environment` struct capture SDL-related environment variables?
- What error handling is implemented when reading or writing settings files?

*Source: unknown | chunk_id: codebase_src_settings.zig_chunk_1*
