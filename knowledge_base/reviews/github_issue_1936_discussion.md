# [issues/issue_1936.md] - Issue #1936 discussion

**Type:** review
**Keywords:** Windows, down scroll, hot-bar, aggressive scroll, input sensitivity, user report
**Concepts:** scroll input handling, UI interaction

## Summary
A user reports that down scroll input does not scroll the hot-bar unless the scroll input is aggressive on Windows.

## Explanation
**Explanation**

The issue is related to the handling of scroll input in the game's UI, specifically for scrolling the hot-bar. The user reported that down scroll input does not scroll the hot-bar unless the scroll input is aggressive on Windows. The user provided a video demonstrating the problem and their system specifications, which include a PC with a 12th Gen Intel Core i5-12600KF CPU, NVIDIA GeForce RTX 4060 Ti GPU, and 28.68 GiB of RAM. There is currently no known issue with scroll input handling on Windows systems, but there might be an issue with the sensitivity or threshold of the scroll input detection. The game's UI handles scroll events for different elements like the hot-bar, but the current threshold for detecting aggressive scroll input in the game is not explicitly stated. There are no plans to adjust the scroll input sensitivity for better user experience at this time.

## Related Questions
- What is the current threshold for detecting aggressive scroll input in the game?
- Is there a known issue with scroll input handling on Windows systems?
- How does the game's UI handle scroll events for different elements like the hot-bar?
- Are there any plans to adjust the scroll input sensitivity for better user experience?
- What system specifications are recommended for optimal performance in the game?
- Is there a way to configure the scroll input sensitivity in the game settings?

*Source: unknown | chunk_id: github_issue_1936_discussion*
