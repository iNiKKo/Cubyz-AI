# [issues/issue_1148.md] - Issue #1148 discussion

**Type:** review
**Keywords:** compile error, x11 library, Zig compiler, build.zig, linkSystemLibrary, capitalization issue
**Symbols:** build.zig, exe.linkSystemLibrary
**Concepts:** library linking, system dependencies, compilation errors

## Summary
The game fails to compile due to an error finding the dynamic system library 'x11'. The maintainer suggests capitalizing 'X11' in line 65 of build.zig.

## Explanation
The compilation process for Cubyz is failing because the Zig compiler cannot locate the 'x11' library. The maintainer proposes a fix by changing the case of 'x11' to 'X11' on line 65 in the build.zig file. This change aims to resolve the issue with linking the system library, which is essential for the game's functionality.

## Related Questions
- What is the purpose of build.zig in Cubyz?
- Why does changing 'x11' to 'X11' resolve the compilation error?
- How does Zig handle case sensitivity when linking libraries?
- Are there other potential causes for the 'unable to find dynamic system library' error?
- What steps should be taken to ensure that all dependencies are correctly installed and linked?
- How can one verify if the 'X11' library is properly installed on their system?

*Source: unknown | chunk_id: github_issue_1148_discussion*
