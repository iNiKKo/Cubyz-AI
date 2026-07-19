# [issues/issue_2069.md] - Issue #2069 discussion

**Type:** review
**Keywords:** Vulkan, MacOS, OpenGL, MoltenVK, GLFW, RPath, build script, error handling
**Symbols:** vulkanTestingWindow, build.zig
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The user reports issues building and running a Vulkan window on MacOS, encountering errors related to thread renaming and unsupported OpenGL version. The maintainer suggests missing MoltenVK and other dependencies, and references a potential fix in pull request #2351.

## Explanation
The user reports issues building and running a Vulkan window on MacOS when setting `vulkanTestingWindow` to true. The primary errors include repeated 'Couldn't rename thread: Unsupported' messages, a Vulkan unsupported error ('Vulkan is not supported. Please update your drivers if you want to keep playing Cubyz in the future.'), and an OpenGL version mismatch ('Requested OpenGL version 4.6, got version 2.1'). These issues are due to missing dependencies such as MoltenVK, GLFW, and Vulkan SDKs for building on MacOS. Specifically, the line in `build.zig` that adds RPath with `/usr/local/GL/lib` is problematic because this path does not exist for the user. The maintainer comments that these issues are being addressed and suggests installing MoltenVK, GLFW, and Vulkan SDKs to resolve them. A potential fix has been proposed in pull request #2351. To install MoltenVK, you can follow these steps: 1. Download the latest version of MoltenVK from the official GitHub repository (https://github.com/KhronosGroup/MoltenVK). 2. Extract the downloaded archive and navigate to the `MoltenVK.xcframework` directory. 3. Copy the `MoltenVK.xcframework` directory to your project's root directory or a location of your choice. 4. In Xcode, open your project and select the target for which you want to add MoltenVK. 5. Go to the 'General' tab and scroll down to the 'Frameworks, Libraries, and Embedded Content' section. 6. Click the '+' button and select 'Add Other...' to add the `MoltenVK.xcframework` directory. 7. Ensure that the framework is set to 'Embed & Sign'. Additionally, you may need to install other dependencies such as GLFW and Vulkan SDKs for MacOS. Refer to the official documentation of these libraries for installation instructions.

## Related Questions
- What is the status of pull request #2351?
- How can I install MoltenVK on my MacOS system?
- Are there any other dependencies required for building Cubyz on MacOS?
- What is the purpose of the `addRPath` function in `build.zig`?
- How does the error 'Requested OpenGL version 4.6, got version 2.1' occur and how can it be resolved?
- What are the implications of the 'Couldn't rename thread: Unsupported' errors on MacOS?

*Source: unknown | chunk_id: github_issue_2069_discussion*
