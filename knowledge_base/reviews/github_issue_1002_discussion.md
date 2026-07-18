# [issues/issue_1002.md] - Issue #1002 discussion

**Type:** review
**Keywords:** fog-start, fog-end, render distance, heightmap, sphere mapping, skybox issues
**Concepts:** fog rendering, skybox, heightmap terrain

## Summary
Discussion on improving fog rendering to avoid skybox issues and enhance visual experience.

## Explanation
The issue revolves around the current fog rendering technique, which fades out total fog as altitude increases. The maintainer suggests an alternative approach where the fog start is faded out while keeping the fog end constant. This could potentially resolve existing skybox issues. The discussion also explores future enhancements by increasing render distance and mapping heightmaps onto a sphere to improve terrain visibility.

## Related Questions
- How does the current fog rendering technique affect skybox visibility?
- What are the potential benefits of fading out only the fog start?
- How could increasing render distance improve terrain visualization?
- Can mapping heightmaps onto a sphere enhance the visual experience in Cubyz?
- What specific method was mentioned for improving fog rendering in issue #647?
- Are there any known limitations to using sphere mapping for terrain rendering?

*Source: unknown | chunk_id: github_issue_1002_discussion*
