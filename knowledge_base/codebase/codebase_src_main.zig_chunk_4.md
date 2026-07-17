# [hard/codebase_src_main.zig] - Chunk 4

**Type:** implementation
**Keywords:** fpsCap, timestamp, handleEvents, deinit, openWindow, setMusic, refAllDeclsRecursiveExceptCImports, stackAllocator, globalAllocator
**Symbols:** refAllDeclsRecursiveExceptCImports
**Concepts:** render loop, frame timing, event handling, world update, GUI rendering, menu transition, reference counting, test recursion, allocator usage

## Summary
Main render loop orchestrating frame timing, event handling, world updates, rendering pipeline, GUI updates, and menu transitions.

## Explanation
The chunk contains the main game loop logic: it computes a minimum frame time from fpsCap, calculates sleep duration accounting for rendering delta (with Windows-specific oversleep handling), records begin timestamp and deltaTime, calls Window.handleEvents and file_monitor.handleEvents, conditionally updates the game world via game.update if game.world is non-null, renders either the player view or menu background depending on whether a world exists, updates and renders the GUI (including GPU performance query start/stop), handles exit-to-menu state by setting mouse ungrabbed, deinitializing the current world if present, opening the main window, and playing music. It also defines refAllDeclsRecursiveExceptCImports, a test-time recursive reference collector that skips C imports named 'c', 'hbft', 'stb_image' and the Managed hashmap type, recursing into struct/enum/union/opaque fields; includes two tests: one invoking refAllDeclsRecursiveExceptCImports on @This() after setting eval branch quota and importing zon.zig, and another verifying stackAllocator and globalAllocator can allocate/deallocate u64.

## Related Questions
- What is the purpose of refAllDeclsRecursiveExceptCImports and how does it handle C imports?
- How are GPU performance measurements captured in this chunk?
- Under what condition does the game world get deinitialized before opening the main window?
- Which allocator implementations are tested for usability, and how are they used?
- What happens to deltaTime calculation if endRendering.nanoseconds exceeds lastBeginRendering.nanoseconds?
- How is Windows oversleep behavior handled differently from other platforms?
- When does the renderer switch between player view and menu background rendering?
- Is there any synchronization mechanism for shouldExitToMenu updates in this chunk?
- What types are recursed into by refAllDeclsRecursiveExceptCImports, and which are skipped?
- How is the minimum sleep duration computed relative to minFrameTime?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_4*
