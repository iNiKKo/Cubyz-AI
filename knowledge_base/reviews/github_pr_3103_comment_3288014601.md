# [src/server/command.zig] - Chunk 3288014601

**Type:** review
**Keywords:** Axis, Coordinate, Absolute, Relative, union, offset, value, type safety, documentation, parser, Zig
**Symbols:** Axis, Coordinate, Absolute, Relative
**Concepts:** type safety, union types, coordinate representation, absolute vs relative coordinates, documentation reduction, parser compatibility, Zig language features

## Summary
The reviewer critiques the current Axis struct for conflating absolute coordinates with relative offsets, suggesting a union-based Coordinate type to explicitly distinguish between Absolute (value) and Relative (offset) representations.

## Explanation
The existing code uses a single 'Axis' struct containing both an offset field and a value field. This design forces the use of comments to explain whether the fields represent absolute or relative coordinates, which is error-prone and obscures intent. The reviewer proposes introducing a union type (or a named union within a struct) that explicitly tags each coordinate as either 'absolute' or 'relative', thereby encoding the distinction in the type system rather than relying on documentation. This change would improve clarity, reduce comment burden, and potentially enable compile-time checks for misuse of absolute vs relative coordinates. However, the reviewer notes uncertainty about how the parser will handle such unions, suggesting that while unions are treated uniquely by Zig's compiler, they may still be acceptable here.

## Related Questions
- What is the current definition of Axis in command.zig?
- How does execute use Axis to parse coordinates?
- Where are absolute and relative coordinate values stored before this change?
- Does Zig support union types inside structs as suggested?
- Will changing Axis to a union break existing parser logic?
- What fields would Absolute and Relative structs contain after refactoring?
- How can we preserve backward compatibility when introducing Coordinate unions?
- Are there any tests that rely on the current Axis layout?
- Could we use tagged unions or inline unions in Zig for this purpose?
- What performance impact might a union-based coordinate have compared to a struct with offset/value fields?

*Source: unknown | chunk_id: github_pr_3103_comment_3288014601*
