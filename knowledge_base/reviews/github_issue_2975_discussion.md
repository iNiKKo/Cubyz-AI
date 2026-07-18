# [issues/issue_2975.md] - Issue #2975 discussion

**Type:** gameplay
**Keywords:** Debian 10, Cubyz game, GLXBadFBConfig, Vulkan support, OpenGL 4.6, glibc version
**Symbols:** __read_alias, GLFW, Mesa, OpenGL, glibc
**Concepts:** Linux distribution compatibility, AppImage, Game development, Graphics drivers, Build configuration

## Summary
User reports issues running Cubyz on Debian 10 due to Mesa version and OpenGL compatibility. Maintainer suggests setting a lower glibc version for releases to address compatibility issues.

## Explanation
The user encountered errors related to GLFW window creation and Mesa support while trying to run the Cubyz game on Debian 10. The maintainer identified that the issue might be due to an outdated Mesa version not supporting OpenGL 4.6 required by the game. The maintainer proposed setting a lower glibc version for future releases, as it is backward compatible and should resolve compatibility issues without shipping additional drivers. The user also mentioned that they have created an AppImage repository for Cubyz and provided feedback on potential improvements to the build process.

## Related Questions
- How to resolve GLFW window creation errors on Debian 10?
- What is the impact of setting a lower glibc version for game releases?
- How can developers ensure compatibility with different Linux distributions when creating AppImages?
- How does OpenGL support affect game development on various Linux systems?
- Can bundling Mesa drivers in an AppImage improve compatibility with older systems?
- What are best practices for handling graphics driver issues in cross-platform applications?

*Source: unknown | chunk_id: github_issue_2975_discussion*
