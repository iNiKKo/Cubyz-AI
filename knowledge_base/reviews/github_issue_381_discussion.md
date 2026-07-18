# [issues/issue_381.md] - Issue #381 discussion

**Type:** review
**Keywords:** Linux, Zig Compiler, System Libraries, README, Terminal Open, Dependencies Installation
**Symbols:** run_linux.sh, build.zig, zig build run
**Concepts:** Dependency Management, Terminal Handling, Documentation Clarity

## Summary
Discusses and resolves issues with compiling Cubyz on Linux, focusing on missing dependencies and terminal handling.

## Explanation
The discussion primarily revolves around two main issues: missing system libraries required for compilation and the behavior of running shell scripts in different environments. The first issue is resolved by ensuring all necessary `-dev` packages are installed as listed in the README, specifically `libgl-dev`, `libasound2-dev`, `libx11-dev`, `libxcursor-dev`, `libxrandr-dev`, `libxinerama-dev`, `libxext-dev`, and `libxi-dev`. The second issue involves modifying the `run_linux.sh` script to always open a terminal, addressing cases where the script might not run in an interactive terminal session. This can be achieved by adding checks within the script to determine if it is running in a terminal and opening one if necessary. The maintainers and users also discuss improving the README for better clarity and user experience.

## Related Questions
-  How can the `run_linux.sh` script be modified to always open a terminal?
-  What are the necessary `-dev` packages for compiling Cubyz on Linux? (libgl-dev, libasound2-dev, libx11-dev, libxcursor-dev, libxrandr-dev, libxinerama-dev, libxext-dev, and libxi-dev)
-  Why does the Zig compiler error occur when using an outdated version?
-  How can the README be restructured to improve clarity and user experience?
-  What is the intended behavior of the script when detecting a missing Zig compiler?
-  How can the build process be improved to provide more informative error messages?

*Source: unknown | chunk_id: github_issue_381_discussion*
