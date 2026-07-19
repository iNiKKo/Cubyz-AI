# [issues/issue_1958.md] - Issue #1958 discussion

**Type:** review
**Keywords:** controller, keyboard, mouse, cursor, top right corner, UV coordinate, deadzone, Godot, input interaction
**Concepts:** input handling, deadzone, cursor movement

## Summary
Users report cursor movement issues when using both a controller and keyboard/mouse, with the cursor moving towards the top right corner of the screen.

## Explanation
Users report a cursor movement issue when using both a controller and keyboard/mouse simultaneously in Cubyz. The cursor moves towards the top right corner of the screen by 1 pixel each frame, with UV coordinates involved. This issue is observed on ArchLinux/Hyprland with an AMD 9950X3D and RTX 5070Ti GPU. The maintainer suggests increasing the default deadzone for controllers to address this recurring problem, noting that Godot has a higher default deadzone percentage of 20%. Changing the controller's deadzone value (e.g., setting it to 10%) can exacerbate the issue by making the cursor move faster towards the top right corner. The maintainer acknowledges that this is a reoccurring issue for many users and should be addressed soon.

## Related Questions
- What is the current default deadzone value for controllers in Cubyz?
- How does changing the controller's deadzone affect cursor movement?
- Are there any known issues with input handling when using both a controller and keyboard/mouse simultaneously?
- Why did the maintainer suggest increasing the default deadzone to 20%?
- Has this issue been reported on other operating systems or window managers besides ArchLinux/Hyprland?
- What are the potential side effects of increasing the default deadzone value?

*Source: unknown | chunk_id: github_issue_1958_discussion*
