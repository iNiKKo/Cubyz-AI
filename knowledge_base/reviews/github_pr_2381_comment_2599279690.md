# [src/main.zig] - PR #2381 review diff

**Type:** review
**Keywords:** placeBlock, use and place, GLFW_MOUSE_BUTTON_RIGHT, GLFW_GAMEPAD_AXIS_LEFT_TRIGGER, game.pressSecondary, game.releaseSecondary, inGame, architectural review, input handling, key binding
**Symbols:** KeyBoard, GLFW_KEY_G, GLFW_KEY_H, GLFW_GAMEPAD_BUTTON_RIGHT_THUMB, GLFW_MOUSE_BUTTON_RIGHT, GLFW_GAMEPAD_AXIS_LEFT_TRIGGER, game.ghostToggle, game.hyperSpeedToggle, game.pressSecondary, game.releaseSecondary
**Concepts:** Input Handling, Gamepad Support, Key Binding, Architectural Review

## Summary
Renamed the 'placeBlock' action to 'use and place' and updated associated function calls.

## Explanation
The change renames the keyboard/mouse/gamepad action from 'placeBlock' to 'use and place', which likely indicates a more generalized interaction that could include both placing blocks and using items. The reviewer suggests renaming it further to 'use or place', implying a choice between these two actions. The associated function calls are updated from `game.pressPlace` and `game.releasePlace` to `game.pressSecondary` and `game.releaseSecondary`, respectively. This change is part of an architectural review that aims to clarify the purpose of the action and ensure consistency in naming conventions.

## Related Questions
- What is the purpose of renaming 'placeBlock' to 'use and place'?
- How does this change affect gamepad input handling?
- Why were the function calls updated from `game.pressPlace` to `game.pressSecondary`?
- Is there any potential impact on backward compatibility with existing save files or configurations?
- What is the intended behavior of the 'use and place' action in the game?
- How does this change align with the overall input architecture of Cubyz?
- Are there any other actions that might need similar renaming for consistency?
- What are the potential performance implications of this change?
- Does this change introduce any new bugs or regressions?
- How should developers test this change to ensure it works as intended?

*Source: unknown | chunk_id: github_pr_2381_comment_2599279690*
