# [hard/codebase_src_graphics_vulkan.zig] - Chunk 3

**Type:** implementation
**Keywords:** swap chain, image views, Vulkan initialization, resource cleanup, format selection, present mode, extent calculation
**Symbols:** SwapChain, SwapChain.swapChain, SwapChain.images, SwapChain.imageViews, SwapChain.imageFormat, SwapChain.extent, SwapChain.SupportDetails, SwapChain.SupportDetails.capabilities, SwapChain.SupportDetails.formats, SwapChain.SupportDetails.presentModes, SwapChain.SupportDetails.init, SwapChain.SupportDetails.deinit, SwapChain.SupportDetails.chooseFormat, SwapChain.SupportDetails.chooseSwapPresentMode, SwapChain.SupportDetails.chooseSwapExtent, SwapChain.createImageView, SwapChain.init, SwapChain.deinit
**Concepts:** Vulkan swap chain management, image view creation, device capabilities query

## Summary
The SwapChain struct manages the creation and destruction of a Vulkan swap chain, including image views.

## Explanation
The SwapChain struct manages the creation and destruction of a Vulkan swap chain, including image views. It includes methods to initialize and deinitialize the swap chain, choose appropriate formats, present modes, and extents based on device capabilities. The init method sets up the swap chain by querying supported formats and present modes, selecting optimal values, and creating image views for each swap chain image. The deinit method cleans up resources by destroying image views and the swap chain itself.

The SupportDetails struct contains methods to query device capabilities, choose a suitable surface format, select a present mode, and determine the swap extent. The chooseFormat method specifically looks for the VK_FORMAT_B8G8R8A8_SRGB format with VK_COLOR_SPACE_SRGB_NONLINEAR_KHR color space. The chooseSwapPresentMode method currently defaults to VK_PRESENT_MODE_FIFO_KHR. The chooseSwapExtent method calculates the extent based on the current window size and device capabilities.

The createImageView function creates an image view for a given Vulkan image, specifying the format and subresource range. The init method initializes the swap chain by creating images and views, while the deinit method cleans up all allocated resources.

## Code Example
```zig
fn chooseFormat(self: SupportDetails) c.VkSurfaceFormatKHR {
	for (self.formats) |format| {
		if (format.format == c.VK_FORMAT_B8G8R8A8_SRGB and format.colorSpace == c.VK_COLOR_SPACE_SRGB_NONLINEAR_KHR) {
			return format;
		}
	}
	@panic("Couldn't find swapchain format BGRA8 SRGB");
}
```

## Related Questions
- How does the SwapChain struct initialize a Vulkan swap chain?
- What methods are available in the SupportDetails struct?
- How is the image format chosen for the swap chain?
- What steps are involved in creating an image view?
- How does the SwapChain handle resource cleanup during deinitialization?
- What conditions determine the sharing mode of the swap chain images?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_3*
