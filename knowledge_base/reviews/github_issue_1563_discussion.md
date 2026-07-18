# [issues/issue_1563.md] - Issue #1563 discussion

**Type:** review
**Keywords:** memory corruption bug, invalid utf8 error, signs, newlines, race condition, #1562
**Concepts:** memory corruption, race condition, thread safety

## Summary
The issue involves a memory corruption bug in Cubyz, likely stemming from a race condition similar to another reported issue (#1562).

## Explanation
The discussion indicates that the problem of adding too many newlines to signs causing them to crash with an invalid UTF-8 error is believed to be a result of memory corruption. The maintainer suggests that this bug shares the same root cause as another issue (#1562), implying a race condition. This points to potential thread safety concerns in how sign data is handled and updated concurrently.

## Related Questions
- What is the race condition identified in issue #1562?
- How does adding newlines to signs trigger memory corruption?
- Are there any existing checks for invalid UTF-8 encoding in sign data handling?
- Can you provide a code snippet showing how sign data is updated concurrently?
- Is there a plan to implement thread safety measures for sign data handling?
- What steps are being taken to prevent similar race conditions in the future?

*Source: unknown | chunk_id: github_issue_1563_discussion*
