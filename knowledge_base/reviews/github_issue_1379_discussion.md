# [issues/issue_1379.md] - Issue #1379 discussion

**Type:** review
**Keywords:** glslang, CI, shader, compilation, SPIRV, installation, binaries, storage, validation
**Symbols:** glslang, SPIRV
**Concepts:** Continuous Integration (CI), shader compilation, binary management

## Summary
Discussion on compiling shaders in CI using glslang, focusing on installation method and handling of SPIRV binaries.

## Explanation
Discussion on compiling shaders in CI using glslang, focusing on installation method and handling of SPIRV binaries. The maintainers explore various aspects such as installing glslang via `sudo apt install` on the CI server, discarding the resulting SPIRV binaries after validation to avoid unnecessary storage, and ensuring seamless integration into the CI pipeline without storing compiled binaries.

## Related Questions
- How is glslang installed on the CI server?
- What are the potential methods for handling SPIRV binaries after compilation?
- Is there a specific reason to discard the SPIRV binaries instead of storing them?
- How does this shader compilation step fit into the overall CI pipeline?

*Source: unknown | chunk_id: github_issue_1379_discussion*
