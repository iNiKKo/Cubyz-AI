# [issues/issue_1619.md] - Issue #1619 discussion

**Type:** review
**Keywords:** textbox, cursor, focus, selection, standard OS behavior, simplicity
**Concepts:** user interface, focus management, cursor visibility

## Summary
The proposal suggests hiding the cursor in textboxes when they are not focused, aligning with standard OS behavior. The debate focuses on whether to also remove selections when focusing away from a textbox.

## Explanation
The issue discusses the current behavior of textboxes in Cubyz where cursors do not disappear even when the textbox loses focus. The proposal suggests that clicking out of the textbox, hitting escape, or any other action to focus away from the textbox should remove both the cursor and selection for simplicity. This aligns with standard OS practices where a cursor is only visible when the textbox is active. The maintainer agrees with this approach, emphasizing simplicity over complex behaviors seen in other applications. User confirmation indicates that the described behavior already matches the current implementation.

## Related Questions
- What are the specific actions that should hide the cursor and selection from a textbox?
- Why does the proposal suggest removing both the cursor and selection when focusing away from a textbox?
- How does maintaining a single cursor across the entire application simplify user interaction?
- Are there any concerns about user confusion if multiple cursors were allowed?

*Source: unknown | chunk_id: github_issue_1619_discussion*
