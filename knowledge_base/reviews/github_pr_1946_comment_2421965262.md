# [src/gui/GuiWindow.zig] - Chunk 2421965262

**Type:** review
**Keywords:** GuiWindow, mainButtonReleased, getButtonPositions, relative coordinates, inclusive bound, dead zone, zoom-out, grabPosition, reorderWindows, showTitleBar
**Symbols:** GuiWindow, getButtonPositions, mainButtonReleased, Vec2f, grabPosition, grabbedWindow, showTitleBar, reorderWindows, closeable, scale
**Concepts:** relative coordinates, inclusive/exclusive bounds, dead zone elimination, event handling robustness, UI hit testing, refactoring for clarity

## Summary
Refactored button hit detection logic to use relative coordinates and fixed an inclusive/exclusive boundary bug in the zoom-out region by making the lower bound inclusive.

## Explanation
The original code compared absolute mouse positions against button positions derived from `self.pos`, but it also implicitly relied on `grabPosition` being non-null before checking button regions. This caused two issues: (1) if the window was not grabbed, button clicks were ignored even when they should trigger actions; (2) the range checks used strict inequality (`>`) for both bounds, creating a tiny gap between icons that never responded to input. The fix moves all comparisons into relative space (`mousePositionRelative` and `grabPositionRelative`), simplifies the guard condition by checking `grabbedWindow == self` first (which already implies we care about this window regardless of grab state), and then evaluates button regions using relative offsets. Crucially, the lower bound is now inclusive (`>=`) while the upper remains exclusive (`<`), eliminating the dead zone between icons. This change preserves existing behavior for close/zoom-in actions while ensuring zoom-out works correctly across the full intended range.

## Related Questions
- What happens if grabPosition is null when a button click occurs?
- Why was the original lower bound strict inequality problematic?
- How does converting to relative coordinates simplify the guard condition?
- Does this change affect close or zoom-in behavior differently from zoom-out?
- Is there any risk of regression for windows without title bars after this refactor?
- What is the exact numeric difference between using > vs >= in this context?
- Could a user accidentally trigger an action by hovering exactly on the boundary now?
- How does this align with the broader UI consistency goals in GuiWindow.zig?
- Are there any other places in the codebase that use similar absolute-vs-relative comparisons?
- What testing scenarios should cover the newly inclusive lower bound?

*Source: unknown | chunk_id: github_pr_1946_comment_2421965262*
