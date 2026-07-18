# [medium/codebase_src_audio.zig] - Chunk 2

**Type:** implementation
**Keywords:** mutex locking, buffer management, callback function, audio mixing, music fading
**Symbols:** addMusic, miniaudioCallback
**Concepts:** audio playback, music transitions, thread safety

## Summary
Handles audio playback and music transitions.

## Explanation
The chunk contains two functions: `addMusic` and `miniaudioCallback`. The `addMusic` function manages the loading and playing of music, including transitioning between different music tracks based on a preferred music ID. It uses a mutex for thread safety and checks if the current music needs to be changed or faded out. The `miniaudioCallback` is a callback function used by the miniaudio library to fill audio buffers with sound data. It initializes the buffer, clears it, and calls `addMusic` to add the appropriate music.

## Code Example
```zig
fn addMusic(buffer: []f32) void {
	mutex.lock();
	defer mutex.unlock();
	if (!std.mem.eql(u8, preferredMusic, activeMusicId)) {
		if (activeMusicId.len == 0) {
			if (findMusic(preferredMusic)) |musicBuffer| {
				currentMusic.init(musicBuffer);
				main.globalAllocator.free(activeMusicId);
				activeMusicId = main.globalAllocator.dupe(u8, preferredMusic);
			}
		} else if (!currentMusic.animationDecaying) {
			_ = findMusic(preferredMusic); // Start loading the next music into the cache ahead of time.
			currentMusic.animationDecaying = true;
			currentMusic.animationProgress = 0;
			currentMusic.interpolationPolynomial = utils.unitIntervalSpline(f32, currentMusic.animationAmplitude, currentMusic.animationVelocity, 0, 0);
		}
	} else if (currentMusic.animationDecaying) { // We returned to the biome before the music faded away.
		currentMusic.animationDecaying = false;
		currentMusic.animationProgress = 0;
		currentMusic.interpolationPolynomial = utils.unitIntervalSpline(f32, currentMusic.animationAmplitude, currentMusic.animationVelocity, 1, 0);
	}
	if (activeMusicId.len == 0) return;

	// Copy the music to the buffer.
	var i: usize = 0;
	while (i < buffer.len) : (i += 2) {
		currentMusic.animationProgress += 1.0/(animationLengthInSeconds*sampleRate);
		var amplitude: f32 = main.settings.musicVolume;
		if (currentMusic.animationProgress > 1) {
			if (currentMusic.animationDecaying) {
				main.globalAllocator.free(activeMusicId);
				activeMusicId = &.{};
				amplitude = 0;
			}
		} else {
			currentMusic.evaluatePolynomial();
			amplitude *= currentMusic.animationAmplitude;
		}
		buffer[i] += amplitude*currentMusic.buffer[currentMusic.pos];
		buffer[i + 1] += amplitude*currentMusic.buffer[currentMusic.pos + 1];
		currentMusic.pos += 2;
		if (currentMusic.pos >= currentMusic.buffer.len) {
			currentMusic.pos = 0;
		}
	}
}
```

## Related Questions
- What is the purpose of the `addMusic` function?
- How does the chunk handle music transitions between different tracks?
- What role does the mutex play in this code?
- Describe the process of loading and playing music in this chunk.
- How is the audio buffer managed in the `miniaudioCallback` function?
- Explain the mechanism for fading out music in this implementation.

*Source: unknown | chunk_id: codebase_src_audio.zig_chunk_2*
