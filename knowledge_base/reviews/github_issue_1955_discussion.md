# [issues/issue_1955.md] - Issue #1955 discussion

**Type:** configuration
**Keywords:** GLXBadFBConfig, Segmentation fault, VK_ERROR_INCOMPATIBLE_DRIVER, OpenGL 3.3, Vulkan support
**Symbols:** GLFW, Wayland, Vulkan, OpenGL, Cubyz
**Concepts:** Linux display server, window context creation, hardware compatibility, game development

## Summary
Cubyz fails to launch due to hardware incompatibility and missing Vulkan support. The user’s system lacks the required OpenGL 4.3 or Vulkan capabilities, leading to various errors such as `GLFW Error(65542): GLX: Failed to create context: GLXBadFBConfig` and `Segmentation fault at address 0x7f9896b35368`. The user’s CPU is an Intel Core i5-2400 with integrated graphics, which does not meet the game's requirements. Additionally, there are issues related to Vulkan support on their system.

## Explanation
The Cubyz game requires OpenGL 4.3 or Vulkan for proper functionality. The user’s hardware (Intel Core i5-2400 with integrated graphics) does not meet these requirements. This results in various errors such as `GLFW Error(65542): GLX: Failed to create context: GLXBadFBConfig` and `Segmentation fault at address 0x7f9896b35368`. The user has also encountered a Vulkan error indicating that their hardware does not support Vulkan. These issues are related to the game’s minimum requirements, which include OpenGL 4.3 or Vulkan for optimal performance on supported hardware.

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
- How can I check if my system supports OpenGL 4.3 or Vulkan?
- What are the known hardware requirements for running Cubyz?
- Is there a way to modify Cubyz to work with older graphics hardware?

*Source: unknown | chunk_id: github_issue_1955_discussion*
