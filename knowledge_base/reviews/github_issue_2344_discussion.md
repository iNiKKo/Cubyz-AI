# [issues/issue_2344.md] - Issue #2344 discussion

**Type:** review
**Keywords:** server, ReleaseFast, leaf decay, block drops, thread safety, optimization
**Concepts:** thread safety, optimization

## Summary
The server is reported to be broken in ReleaseFast mode, specifically with leaf decay and block drops not working.

## Explanation
The issue revolves around the functionality of leaf decay and block drops in the server thread when running in ReleaseFast optimization mode. The user initially tested the build without issues but later clarified that the problem is specific to the server thread. This suggests a potential bug related to thread safety or optimization-specific code paths.

## Related Questions
- What changes were made to the server thread code recently?
- Are there any known issues with leaf decay and block drops in ReleaseFast mode?
- How does the server thread handle optimization settings like ReleaseFast?
- Is there a way to isolate the issue to specific parts of the server thread code?
- Could there be a race condition or synchronization issue causing this problem?
- Are there any logs or error messages that could provide more context about the failure?

*Source: unknown | chunk_id: github_issue_2344_discussion*
