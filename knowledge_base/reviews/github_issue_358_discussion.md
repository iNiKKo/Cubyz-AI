# [issues/issue_358.md] - Issue #358 discussion

**Type:** review
**Keywords:** Wayland support, GLFW, custom build script, upstream Zig library, system-installed wayland-scanner, xkbcommon headers, security vulnerability, dependency bloat, hard-fork, Zig maintenance
**Symbols:** GLFW, Wayland, wayland-scanner, xkbcommon
**Concepts:** Dependency management, Security considerations, Build system integration

## Summary
Discussion on supporting Wayland in Cubyz by exploring various approaches to integrate GLFW with Wayland without adding excessive bloat or introducing security vulnerabilities.

## Explanation
Discussion on supporting Wayland in Cubyz by exploring various approaches to integrate GLFW with Wayland without adding excessive bloat or introducing security vulnerabilities. The initial approach using a custom build script was deemed too complex and bloated, as it required compiling wayland-scanner and generating code for GLFW with Wayland support while also handling xkbcommon headers manually. Other options include using upstream Zig libraries (which introduce an extra dependency), leveraging system-installed wayland-scanner (with concerns about xkbcommon headers handling), or forking the necessary projects. There is also mention of security concerns with adding middleman dependencies and the need for ongoing maintenance, especially in the context of Zig's upcoming 1.0 release.

## Related Questions
- What are the potential security risks of adding middleman dependencies for Wayland support?
- How can we handle xkbcommon headers without introducing additional complexity?
- What is the current status of integrating GLFW with Wayland in Cubyz?
- Why was the custom build script approach deemed too complex?
- Are there any Zig libraries that could simplify the integration of Wayland and GLFW?
- What are the advantages and disadvantages of forking necessary projects for Wayland support?

*Source: unknown | chunk_id: github_issue_358_discussion*
