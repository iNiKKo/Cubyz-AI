# [issues/issue_118.md] - Issue #118 discussion

**Type:** review
**Keywords:** source code distribution, Zig compiler, cross-platform compatibility, local library handling, build automation
**Symbols:** Zig, Cubyz, build.zig, build.zig.zon, Makefile
**Concepts:** Build System, Dependency Management, Cross-Platform Development

## Summary
Discussion on shipping Cubyz source code and Zig compiler, focusing on practicality and potential complications.

## Explanation
The discussion revolves around the feasibility of shipping Cubyz's source code along with the Zig compiler. The maintainer notes that this is mostly implemented but requires verification for practical use without additional installations. Users report initial challenges in building Cubyz due to Zig version issues, which were mitigated by scripts like `run.sh` and a Makefile. The maintainer suggests modifying build configurations to handle local libraries more easily, though it remains somewhat cumbersome.

## Related Questions
- How can the Zig build system be configured to handle local libraries more seamlessly?
- What are potential bandwidth savings from shipping source code with a pre-packaged compiler?
- Are there any known issues with using different versions of Zig for Cubyz development?
- How can users isolate and resolve Zig compilation crashes during Cubyz builds?
- Can the `build.zig` file be modified to include custom steps like packaging libraries?
- What are the potential performance implications of compiling Cubyz on user machines?

*Source: unknown | chunk_id: github_issue_118_discussion*
