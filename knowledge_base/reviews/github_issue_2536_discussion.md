# [issues/issue_2536.md] - Issue #2536 discussion

**Type:** review
**Keywords:** music player, .ogg, .FLAC, file search, audio formats
**Concepts:** file handling, audio playback

## Summary
The music player is only configured to search for .ogg files and does not attempt to find .FLAC files.

## Explanation
The issue report indicates that the current implementation of the music player in Cubyz is limited to searching for .ogg audio files. This limitation prevents users from playing .FLAC files, which are also a common format for high-quality audio. The maintainer's comment suggests that this behavior needs to be addressed by modifying the file search logic to include .FLAC files.

## Related Questions
- What is the current file extension filter for audio files in the music player?
- How can we modify the code to include .FLAC files in the search criteria?
- Are there any compatibility issues with adding support for .FLAC files?
- Does the music player need to be updated to handle additional audio formats?
- What is the expected behavior of the music player when encountering unsupported file types?
- How can we ensure that the addition of .FLAC support does not break existing functionality?

*Source: unknown | chunk_id: github_issue_2536_discussion*
