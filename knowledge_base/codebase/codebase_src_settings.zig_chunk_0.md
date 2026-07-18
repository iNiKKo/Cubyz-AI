# [medium/codebase_src_settings.zig] - Chunk 0

**Type:** configuration
**Keywords:** ZON file, settings initialization, optional values, data parsing, logging errors
**Symbols:** version, defaultPort, connectionTimeout, entityLookback, highestSupportedLod, lastVersionString, simulationDistance, cpuThreads, anisotropicFiltering, fpsCap, fov, mouseSensitivity, controllerSensitivity, invertMouseY, renderDistance, highestLod, resolutionScale, bloom, vsync, playerName, showPlayerIndexWithName, streamerMode, lastUsedIPAddress, storedAccount, guiScale, musicVolume, leavesQuality, lod0.5Distance, blockContrast, nightBrightness, storageTime, updateRepeatSpeed, updateRepeatDelay, controllerAxisDeadzone, settingsFile, init
**Concepts:** configuration, file I/O, error handling

## Summary
This chunk defines various configuration settings for the Cubyz engine and provides a function to initialize these settings from a ZON file.

## Explanation
The chunk declares a series of public constants and variables representing different settings such as default port, connection timeout, entity lookback, and more. It also includes an `init` function that reads settings from a ZON file into these variables. The function handles various data types, including optional values and custom structs like `std.Io.Duration`. It logs errors if the settings file cannot be read or if there are issues parsing specific settings.

## Code Example
```zig
pub fn init() void {
	const zon: ZonElement = main.files.cubyzDir().readToZon(main.stackAllocator, settingsFile) catch |err| blk: {
		if (err != error.FileNotFound) {
			std.log.err("Could not read settings file: {s}", .{@errorName(err)});
		}
		break :blk .null;
	};
	defer zon.deinit(main.stackAllocator);

	inline for (@typeInfo(@This()).@"struct".decls) |decl| runtimeContinueInsideOfComptimeBlock: {
		const is_const = @typeInfo(@TypeOf(&@field(@This(), decl.name))).pointer.is_const; // Sadly there is no direct way to check if a declaration is const.
		if (!is_const) {
			comptime var DeclType = @TypeOf(@field(@This(), decl.name));
			if (@typeInfo(DeclType) == .optional) {
				DeclType = @typeInfo(DeclType).optional.child;
			}
			if (@typeInfo(DeclType) == .@"struct") {
				if (DeclType == std.Io.Duration) {
					const defaultMilli = @as(f64, @floatFromInt(@field(@This(), decl.name).toNanoseconds()))/1.0e6;
					@field(@This(), decl.name) = .fromNanoseconds(@trunc((zon.get(f64, decl.name) orelse defaultMilli)*1.0e6));
					continue;
				}
				@field(@This(), decl.name) = DeclType.fromZon(main.globalAllocator, zon.getChild(decl.name)) catch |err| {
					std.log.err("Got error while loading setting {s}: {s}", .{decl.name, @errorName(err)});
					break :runtimeContinueInsideOfComptimeBlock;
				};
				continue;
			}
			@field(@This(), decl.name) = zon.get(DeclType, decl.name) orelse @field(@This(), decl.name);
			if (@typeInfo(DeclType) == .pointer) {
				if (@typeInfo(DeclType).pointer.size == .slice) {
					@field(@This(), decl.name) = main.globalAllocator.dupe(@typeInfo(DeclType).pointer.child, @field(@This(), decl.name));
				} else {
					@compileError("Not implemented yet.");
				}
			}
		}
	}

	if (resolutionScale != 1 and resolutionScale != 0.5 and resolutionScale != 0.25) resolutionScale = 1;

	// keyboard settings:
	const keyboard = zon.getChild("keyboard");
	for (&main.KeyBoard.keys) |*key| {
		const keyZon = keyboard.getChild(key.name);
		key.key = keyZon.get(c_int, "key") orelse key.key;
		key.mouseButton = keyZon.get(c_int, "mouseButton") orelse key.mouseButton;
		key.scancode = keyZon.get(c_int, "scancode") orelse key.scancode;
		if (key.isToggling != .never) {
			key.isToggling = std.meta.stringToEnum(Window.Key.IsToggling, keyZon.get([]const u8, "isToggling") orelse "") orelse key.isToggling;
		}
	}
}
```

## Related Questions
- What is the default port setting for Cubyz?
- How does the engine handle missing settings in the ZON file?
- Which settings are optional and how are they handled?
- What is the purpose of the `init` function in this chunk?
- How are durations like `storageTime` parsed from the ZON file?
- What error handling is implemented when reading the settings file?

*Source: unknown | chunk_id: codebase_src_settings.zig_chunk_0*
