# [issues/issue_2906.md] - Issue #2906 discussion

**Type:** review
**Keywords:** segfault, world exit, entityModel.zig, texture deinit, server thread, OpenGL context, NVIDIA drivers, prime-run
**Symbols:** reset, deinit, main.assets.unloadAssets, startFromExistingThread, startFromNewThread, c.glDeleteTextures
**Concepts:** thread safety, OpenGL context, driver interaction, undefined behavior

## Summary
A consistent segfault occurs during world exit due to OpenGL operations being performed on a thread without an OpenGL context.

## Explanation
The issue arises from attempting to deinitialize textures in the `entityModel.zig` file on a server thread that lacks an OpenGL context. This leads to undefined behavior, resulting in a segmentation fault. The maintainer suspects that this is related to recent changes in the codebase, particularly around texture management and threading. The user identified that forcing Cubyz to use the discrete GPU with `prime-run` resolves the issue, suggesting a potential interaction between the OpenGL context and the NVIDIA drivers.

## Related Questions
- What is the impact of performing OpenGL operations on a thread without an OpenGL context?
- How can we ensure that texture deinitialization occurs in the correct thread with an OpenGL context?
- Are there any other parts of the codebase where similar threading issues might exist?
- How can we prevent future regressions related to OpenGL context management and threading?
- What are the potential implications of driver interactions on OpenGL operations in Cubyz?
- How can we add logging to identify which model ID is causing the crash during texture deinitialization?

*Source: unknown | chunk_id: github_issue_2906_discussion*
