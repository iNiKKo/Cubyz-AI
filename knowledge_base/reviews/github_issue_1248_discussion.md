# [issues/issue_1248.md] - Issue #1248 discussion

**Type:** review
**Keywords:** same world, uninitialized seed, threadlocal, world generation, random seed
**Concepts:** thread safety, random number generation

## Summary
The issue involves multiple world generations resulting in identical worlds due to an uninitialized thread-local seed.

## Explanation
The problem stems from the use of a thread-local variable for storing the random seed, which was not properly initialized. This led to all threads using the same default seed value, causing the generation of identical worlds. The maintainer recognized this as a potential issue with uninitialized thread-local variables and acknowledged that it could lead to such problems.

## Related Questions
- What is the current implementation of random seed initialization in Cubyz?
- How does Cubyz handle thread-local variables for random number generation?
- Are there any other instances where uninitialized thread-local variables could cause similar issues in Cubyz?
- How can we ensure that each world generation uses a unique seed?
- What are the implications of using uninitialized seeds on performance and correctness?
- Is there a plan to refactor the random seed initialization process to prevent such issues?

*Source: unknown | chunk_id: github_issue_1248_discussion*
