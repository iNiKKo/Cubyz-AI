# [easy/codebase_src_server_command_particles.zig] - Chunk 0

**Type:** implementation
**Keywords:** command parsing, particle system, error management, user interaction, network communication
**Symbols:** description, usage, execute, parseArguments, parseBool, parseNumber
**Concepts:** command handling, particle spawning, error handling

## Summary
Handles the /particles command to spawn particles in the game world.

## Explanation
Handles the /particles command to spawn particles in the game world. The chunk defines a function `execute` that parses arguments for spawning particles and sends them to connected users. It uses helper functions like `parseArguments`, `parseBool`, and `parseNumber` to validate and parse input parameters. The function handles errors such as too few or many arguments, invalid boolean values, and overflowed particle counts.

The command usage is defined as follows:
```
/particles <id> <x> <y> <z>
/particles <id> <x> <y> <z> <collides>
/particles <id> <x> <y> <z> <collides> <count>
/particles <id> <x> <y> <z> <collides> <count> <spawnDataZon>
```
The `execute` function sends particles to connected users using the `main.network.protocols.genericUpdate.sendParticles` function. The maximum number of particles that can be spawned is determined by `particles.ParticleSystem.maxCapacity`. If a particle count exceeds this limit, an error message is sent to the user and the command execution stops.

The helper functions are:
- `parseArguments`: Parses arguments for spawning particles and handles errors such as too few or many arguments, invalid boolean values, and overflowed particle counts. It sends appropriate error messages to the user if any of these conditions occur. The specific error handling messages include '#ff0000Too few arguments for command /particles', '#ff0000Too many arguments for command /particles', '#ff0000Invalid argument. Expected "true" or "false"', and '#ff0000Expected number, found "{s}"'.
- `parseBool`: Validates whether a given argument is either 'true' or 'false'. If not, it returns an error message indicating an invalid boolean value.
- `parseNumber`: Parses a number and handles overflow errors by sending an error message with the maximum particle count. The specific error handling message includes '#ff0000Too many particles spawned "{s}", maximum: "{d}"', where `{d}` is the value of `particles.ParticleSystem.maxCapacity`.

Additionally, the command usage supports using '~' to apply current player position coordinates in `<x> <y> <z>` fields. The `spawnDataZon` parameter can be used to specify additional properties for particles such as shape, radius, mode, speed, lifeTime, and randomRotate. The structure of `spawnDataZon` is a JSON-like object with the following fields:
- `.shape`: Specifies the shape of the particle spawn area (e.g., .sphere).
- `.radius`: Specifies the radius of the particle spawn area.
- `.mode`: Specifies the mode of particle spawning (e.g., .scatter).
- `.speed`: Specifies the speed range for particles as a tuple (min, max).
- `.lifeTime`: Specifies the lifetime range for particles as a tuple (min, max).
- `.randomRotate`: A boolean indicating whether particles should rotate randomly.

The `execute` function handles invalid number inputs for particle count by sending an error message '#ff0000Expected number, found "{s}"' and returning without further execution.

## Code Example
```zig
fn execute(args: []const u8, source: *User) void {
	parseArguments(source, args) catch |err| {
		switch (err) {
			error.TooFewArguments => source.sendMessage("#ff0000Too few arguments for command /particles", .{}),
			error.TooManyArguments => source.sendMessage("#ff0000Too many arguments for command /particles", .{}),
			error.InvalidBoolean => source.sendMessage("#ff0000Invalid argument. Expected \"true\" or \"false\"", .{}),
			error.InvalidNumber => return,
		}
		return;
	};
}
```

## Related Questions
- What is the purpose of the `execute` function in this chunk?
- How does the `parseArguments` function handle errors and what messages are sent to the user if an error occurs?
- What is the role of the `parseBool` function in the command handling process?
- What is the maximum number of particles that can be spawned according to the code, and how is it handled if a particle count exceeds this limit?
- How does the `execute` function send particles to connected users?
- What are the possible errors that can occur during the execution of the `/particles` command and what messages are sent to the user in each case?
- What is the purpose of the `parseNumber` function in the command handling process?
- How does the `execute` function handle invalid number inputs for particle count?
- What is the role of the `main.server.getUserListAndIncreaseRefCount` and `main.server.freeUserListAndDecreaseRefCount` functions in the code?
- What is the purpose of the `main.network.protocols.genericUpdate.sendParticles` function in the code?
- How does the `execute` function handle cases where the user list is empty or null?
- What are the possible scenarios where the `parseArguments` function might fail and what messages are sent to the user?

*Source: unknown | chunk_id: codebase_src_server_command_particles.zig_chunk_0*
