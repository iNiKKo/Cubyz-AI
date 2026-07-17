# [medium/codebase_src_server_command.zig] - Chunk 0

**Type:** api
**Keywords:** StringHashMap, union enum, parse float, clamp, permission path, user pointer, split iterator, invalid argument error, too few arguments, reference count
**Symbols:** commandList, Command, commands, init, deinit, execute, Coordinate, parse, resolveCoordinates, parseAxis, parseCoordinates, parsePlayerIndexAndIncreaseRefCount, Target
**Concepts:** command registry, permission checking, coordinate parsing, relative coordinates, player index specifier, reference counting, argument splitting

## Summary
This chunk defines the server command system, including a Command struct with execution callbacks, a global commands registry initialized from an imported list, and parsing utilities for coordinates (absolute/relative), axis arguments, player index specifiers, and target resolution.

## Explanation
The chunk declares pub const commandList as an import from 'command/_list.zig', which is used to populate the global std.StringHashMap(Command) commands via init(). The Command struct contains fields exec (a function pointer), name, description, usage, and permissionPath. The execute(msg, source) function parses the incoming message up to the first space to extract the command name, looks it up in the registry, checks permissions on the User object, logs a green success or red failure message, and invokes cmd.exec with any remaining arguments. Coordinate is a union(enum) with relative (f64) and absolute (f64) variants; its parse method handles optional leading '~' prefix, returns zero for empty relative input, parses numbers via std.fmt.parseFloat, and reports ParseError on invalid input. resolveCoordinates takes three Coordinate values and a player pointer, clamps each axis to [-1e9, 1e9] (with a TODO to remove the clamp after issue #310), and returns a main.vec.Vec3d. parseAxis is an internal helper that mirrors coordinate parsing for single-axis arguments, also clamping and reporting InvalidNumber on failure. parseCoordinates iterates over three split tokens using parseAxis, handling TooFewArguments if fewer than three args are present. parsePlayerIndexAndIncreaseRefCount validates that a player specifier starts with '@', parses the integer index after '@', calls main.server.getUserByIndexAndIncreaseRefCount, and reports InvalidArg if not found or not online. Target is a struct holding a user pointer and an increasedRefCount flag; its init method peeks at the first split token to decide whether it's a player specifier (starting with '@') or just the source itself, calling parsePlayerIndexAndIncreaseRefCount for the former and setting increasedRefCount accordingly.

## Related Questions
- How does the command registry initialize from the imported list?
- What happens when a user lacks permission for a command in execute?
- How are relative coordinates distinguished from absolute ones in Coordinate.parse?
- Why is there a clamp around coordinate values and what issue number relates to removing it?
- What error is returned if parseCoordinates receives fewer than three arguments?
- How does parsePlayerIndexAndIncreaseRefCount validate the '@' prefix for player specifiers?
- When does Target.init treat the first split token as just the source user instead of a player specifier?
- Which function is responsible for increasing the reference count on a User when resolving targets?
- What message is sent to the user if parseAxis fails to convert an argument to a number?
- How does execute handle unrecognized commands versus permission-denied cases?

*Source: unknown | chunk_id: codebase_src_server_command.zig_chunk_0*
