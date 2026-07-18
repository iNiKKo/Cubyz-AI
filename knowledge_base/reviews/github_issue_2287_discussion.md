# [issues/issue_2287.md] - Issue #2287 discussion

**Type:** review
**Keywords:** timed game exit, launchConfig, CI, stdin command, automatic termination
**Concepts:** Continuous Integration, game exit, runtime loop

## Summary
The issue proposes adding a timed game exit feature specified by the user, initially intended for CI but with potential other uses. The maintainer suggests implementing this via a command to stdin instead.

## Explanation
The discussion revolves around adding a new configuration option in the launchConfig that allows the game to automatically exit after a specified duration. This feature is primarily aimed at facilitating Continuous Integration (CI) processes, but it may also be useful for other scenarios where automatic termination of the game runtime loop is beneficial. The maintainer's comment suggests an alternative approach using stdin commands, which could offer more flexibility and control over when and how the game exits.

## Related Questions
- What is the primary motivation for adding a timed game exit feature?
- How does the maintainer suggest implementing the timed game exit feature?
- Are there any potential use cases for this feature beyond CI?
- What are the benefits of using stdin commands for controlling game termination?
- How might this feature impact the game's runtime loop behavior?
- Is there a specific time unit proposed for specifying the duration in the launchConfig?

*Source: unknown | chunk_id: github_issue_2287_discussion*
