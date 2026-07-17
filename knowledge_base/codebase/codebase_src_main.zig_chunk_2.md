# [hard/codebase_src_main.zig] - Chunk 2

**Type:** implementation
**Keywords:** threading, logging, command line arguments, environment variables, file system, windowing, graphics, audio, input bindings
**Symbols:** lastFrameTime, lastDeltaTime, shouldExitToMenu, exitToMenu, isHiddenOrParentHiddenPosix, main, findKey, key, setIsToggling
**Concepts:** input handling, game initialization, subsystem management, environment configuration

## Summary
Handles initialization and main loop of the Cubyz game engine, including setting up input bindings, logging, and initializing various subsystems.

## Explanation
This chunk contains the main entry point for the Cubyz game engine. It initializes essential components such as thread locals, logging, command line argument handling, environment settings, file system management, a thread pool, file monitoring, windowing, graphics, and audio systems. The code also defines input bindings for hotbar slots and camera controls, including both keyboard and gamepad inputs. Functions like `findKey`, `key`, and `setIsToggling` manage these input bindings. Additionally, it includes utility functions for checking hidden directories on POSIX systems and a global variable to track the last frame time.

## Code Example
```zig
fn findKey(name: []const u8) ?*Window.Key { // TODO: Maybe I should use a hashmap here?
	for (&keys) |*_key| {
		if (std.mem.eql(u8, name, _key.name)) {
			return _key;
		}
	}
	return null;
}
```

## Related Questions
- How does the game handle command line arguments?
- What is the purpose of the `findKey` function in the code?
- How are input bindings defined for hotbar slots and camera controls?
- What subsystems are initialized by the main function?
- How does the game manage hidden directories on POSIX systems?
- What is the role of the `lastFrameTime` variable in the engine?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_2*
