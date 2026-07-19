# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 1

**Type:** implementation
**Keywords:** enum, union, switch, rotation logic, fixed rotation, random rotation, inherit rotation
**Symbols:** isChildBlock, isOriginBlock, RotationMode, Rotation, Rotation.FixedRotation, Rotation.apply, Rotation.getInitialRotation, Rotation.sampleRandom, Rotation.getChildRotation, Rotation.fromZon
**Concepts:** block rotation, child block check, origin block check

## Summary
Defines block rotation logic and checks for child and origin blocks.

## Explanation
This chunk defines functions to check if a block is a child or origin block. It also defines an enum `RotationMode` with three modes: fixed, random, and inherit. A union `Rotation` includes these modes along with methods for applying, getting initial, sampling random, and getting child rotations. The `FixedRotation` nested enum represents four fixed rotation angles: 0 ('@0'), 90 ('@90'), 180 ('@180'), and 270 ('@270') degrees.

The `apply` method applies a rotation to another rotation based on the current mode. If the mode is fixed, it adds the rotations modulo 4. For random and inherit modes, it returns the input rotation unchanged.

The `getInitialRotation` method returns the initial rotation based on the mode. For fixed mode, it returns the current rotation. For random mode, it samples a new random rotation. For inherit mode, it returns a fixed rotation of 0 degrees.

The `sampleRandom` function generates a random fixed rotation by sampling from the range [0, 3].

The `getChildRotation` method determines the child's rotation based on the direction and the child's rotation mode. If the direction is up or down, it handles random and inherit modes accordingly. For other directions, it returns a fixed rotation of 0 degrees.

The `fromZon` method parses rotations from Zon elements, supporting string and integer representations of rotation modes. It converts strings like 'fixed', 'random', or 'inherit' to their corresponding enum values. For integers, it calculates the equivalent fixed rotation by taking the absolute value modulo 4. The exact syntax for this method is as follows:

```zig
pub fn fromZon(zon: ZonElement) error{ UnknownString, UnknownType }!Rotation {
    return switch (zon) {
        .string, .stringOwned => |str| {
            if (std.meta.stringToEnum(FixedRotation, str)) |r| {
                return .{.fixed = r};
            }
            if (std.meta.stringToEnum(RotationMode, str)) |mode| {
                return switch (mode) {
                    .fixed => .{.fixed = .@"0"},
                    .random => .{.random = {}},
                    .inherit => .{.inherit = {}},
                };
            }
            return error.UnknownString;
        },
        .int => |value| .{.fixed = @enumFromInt(@abs(@divTrunc(value, 90))%4)},
        .float => |value| .{.fixed = @enumFromInt(@abs(@as(u64, @trunc(value/90.0)))%4)},
        .null => Rotation.random,
        else => return error.UnknownType,
    };
}
```

## Code Example
```zig
pub fn isChildBlock(block: Block) bool {
	return childBlockNumericIdMap.contains(block.typ);
}
```

## Related Questions
- How do you check if a block is a child block?
- What are the different rotation modes defined in this chunk?
- How does the `apply` method work for rotations?
- What is the purpose of the `sampleRandom` function?
- How is a rotation parsed from a Zon element?
- What fixed rotation angles are supported?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_1*
