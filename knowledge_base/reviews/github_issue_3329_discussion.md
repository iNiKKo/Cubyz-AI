# [issues/issue_3329.md] - Issue #3329 discussion

**Type:** review
**Keywords:** zig compiler, armv7l, 32 bit processors, cross compiling, Kindle Paperwhite
**Concepts:** cross-compilation, architecture compatibility

## Summary
The issue discusses Cubyz's inability to find the Zig compiler for armv7l architecture, which is commonly found in devices like the Kindle Paperwhite. The maintainer advises that Cubyz is not designed for 32-bit processors and suggests cross-compiling as a potential solution.

## Explanation
The user reports that Cubyz cannot locate the Zig compiler suitable for the armv7l processor, which can be verified by running `uname -m` returning `armv7l`. The maintainer advises that Cubyz is not designed for 32-bit processors and suggests cross-compiling as a potential solution. This approach may help mitigate issues encountered when attempting to compile Cubyz on such architectures.

## Related Questions
- What is the recommended approach for cross-compiling Cubyz for armv7l?
- Are there any known issues with running Cubyz on 32-bit processors?
- How can one verify if Zig supports cross-compilation to armv7l?
- What are the potential challenges in compiling Cubyz for armv7l?
- Is there a specific version of Zig required for armv7l compatibility?

*Source: unknown | chunk_id: github_issue_3329_discussion*
