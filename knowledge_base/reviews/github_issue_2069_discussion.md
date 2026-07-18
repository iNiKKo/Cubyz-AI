# [issues/issue_2069.md] - Issue #2069 discussion

**Type:** review
**Keywords:** Vulkan, MacOS, OpenGL, MoltenVK, GLFW, RPath, build script, error handling
**Symbols:** vulkanTestingWindow, build.zig
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The user reports issues building and running a Vulkan window on MacOS, encountering errors related to thread renaming and unsupported OpenGL version. The maintainer suggests missing MoltenVK and other dependencies, and references a potential fix in pull request #2351.

## Explanation
The user is attempting to work on Vulkan migration steps but encounters multiple issues when running the build command with `vulkanTestingWindow` set to true. The primary errors include repeated 'Couldn't rename thread: Unsupported' messages, a Vulkan unsupported error, and an OpenGL version mismatch. The maintainer comments that these issues are likely due to missing dependencies such as MoltenVK and other required libraries for building on MacOS. They also mention that a potential fix has been proposed in pull request #2351.

## Related Questions
- What is the status of pull request #2351?
- How can I install MoltenVK on my MacOS system?
- Are there any other dependencies required for building Cubyz on MacOS?
- What is the purpose of the `addRPath` function in `build.zig`?
- How does the error 'Requested OpenGL version 4.6, got version 2.1' occur and how can it be resolved?
- What are the implications of the 'Couldn't rename thread: Unsupported' errors on MacOS?

*Source: unknown | chunk_id: github_issue_2069_discussion*
