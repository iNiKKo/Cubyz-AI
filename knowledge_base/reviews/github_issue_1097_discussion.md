# [issues/issue_1097.md] - Issue #1097 discussion

**Type:** review
**Keywords:** headless servers, compile-time options, UI-related libraries, OpenGL dependencies, build.zig, main.zig, graphics.zig, asset loading, code separation, dependencies management
**Symbols:** launchConfig.headlessMode, build.zig, main.zig, graphics.zig
**Concepts:** Compile-time options, Code separation, Dependencies management

## Summary
Discussion about implementing headless servers, focusing on compile-time options to exclude UI-related libraries and address dependencies on OpenGL.

## Explanation
The discussion revolves around the implementation of headless servers in Cubyz. The primary concern is to create a build target that excludes UI-related libraries, which can be achieved by using a compile-time option provided by `build.zig`. This approach aims to simplify the server build process and avoid unnecessary linking. However, there are significant challenges due to dependencies on OpenGL for asset loading, which currently ties the server to client-side graphics code. The reviewer suggests either removing these dependencies or splitting out relevant pieces of code to ensure that the server can operate independently without relying on OpenGL.

## Related Questions
- How can the compile-time option `-Dheadless` be implemented in `build.zig` to exclude UI-related libraries?
- What are the potential impacts of removing OpenGL dependencies from asset loading on server performance?
- How can the existing codebase be refactored to split out relevant pieces for headless server operation?
- What steps should be taken to ensure that the headless server build does not include any unnecessary client-side graphics code?
- How can a CI test be added to verify that the standalone server launches and closes correctly without error logs?
- What are the benefits of using a compile-time approach for defining headless mode compared to runtime configuration?

*Source: unknown | chunk_id: github_issue_1097_discussion*
