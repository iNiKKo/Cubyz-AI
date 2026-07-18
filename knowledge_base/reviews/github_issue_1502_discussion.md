# [issues/issue_1502.md] - Issue #1502 discussion

**Type:** review
**Keywords:** FPS limiting, low-end monitor, sleep, busy waiting, Windows thread scheduling, power consumption, reproduction issue, better waiting methods
**Symbols:** FPS, Cubyz, miniaudio, git bisect, 4b856619b5d093e990a436292e650f033dbc9b56
**Concepts:** thread scheduling, power-saving, busy waiting

## Summary
The issue discusses FPS limiting problems in Cubyz where the game limits itself further than intended on low-end monitors.

## Explanation
The maintainers are unable to reproduce the issue consistently, but suspect it may be related to the use of sleep for power-saving purposes instead of busy waiting. They consider reverting to busy waiting as a potential solution, despite increased power consumption, due to Windows' thread scheduling issues. A user mentions investigating better waiting methods and is considering making a PR if others want to test it.

## Related Questions
- What is the root cause of the FPS limiting issue in Cubyz?
- How does the use of sleep for power-saving purposes affect FPS limiting on Windows?
- Why might the maintainers consider reverting to busy waiting despite increased power consumption?
- What are some better waiting methods mentioned in the discussion?
- Is there a plan to implement any changes based on the investigation into better waiting methods?
- How can the maintainers ensure that any changes do not introduce new issues or regressions?

*Source: unknown | chunk_id: github_issue_1502_discussion*
