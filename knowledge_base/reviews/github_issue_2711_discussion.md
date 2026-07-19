# [issues/issue_2711.md] - Issue #2711 discussion

**Type:** review
**Keywords:** 75 Hz, tabbing out, GUI, uncapping, 38 fps, 75 fps
**Concepts:** performance, frame rate, stuttering

## Summary
The issue describes significant stuttering in the game at 75 Hz, particularly after tabbing out or opening the GUI. The problem persists even when uncapping the frame rate.

## Explanation
The issue describes significant stuttering in the game at 75 Hz, particularly after tabbing out or opening the GUI. The problem persists even when uncapping the frame rate. Users report that the stuttering alternates between 38 and 75 fps. One user noted that after flying up to skyislands and falling down while tabbed out, the game ran consistently at around ~65 fps upon returning to gameplay. This consistent lower frame rate was observed even when changing the frame rate limit multiple times. After a few seconds, the framerate returned to 75 Hz once the limit was set back to 75 Hz.

## Related Questions
- What specific changes were made to address the stuttering issue at 75 Hz?
- Are there any known performance bottlenecks in the game that could cause this behavior?
- How does the game's resource management affect its frame rate when interacting with the GUI?
- Is there a way to optimize the LOD (Level of Detail) loading process to reduce stuttering?
- What impact does tabbing out and back into the game have on its performance?
- Are there any settings or configurations that can help mitigate the stuttering issue?

*Source: unknown | chunk_id: github_issue_2711_discussion*
