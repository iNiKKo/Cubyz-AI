# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 0

**Type:** implementation
**Keywords:** pipeline init, alpha blending, SimpleVertex2D, texture load, deinit cleanup, enum variant, union relative position, callback function pointer, uniform struct, asset path
**Symbols:** GuiWindow, AttachmentPoint, OrientationLine, RelativePosition, globalInit, globalDeinit, defaultFunction, defaultFunctionWithResult
**Concepts:** GUI window management, shader pipeline initialization, texture loading, callback defaults, relative positioning system

## Summary
Defines the GuiWindow struct and its global initialization/deinitialization functions, including shader pipelines, textures, and callback defaults.

## Explanation
The chunk declares the GuiWindow struct with fields for position/size (Vec2f), content size, scale, spacing, relative positions (RelativePosition union), ID string, root component pointer, title bar reference, inventory shift pointer, render/update callbacks (defaultFunction/defaultFunctionWithResult), open/close callbacks, grabbed window state, background/title/close/zoom textures, and pipeline uniforms. It defines enums AttachmentPoint and RelativePosition unions with attachedToFrame/relativeToWindow/attachedToWindow variants. The globalInit function creates two graphics pipelines (button.vert/frag and window_border.vert/frag) using SimpleVertex2D, sets cullMode to none, depthTest/depthWrite false, alphaBlending attachments, then loads textures from assets/cubyz/ui/*.png files. globalDeinit calls deinit on pipeline and the three main textures (background, title, close). defaultFunction is an empty void function; defaultFunctionWithResult returns .ignored. All declarations are pub where appropriate for API exposure.

## Related Questions
- What are the default values for GuiWindow fields like pos, size, scale, and spacing?
- Which shader files are used to initialize the button pipeline in globalInit?
- How does RelativePosition handle attachment points versus ratio-based positioning?
- What happens to textures during globalDeinit compared to other resources?
- Why is cullMode set to none for both pipelines?
- What is the purpose of the grabPosition field and how does it relate to window dragging?
- How are renderFn, updateFn, and onOpenFn typed in the struct definition?
- Does GuiWindow store any state about whether a title bar should be shown or hidden?
- What uniform fields are defined for the border pipeline versus the main window pipeline?
- Is there any logic to handle multiple windows being grabbed simultaneously?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_0*
