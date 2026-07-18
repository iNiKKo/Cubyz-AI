# [hard/codebase_src_main.zig] - Chunk 4

**Type:** implementation
**Keywords:** game loop, event handling, world updates, rendering, FPS capping, testing utilities
**Symbols:** clientMain, refAllDeclsRecursiveExceptCImports
**Concepts:** game loop, GUI management, audio handling, rendering, FPS capping, testing utilities

## Summary
The chunk defines the main client entry point and utility functions for testing.

## Explanation
This chunk contains the `clientMain` function, which serves as the primary entry point for the Cubyz client. It handles initialization tasks such as setting up the GUI, audio, and rendering environment. The function manages the game loop, including event handling, world updates, rendering, and FPS capping. Additionally, it provides a utility function `refAllDeclsRecursiveExceptCImports` to recursively reference all declarations in a type while excluding C imports. The chunk also includes test functions to ensure allocators are usable in tests.

## Code Example
```zig
pub fn clientMain() void { // MARK: clientMain()
	if (settings.playerName.len == 0) {
		gui.openWindow("change_name");
	} else if (settings.launchConfig.autoEnterWorld.len == 0) {
		gui.openWindow("main");
	} else {
		// Speed up the dev process by entering the world directly.
		gui.windowlist.save_selection.openWorld(settings.launchConfig.autoEnterWorld);
	}

	Window.GLFWCallbacks.framebufferSize(undefined, Window.width, Window.height);
	var lastBeginRendering = timestamp();

	audio.setMusic("cubyz:totaldemented/cubyz_remastered");

	while (c.glfwWindowShouldClose(Window.window) == 0) {
		heap.GarbageCollection.syncPoint();
		const isHidden = c.glfwGetWindowAttrib(Window.window, c.GLFW_ICONIFIED) == c.GLFW_TRUE;
		if (!isHidden) {
			c.glfwSwapBuffers(Window.window);
			// Clear may also wait on vsync, so it's done before handling events:
			gui.windowlist.gpu_performance_measuring.startQuery(.screenbuffer_clear);
			c.glDepthFunc(c.GL_LESS);
			c.glDepthMask(c.GL_TRUE);
			c.glDisable(c.GL_SCISSOR_TEST);
			c.glClearColor(0.5, 1, 1, 1);
			c.glClear(c.GL_DEPTH_BUFFER_BIT | c.GL_STENCIL_BUFFER_BIT | c.GL_COLOR_BUFFER_BIT);
			gui.windowlist.gpu_performance_measuring.stopQuery();
		} else {
			io.sleep(.fromMilliseconds(16), .awake) catch {};
		}

		const endRendering = timestamp();
		const frameTime = @as(f64, @floatFromInt(endRendering.nanoseconds -% lastBeginRendering.nanoseconds))/1.0e9;
		lastFrameTime.store(frameTime, .monotonic);

		if (settings.fpsCap) |fpsCap| {
			const minFrameTime = @divFloor(1000*1000*1000, fpsCap);
			const sleep = @min(minFrameTime, @max(0, minFrameTime - (endRendering.nanoseconds -% lastBeginRendering.nanoseconds)));
			if (builtin.os.tag == .windows and minFrameTime < 20_000_000) { // Windows can oversleep a lot, so we waste power instead
				const targetTime = timestamp().addDuration(.fromNanoseconds(sleep));
				while (timestamp().durationTo(targetTime).nanoseconds > 0) {}
			} else {
				io.sleep(.fromNanoseconds(sleep), .awake) catch {};
			}
		}
		const begin = timestamp();
		const deltaTime = @as(f64, @floatFromInt(begin.nanoseconds -% lastBeginRendering.nanoseconds))/1.0e9;
		lastDeltaTime.store(deltaTime, .monotonic);
		lastBeginRendering = begin;

		Window.handleEvents(deltaTime);

		file_monitor.handleEvents();

		if (game.world != null) { // Update the game
			game.update(deltaTime);
		}

		if (!isHidden) {
			if (game.world != null) {
				renderer.updateFov(settings.fov);
				renderer.render(game.Player.getEyePosBlocking(), deltaTime);
			} else {
				renderer.updateFov(70.0);
				renderer.MenuBackGround.render(deltaTime);
			}
			// Render the GUI
			gui.windowlist.gpu_performance_measuring.startQuery(.gui);
			gui.updateAndRenderGui();
			gui.windowlist.gpu_performance_measuring.stopQuery();
		}

		if (shouldExitToMenu.load(.monotonic)) {
			shouldExitToMenu.store(false, .monotonic);
			Window.setMouseGrabbed(false);
			if (game.world) |world| {
				world.deinit();
				game.world = null;
			}
			gui.openWindow("main");
			audio.setMusic("cubyz:totaldemented/cubyz_remastered");
		}
	}

	if (game.world) |world| {
		world.deinit();
		game.world = null;
	}
}
```

## Related Questions
- What is the primary entry point for the Cubyz client?
- How does the `clientMain` function handle initialization tasks?
- What is the role of the game loop in the `clientMain` function?
- How does the `clientMain` function manage FPS capping?
- What utility functions are provided in this chunk?
- How does the `refAllDeclsRecursiveExceptCImports` function work?
- What tests are included in this chunk?
- How do the test functions ensure allocators are usable?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_4*
