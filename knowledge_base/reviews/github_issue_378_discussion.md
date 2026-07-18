# [issues/issue_378.md] - Issue #378 discussion

**Type:** review
**Keywords:** UI inconsistency, pixel dimensions, distortions, inventory windows, window size
**Concepts:** UI consistency, pixel scaling

## Summary
The UI is not pixel consistent due to odd-numbered pixel dimensions causing distortions at small scales.

## Explanation
The issue arises from using an odd number of pixels for items in the UI, which leads to distortions when scaled down. The maintainer addressed this by recommending a 4x4 pixel size for items and adjusting the default window size of inventory windows to 0.75 to prevent item slots from becoming too large.

## Related Questions
- What is the recommended pixel size for UI items to ensure consistency?
- How did the maintainer adjust the inventory window sizes?
- Why was it necessary to change the default window size of inventory windows?
- What are the potential consequences of using odd-numbered pixel dimensions in UI elements?
- How does changing the window size affect the appearance of item slots in the inventory?
- Can you explain the impact of pixel scaling on UI consistency in Cubyz?

*Source: unknown | chunk_id: github_issue_378_discussion*
