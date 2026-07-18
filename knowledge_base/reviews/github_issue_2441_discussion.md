# [issues/issue_2441.md] - Issue #2441 discussion

**Type:** review
**Keywords:** diagonal movement, controller, keyboard, speed comparison, F3
**Concepts:** input handling, controller support, keyboard support

## Summary
The issue discusses diagonal movement being slower with a controller compared to a keyboard.

## Explanation
The issue discusses diagonal movement being slower with a controller compared to a keyboard. The maintainers have asked for specific details such as the movement speed and provided visual comparisons between the two input methods. They noted that the keyboard output is normalized to 1, but in practice, this does not result in equal speeds for diagonal movement. Visual comparisons are available at these links: Keyboard: https://github.com/user-attachments/assets/df1f3f30-e421-402e-8b28-a9f5baac0c71 and Controller: https://github.com/user-attachments/assets/6ad83d1b-2d97-4139-93f2-4290fa4b7a6c. The maintainers are investigating why diagonal movement is slower when using a controller instead of a keyboard.

## Related Questions
- What is the current implementation of diagonal movement normalization for controllers?
- Are there any known discrepancies between keyboard and controller input processing?
- How can we ensure consistent speed across different input methods for diagonal movement?
- Is there a specific configuration or setting that affects the speed of controller inputs?
- Can you provide more detailed logs or data on the speeds observed during diagonal movement?
- What are the potential architectural changes needed to address this issue?

*Source: unknown | chunk_id: github_issue_2441_discussion*
