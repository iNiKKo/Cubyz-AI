# [issues/issue_2344.md] - Issue #2344 discussion

**Type:** review
**Keywords:** server, ReleaseFast, leaf decay, block drops, thread safety, optimization
**Concepts:** thread safety, optimization

## Summary
The server is reported to be broken in ReleaseFast mode, specifically with leaf decay and block drops not working.

## Explanation
The issue revolves around the functionality of leaf decay and block drops failing in the server thread when running in ReleaseFast optimization mode. The maintainer clarified that the problem is specific to the server thread rather than the headless server or client-side operations. A user reported testing 'compiler/zig/zig build -Doptimize=ReleaseFast' without encountering any issues with leaf decay, indicating that the issue is isolated to the server thread's operation under ReleaseFast mode. This suggests a potential bug related to thread safety or optimization-specific code paths in the server thread.

## Related Questions
- What changes were made to the server thread code recently?
- How does the server thread handle optimization settings like ReleaseFast?
- Is there a way to isolate the issue to specific parts of the server thread code?
- Could there be a race condition or synchronization issue causing this problem?

*Source: unknown | chunk_id: github_issue_2344_discussion*
