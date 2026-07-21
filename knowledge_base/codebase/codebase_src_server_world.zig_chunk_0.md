# [hard/codebase_src_server_world.zig] - Chunk 0

**Type:** implementation
**Keywords:** world settings, folder name validation, ZonElement serialization, directory creation, error handling
**Symbols:** Settings, Settings.defaultGamemode, Settings.allowCheats, Settings.testingMode, Settings.seed, Settings.defaults, Settings.fromZon, Settings.toZon, findValidFolderName, tryCreateWorld
**Concepts:** world creation, settings management, file I/O, directory handling

## Summary
Handles world creation and settings management.

## Explanation
**Explanation**

This chunk defines the `Settings` struct for managing world configuration, including default gamemode (`creative`), cheat allowance (`true`), testing mode (`false`), and seed (`undefined`). It includes methods to load (`fromZon`) and save (`toZon`) these settings from/to a ZonElement format. The `findValidFolderName` function ensures that the world folder name is valid by escaping illegal characters (e.g., replacing non-ASCII characters with `-`) and avoiding duplicates by appending an index if necessary. The `tryCreateWorld` function creates a new world directory, initializes world information, writes it to disk, and sets up necessary subdirectories (`assets`). Additionally, the code handles errors such as missing seeds when loading world settings.

**Detailed Explanation**

- **Settings Struct**: The `Settings` struct contains four fields: `defaultGamemode`, `allowCheats`, `testingMode`, and `seed`. The default values are set to `.creative`, `true`, `false`, and `undefined`, respectively. The `defaults` constant provides a default instance of the `Settings` struct.

- **fromZon Method**: This method loads settings from a ZonElement. It retrieves the seed, default gamemode, allowCheats, and testingMode values. If any of these values are missing, it uses the default value. If the seed is missing, it logs an error and returns `error.NoSeed`.

- **toZon Method**: This method saves settings to a ZonElement. It converts the `defaultGamemode` to its string representation using `@tagName`, and then adds all fields (`allowCheats`, `testingMode`, and `seed`) to the ZonElement.

- **findValidFolderName Function**: This function ensures that the world folder name is valid by escaping illegal characters (e.g., replacing non-ASCII characters with `-`). It also avoids duplicates by appending an index if necessary. The function uses a stack allocator for temporary storage and returns a duplicated string using the provided allocator.

- **tryCreateWorld Function**: This function creates a new world directory, initializes world information, writes it to disk, and sets up necessary subdirectories (`assets`). It handles errors such as missing seeds when loading world settings. The function uses stack allocators for temporary storage and returns an error if any step fails.

**Code Example**

```zig
pub const Settings = struct {
    defaultGamemode: Gamemode = .creative,
    allowCheats: bool = true,
    testingMode: bool = false,
    seed: u64 = undefined,

    pub const defaults: Settings = .{};

    pub fn fromZon(zon: ZonElement) error{NoSeed}!Settings {
        return .{
            .seed = zon.get(u64, "seed") orelse {
                std.log.err("Cannot load world. World has no seed!", .{});
                return error.NoSeed;
            },
            .defaultGamemode = std.meta.stringToEnum(main.game.Gamemode, zon.get([]const u8, "defaultGamemode") orelse @tagName(defaults.defaultGamemode)) orelse defaults.defaultGamemode,
            .allowCheats = zon.get(bool, "allowCheats") orelse defaults.allowCheats,
            .testingMode = zon.get(bool, "testingMode") orelse defaults.testingMode,
        };
    }

    pub fn toZon(self: Settings, allocator: NeverFailingAllocator) ZonElement {
        const zon = main.ZonElement.initObject(allocator);

        zon.put("defaultGamemode", @tagName(self.defaultGamemode));
        zon.put("allowCheats", self.allowCheats);
        zon.put("testingMode", self.testingMode);
        zon.put("seed", self.seed);

        return zon;
    }
}
```

## Code Example
```zig
pub const Settings = struct {
	defaultGamemode: Gamemode = .creative,
	allowCheats: bool = true,
	testingMode: bool = false,
	seed: u64 = undefined,

	pub const defaults: Settings = .{};

	pub fn fromZon(zon: ZonElement) error{NoSeed}!Settings {
		return .{
			.seed = zon.get(u64, "seed") orelse {
				std.log.err("Cannot load world. World has no seed!", .{});
				return error.NoSeed;
			},
			.defaultGamemode = std.meta.stringToEnum(main.game.Gamemode, zon.get([]const u8, "defaultGamemode") orelse @tagName(defaults.defaultGamemode)) orelse defaults.defaultGamemode,
			.allowCheats = zon.get(bool, "allowCheats") orelse defaults.allowCheats,
			.testingMode = zon.get(bool, "testingMode") orelse defaults.testingMode,
		};
	}

	pub fn toZon(self: Settings, allocator: NeverFailingAllocator) ZonElement {
		const zon = main.ZonElement.initObject(allocator);

		zon.put("defaultGamemode", @tagName(self.defaultGamemode));
		zon.put("allowCheats", self.allowCheats);
		zon.put("testingMode", self.testingMode);
		zon.put("seed", self.seed);

		return zon;
	}
}
```

## Related Questions
- How does the `Settings` struct handle default values?
- What is the purpose of the `findValidFolderName` function?
- How are world settings serialized and deserialized in this chunk?
- What error handling is implemented when creating a new world?
- How does the chunk ensure unique folder names for worlds?
- What subdirectories are created during world initialization?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_0*
