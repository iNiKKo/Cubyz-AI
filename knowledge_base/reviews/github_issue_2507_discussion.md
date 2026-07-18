# [issues/issue_2507.md] - Issue #2507 discussion

**Type:** review
**Keywords:** Zig, GLFW, Wayland, segmentation fault, build from source, vendored libraries, system package manager, distribution maintainers, musl libc, void-linux
**Symbols:** Cubyz, GLFW, Wayland, zig-out/bin/Cubyz, run_linux.sh
**Concepts:** packaging, distribution support, library vendoring, compatibility, precompiled binaries

## Summary
The issue discusses difficulties in packaging Cubyz for Linux/BSD distributions due to reliance on specific Zig versions, vendored libraries without Wayland support, and precompiled binaries that may not work across different systems.

## Explanation
The discussion revolves around the challenges faced by distribution maintainers in packaging Cubyz. The main issues include the use of unreleased Zig versions, which makes it difficult to rely on system-packaged compilers; vendored libraries like GLFW without Wayland support, leading to compatibility problems on systems that require Wayland; and precompiled binaries that may not work across different distributions due to varying dependencies and configurations. The user reports a segmentation fault with the latest binary and an initialization error when trying to build from source using the run script. The maintainer acknowledges these issues but notes that enabling Wayland support in GLFW was previously rejected due to compatibility concerns, and prebuilt binaries must use self-built libraries for maximum compatibility.

## Related Questions
- What is the impact of using unreleased Zig versions on distribution packaging?
- How can Cubyz be modified to support Wayland in GLFW without breaking compatibility with other systems?
- Why are prebuilt binaries necessary for maximum compatibility, and what challenges do they present?
- What steps can be taken to ensure that vendored libraries like GLFW work correctly across different distributions?
- How can the build process be improved to allow building from source using system libraries?
- What is the root cause of the segmentation fault reported with the latest Cubyz binary on void-linux with musl libc?

*Source: unknown | chunk_id: github_issue_2507_discussion*
