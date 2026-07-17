# [hard/codebase_src_main.zig] - Chunk 3

**Type:** implementation
**Keywords:** thread pool, environment variables, FPS cap, iconified window, swap buffers, depth test, garbage collection sync point, GLFW callbacks, delta time, auto-enter world
**Symbols:** clientMain
**Concepts:** initialization, event loop, FPS limiting, window management, graphics rendering, garbage collection synchronization, headless mode, auto-enter world, GLFW callbacks, delta time calculation

## Summary
The main entry point for the client-side game loop, handling initialization of subsystems, window management, rendering updates with FPS limiting and event processing.

## Explanation
This chunk defines the global initialization sequence executed at startup: it retrieves the home path from environment variables (USERPROFILE on Windows or HOME otherwise), initializes file system settings, creates a thread pool sized to available CPU cores minus one, sets up file monitoring, window creation, graphics, audio, dynamic integer array storage, rotation callbacks, block entities, models, items, synchronization client, item-drop renderer, assets, mesh generation, rendering pipeline, network layer, entity client, GUI, and particle manager. It also initializes server terrain globally. For headless mode it starts the server thread directly; otherwise it enters clientMain(). The clientMain function checks settings.playerName to decide whether to open a name-change window or proceed to the main menu (or auto-enter world in dev builds). It sets up GLFW callbacks for framebuffer size, configures audio music, and then enters an event loop that runs while the GLFW window is not closed. Inside the loop it syncs garbage collection, checks if the window is iconified, swaps buffers when visible, measures GPU clear performance, clears depth/stencil/color with specific functions (GL_LESS depth test enabled, scissor disabled), and sleeps briefly if hidden. It calculates frame time using timestamps, enforces fpsCap by computing a sleep duration (with special handling for Windows oversleeping to avoid wasting power), computes deltaTime between frames, handles window events via Window.handleEvents(), processes file monitor events, updates the game world if present, renders either the player view or menu background depending on world state. The chunk contains no struct/enum definitions and all function bodies are large; therefore CODE_EXAMPLE is null.

## Related Questions
- What subsystems are initialized in the global init block of main.zig?
- How does clientMain decide whether to open a name-change window or proceed directly to the main menu?
- Under what condition is server.startFromExistingThread invoked instead of entering clientMain?
- Which GLFW function is used to check if the window has been iconified, and how is that state handled in the render loop?
- How does the code enforce a frame rate cap on Windows versus other platforms when minFrameTime becomes too large?
- What happens to rendering updates when game.world is null inside the main event loop?
- Where is the home path allocated, and how is its memory deallocated after initialization?
- Which entities are initialized only if headless mode is false (e.g., Window, graphics, audio)?
- How does the code measure GPU performance for the clear operation before clearing buffers?
- What is the purpose of heap.GarbageCollection.syncPoint() at the start of each frame?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_3*
