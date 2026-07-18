# [issues/issue_2287.md] - Issue #2287 discussion

**Type:** review
**Keywords:** timed game exit, launchConfig, CI, stdin command, automatic termination
**Concepts:** Continuous Integration, game exit, runtime loop

## Summary
The issue proposes adding a timed game exit feature specified by the user, initially intended for CI but with potential other uses. The maintainer suggests implementing this via a command to stdin instead.

## Explanation
The issue proposes adding a timed game exit feature to the launchConfig, which will be specified by the user in some time unit (microseconds or milliseconds, undecided). Once this duration elapses after opening the game (primarily in headless mode but not limited to it), the game will gracefully exit its runtime loop. The primary motivation for this is to facilitate Continuous Integration (CI) processes, although QD mentioned other potential uses in comment #2227. The maintainer suggests implementing this feature via a command sent to stdin instead of through configuration options.

## Related Questions
- What specific time unit will be used to specify the duration for timed game exit?
- How does the game gracefully exit its runtime loop after the specified duration?
- Is there any flexibility in specifying the mode (headless or not) when using this feature?

*Source: unknown | chunk_id: github_issue_2287_discussion*
