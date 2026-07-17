# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 1

**Type:** implementation
**Keywords:** globalDeinit, mainButtonPressed, getButtonPositions, detectCycles, snapToOtherWindow, relativePosition, attachedToFrame, grabbedWindow
**Symbols:** globalDeinit, defaultFunction, defaultFunctionWithResult, mainButtonPressed, getButtonPositions, mainButtonReleased, detectCycles, snapToOtherWindow
**Concepts:** window lifecycle management, mouse interaction handling, drag and drop, zoom scaling, cycle detection in window hierarchy, window snapping alignment

## Summary
Implements the GuiWindow struct and its lifecycle functions, including initialization of graphics pipelines and textures, mouse interaction handlers for window dragging and zooming, cycle detection between windows, and snapping logic to align windows.

## Explanation
The chunk defines a pub fn globalDeinit that cleans up pipeline and texture resources. It declares defaultFunction and defaultFunctionWithResult as stubs returning .ignored. The mainButtonPressed function handles mouse clicks on the title bar (grabbing the window) or delegates to rootComponent/mainButtonPressed if present, otherwise returns .handled for background windows. getButtonPositions computes positions of close/zoom buttons based on scale and iconWidth. mainButtonReleased processes drag-release events: it checks grabPosition against button regions to decide whether to zoom in/out (adjusting self.scale with bounds) or close the window; after handling it resets grabPosition and grabbedWindow, then forwards release events to titleBar and rootComponent if they exist. detectCycles walks the relativePosition fields of another window following attachedToFrame/relativeToWindow/attachedToWindow links until hitting a ratio (which terminates the walk), returning true only if self is encountered; this prevents infinite recursion when windows are cyclically attached. snapToOtherWindow iterates over gui.openWindows.items, computes overlap intervals on each axis, skips non-overlapping pairs and those that would create cycles via detectCycles, then measures distance to the nearest overlapping window (minDist) to decide snapping.

## Related Questions
- What does globalDeinit clean up in GuiWindow?
- How are button positions calculated for close and zoom controls?
- Under what conditions does mainButtonPressed return .handled versus delegating to rootComponent?
- Describe the logic inside detectCycles that walks relativePosition fields.
- What happens when a user releases the mouse over the zoom region in mainButtonReleased?
- How does snapToOtherWindow decide which window is closest for snapping?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_1*
