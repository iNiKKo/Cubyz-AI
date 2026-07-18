# [issues/issue_324.md] - Issue #324 discussion

**Type:** review
**Keywords:** Mac support, Cubyz compilation, GLFW context, EGL runtime, Zink driver, libcubyz_deps.a, Mesa LLVMpipe/Zink, Git submodules, Zig package manager, Install instructions
**Symbols:** Cubyz, build.zig, libGL, EGL, Zink driver, run_linux.sh, Cubyz-libs, libcubyz_deps.a, Mesa LLVMpipe/Zink libGL, GLFW
**Concepts:** Cross-platform compilation, Dependency management, Build system integration, Performance considerations, User experience

## Summary
The discussion revolves around merging changes to allow Cubyz to compile on Mac, with considerations for future Vulkan support and avoiding unnecessary complexity.

## Explanation
As of now, Cubyz officially does NOT support Mac -- the documented reason (per the project README) is that Mac lacks OpenGL 4.3, which Cubyz requires. This issue is a separate, unmerged community proposal discussing what it would take to add Mac *compilation* support in the future; it does not describe the current, official state of Mac support, and its GLFW/libGL/EGL/Zink details are about that future build-system work, not the reason Mac is currently unsupported. The issue aims to enable Cubyz compilation on Mac, addressing benefits such as preventing modifications from going stale and allowing easier contributions. The maintainer is generally supportive but suggests avoiding adding too much extra functionality like Zink driver support until Vulkan (#102) is considered. There are concerns about the size of `libcubyz_deps.a` when built for multiple platforms and the potential harm of providing install instructions that might give false impressions about Mac compatibility. The maintainer also recommends using Zig's package manager instead of Git submodules for dependencies like GLFW.

## Related Questions
- What changes are needed to update `build.zig` for Mac support?
- Why is the maintainer concerned about duplicating `libcubyz_deps.a`?
- How does the maintainer suggest managing GLFW dependencies?
- What potential issues might arise from providing install instructions on Mac?
- How will future Vulkan support impact the current Mac compilation efforts?
- Is there a plan to address the size issue of `libcubyz_deps.a` for multiple platforms?

*Source: unknown | chunk_id: github_issue_324_discussion*
