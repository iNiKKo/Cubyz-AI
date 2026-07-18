# [medium/codebase_src_audio.zig] - Chunk 2

**Type:** implementation
**Keywords:** mutex locking, buffer management, callback function, audio mixing, music fading
**Symbols:** addMusic, miniaudioCallback
**Concepts:** audio playback, music transitions, thread safety

## Summary
Handles audio playback and music transitions.

## Explanation
The chunk contains two functions: `addMusic` and `miniaudioCallback`. The `addMusic` function manages the loading and playing of music, including transitioning between different music tracks based on a preferred music ID. It uses a mutex for thread safety and checks if the current music needs to be changed or faded out. Specifically, it performs the following actions:

1. **Mutex Locking:** The `addMusic` function locks the mutex at the beginning of its execution and unlocks it upon completion.
2. **Transition Conditions:** If the preferred music ID (`preferredMusic`) does not match the active music ID (`activeMusicId`), the function checks if there is no currently loaded music (`activeMusicId.len == 0`). If so, it loads the new music using `findMusic(preferredMusic)` and initializes the current music with the buffer obtained from this call. It also updates the active music ID.
3. **Fading Mechanism:** If there is already a loaded music track but fading has not started (`!currentMusic.animationDecaying`), it initiates the fade-in process by setting `animationDecaying = true`, initializing `animationProgress` to 0, and calculating an interpolation polynomial for smooth transition.
4. **Return to Previous Track:** If the current music is decaying and the player returns to a biome before the music fades out completely (`currentMusic.animationDecaying`), it resets the fading process by setting `animationDecaying = false`, resetting `animationProgress` to 0, and recalculating the interpolation polynomial.
5. **Buffer Management:** If there is no active music ID (`activeMusicId.len == 0`), the function returns immediately without further processing.
6. **Copying Music to Buffer:** The function iterates through the buffer, updating `animationProgress`, calculating amplitude based on the current volume and fading state, and copying the appropriate music data into the buffer. It also handles the case where the position in the music buffer exceeds its length by resetting it to 0.

The `miniaudioCallback` is a callback function used by the miniaudio library to fill audio buffers with sound data. It initializes the buffer, clears it, and calls `addMusic` to add the appropriate music.

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
- What are the specific conditions for transitioning between different music tracks in the `addMusic` function?
- How does the fading mechanism work when switching from one track to another?
- Describe the exact process of loading and playing a new music track if there is no currently loaded music.
- Explain how the buffer management works within the `miniaudioCallback` function.

*Source: unknown | chunk_id: codebase_src_audio.zig_chunk_2*
