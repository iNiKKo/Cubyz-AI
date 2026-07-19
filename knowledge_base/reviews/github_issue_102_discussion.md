# [issues/issue_102.md] - Issue #102 discussion

**Type:** review
**Keywords:** vulkan, opengl, vulkan-zig, glad, vk.xml, InstanceCreateInfo, AllocationCallbacks, Instance, Result, vkCreateInstance, type safety, driver reliability, platform support, error handling
**Symbols:** vulkan, opengl, vulkan-zig, glad, vk.xml, InstanceCreateInfo, AllocationCallbacks, Instance, Result, vkCreateInstance
**Concepts:** API transition, type safety, driver reliability, platform support, error handling

## Summary
The discussion revolves around transitioning Cubyz from OpenGL to Vulkan, highlighting advantages like better tooling, platform support, and error detection, but also noting potential development costs and bugs in existing Vulkan implementations.

## Explanation
The discussion revolves around transitioning Cubyz from OpenGL to Vulkan, highlighting advantages like better tooling, platform support, and error detection, but also noting potential development costs and bugs in existing Vulkan implementations. Key points include:

- **Better Tooling**: Vulkan has a GPU profiler from AMD.
- **Broader Platform Support**: Vulkan supports macOS via MoltenVK and mobile GPUs, whereas OpenGL ES is required otherwise.
- **Improved Error Detection**: Vulkan's validation layers provide better error handling compared to inconsistent OpenGL errors.
- **Consistent Performance**: On Intel laptops, Vulkan avoids buffer copies that OpenGL creates.
- **Future-Proofing**: Vulkan is more likely to support future hardware features.
- **Larger Buffers**: SSBOs can be up to 4GB in Vulkan instead of 2GB in OpenGL.

However, the transition comes with significant development costs. The maintainer expresses concerns about using Zig libraries like 'vulkan-zig' due to potential instability and difficulty maintaining abstraction layers compared to C libraries. Users suggest that 'vulkan-zig' offers better type safety and error handling but acknowledges potential issues with diverging from official documentation.

The discussion also highlights reliability concerns with Vulkan drivers, citing bugs in GTK4's Vulkan renderer and performance issues on Intel GPUs. Despite these challenges, there is a desire to use Vulkan for its wider support and better extension capabilities, particularly for macOS compatibility and improved device coverage.

**Specific Details about 'vulkan-zig'**:
- **Error Handling**: The library provides an error set per function, making it clear what errors can be thrown by each function. For example, the `createInstance` function has specific error types like `OutOfHostMemory`, `OutOfDeviceMemory`, etc.
- **Type Safety**: It uses Zig constructs to make the interface more type safe, such as packed structs instead of flags and enums as handles instead of opaque pointers.

**Maintainer's Concerns**:
- **Stable API**: C libraries have a stable API, which is beneficial for maintaining compatibility with existing resources. Zig changes dynamically, making it harder to keep up with third-party codebases.
- **Abstraction Layers**: Using abstraction layers like 'vulkan-zig' adds complexity and makes it more difficult to refer to official Vulkan documentation and tutorials.

**User's Perspective**:
- **Type Safety and Error Handling**: The library offers better type safety and error handling compared to traditional C bindings, making the code more robust and easier to debug.
- **Minimal Abstraction**: The abstraction provided by 'vulkan-zig' is minimal, similar to glad, and generates bindings directly from vk.xml, ensuring compatibility with future Vulkan versions.

**Driver Reliability Concerns**:
- **GTK4 Bugs**: GTK4's Vulkan renderer has been found to have bugs, requiring workarounds like setting `GSK_RENDERER=gl`.
- **Intel GPU Issues**: Intel GPUs have had performance issues with Vulkan, necessitating workarounds and sometimes reverting to older drivers for better compatibility.

**Future Prospects**:
- **Driver Improvements**: Despite current challenges, there is a belief that Vulkan drivers will improve over time, offering better support and reliability compared to OpenGL drivers.
- **Desire for Vulkan**: The desire to use Vulkan stems from its wider support on platforms like macOS and better extension capabilities, which are crucial for device coverage and compatibility.

## Related Questions
- What are the specific advantages of using Vulkan over OpenGL for Cubyz?
- Why does the maintainer have concerns about maintaining Zig libraries compared to C libraries?
- How does 'vulkan-zig' improve upon traditional Vulkan bindings in terms of type safety and error handling?
- What specific bugs have been encountered with Vulkan drivers, particularly on Intel GPUs?
- What are the potential performance gains from using Vulkan in Cubyz?
- Why is there a desire to use Vulkan for its wider support and better extension capabilities?

*Source: unknown | chunk_id: github_issue_102_discussion*
