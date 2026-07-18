# [issues/issue_1097.md] - Issue #1097 discussion

**Type:** review
**Keywords:** headless servers, compile-time options, UI-related libraries, OpenGL dependencies, build.zig, main.zig, graphics.zig, asset loading, code separation, dependencies management
**Symbols:** launchConfig.headlessMode, build.zig, main.zig, graphics.zig
**Concepts:** Compile-time options, Code separation, Dependencies management

## Summary
Discussion about implementing headless servers, focusing on compile-time options to exclude UI-related libraries and address dependencies on OpenGL.

## Explanation
The discussion revolves around implementing headless servers in Cubyz to support server-side operations without UI-related libraries. The primary tasks include creating a build target that excludes UI-related libraries using compile-time options provided by `build.zig`. This involves specifying `-Dheadless` as a compile option, which simplifies the build process and avoids unnecessary linking of client-side code. However, significant challenges arise due to dependencies on OpenGL for asset loading, necessitating either removing these dependencies or splitting out relevant pieces of code to ensure independent server operation without relying on OpenGL graphics code.

The remaining work includes:
- [ ] Releasing version 0 to coordinate player versions (https://github.com/PixelGuys/Cubyz/milestone/2)
- [ ] Establishing a release schedule for timely updates
- [ ] Adding an install/launch script for Windows and Linux
- [ ] Creating a file or wiki entry explaining server setup, including external requirements like port forwarding
- [ ] Implementing a CI test that launches and closes the standalone server to check for error logs.

The reviewer suggests using compile-time options in `build.zig` to exclude UI-related libraries by specifying `-Dheadless`, which simplifies the build process. However, this approach requires significant refactoring of the codebase to address dependencies on OpenGL for asset loading and ensure that the server can operate independently without client-side graphics code.

## Related Questions
- How can the compile-time option `-Dheadless` be implemented in `build.zig` to exclude UI-related libraries?
- What are the potential impacts of removing OpenGL dependencies from asset loading on server performance?
- How can the existing codebase be refactored to split out relevant pieces for headless server operation?
- What steps should be taken to ensure that the headless server build does not include any unnecessary client-side graphics code?
- How can a CI test be added to verify that the standalone server launches and closes correctly without error logs?
- What are the benefits of using a compile-time approach for defining headless mode compared to runtime configuration?

*Source: unknown | chunk_id: github_issue_1097_discussion*
