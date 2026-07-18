# [issues/issue_872.md] - Issue #872 discussion

**Type:** review
**Keywords:** world select screen, buttons, stone background, unique background, layout components, scrolling effect
**Concepts:** layout, background, scrolling, visual consistency

## Summary
The issue discusses making the background for the world select screen scroll with the buttons instead of remaining static.

## Explanation
The current implementation causes a visual inconsistency where buttons move while the stone background remains still, creating an unnatural appearance. The maintainer suggests that implementing this feature would require assigning unique backgrounds to layout components, which could lead to unintended visual effects in other parts of the application where scrolling is not desired.

## Related Questions
- How can we ensure that the scrolling effect is consistent across different screens?
- What are the potential impacts of assigning unique backgrounds to layout components?
- Can you provide a mockup of how the world select screen would look with the proposed changes?
- How will this change affect the performance of the application?
- Are there any accessibility concerns we should consider with this feature?
- What is the current implementation for handling background and button movement in the world select screen?
- How can we test the scrolling effect to ensure it works as expected?
- Is there a way to implement this feature without affecting other parts of the application?
- Can you provide a timeline for when this change will be implemented?
- What are the potential regressions we should watch out for with this change?

*Source: unknown | chunk_id: github_issue_872_discussion*
