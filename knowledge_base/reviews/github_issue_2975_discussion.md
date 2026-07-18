# [issues/issue_2975.md] - Issue #2975 discussion

**Type:** gameplay
**Keywords:** Debian 10, Cubyz game, GLXBadFBConfig, Vulkan support, OpenGL 4.6, glibc version
**Symbols:** __read_alias, GLFW, Mesa, OpenGL, glibc
**Concepts:** Linux distribution compatibility, AppImage, Game development, Graphics drivers, Build configuration

## Summary
User reports difficulties running Cubyz on Debian 10 due to Mesa version limitations and OpenGL compatibility. Specific errors include `GLFW Error(65543): GLX: Failed to create context: GLXBadFBConfig` and `thread 16290 panic: Failed to create GLFW window`. The maintainer identified the issue as outdated Mesa not supporting OpenGL 4.6 required by Cubyz, proposing a solution of setting a lower glibc version for future releases to ensure compatibility with older systems without requiring users to update their graphics drivers or system libraries.

## Explanation
The user encountered specific errors such as `GLFW Error(65543): GLX: Failed to create context: GLXBadFBConfig` and `thread 16290 panic: Failed to create GLFW window`. These issues are related to the Mesa version on Debian 10, which does not support OpenGL 4.6 required by Cubyz. Additionally, CI tests encountered Vulkan-related errors due to limitations with vulkan-swrast. The maintainer proposed setting a lower glibc version for future releases of Cubyz to ensure compatibility with older systems like Debian 10 without requiring users to update their graphics drivers or system libraries. This approach leverages the backward compatibility of glibc and avoids bundling Mesa drivers in an AppImage, which could increase package size.

## Related Questions
- How can developers resolve GLFW window creation errors on Debian 10?
- What are the implications of setting a lower glibc version for game releases?
- How do developers ensure compatibility with different Linux distributions when creating AppImages?
- How does OpenGL support impact game development across various Linux systems?
- Can bundling Mesa drivers in an AppImage improve compatibility with older systems?
- What are best practices for handling graphics driver issues in cross-platform applications?

*Source: unknown | chunk_id: github_issue_2975_discussion*
