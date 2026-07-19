# [src/graphics/vulkan.zig] - PR #1620 review diff

**Type:** review
**Keywords:** Vulkan, VkResultEnum, checkResult, VK_INCOMPLETE, vkEnumerateInstanceLayerProperties, allocEnumerationGeneric, NeverFailingAllocator
**Symbols:** VkResultEnum, checkResult, checkResultIfAvailable, allocEnumerationGeneric, enumerateInstanceLayerProperties
**Concepts:** Error Handling, API Enumeration, Vulkan API

## Summary
The code introduces a new file `vulkan.zig` with Vulkan error handling functions and an enumeration function for instance layer properties.

## Explanation
The added code defines an enum `VkResultEnum` to map Vulkan result codes to human-readable strings. The enum includes the following values:

- VK_SUCCESS = 0
- VK_NOT_READY = 1
- VK_TIMEOUT = 2
- VK_EVENT_SET = 3
- VK_EVENT_RESET = 4
- VK_INCOMPLETE = 5
- VK_ERROR_OUT_OF_HOST_MEMORY = -1
- VK_ERROR_OUT_OF_DEVICE_MEMORY = -2
- VK_ERROR_INITIALIZATION_FAILED = -3
- VK_ERROR_DEVICE_LOST = -4
- VK_ERROR_MEMORY_MAP_FAILED = -5
- VK_ERROR_LAYER_NOT_PRESENT = -6
- VK_ERROR_EXTENSION_NOT_PRESENT = -7
- VK_ERROR_FEATURE_NOT_PRESENT = -8
- VK_ERROR_INCOMPATIBLE_DRIVER = -9
- VK_ERROR_TOO_MANY_OBJECTS = -10
- VK_ERROR_FORMAT_NOT_SUPPORTED = -11
- VK_ERROR_FRAGMENTED_POOL = -12
- VK_ERROR_UNKNOWN = -13
- VK_ERROR_OUT_OF_POOL_MEMORY = -1000069000
- VK_ERROR_INVALID_EXTERNAL_HANDLE = -1000072003
- VK_ERROR_FRAGMENTATION = -1000161000
- VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS = -1000257000
- VK_PIPELINE_COMPILE_REQUIRED = 1000297000
- VK_ERROR_NOT_PERMITTED = -1000174001
- VK_ERROR_SURFACE_LOST_KHR = -1000000000
- VK_ERROR_NATIVE_WINDOW_IN_USE_KHR = -1000000001
- VK_SUBOPTIMAL_KHR = 1000001003
- VK_ERROR_OUT_OF_DATE_KHR = -1000001004
- VK_ERROR_INCOMPATIBLE_DISPLAY_KHR = -1000003001
- VK_ERROR_VALIDATION_FAILED_EXT = -1000011001
- VK_ERROR_INVALID_SHADER_NV = -1000012000
- VK_ERROR_IMAGE_USAGE_NOT_SUPPORTED_KHR = -1000023000
- VK_ERROR_VIDEO_PICTURE_LAYOUT_NOT_SUPPORTED_KHR = -1000023001
- VK_ERROR_VIDEO_PROFILE_OPERATION_NOT_SUPPORTED_KHR = -1000023002
- VK_ERROR_VIDEO_PROFILE_FORMAT_NOT_SUPPORTED_KHR = -1000023003
- VK_ERROR_VIDEO_PROFILE_CODEC_NOT_SUPPORTED_KHR = -1000023004
- VK_ERROR_VIDEO_STD_VERSION_NOT_SUPPORTED_KHR = -1000023005
- VK_ERROR_INVALID_DRM_FORMAT_MODIFIER_PLANE_LAYOUT_EXT = -1000158000
- VK_ERROR_FULL_SCREEN_EXCLUSIVE_MODE_LOST_EXT = -1000255000
- VK_THREAD_IDLE_KHR = 1000268000
- VK_THREAD_DONE_KHR = 1000268001
- VK_OPERATION_DEFERRED_KHR = 1000268002
- VK_OPERATION_NOT_DEFERRED_KHR = 1000268003
- VK_ERROR_INVALID_VIDEO_STD_PARAMETERS_KHR = -1000299000
- VK_ERROR_COMPRESSION_EXHAUSTED_EXT = -1000338000
- VK_PIPELINE_BINARY_MISSING_KHR = 1000483000
- VK_ERROR_NOT_ENOUGH_SPACE_KHR = -1000483000
- VK_ERROR_INCOMPATIBLE_SHADER_BINARY_EXT = 1000482000
- VK_RESULT_MAX_ENUM = 2147483647

The `checkResult` function logs errors based on the result code. If the result is `VK_SUCCESS`, it returns without logging anything. Otherwise, it logs an error message with the corresponding human-readable string from `VkResultEnum`. The `checkResultIfAvailable` function checks if the type of the result is not `void` and calls `checkResult` if it is not.

The `allocEnumerationGeneric` function handles Vulkan API calls that require multiple enumeration steps. It first calls the function with a null pointer for the output array to get the count of available properties, then allocates memory using `NeverFailingAllocator`, and finally calls the function again to fill the allocated memory with the properties.

The reviewer points out a critical architectural issue: `vkEnumerateInstanceLayerProperties` can return `VK_INCOMPLETE` as a success status, which would be incorrectly treated as an error by the current implementation.

## Related Questions
-  How does the `checkResult` function handle unknown Vulkan error codes?
-  What is the purpose of the `allocEnumerationGeneric` function in the context of Vulkan API calls?
-  Why is `VK_INCOMPLETE` considered a success status for `vkEnumerateInstanceLayerProperties`?
-  How does the code ensure that memory allocation failures are handled correctly?
-  What changes need to be made to handle `VK_INCOMPLETE` as a valid result in `checkResult`?
-  How does the use of `NeverFailingAllocator` impact error handling in Vulkan operations?

*Source: unknown | chunk_id: github_pr_1620_comment_2264999231*
