# [issues/issue_1955.md] - Issue #1955 discussion

**Type:** configuration
**Keywords:** GLXBadFBConfig, Segmentation fault, VK_ERROR_INCOMPATIBLE_DRIVER, OpenGL 3.3, Vulkan support
**Symbols:** GLFW, Wayland, Vulkan, OpenGL, Cubyz
**Concepts:** Linux display server, window context creation, hardware compatibility, game development

## Summary
Cubyz fails to launch on Wayland with GLFW context creation error

## Explanation
The user is experiencing issues launching the Cubyz game on a Linux system using Wayland as the display server. The initial attempt to build and run Cubyz from source results in a GLFW error related to creating a window context, specifically `GLFW Error(65543): GLX: Failed to create context: GLXBadFBConfig`. This error suggests that there is an issue with the framebuffer configuration when trying to create a window using GLFW on Wayland.

The user then removed a line of code related to setting the window icon, which led to a different error: `Segmentation fault at address 0x7f9896b35368`. This new error points to an issue within the `_glfwSetWindowIconX11` function in the GLFW library.

The user also mentions that they have tried using the latest release version of Cubyz instead of the dev branch, but encountered a Vulkan error indicating that their hardware does not support Vulkan. The CPU is an Intel Core i5-2400 and the GPU is integrated graphics from the 2nd Generation Core Processor Family.

The user has OpenGL 3.3, which is older than the minimum requirements for Cubyz, which likely supports OpenGL 4.3 or Vulkan. This suggests that the hardware may not be compatible with the game's requirements.

The user concludes by considering closing the issue due to the hardware limitations.

## Code Example
```zig
```bash
./Cubyz 
Starting game client with version 0.0.0
Availabe vulkan instance extensions:
    VK_EXT_debug_report
    VK_EXT_debug_utils
    VK_KHR_portability_enumeration
    VK_LUNARG_direct_driver_loading
Couldn't find validation layer VK_LAYER_KHRONOS_validation
Encountered a vulkan error: VK_ERROR_INCOMPATIBLE_DRIVER
GLFW Error(65542): Vulkan: Window surface creation extensions not found
Encountered a vulkan error: VK_ERROR_EXTENSION_NOT_PRESENT
[Vulkan Loader] ERROR:          vkEnumeratePhysicalDevices: Invalid instance [VUID-vkEnumeratePhysicalDevices-instance-parameter]
Aborted                    (core dumped) ./Cubyz
```
Seems like a vulkan thing ig.
RandomScientist (discord) said -
To remove this from graphics/Window.zig -
```bash
if(c.glfwVulkanSupported() == c.GLFW_FALSE) {
    std.log.err("Vulkan is not supported. Please update your drivers if you want to keep playing Cubyz in the future.", .{});
}
```

## Related Questions
- How can I resolve GLFW context creation errors on Wayland?
- What are the minimum hardware requirements for running Cubyz?
- How do I check if my system supports Vulkan or OpenGL 4.3?
- How can I modify Cubyz to work with older graphics hardware?
- Are there any known issues with running Cubyz on Wayland?
- Can I run Cubyz using software rendering instead of hardware acceleration?

*Source: unknown | chunk_id: github_issue_1955_discussion*
