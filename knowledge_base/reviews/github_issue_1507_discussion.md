# [issues/issue_1507.md] - Issue #1507 discussion

**Type:** review
**Keywords:** modding, comptime, DLL, WASM, JS, lua, API, ABI, security, performance, maintenance, registry, mod pack, precompiled executables
**Symbols:** comptime modding, runtime (DLL) modding, runtime (WASM/JS/lua) modding
**Concepts:** modding API, ABI compatibility, security, performance, maintenance

## Summary
The discussion focuses on selecting a modding approach for Cubyz among no native modding, comptime modding, runtime (DLL) modding, and runtime (WASM/JS/lua) modding. Comptime modding is chosen due to its ease of maintenance and performance benefits, with plans for implementing a registry system.

## Explanation
The maintainers discuss various approaches to implement modding in Cubyz: no native modding, comptime modding, runtime (DLL) modding, and runtime (WASM/JS/lua) modding. No native modding avoids maintaining an API but limits third-party contributions due to the difficulty of keeping up with base game changes. Comptime modding leverages existing functions without requiring a dedicated API, offering fast execution and ease of maintenance. Runtime (DLL) modding requires maintaining a C ABI-compatible API and can be insecure. WASM/JS/LUA modding provides security through controlled access but incurs performance penalties due to interaction overhead and non-native runtime constraints.

The maintainers lean towards comptime modding because it balances ease of maintenance and performance benefits. They also discuss the potential for a registry system that would manage mod dependencies, similar to package managers, reducing overhead when joining servers with compatible mods. This approach allows users to add third-party registries with modifications following a defined protocol based on zon metadata format.

The maintainers consider comptime modding as the best choice due to its simplicity and performance benefits compared to other options requiring more development time.

## Related Questions
- What are the potential security risks associated with comptime modding?
- How does runtime (DLL) modding impact ABI stability?
- Can WASM/JS/lua modding be integrated into Cubyz without significant performance overhead?
- What are the advantages and disadvantages of using a registry system for managing mods?
- How can compilation times for comptime modding be optimized in the future?
- What challenges arise from maintaining a stable modding API?

*Source: unknown | chunk_id: github_issue_1507_discussion*
