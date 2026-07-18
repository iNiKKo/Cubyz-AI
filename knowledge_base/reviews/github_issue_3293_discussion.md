# [issues/issue_3293.md] - Issue #3293 discussion

**Type:** review
**Keywords:** flicker, chunks, mouse movement, x:0 y:0, version
**Concepts:** visual glitch, chunk rendering, player position

## Summary
A visual glitch causes chunks to flicker when the player is at coordinates x:0 y:0.

## Explanation
The issue report describes a visual glitch where chunks flicker in and out when the player moves the mouse while standing at coordinates (0, 0). The maintainer asks for clarification on which version of the software was used to reproduce this issue. This information is crucial for diagnosing whether the bug is due to a specific code change or if it has been present since an earlier release.

## Related Questions
- What version of the software was used to reproduce this issue?
- Is there a known bug related to chunk rendering at specific coordinates?
- Are there any recent changes in the codebase that could affect chunk visibility?
- How does the chunk rendering system handle edge cases like player position (0, 0)?
- Could this be related to a threading or synchronization issue in the rendering engine?
- Is there any existing test case for this specific scenario?
- What are the expected behavior and performance implications of fixing this glitch?
- Are there any similar issues reported in previous versions?
- How does the flickering affect adjacent chunks, and is this intentional?
- Could optimizing the chunk rendering logic resolve this issue?

*Source: unknown | chunk_id: github_issue_3293_discussion*
