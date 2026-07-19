# [src/server/command/_command.zig] - PR #2825 review diff

**Type:** review
**Keywords:** Blueprint.capture, Selection, init, min/max, refactor, encapsulation, code organization, redundancy reduction, Vec3i, capture
**Symbols:** Blueprint.capture, Selection, init, minPos, maxPos, Vec3i
**Concepts:** Code Refactoring, Structural Improvements, Encapsulation, Redundancy Reduction

## Summary
The reviewer suggests improving the `Blueprint.capture` function by changing its parameter to a `Selection` struct that includes methods for initialization and size calculation, reducing redundancy in min/max operations.

## Explanation
The reviewer suggests improving the `Blueprint.capture` function by changing its parameter to a `Selection` struct that includes methods for initialization and size calculation, reducing redundancy in min/max operations. The `Selection` struct should be defined in `blueprint.zig` with `minPos`, `maxPos`, and an `init` method that automatically handles min/maxing of the provided positions. Additionally, adding a `size` method to the `Selection` struct could further simplify related logic in other parts of the codebase. This change aims to enhance code organization and reduce duplication.

The `Selection` struct would be defined as follows:
```zig
const Selection = struct {
    minPos: Vec3i,
    maxPos: Vec3i,

    fn init(pos1: Vec3i, pos2: Vec3i) Selection {
        const startX = @min(pos1[0], pos2[0]);
        const startY = @min(pos1[1], pos2[1]);
        const startZ = @min(pos1[2], pos2[2]);

        const endX = @max(pos1[0], pos2[0]);
        const endY = @max(pos1[1], pos2[1]);
        const endZ = @max(pos1[2], pos2[2]);

        return Selection{
            .minPos = Vec3i{.x = startX, .y = startY, .z = startZ},
            .maxPos = Vec3i{.x = endX, .y = endY, .z = endZ},
        };
    }

    fn size(self: Selection) Vec3i {
        return Vec3i{
            .x = self.maxPos.x - self.minPos.x + 1,
            .y = self.maxPos.y - self.minPos.y + 1,
            .z = self.maxPos.z - self.minPos.z + 1,
        };
    }
};
```

The `Blueprint.capture` function would then be updated to accept a `Selection` struct instead of raw positions:
```zig
pub fn capture(allocator: NeverFailingAllocator, selection: Selection) CaptureResult {
    const startX = selection.minPos.x;
    const startY = selection.minPos.y;
    const startZ = selection.minPos.z;

    const endX = selection.maxPos.x;
    const endY = selection.maxPos.y;
    const endZ = selection.maxPos.z;

    // Existing capture logic using startX, startY, startZ, endX, endY, endZ
}
```

By encapsulating the selection logic within a dedicated struct, the code becomes more organized and reduces redundancy in min/max operations.

## Related Questions
- How does the proposed `Selection` struct improve code readability?
- What are the potential performance implications of using a `Selection` struct instead of raw positions?
- Can you provide an example of how the `size` method in the `Selection` struct could be implemented?
- How might this change affect existing code that calls `Blueprint.capture`?
- What are the benefits of encapsulating selection logic within a dedicated struct?
- How does this refactoring align with the overall architecture of the Cubyz project?

*Source: unknown | chunk_id: github_pr_2825_comment_3039281803*
