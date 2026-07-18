# [issues/issue_1690.md] - Issue #1690 discussion

**Type:** review
**Keywords:** rendering performance, older Intel iGPUs, 60 fps, low resolution scale, low leaves quality
**Concepts:** performance, rendering, frame rate

## Summary
The rendering performance on older Intel iGPUs is slow, failing to consistently reach 60 fps even at low settings.

## Explanation
The issue report indicates that the rendering performance is suboptimal on older Intel integrated GPUs (iGPUs), with frame rates not improving significantly despite reducing rendered chunks and resolution scale. The maintainer tested the scenario with low resolution and leaf quality settings and was able to achieve 60 fps, suggesting that further optimization might be limited or challenging.

## Related Questions
- What specific rendering settings were used to achieve 60 fps on the older Intel iGPU?
- Are there any known limitations or constraints with older Intel iGPUs that could affect performance?
- How can further investigation be conducted to identify the bottleneck in rendering performance?
- Is there a possibility of implementing software optimizations to improve rendering performance on older GPUs?
- What are the potential trade-offs between visual quality and frame rate on low-end hardware?
- Are there any plans to provide alternative rendering paths for lower-end GPUs to enhance performance?

*Source: unknown | chunk_id: github_issue_1690_discussion*
