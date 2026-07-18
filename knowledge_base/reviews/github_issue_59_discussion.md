# [issues/issue_59.md] - Issue #59 discussion

**Type:** review
**Keywords:** sound system, stereo, doppler, channels, miniaudio, high-level API, resource management, streaming, music tracks, caching
**Symbols:** Sound System, stereo sound, doppler effect, sound channels, miniaudio, resource management, streaming
**Concepts:** audio processing, memory management, design patterns

## Summary
The discussion revolves around implementing a proper sound system in Cubyz with stereo sound, doppler effect, and multiple track support. The maintainer suggests using sound channels for different types of sounds and mentions the use of `miniaudio`. There's also a mention of potential improvements to resource management and streaming music tracks.

## Explanation
The issue highlights the need for a comprehensive sound system in Cubyz, emphasizing features like stereo sound for spatial audio and the doppler effect for velocity determination. The maintainer proposes organizing sounds into channels (music, ambience, SFX) and using `miniaudio` for implementation. There's a discussion about whether to use the high-level API of `miniaudio`, with considerations for mixing, effects, and resource management. Additionally, there's a concern about excessive memory usage due to caching uncompressed music tracks, suggesting a streaming approach as an alternative.

## Related Questions
- What is the current implementation of sound channels in Cubyz?
- How does `miniaudio` fit into the proposed sound system architecture?
- Are there any plans to evaluate the high-level API of `miniaudio` for use in Cubyz?
- What are the potential benefits and drawbacks of using a streaming approach for music tracks?
- How can resource management be improved to reduce memory usage in Cubyz?
- Is there a timeline or roadmap for implementing the sound system features discussed?

*Source: unknown | chunk_id: github_issue_59_discussion*
