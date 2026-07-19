# [issues/issue_59.md] - Issue #59 discussion

**Type:** review
**Keywords:** sound system, stereo, doppler, channels, miniaudio, high-level API, resource management, streaming, music tracks, caching
**Symbols:** Sound System, stereo sound, doppler effect, sound channels, miniaudio, resource management, streaming
**Concepts:** audio processing, memory management, design patterns

## Summary
The discussion revolves around implementing a proper sound system in Cubyz with stereo sound, doppler effect, and multiple track support. The maintainer suggests using sound channels for different types of sounds and mentions the use of `miniaudio`. There's also a mention of potential improvements to resource management and streaming music tracks.

## Explanation
The discussion revolves around implementing a proper sound system in Cubyz with stereo sound, doppler effect, and multiple track support. The maintainer suggests using sound channels for different types of sounds and mentions the use of `miniaudio`. There's also a mention of potential improvements to resource management and streaming music tracks.

The issue highlights the need for a comprehensive sound system in Cubyz with features like stereo sound for spatial audio and the doppler effect for velocity determination. The maintainer proposes organizing sounds into specific channels: Sound channel 1 for Music, Sound channels 2-10 for Ambience, and Sound channels 11-99 for SFX. The current implementation uses `miniaudio`'s low-level API, but there is a discussion about potentially using its high-level API for mixing and applying effects. The maintainer mentions that the game currently stores up to 16 uncompressed music tracks in cache, which can consume around 250MB of memory. In testing, this has been observed to reach up to 600MB. There is a suggestion to implement a streaming approach to reduce memory usage.

The issue also mentions that the current code only uses `miniaudio`'s low-level API and there is no plan yet to make use of its higher-level API. The maintainer suggests evaluating how good the high-level API is and whether it is suitable for Cubyz's purposes. Additionally, there is a suggestion to implement a streaming approach to reduce memory usage by caching fewer music tracks.

## Related Questions
- What is the current implementation of sound channels in Cubyz?
- How does `miniaudio` fit into the proposed sound system architecture?
- Are there any plans to evaluate the high-level API of `miniaudio` for use in Cubyz?
- What are the potential benefits and drawbacks of using a streaming approach for music tracks?
- How can resource management be improved to reduce memory usage in Cubyz?
- Is there a timeline or roadmap for implementing the sound system features discussed?

*Source: unknown | chunk_id: github_issue_59_discussion*
