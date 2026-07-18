# [issues/issue_109.md] - Issue #109 discussion

**Type:** review
**Keywords:** data race, transparency sorting, index out of bounds, thread sanitizer, panic
**Symbols:** renderTransparent, renderWorld, render, main
**Concepts:** thread safety, data race, index out of bounds

## Summary
The issue reports an index out of bounds error during transparency sorting, potentially caused by a data race.

## Explanation
The report indicates a panic due to an index out of bounds error at line 1095 in chunk.zig. The thread sanitizer is mentioned as being broken, making it difficult to pinpoint the exact location of the data race. The maintainer has not observed these issues and found no data races in that code using the thread sanitizer.

## Related Questions
- What is the current status of the thread sanitizer in Zig?
- Are there any known issues with index out of bounds errors in Cubyz's transparency sorting?
- How can we verify if the data race is indeed occurring in the reported code?
- What steps should be taken to prevent similar index out of bounds errors in the future?
- Is there a way to improve thread safety in the rendering pipeline?
- Can you provide more details on how the thread sanitizer failed to detect the data race?

*Source: unknown | chunk_id: github_issue_109_discussion*
