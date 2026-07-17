# [src/gui/windows/graphics.zig] - Chunk 2882110596

**Type:** review
**Keywords:** fpsCapRound, FPSPresetsValue, u16, f32, preset, lookup table, static const, branching, rounding, deterministic
**Symbols:** fpsCapRound, FPSPresetsValue
**Concepts:** FPS preset values, static lookup table, floating-point comparison, deterministic behavior, code simplification, rounding logic

## Summary
Replaced a custom rounding function for FPS values with a static array of preset FPS values to simplify logic and improve readability.

## Explanation
The original code defined a function fpsCapRound that took an f32, performed conditional integer division by 5.0 when the value was below 144.0, returned a capped value between 144.0 and 149.0 as-is, and otherwise returned null. This approach required floating-point comparisons and branching logic at runtime. The reviewer suggested replacing this with a const array FPSPresetsValue containing discrete FPS steps (5, 10, 15, ..., 360, 480). By using a static lookup table, the code becomes deterministic, avoids unnecessary float-to-int conversions, and makes it obvious which values are supported. This change also reduces potential for rounding errors and simplifies any downstream selection logic that previously relied on the function's return type (?u32) to now work with a fixed set of u16 presets.

## Related Questions
- What values are included in the FPSPresetsValue array?
- How does fpsCapRound handle inputs below 144.0 before the change?
- Why was fpsCapRound replaced with a static array instead of keeping the function?
- Is there any runtime computation involved after introducing FPSPresetsValue?
- What type is returned by fpsCapRound in the original code versus the new approach?
- Does the new preset list cover all previously supported FPS values from fpsCapRound?
- How might downstream code that called fpsCapRound need to adapt to use FPSPresetsValue?
- Are there any edge cases where a non-preset FPS value would be lost with the static array?
- What is the benefit of using u16 for presets compared to returning ?u32 from fpsCapRound?
- Could the static array cause issues if new hardware supports higher FPS not in the list?

*Source: unknown | chunk_id: github_pr_2395_comment_2882110596*
