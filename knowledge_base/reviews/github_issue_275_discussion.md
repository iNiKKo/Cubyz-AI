# [issues/issue_275.md] - Issue #275 discussion

**Type:** review
**Keywords:** lighting bugs, dark strip, render distance, chunk updates, neighbor unloading, lighting data
**Concepts:** chunk updates, neighbor unloading, lighting data

## Summary
Reported lighting bugs occur when moving up and down, causing a strip of darkness at the edge of the render distance due to chunk updates and neighbor unloading.

## Explanation
The issue involves lighting data discrepancies when chunks are updated while their neighboring chunks have been unloaded. This leads to visual artifacts like a dark strip at the edge of the render distance. The maintainer notes that they haven't encountered these issues recently, suggesting potential improvements or changes in the chunk update and unloading logic.

## Related Questions
- What changes were made to chunk update and unloading logic recently?
- Are there any known issues with lighting data persistence across chunk boundaries?
- How does the current implementation handle updates to chunks that are near the render distance?
- Is there a mechanism to ensure lighting data consistency when neighboring chunks are unloaded?
- What steps can be taken to prevent visual artifacts like dark strips at the edge of the render distance?
- Are there any plans to improve the handling of chunk updates and unloading in future releases?

*Source: unknown | chunk_id: github_issue_275_discussion*
