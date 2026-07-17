# [src/gui/windows/debug.zig] - Chunk 1660759153

**Type:** review
**Keywords:** fpsCapText, allocPrint, stackAllocator, unreachable, vsync, render, settings, conditional, string formatting, UI
**Symbols:** draw.setColor, draw.print, main.lastFrameTime, main.settings.vsync, main.settings.fpsCap, fpsCap, std.fmt.allocPrint, main.stackAllocator.allocator
**Concepts:** UI rendering, conditional string formatting, memory allocation safety, backwards compatibility, configuration-driven display, vsync indicator, FPS cap hint, error handling with unreachable

## Summary
The diff introduces a new `fpsCapText` string that conditionally appends an FPS limit note when `main.settings.fpsCap` is set, and replaces the previous hardcoded vsync-only suffix with this more flexible approach.

## Explanation
Previously the UI only displayed a vsync indicator (or none) based on `main.settings.vsync`. The reviewer notes that many standard library data structures depend on the existing behavior, so changing it would be risky. Instead of altering those dependencies, the change adds a separate optional string (`fpsCapText`) constructed via `std.fmt.allocPrint` using the allocator from `main.stackAllocator`. This preserves backward compatibility while allowing an FPS cap hint to appear when configured. The use of `catch unreachable` indicates confidence that allocation will succeed given the current memory model; if it fails, execution would be undefined (acceptable in this context). Architecturally, this decouples the UI text generation from the core vsync logic and keeps the rendering pipeline stable.

## Related Questions
- What is the type of `main.lastFrameTime` and why is `.load(.monotonic)` used?
- How does `std.fmt.allocPrint` interact with `main.stackAllocator.allocator` in this context?
- Why is `catch unreachable` acceptable here instead of a proper error handling path?
- What happens if `main.settings.fpsCap` is null versus non-null after the ternary expression?
- Does changing the vsync suffix to include fpsCap affect any existing tests or UI expectations?
- Is there any risk that allocating inside `render()` could cause performance issues on low-end devices?
- How does this change relate to the reviewer's comment about standard library data structures depending on something unchanged?
- What is the expected behavior of `draw.print` when `fpsCapText` is null versus a non-null string?
- Could `main.settings.fpsCap` be mutated between frames, and if so, how does that affect UI consistency?
- Is there any documentation or API contract for `GuiWindow.render()` that this modification must respect?

*Source: unknown | chunk_id: github_pr_532_comment_1660759153*
