# [issues/issue_1485.md] - Issue #1485 discussion

**Type:** review
**Keywords:** popup, game update, GitHub API, rate limiting, direct links, version checking, pre-releases, latest releases page
**Symbols:** Cubyz, github.com/PixelGuys/Cubyz/releases/latest, settings.version.version
**Concepts:** Rate Limiting, Version Checking, User Notifications

## Summary
Discussion on implementing a game update popup for Cubyz. The team decides to use direct download links instead of the GitHub API due to rate limiting concerns.

## Explanation
Discussion on implementing a game update popup for Cubyz. The team decides to use direct download links instead of the GitHub API due to stricter rate limiting concerns with the API. Initially, there was a suggestion to use the GitHub API for fetching release information, but this was rejected because it has stricter rate limits compared to direct links. The team considers checking if a newer version tag exists by incrementing each part of the current version number, but finds this approach insufficient as it may not correctly identify the latest release in all scenarios (e.g., from 0.0.0 to 2.4.1). Instead, they opt to link directly to the latest releases page on GitHub at https://github.com/PixelGuys/Cubyz/releases/latest, accepting that pre-releases might be included but considering that most pre-releases occur before the final release and thus are less likely to cause issues.

## Related Questions
- What is the main reason for avoiding the GitHub API?
- How does the team plan to check for newer versions without using the API?
- Why is linking directly to the latest releases page acceptable?
- What are the potential issues with checking version numbers incrementally?
- How does the team handle pre-releases in this update notification system?

*Source: unknown | chunk_id: github_issue_1485_discussion*
