# [src/gui/tooltip.zig] - Chunk 3487928535

**Type:** review
**Keywords:** tooltip, texture, cornerSize, globalInit, renderFromText, GuiComponent, defer deinit, alignment, bound9SliceImage, window bounds
**Symbols:** tooltipTexture, cornerSize, globalInit, globalDeinit, posFromAlignment, render, renderFromText, GuiComponent.Label.init, draw.bound9SliceImage
**Concepts:** defer cleanup placement, texture binding, 9-slice scaling, alignment clamping, window bounds checking, line break calculation, resource lifecycle management

## Summary
The tooltip module introduces a background texture and corner sizing logic for rendering tooltips with proper alignment relative to mouse position and window bounds.

## Explanation
This change adds the tooltipTexture and cornerSize variables, initializes them in globalInit(), and provides render() and renderFromText() functions. The render() function computes the final position based on alignment (right/left/center) with offset handling for centering, then clamps to window bounds. It binds the texture, draws a 9-slice scaled image using cornerSize, and updates the GuiComponent's position before rendering the label. The renderFromText() function builds a Label component from raw text, calculates line breaks at fontSize=16 with max width 300, adjusts size accordingly, then renders via the same render logic. A reviewer flagged that the defer deinit for the component is placed far from its init (10 lines later), which violates the principle of keeping resource cleanup adjacent to allocation for clarity and safety.

## Related Questions
- What is the purpose of the cornerSize variable in tooltip.zig?
- How does posFromAlignment compute positions for different text alignments?
- Why is the texture bound to slot 0 before drawing?
- What happens if renderpos exceeds window bounds horizontally or vertically?
- Where should the defer deinit be placed according to the reviewer's concern?
- Does renderFromText handle multi-line text correctly with lineBreaks?
- Is there any risk of memory leaks in the tooltip module after this change?
- How does the code ensure tooltips stay within the window viewport?
- What is the role of draw.bound9SliceImage in rendering the tooltip background?
- Are there any assumptions about the size of tooltipTexture that could break on different resolutions?

*Source: unknown | chunk_id: github_pr_3276_comment_3487928535*
