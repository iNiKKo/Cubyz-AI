# [issues/issue_1040.md] - Issue #1040 discussion

**Type:** review
**Keywords:** X11 library, Zig compiler, missing dependencies, Linux distribution, Wayland support
**Concepts:** build system, dependency management, library linking

## Summary
The user reports a failure to build Cubyz due to missing X11 library dependencies.

## Explanation
The error indicates that the Zig compiler is unable to find the dynamic system library 'x11' during the build process. The maintainer suspects that either the X11 libraries are not installed or have been removed from the user's system. The maintainer asks for more information about how the dependencies were installed and the Linux distribution used. There is a possibility that Wayland might be in use instead of X11, as Cubyz does not currently support Wayland (#358). The maintainer suggests trying to remove and reinstall the packages as a potential solution.

## Related Questions
- What is the output of the install command?
- Which Linux distribution is being used?
- Are there any logs or error messages related to X11 installation?
- Is Wayland installed on the system instead of X11?
- How can I check if X11 libraries are installed and where they are located?
- What steps should I follow to remove and reinstall the X11 libraries?
- Are there any known issues with Cubyz and Wayland compatibility?
- Can you provide a list of required dependencies for building Cubyz?
- How can I ensure that all necessary build tools and libraries are installed on my system?
- What is the current status of Wayland support in Cubyz?

*Source: unknown | chunk_id: github_issue_1040_discussion*
