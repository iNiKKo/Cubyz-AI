# [issues/issue_1485.md] - Issue #1485 discussion

**Type:** review
**Keywords:** popup, game update, GitHub API, rate limiting, direct links, version checking, pre-releases, latest releases page
**Symbols:** Cubyz, github.com/PixelGuys/Cubyz/releases/latest, settings.version.version
**Concepts:** Rate Limiting, Version Checking, User Notifications

## Summary
Discussion on implementing a game update popup for Cubyz. The team decides to use direct download links instead of the GitHub API due to rate limiting concerns.

## Explanation
The discussion revolves around adding a feature to notify users when a new game update is available. Initially, there was a suggestion to use the GitHub API for fetching release information, but this was rejected due to stricter rate limits compared to direct links. The team decides to check if a newer version tag exists by incrementing each part of the current version number. However, this approach is deemed insufficient as it may not correctly identify the latest release in all scenarios. Instead, they opt to link directly to the latest releases page on GitHub, accepting that pre-releases might be included but considering that most pre-releases occur before the final release.

## Related Questions
- What is the main reason for avoiding the GitHub API?
- How does the team plan to check for newer versions without using the API?
- Why is linking directly to the latest releases page acceptable?
- What are the potential issues with checking version numbers incrementally?
- How does the team handle pre-releases in this update notification system?
- Can you explain the rate limiting concerns mentioned in the discussion?

*Source: unknown | chunk_id: github_issue_1485_discussion*
