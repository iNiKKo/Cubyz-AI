# [src/main.zig] - PR #2625 review diff

**Type:** review
**Keywords:** modifier keys, actionModifier, textModifier, un-rebindable, input handling system, GLFW constants, key struct
**Symbols:** KeyBoard, GLFW_MOUSE_BUTTON_LEFT, GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER, pressBreak, releaseBreak, GLFW_MOUSE_BUTTON_MIDDLE, GLFW_GAMEPAD_BUTTON_DPAD_LEFT, pressAcquireSelectedBlock, GLFW_KEY_Q, dropFromHand, GLFW_KEY_LEFT_SHIFT, Tag.controlModifier0
**Concepts:** input handling, keyboard actions, modularity, refactoring

## Summary
Added a new keyboard action for modifier keys, renaming existing modifiers.

## Explanation
The change introduces a new keyboard action named 'modifier0' associated with the left shift key. This addition is part of a broader architectural review aimed at refining how keyboard actions are handled within the game. The reviewer renamed existing modifier-related actions to `actionModifier` and introduced a new flag on the key struct called `textModifier`, which is intended to be un-rebindable. This refactoring likely aims to improve the modularity and clarity of the input handling system, ensuring that different types of modifiers are distinctly managed.

## Related Questions
- What is the purpose of renaming existing modifier actions to `actionModifier`?
- How does the introduction of `textModifier` affect the rebindability of keyboard actions?
- Can you explain the role of the `Tag.controlModifier0` in this context?
- What changes were made to the key struct as part of this refactoring?
- How might this refactoring impact existing game controls?
- Are there any potential performance implications from these changes?

*Source: unknown | chunk_id: github_pr_2625_comment_2900879676*
