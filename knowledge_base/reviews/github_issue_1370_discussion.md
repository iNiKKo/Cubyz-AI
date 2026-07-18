# [issues/issue_1370.md] - Issue #1370 discussion

**Type:** review
**Keywords:** Durability bar, iron pick, wooden handle, diamond tip, floating point issue, fragile modifier
**Concepts:** floating point, bug, durability bar

## Summary
Discussion about an issue where the durability bar on undamaged tools appears incorrectly.

## Explanation
The discussion revolves around an issue where the durability bar for an iron pick with a wooden/branch handle and diamond tip is displayed incorrectly. The maintainer suggests that it might be due to a floating-point precision issue or the presence of a fragile modifier. The goal is to identify the root cause and determine if there are any specific conditions under which this bug occurs.

## Related Questions
- What is the current implementation of the durability bar calculation?
- Are there any known issues with floating-point precision in this part of the code?
- How does the fragile modifier interact with the durability bar display?
- Can you provide a test case to reproduce the issue consistently?
- Is there any logging or debugging information available for this specific tool and its durability bar?
- Have there been any recent changes to the tool or durability system that might have introduced this bug?

*Source: unknown | chunk_id: github_issue_1370_discussion*
