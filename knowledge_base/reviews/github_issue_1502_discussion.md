# [issues/issue_1502.md] - Issue #1502 discussion

**Type:** review
**Keywords:** FPS limiting, low-end monitor, sleep, busy waiting, Windows thread scheduling, power consumption, reproduction issue, better waiting methods
**Symbols:** FPS, Cubyz, miniaudio, git bisect, 4b856619b5d093e990a436292e650f033dbc9b56
**Concepts:** thread scheduling, power-saving, busy waiting

## Summary
The issue discusses FPS limiting problems in Cubyz where the game limits itself further than intended on low-end monitors.

## Explanation
In Cubyz, under certain circumstances, the FPS limit decided to set a limit of 144 FPS, which was deemed too high for the user's low-end monitor. This led to further limiting of the FPS. The maintainers were unable to consistently reproduce the issue but suspected it might be related to using sleep for power-saving purposes instead of busy waiting. They considered reverting to busy waiting as a potential solution, despite increased power consumption, due to Windows' thread scheduling issues. A user mentioned investigating better waiting methods and was considering making a PR if others wanted to test it.

## Related Questions
- What is the root cause of the FPS limiting issue in Cubyz?
- How does the use of sleep for power-saving purposes affect FPS limiting on Windows?
- Why might the maintainers consider reverting to busy waiting despite increased power consumption?
- What are some better waiting methods mentioned in the discussion?
- Is there a plan to implement any changes based on the investigation into better waiting methods?
- How can the maintainers ensure that any changes do not introduce new issues or regressions?

*Source: unknown | chunk_id: github_issue_1502_discussion*
