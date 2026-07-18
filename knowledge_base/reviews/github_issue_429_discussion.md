# [issues/issue_429.md] - Issue #429 discussion

**Type:** review
**Keywords:** GLSL 4.60, MESA_GLSL_VERSION_OVERRIDE, frame time, accuracy, noisy data, running average
**Concepts:** GLSL version support, shader compilation, performance measurement

## Summary
Discusses issues with GLSL version support on Mac and potential performance impacts.

## Explanation
The discussion revolves around a problem where the latest Mac build fails to compile shaders due to unsupported GLSL 4.60 version. The user finds a workaround by setting `MESA_GLSL_VERSION_OVERRIDE`, but this introduces a slight increase in frame time from 150 to 160. The maintainer suggests making accurate measurements by staying at the spawn location and not rotating the camera. The user expresses difficulty with noisy data and proposes adding a global option for running average measurements to the frame-time graph.

## Related Questions
- What is the impact of using `MESA_GLSL_VERSION_OVERRIDE` on frame time?
- How can accurate measurements be made for shader performance?
- Why is GLSL 4.60 not supported on Mac builds?
- What are the potential solutions to handle noisy data in performance measurements?
- How can a running average be added to the frame-time graph?
- Are there any other workarounds for unsupported GLSL versions?

*Source: unknown | chunk_id: github_issue_429_discussion*
