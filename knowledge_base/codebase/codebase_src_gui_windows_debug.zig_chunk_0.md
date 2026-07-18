# [easy/codebase_src_gui_windows_debug.zig] - Chunk 0

**Type:** implementation
**Keywords:** FPS, frame time, window size, player position, game world, thread pool, mesh memory, light memory, biome properties, particle count
**Symbols:** graphics, draw, Texture, Vec2f, TaskType, GuiWindow, GuiComponent, onOpen, window, render
**Concepts:** debugging, performance monitoring, world state display, thread pool metrics, mesh memory usage, light memory usage, biome properties, particle count

## Summary
Debug window rendering function

## Explanation
This function renders various debug information on the game window. It includes FPS, frame time, window size, player position and velocity, game world state, thread pool performance metrics, mesh memory usage, light memory usage, biome properties, and particle count.

## Code Example
```zig
pub fn render() void {
	var y: f32 = 0;
	const fpsCapText = if (main.settings.fpsCap) |fpsCap| std.fmt.allocPrint(main.stackAllocator.allocator, " (limit: {d:.0} Hz)", .{fpsCap}) catch unreachable else "";
	defer main.stackAllocator.allocator.free(fpsCapText);
	const fpsLimit = std.fmt.allocPrint(main.stackAllocator.allocator, "{s}{s}", .{
		fpsCapText,
		if (main.settings.vsync) " (vsync)" else "",
	}) catch unreachable;
	defer main.stackAllocator.allocator.free(fpsLimit);
	draw.print("fps: {d:.0} Hz{s}", .{1.0/main.lastDeltaTime.load(.monotonic), fpsLimit}, 0, y, 8);
	y += 8;
	draw.print("frameTime: {d:.1} ms", .{main.lastFrameTime.load(.monotonic)*1000.0}, 0, y, 8);
	y += 8;
	draw.print("window size: {}×{}", .{main.Window.width, main.Window.height}, 0, y, 8);
	y += 8;
	if (main.game.world != null) {
		const player = main.game.Player;
		draw.print("Pos: {d:.1}", .{player.getPosBlocking()}, 0, y, 8);
		y += 8;
		draw.print("Gamemode: {} IsFlying: {} IsGhost: {} HyperSpeed: {}", .{
			player.gamemode.load(.monotonic),
			player.isFlying.load(.monotonic),
			player.isGhost.load(.monotonic),
			player.hyperSpeed.load(.monotonic),
		}, 0, y, 8);
		y += 8;
		draw.print("OnGround: {} JumpCooldown: {d:.3} JumpCoyote: {d:.3}", .{
			player.onGround,
			player.jumpCooldown,
			@max(0, player.getJumpCoyoteBlocking()),
		}, 0, y, 8);
		y += 8;
		draw.print("Velocity: {d:.1}", .{player.getVelBlocking()}, 0, y, 8);
		y += 8;
		draw.print("EyePos: {d:.1} EyeVelocity: {d:.1} EyeCoyote: {d:.3}", .{player.getEyePosBlocking(), player.getEyeVelBlocking(), @max(0, player.getEyeCoyoteBlocking())}, 0, y, 8);
		y += 8;
		draw.print("Game Time: {} Day Time: {}", .{main.game.world.?.gameTime.load(.monotonic), main.game.world.?.dayTime.dayTime}, 0, y, 8);
		y += 8;
		draw.print("Queue size: {}", .{main.threadPool.queueSize()}, 0, y, 8);
		y += 8;
		const perf = main.threadPool.performance.read();
		const values = comptime std.enums.values(TaskType);
		var totalUtime: i64 = 0;
		for (values) |task| {
			totalUtime += perf.utime[@intFromEnum(task)];
		}
		for (values) |t| {
			const name = @tagName(t);
			const i = @intFromEnum(t);
			const taskTime = @divFloor(perf.utime[i], @max(1, perf.tasks[i]));
			const relativeTime = 100.0*@as(f32, @floatFromInt(perf.utime[i]))/@as(f32, @floatFromInt(totalUtime));
			draw.print("    {s}: {} µs/task ({d:.1}%)", .{name, taskTime, relativeTime}, 0, y, 8);
			y += 8;
		}
		draw.print("Mesh Queue size: {}", .{main.renderer.mesh_storage.updatableList.items.len}, 0, y, 8);
		y += 8;
		for (0..main.settings.highestLod + 1) |lod| {
			const faceDataSize: usize = @sizeOf(main.renderer.chunk_meshing.FaceData);
			const size: usize = main.renderer.chunk_meshing.faceBuffers[lod].capacity*faceDataSize;
			const used: usize = main.renderer.chunk_meshing.faceBuffers[lod].used*faceDataSize;
			draw.print("ChunkMesh memory LOD{}: {} MiB / {} MiB", .{lod, used >> 20, size >> 20}, 0, y, 8);
			y += 8;
		}
		for (0..main.settings.highestLod + 1) |lod| {
			const lightDataSize: usize = @sizeOf(u32);
			const size: usize = main.renderer.chunk_meshing.lightBuffers[lod].capacity*lightDataSize;
			const used: usize = main.renderer.chunk_meshing.lightBuffers[lod].used*lightDataSize;
			draw.print("Light memory LOD{}: {} MiB / {} MiB", .{lod, used >> 20, size >> 20}, 0, y, 8);
			y += 8;
		}
		{
			const biome = main.game.world.?.playerBiome.load(.monotonic);
			var tags = main.ListManaged(u8).init(main.stackAllocator);
			defer tags.deinit();
			inline for (comptime std.meta.fieldNames(main.server.terrain.biomes.Biome.GenerationProperties)) |name| {
				if (@field(biome.properties, name)) {
					if (tags.items.len != 0) tags.appendSlice(", ");
					tags.appendSlice(name);
				}
			}
			draw.print("Biome: {s}", .{biome.id}, 0, y, 8);
			y += 8;
			draw.print("Biome Properties: {s}", .{tags.items}, 0, y, 8);
			y += 8;
		}
		draw.print("Opaque faces: {}, Transparent faces: {}", .{main.renderer.chunk_meshing.quadsDrawn, main.renderer.chunk_meshing.transparentQuadsDrawn}, 0, y, 8);
		y += 8;
		draw.print("Particle count: {}/{}", .{main.particles.ParticleSystem.getParticleCount(), main.particles.ParticleSystem.maxCapacity}, 0, y, 8);
		y += 8;
		draw.print("items: {} entities: {}", .{main.game.world.?.itemDrops.super.size, main.client.entity_manager.entities.len}, 0, y, 8);
		y += 8;
	}
}
```

## Related Questions
- What is the purpose of the `onOpen` function?
- How does the `render` function calculate FPS and frame time?
- What information is displayed about the player's position and velocity in the debug window?
- How is the game world state displayed in the debug window?
- What metrics are collected by the thread pool performance monitoring in the debug window?
- How is mesh memory usage displayed in the debug window?
- How is light memory usage displayed in the debug window?
- What information is displayed about the biome properties in the debug window?
- How is particle count displayed in the debug window?
- How many items and entities are displayed in the debug window?
- What is the purpose of the `draw.print` function used in the `render` function?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug.zig_chunk_0*
