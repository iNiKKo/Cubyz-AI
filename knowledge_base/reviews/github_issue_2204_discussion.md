# [issues/issue_2204.md] - Issue #2204 discussion

**Type:** review
**Keywords:** RAM usage, antialiasing, system slowdown, game freeze, Btop, logs
**Concepts:** memory leak, performance degradation

## Summary
The game experiences a significant increase in RAM usage and system slowdown when lowering antialiasing settings.

## Explanation
The user reports that while testing the game on max graphics, RAM usage was initially stable at around 1400 MiB. However, upon reducing antialiasing settings, the game froze immediately, leading to rapid RAM consumption until it severely impacted system performance. The user had to forcefully terminate the process using Btop due to inability to close it through normal means. Logs from the game are provided for further analysis.

## Related Questions
- What is the impact of changing antialiasing settings on RAM usage?
- Are there any known issues with memory management in Cubyz when adjusting graphics settings?
- How does the game's performance behave under different render distances and antialiasing levels?
- Can the rapid increase in RAM usage be attributed to a specific part of the codebase?
- What steps can be taken to prevent system slowdowns due to high RAM consumption in Cubyz?
- Is there any correlation between the reported issue and the game's graphics rendering pipeline?

*Source: unknown | chunk_id: github_issue_2204_discussion*
