# [issues/issue_2711.md] - Issue #2711 discussion

**Type:** review
**Keywords:** 75 Hz, tabbing out, GUI, uncapping, 38 fps, 75 fps
**Concepts:** performance, frame rate, stuttering

## Summary
The issue describes significant stuttering in the game at 75 Hz, particularly after tabbing out or opening the GUI. The problem persists even when uncapping the frame rate.

## Explanation
The issue describes significant stuttering in the game at 75 Hz, particularly after tabbing out or opening the GUI. The problem persists even when uncapping the frame rate. A user reported experiencing significant stuttering in the game at 75 Hz, especially after tabbing out or interacting with the GUI. The issue was observed to get worse after LODs (Level of Detail) have finished loading. The game runs fine at 60 Hz but exhibits consistent lower frame rates around ~65 fps when tabbed back in after flying up to skyislands and falling down. This behavior persists even when changing the frame rate limit multiple times, including uncapping it. After a few seconds, the framerate returns to 75 Hz once the limit is set back to 75 Hz. Another user noted that the stuttering alternates between 38 and 75 fps every frame. The issue seems to be related to how the game handles resource management when interacting with the GUI and the LOD loading process.

## Related Questions
- What specific changes were made to address the stuttering issue at 75 Hz?
- Are there any known performance bottlenecks in the game that could cause this behavior?
- How does the game's resource management affect its frame rate when interacting with the GUI?
- Is there a way to optimize the LOD (Level of Detail) loading process to reduce stuttering?
- What impact does tabbing out and back into the game have on its performance?
- Are there any settings or configurations that can help mitigate the stuttering issue?

*Source: unknown | chunk_id: github_issue_2711_discussion*
