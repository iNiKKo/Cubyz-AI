# [issues/issue_1263.md] - Issue #1263 discussion

**Type:** review
**Keywords:** world edit, /blueprint, arbitrary file access, path sanitization, file names, absolute paths, environment variables, control characters
**Concepts:** security, file access, path sanitization

## Summary
The world edit `/blueprint` sub commands allow arbitrary file access due to lack of path sanitization.

## Explanation
The current implementation of the `/blueprint` sub commands in the world edit feature does not sanitize the paths provided by users, allowing them to access arbitrary files using sequences like `..`, `~`, or leading `/`. The maintainer suggests eliminating all characters that aren't allowed in file names to prevent potential security issues. Specifically, the following sequences should be blocked: `..`, `~`, and leading `/`. They also mention concerns about absolute paths and environment variables being resolved, although they believe this is unlikely due to how operating systems handle paths from system calls. Additionally, control characters could be injected via a modified client.

## Related Questions
- What specific sequences should be blocked to prevent arbitrary file access?
- How does Zig's file opening function handle concatenated file names?

*Source: unknown | chunk_id: github_issue_1263_discussion*
