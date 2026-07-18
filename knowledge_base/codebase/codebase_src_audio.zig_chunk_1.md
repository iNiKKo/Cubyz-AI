# [medium/codebase_src_audio.zig] - Chunk 1

**Type:** implementation
**Keywords:** audio device, task scheduling, miniaudio library, music cache, animation parameters
**Symbols:** MusicLoadTask, MusicLoadTask.musicId, MusicLoadTask.vtable, MusicLoadTask.schedule, MusicLoadTask.getPriority, MusicLoadTask.isStillNeeded, MusicLoadTask.run, MusicLoadTask.clean, device, sampleRate, init, deinit, currentMusic, currentMusic.buffer, currentMusic.animationAmplitude, currentMusic.animationVelocity, currentMusic.animationDecaying, currentMusic.animationProgress, currentMusic.interpolationPolynomial, currentMusic.pos, currentMusic.init, currentMusic.evaluatePolynomial, activeMusicId, partialFrame, animationLengthInSeconds, curIndex, curEndIndex, mutex, preferredMusic, setMusic
**Concepts:** audio initialization, music loading, asynchronous task management, Miniaudio integration

## Summary
Handles audio initialization, deinitialization, and music loading tasks.

## Explanation
This chunk defines the `MusicLoadTask` struct for managing asynchronous music loading tasks. It includes methods for scheduling tasks (`schedule`), determining task priority (`getPriority`), checking if a task is still needed (`isStillNeeded`), running the task to load music data into a cache (`run`), and cleaning up after the task (`clean`). The `init` function initializes the audio device using Miniaudio, setting up playback configuration with format as `ma_format_f32`, channels set to 2, and starting the device. The sample rate is explicitly set to 44100 Hz in the `config.sampleRate = 44100;` line. The `deinit` function stops and uninitializes the audio device, closes all pending music loading tasks, clears the music cache, deallocates resources, and frees memory for `activeMusicId` and `preferredMusic`. The `currentMusic` struct manages current music state, including buffer data (`buffer`), animation parameters (`animationAmplitude`, `animationVelocity`, `animationDecaying`, `animationProgress`, `interpolationPolynomial`, `pos`), and provides functions like `init` for initializing the music state and `evaluatePolynomial` for evaluating polynomial values. The `setMusic` function allows setting the preferred music to play, ensuring it does not duplicate if already set.

## Code Example
```zig
pub fn schedule(musicId: []const u8) void {
	const task = main.globalAllocator.create(MusicLoadTask);
	task.* = MusicLoadTask{
		.musicId = main.globalAllocator.dupe(u8, musicId),
	};
	main.threadPool.addTask(task, &vtable);
	taskMutex.lock();
	defer taskMutex.unlock();
	activeTasks.append(main.globalAllocator, task.musicId);
}
```

## Related Questions
- How does the `MusicLoadTask` struct manage music loading tasks?
- What is the purpose of the `init` function in this chunk?
- How does the `deinit` function handle cleanup for audio resources?
- What role does the `currentMusic` struct play in managing music state?
- How are music tasks scheduled and managed by the thread pool?
- What is the significance of the `animationLengthInSeconds` constant?

*Source: unknown | chunk_id: codebase_src_audio.zig_chunk_1*
