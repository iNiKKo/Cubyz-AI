# [issues/issue_2960.md] - Issue #2960 discussion

**Type:** review
**Keywords:** VK_KHR_buffer_device_address, GPU pointers, SSBO size limit, performance enhancement, memory management
**Concepts:** GPU memory management, Shader Storage Buffers, Extension integration

## Summary
Discussion about integrating the VK_KHR_buffer_device_address extension for improved GPU pointer management and potential SSBO size increase.

## Explanation
The maintainer is discussing the integration of the VK_KHR_buffer_device_address extension, which allows direct pointers on the GPU without binding operations. This change aims to simplify setup processes and potentially overcome the current 4 GiB limit for Shader Storage Buffer Objects (SSBOs). The primary motivation is to enhance performance and flexibility in handling larger data sets directly on the GPU.

## Related Questions
- What are the potential benefits of using VK_KHR_buffer_device_address in Cubyz?
- How does this extension impact the current SSBO size limitations?
- Can you explain the setup process for integrating VK_KHR_buffer_device_address in Cubyz?
- What are the expected performance improvements with this extension?
- Are there any compatibility concerns with existing GPU hardware when using this extension?
- How will this change affect memory management within Cubyz?

*Source: unknown | chunk_id: github_issue_2960_discussion*
