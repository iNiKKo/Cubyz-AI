# [issues/issue_1379.md] - Issue #1379 discussion

**Type:** review
**Keywords:** glslang, CI, shader, compilation, SPIRV, installation, binaries, storage, validation
**Symbols:** glslang, SPIRV
**Concepts:** Continuous Integration (CI), shader compilation, binary management

## Summary
Discussion on compiling shaders in CI using glslang, focusing on installation method and handling of SPIRV binaries.

## Explanation
The discussion revolves around the feasibility of compiling shaders in the Continuous Integration (CI) environment using the glslang tool. The maintainers explore various aspects such as the installation method for glslang on the CI server, the potential methods for storing or discarding the resulting SPIRV binaries, and the overall purpose of this compilation step. The primary concern is to ensure that the shader compilation process is integrated seamlessly into the CI pipeline without unnecessary storage of compiled binaries.

## Related Questions
- How is glslang installed on the CI server?
- What are the potential methods for handling SPIRV binaries after compilation?
- Is there a specific reason to discard the SPIRV binaries instead of storing them?
- How does this shader compilation step fit into the overall CI pipeline?
- Are there any backward compatibility concerns with integrating glslang in the CI process?
- What are the potential performance implications of compiling shaders in the CI environment?

*Source: unknown | chunk_id: github_issue_1379_discussion*
