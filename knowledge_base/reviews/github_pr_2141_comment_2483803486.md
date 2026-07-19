# [src/graphics/vulkan.zig] - PR #2141 review diff

**Type:** review
**Keywords:** vulkan, extensions, allocation, macOS, performance, compatibility, array handling, zig noob
**Symbols:** createInstance, glfwExtensions
**Concepts:** thread safety, backwards compatibility, memory management

## Summary
The change introduces an array of Vulkan extensions and avoids allocation when not on macOS.

## Explanation
**Explanation**
The change introduces an array of Vulkan extensions and avoids allocation when not on macOS. The reviewer notes that the code is ugly due to array handling but acknowledges it as a necessary workaround for avoiding allocation on non-macOS platforms. The architectural review suggests ensuring this approach does not introduce performance regressions or memory leaks, while maintaining compatibility with other systems.

The specific array handling code involves copying `glfwExtensions` into a local variable named `extensions`. This is done to avoid dynamic allocation when the platform is not macOS. The reviewer mentions being a 'zig noob' and finding this array stuff really ugly.

**Related Questions**
- What is the purpose of the 'glfwExtensions' array in this code?
- How does avoiding allocation on non-macOS platforms impact performance?
- Are there any potential memory leaks introduced by this change?
- Does this code maintain backwards compatibility with previous versions?
- What are the implications of using an array for Vulkan extensions?
- How can we ensure thread safety in this modified section?
- Is there a more elegant way to handle Vulkan extensions without allocation?
- What are the potential performance regressions introduced by this change?
- How does this code interact with other systems and platforms?
- Are there any known issues with using arrays for Vulkan extensions?

## Related Questions
- What is the purpose of the 'glfwExtensions' array in this code?
- How does avoiding allocation on non-macOS platforms impact performance?
- Are there any potential memory leaks introduced by this change?
- Does this code maintain backwards compatibility with previous versions?
- What are the implications of using an array for Vulkan extensions?
- How can we ensure thread safety in this modified section?
- Is there a more elegant way to handle Vulkan extensions without allocation?
- What are the potential performance regressions introduced by this change?
- How does this code interact with other systems and platforms?
- Are there any known issues with using arrays for Vulkan extensions?

*Source: unknown | chunk_id: github_pr_2141_comment_2483803486*
