# [issues/issue_1015.md] - Issue #1015 discussion

**Type:** review
**Keywords:** Expand-Archive, tar, Windows 10, build 17063, compilation errors, file extraction
**Concepts:** build process, reliability, compatibility

## Summary
The Windows `Expand-Archive` command is unreliable for compiling the game, causing random errors. A discussion suggests using `tar` as an alternative starting from Windows 10 build 17063.

## Explanation
The issue highlights a recurring problem with the `Expand-Archive` command on certain Windows instances, leading to compilation failures due to errors about deleting files that haven't been extracted yet. The maintainer proposes using the `tar` command as a more reliable alternative, leveraging its support in newer Windows builds (17063 and later). This change aims to improve the build process's robustness and reliability across different Windows environments.

## Related Questions
- What are the specific error messages encountered with `Expand-Archive`?
- How does the use of `tar` improve the build process reliability?
- Are there any known issues with using `tar` on Windows builds older than 17063?
- Can you provide a comparison of the performance between `Expand-Archive` and `tar`?
- What steps are being taken to ensure backwards compatibility for users still on older Windows builds?
- How will this change be tested across different Windows environments?

*Source: unknown | chunk_id: github_issue_1015_discussion*
