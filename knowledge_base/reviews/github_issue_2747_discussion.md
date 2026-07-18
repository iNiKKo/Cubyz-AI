# [issues/issue_2747.md] - Issue #2747 discussion

**Type:** review
**Keywords:** z-fighting, pixel errors, #92, reverse-z-buffer, performance issue, Vulkan
**Concepts:** z-fighting, reverse-z-buffer, performance

## Summary
The maintainer revisits the reverse-z-buffer approach to address z-fighting issues but notes ongoing performance concerns.

## Explanation
The issue report indicates that z-fighting is causing significant pixel errors, similar to a previously reported issue (#92). The maintainer attempts to resolve this by re-evaluating the reverse-z-buffer technique. However, they encounter persistent performance issues with this approach. The maintainer suggests revisiting the reverse-z-buffer after Vulkan integration but does not see any immediate alternative solutions.

## Related Questions
- What are the specific performance issues encountered with the reverse-z-buffer?
- How does z-fighting affect pixel errors in rendering?
- Why was the reverse-z-buffer revisited as a solution to z-fighting?
- Are there any alternative solutions proposed for addressing z-fighting besides the reverse-z-buffer?
- What is the expected improvement from integrating Vulkan with the reverse-z-buffer?
- How does the performance of the reverse-z-buffer compare to other rendering techniques?

*Source: unknown | chunk_id: github_issue_2747_discussion*
