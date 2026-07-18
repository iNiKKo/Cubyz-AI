# [issues/issue_2318.md] - Issue #2318 discussion

**Type:** review
**Keywords:** command handling, argument parsing, reflection, standardization, error messages, custom types, usage generation
**Symbols:** CommandCaller, Arguments, execute, @typeInfo, Coordinate, parse
**Concepts:** Reflection, Standardization, Error Handling, Custom Types

## Summary
Proposes unifying command handling by creating a shared `CommandCaller` that parses arguments using reflection.

## Explanation
Proposes unifying command handling by creating a shared `CommandCaller` that parses arguments using reflection. The current implementation of commands in Cubyz results in duplicated parsing logic and inconsistent behavior. The proposed solution involves creating a `CommandCaller` that handles argument parsing, error message generation, and execution. This would standardize command handling, simplify the addition of new commands, and prevent inconsistencies.

The `CommandCaller` uses reflection (`@typeInfo`) to parse arguments based on their declared types, allowing for automatic error messages and support for custom types with a `parse` function. For example, the struct definition for `Arguments` is as follows:

```zig
pub const Arguments = struct {
    x: usize,
    y: usize,
    z: usize,
    player: []const u8,
};
```

The `execute` function receives this struct as its parameter. Additionally, custom types like `Coordinate` can be defined with a `parse` function to handle specific parsing logic:

```zig
pub const Coordinate = struct {
    value: ?isize = null,

    pub fn parse(str: []const u8) !Coordinate {
        if (str.len == 1 and str[0] == '~') return .{};
        return .{ .value = try std.fmt.parseInt(isize, str, 10) };
    }
};
```

The `CommandCaller` can also generate usage messages and descriptions automatically. This approach simplifies the addition of new commands by providing a standardized way to handle arguments and errors.

## Related Questions
- How does the `CommandCaller` handle custom argument types?
- What is the role of the `parse` function in custom types?
- How does the `CommandCaller` generate error messages for invalid arguments?
- Can you explain how reflection (`@typeInfo`) is used to parse command arguments?
- What are the benefits of using a shared `CommandCaller` for command handling?
- How would adding a new command differ with this unified approach?
- Is there any potential performance impact from using reflection in argument parsing?
- Can you provide an example of how the `printUsage` function might be implemented?

*Source: unknown | chunk_id: github_issue_2318_discussion*
