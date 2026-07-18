# [issues/issue_1202.md] - Issue #1202 discussion

**Type:** review
**Keywords:** buffer size, OpenGL limit, memory leak, render distance, LOD, SSBO, draw call, freeing code, crashes, glitches
**Symbols:** SSBO, draw call, LOD0, LOD1, LOD0.5
**Concepts:** memory leak, OpenGL buffer limit, thread safety, performance

## Summary
The buffers are growing too large, reaching the OpenGL 2 GB limit. A memory leak was identified and needs fixing.

## Explanation
The issue arises because the buffers used in rendering are accumulating data beyond the 2 GB limit of OpenGL, particularly at maximum render distances. The maintainer suspects a memory leak, which has been confirmed by the accidental removal of buffer-freeing code in commit e7ecd161ce00851240ad5bb9bcb1aa0bd69dc1d5. This leak causes memory usage to increase over time, leading to crashes and glitches for users who set their render distance to maximum.

## Related Questions
- What is the current status of the memory leak issue in Cubyz?
- Which commit introduced the memory leak, and what was the impact?
- How can we prevent similar memory leaks from occurring in the future?
- What are the potential performance implications of splitting buffers by LOD?
- Is there a plan to implement the alternative solution allowing for 4 GiB buffers?
- How does the removal of buffer-freeing code affect memory usage over time?

*Source: unknown | chunk_id: github_issue_1202_discussion*
