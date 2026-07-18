# [issues/issue_2545.md] - Issue #2545 discussion

**Type:** review
**Keywords:** crash, Hall Effect keyboard, Linux, Wayland, GLFW, illegal instruction, stack trace, debugging
**Symbols:** _glfwPollJoystickLinux, main.clientMain, main.main, main
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
A crash occurs when using a Hall Effect keyboard on Linux, specifically the Keychron K10 HE.

## Explanation
The issue is related to an illegal instruction error in the GLFW library's joystick polling function for Linux. The user suggests running the latest master version compiled with debug_linux.sh to obtain a more detailed stack trace, which could help identify the root cause of the crash.

## Related Questions
- What is the specific illegal instruction causing the crash?
- How does GLFW handle joystick polling on Linux?
- Are there known issues with Hall Effect keyboards in GLFW?
- Can running the latest master version provide more insights into the crash?
- Is there a way to compile Cubyz with additional debugging symbols for better stack traces?
- What are the potential causes of illegal instructions in Linux applications?

*Source: unknown | chunk_id: github_issue_2545_discussion*
