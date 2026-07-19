# [issues/issue_1502.md] - Issue #1502 discussion

**Type:** review
**Keywords:** FPS limiting, low-end monitor, sleep, busy waiting, Windows thread scheduling, power consumption, reproduction issue, better waiting methods
**Symbols:** FPS, Cubyz, miniaudio, git bisect, 4b856619b5d093e990a436292e650f033dbc9b56
**Concepts:** thread scheduling, power-saving, busy waiting

## Summary
The issue discusses FPS limiting problems in Cubyz where the game limits itself further than intended on low-end monitors.

## Explanation
The issue discusses FPS limiting problems in Cubyz where the game limits itself further than intended on low-end monitors. Under certain circumstances, the FPS limit decided to set a specific limit of 144 FPS, which was deemed too high for the user's low-end monitor, leading to further limiting of the FPS. The maintainers were unable to consistently reproduce the issue but suspected it might be related to using sleep for power-saving purposes instead of busy waiting. They considered reverting to busy waiting as a potential solution, despite increased power consumption, due to Windows' thread scheduling issues. A user mentioned investigating better waiting methods and was considering making a PR if others wanted to test it. The specific commit hash `4b856619b5d093e990a436292e650f033dbc9b56` is associated with the issue, and there is a video link to better waiting methods: [this video](https://youtu.be/3dkN-6TJNHs?si=UIiuMVkCEx9ISU5q).

## Related Questions
- What is the specific FPS limit that Cubyz sets under certain circumstances?
- How does the use of sleep for power-saving purposes affect FPS limiting on Windows?
- Why might the maintainers consider reverting to busy waiting despite increased power consumption?
- What are some better waiting methods mentioned in the discussion?
- Is there a plan to implement any changes based on the investigation into better waiting methods?
- How can the maintainers ensure that any changes do not introduce new issues or regressions?

*Source: unknown | chunk_id: github_issue_1502_discussion*
