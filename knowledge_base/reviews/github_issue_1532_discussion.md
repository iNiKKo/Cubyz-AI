# [issues/issue_1532.md] - Issue #1532 discussion

**Type:** review
**Keywords:** OpenGL, warnings, release safe, log clutter, other messages
**Concepts:** OpenGL, logging, release builds

## Summary
The issue discusses silencing OpenGL 'other' messages in release builds to reduce log clutter.

## Explanation
The discussion revolves around addressing the verbosity of OpenGL driver logs, particularly focusing on 'other' messages that are not considered warnings. The maintainer suggests removing these messages entirely, as they have not observed any useful information from them. This change aims to clean up the release build logs and reduce unnecessary log file sizes.

## Related Questions
- What is the impact of removing OpenGL 'other' messages on log file sizes?
- Are there any potential side effects from filtering out non-warning OpenGL messages?
- How can we ensure that useful information is not inadvertently removed by silencing these messages?
- What are the implications of this change for debugging in release builds?
- Can you provide a list of other types of OpenGL messages that might be considered for similar treatment?
- How does this change affect the performance of the application in release mode?

*Source: unknown | chunk_id: github_issue_1532_discussion*
