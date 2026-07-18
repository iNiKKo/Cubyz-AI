# [issues/issue_3375.md] - Issue #3375 discussion

**Type:** review
**Keywords:** Windows winsock error, WSAECONNRESET, Cubyz development history, issue_3375.md, cf7917787a9888c32bca90ad1d67ce9d188b1bd6
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue involves a missing Windows winsock error (WSAECONNRESET) that appeared for @Crepestrom on #3370.

## Explanation
This error, which was previously fixed in commit cf7917787a9888c32bca90ad1d67ce9d188b1bd6, reappeared due to oversight when transitioning away from Zig's posix layer. The maintainer notes that this case was forgotten during the switch, leading to the current issue.

## Related Questions
- What was the previous commit that fixed WSAECONNRESET?
- Why was this case forgotten during the switch to Zig's posix layer?
- How can we prevent similar oversights in future transitions?
- Are there any other winsock errors that might have been overlooked?
- What is the impact of this error on Cubyz users?
- How can we ensure backwards compatibility while making changes like this?

*Source: unknown | chunk_id: github_issue_3375_discussion*
