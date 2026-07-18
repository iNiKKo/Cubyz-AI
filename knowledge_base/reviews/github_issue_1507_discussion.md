# [issues/issue_1507.md] - Issue #1507 discussion

**Type:** review
**Keywords:** modding, comptime, DLL, WASM, JS, lua, API, ABI, security, performance, maintenance, registry, mod pack, precompiled executables
**Symbols:** comptime modding, runtime (DLL) modding, runtime (WASM/JS/lua) modding
**Concepts:** modding API, ABI compatibility, security, performance, maintenance

## Summary
The discussion revolves around deciding on a modding approach for Cubyz. The options include no native modding, comptime modding, runtime (DLL) modding, and runtime (WASM/JS/lua) modding. The maintainers lean towards comptime modding due to its ease of maintenance and performance benefits.

## Explanation
The discussion centers on the decision-making process for implementing a modding system in Cubyz. The team evaluates several options, including no native modding, which avoids maintaining a stable API but limits third-party contributions; comptime modding, which leverages existing functions without requiring a dedicated API and offers fast execution; runtime (DLL) modding, which requires maintaining a C ABI-compatible modding API but can be insecure; and runtime (WASM/JS/lua) modding, which provides security through controlled access to memory and functions but incurs performance penalties. The maintainers ultimately decide on comptime modding due to its balance of ease of maintenance and performance, with the potential for a registry system to manage mod dependencies.

## Related Questions
- What are the potential security risks associated with comptime modding?
- How does runtime (DLL) modding impact ABI stability?
- Can WASM/JS/lua modding be integrated into Cubyz without significant performance overhead?
- What are the advantages and disadvantages of using a registry system for managing mods?
- How can the compilation times for comptime modding be optimized in the future?
- What are the potential challenges in maintaining a stable modding API?

*Source: unknown | chunk_id: github_issue_1507_discussion*
