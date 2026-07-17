# [easy/codebase_src_gui_windows_debug_vulkan_info.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, vulkan.version, interestingExtensions, std.meta.fieldNames, draw.print, @field, relativePosition, contentSize, isHud, showTitleBar
**Symbols:** onOpen, window, render
**Concepts:** debug GUI window, Vulkan version display, extension enumeration, draw API usage

## Summary
This chunk defines a debug GUI window that renders Vulkan version and enabled extension information.

## Explanation
The chunk imports the main module to access graphics, draw, vec, utils, and vulkan submodules; it also imports the gui module for GuiWindow and GuiComponent. It declares pub fn onOpen() which clears the threadPool.performance data. It defines a global pub var window of type GuiWindow with relativePosition set to two identical self-attached upper points, contentSize computed from Vec2f{160, 8 + 8*std.meta.fieldNames(@TypeOf(vulkan.interestingExtensions)).len}, and several boolean flags (isHud=false, showTitleBar=false, hasBackground=false, hideIfMouseIsGrabbed=false). The pub fn render() function iterates over vulkan.version.major/minor using draw.print, then comptime loops over std.meta.fieldNames(@TypeOf(vulkan.interestingExtensions)) to check each extension via @field and prints present extensions with draw.print.

## Related Questions
- What does onOpen() do in this chunk?
- How is the window contentSize calculated?
- Which fields of vulkan.interestingExtensions are checked at runtime?
- Does render() print all extensions or only enabled ones?
- Are any boolean flags set to true by default in window?
- What imports does this chunk depend on from main.graphics?
- How is the relativePosition configured for the GuiWindow?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug_vulkan_info.zig_chunk_0*
