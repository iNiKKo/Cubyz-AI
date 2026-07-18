# [issues/issue_7.md] - Issue #7 discussion

**Type:** review
**Keywords:** mouse input, Windows 10, sensitivity issue, fix, commit 4b6f7b2, compatibility, bug resolution
**Concepts:** mouse input, operating system compatibility, bug fixing

## Summary
A user reported that Cubyz's mouse input was overly sensitive on Windows 10, causing the camera to spin violently. The maintainer identified potential issues with unsupported mouse states and implemented a fix in commit 4b6f7b2.

## Explanation
The issue arose due to Cubyz using specific mouse state handling that may not be compatible with standard Windows 10 configurations. The maintainer addressed this by modifying the code to support more generic mouse input handling, which resolved the sensitivity problem and an additional bug. The fix was confirmed by another tester.

## Related Questions
- What specific mouse states were causing the sensitivity issue in Cubyz?
- How did the maintainer modify the code to fix the mouse input sensitivity problem?
- Was there any additional bug fixed alongside the mouse input issue?
- How was the effectiveness of the fix confirmed?
- Are there any known limitations or further improvements for mouse input handling in Cubyz?
- What steps can users take if they still experience issues with mouse input after applying this fix?

*Source: unknown | chunk_id: github_issue_7_discussion*
