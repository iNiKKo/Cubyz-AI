# [issues/issue_2079.md] - Issue #2079 discussion

**Type:** review
**Keywords:** dead zone, controller, sensitivity, bug, workaround, reboot
**Concepts:** input handling, gamepad support, dead zone

## Summary
The dead zone setting in the game's controller configuration cannot be adjusted once set to maximum, causing cursor movement issues.

## Explanation
The user encountered an issue where the dead zone setting in the game's controller configuration was stuck at 500%, preventing them from adjusting the cursor sensitivity. Reinstalling the game did not solve the issue, and the user could not find anything to edit in the files. The maintainer suggested unplugging the controller and rebooting the game as a temporary workaround. Additionally, there are reports of inconsistent gamepad sensitivity, with one stick being too sensitive and the other not sensitive enough. This indicates potential bugs in the game's input handling for controllers. The maintainer also recommended using a keyboard and mouse as an alternative due to bugged gamepad support.

## Related Questions
- How can the dead zone setting be made adjustable after being set to maximum?
- What is causing the inconsistent sensitivity between the left and right sticks on the gamepad?
- Are there any known issues with the input handling for controllers in this version of the game?
- Can unplugging the controller and rebooting the game resolve all input-related issues?
- Is there a way to manually edit the configuration files to adjust the dead zone setting?
- What steps can be taken to improve the overall gamepad support in future updates?

*Source: unknown | chunk_id: github_issue_2079_discussion*
