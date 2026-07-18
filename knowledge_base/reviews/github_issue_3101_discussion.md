# [issues/issue_3101.md] - Issue #3101 discussion

**Type:** review
**Keywords:** button UI, hitbox misalignment, titleBarHeight, window scale, clickable area
**Symbols:** titleBarHeight, scale
**Concepts:** UI alignment, hitbox, scaling factor

## Summary
The button UI and its hitbox are misaligned due to the `titleBarHeight` not being scaled with the `scale` variable of the window.

## Explanation
The issue arises because the `titleBarHeight` is used in all if statements without considering the scaling factor applied to the window. This discrepancy causes the button's clickable area (hitbox) to be out of sync with its visual representation, leading to a situation where clicking on what appears to be the button does not register any action.

## Related Questions
- Why is the `titleBarHeight` not being scaled with the window's `scale` variable?
- How does the misalignment between the button UI and its hitbox affect user interaction?
- What changes are needed to ensure that the `titleBarHeight` is properly scaled with the window's scale factor?
- Are there any other components in the UI that might be affected by this scaling issue?
- How can we verify that the fix for this issue does not introduce any regressions in other parts of the application?
- What are the potential implications of not scaling `titleBarHeight` on different screen resolutions?

*Source: unknown | chunk_id: github_issue_3101_discussion*
