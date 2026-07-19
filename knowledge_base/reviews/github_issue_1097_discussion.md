# [issues/issue_1097.md] - Issue #1097 discussion

**Type:** review
**Keywords:** headless servers, compile-time options, UI-related libraries, OpenGL dependencies, build.zig, main.zig, graphics.zig, asset loading, code separation, dependencies management
**Symbols:** launchConfig.headlessMode, build.zig, main.zig, graphics.zig
**Concepts:** Compile-time options, Code separation, Dependencies management

## Summary
Discussion about implementing headless servers, focusing on compile-time options to exclude UI-related libraries and address dependencies on OpenGL.

## Explanation
Discussion about implementing headless servers in Cubyz to support server-side operations without UI-related libraries. The primary tasks include creating a build target that excludes UI-related libraries using compile-time options provided by `build.zig`. This involves specifying `-Dheadless` as a compile option, which simplifies the build process and avoids unnecessary linking of client-side code. However, significant challenges arise due to dependencies on OpenGL for asset loading, necessitating either removing these dependencies or splitting out relevant pieces of code to ensure independent server operation without relying on OpenGL graphics code.

The remaining work includes:
- [ ] Releasing version 0 to coordinate player versions (https://github.com/PixelGuys/Cubyz/milestone/2)
- [ ] Establishing a release schedule for timely updates
- [ ] Adding an install/launch script for Windows and Linux
- [ ] Creating a file or wiki entry explaining server setup, including external requirements like port forwarding
- [ ] Implementing a CI test that launches and closes the standalone server to check for error logs.

The reviewer suggests using compile-time options in `build.zig` to exclude UI-related libraries by specifying `-Dheadless`, which simplifies the build process. However, this approach requires significant refactoring of the codebase to address dependencies on OpenGL for asset loading and ensure that the server can operate independently without client-side graphics code.

To implement the compile-time option `-Dheadless` in `build.zig`, developers need to modify the build configuration to include a new target that excludes UI-related libraries. This involves editing the `build.zig` file to add a new build step with the `-Dheadless` flag, which will prevent linking of any client-side code.

Removing OpenGL dependencies from asset loading can have significant impacts on server performance, as it may require additional processing or alternative methods for handling assets. Developers need to carefully consider these impacts and explore potential solutions, such as splitting out relevant pieces of code or using alternative libraries that do not rely on OpenGL.

Refactoring the existing codebase to split out relevant pieces for headless server operation involves identifying and separating code that is specific to client-side graphics from the core server functionality. This may require significant changes to the code structure, but it is necessary to ensure that the headless server can operate independently without relying on OpenGL graphics code.

To ensure that the headless server build does not include any unnecessary client-side graphics code, developers need to carefully review and test the build configuration to verify that all UI-related libraries are excluded. This may involve additional testing and debugging to identify and resolve any issues that arise during the build process.

Adding a CI test to verify that the standalone server launches and closes correctly without error logs involves creating a new test script that simulates the launch and shutdown of the headless server. This test should check for any error messages or other issues that may indicate problems with the server operation, and it should be integrated into the continuous integration pipeline to ensure that it is run automatically during each build.

Using a compile-time approach for defining headless mode compared to runtime configuration has several benefits. First, it simplifies the build process by avoiding unnecessary linking of client-side code. Second, it ensures that the server can operate independently without relying on OpenGL graphics code, which can improve performance and reduce dependencies. Third, it provides a clear and consistent way to define the headless mode, making it easier for developers to understand and maintain the codebase.

## Related Questions
- How can the compile-time option `-Dheadless` be implemented in `build.zig` to exclude UI-related libraries?
- What are the potential impacts of removing OpenGL dependencies from asset loading on server performance?
- How can the existing codebase be refactored to split out relevant pieces for headless server operation?
- What steps should be taken to ensure that the headless server build does not include any unnecessary client-side graphics code?
- How can a CI test be added to verify that the standalone server launches and closes correctly without error logs?
- What are the benefits of using a compile-time approach for defining headless mode compared to runtime configuration?

*Source: unknown | chunk_id: github_issue_1097_discussion*
