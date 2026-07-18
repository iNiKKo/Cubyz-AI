# [issues/issue_1366.md] - Issue #1366 discussion

**Type:** other
**Keywords:** OpenGL warning, vertex attribute array pointer, buffer usage, segmentation fault, Cubyz, Zig
**Symbols:** 0x7f506a548f69, libGLdispatch.so.0, finalize, receive, protocolReceive, run, entryFn, libc.so.6
**Concepts:** OpenGL, vertex attribute array, buffer object, usage hint, segmentation fault, Cubyz game engine, Zig programming language

## Summary
OpenGL warning about vertex attribute array pointer and potential segmentation fault in Cubyz game engine

## Explanation
The user is experiencing an OpenGL usage warning related to a generic vertex attribute array using a small value (0x(nil)) as a pointer, which might be intended as an offset into a buffer object. Additionally, there's a buffer usage warning suggesting that the usage hint for a specific buffer object is inconsistent with its actual usage pattern. The user also encountered a segmentation fault at address 0xa38, likely due to improper handling of memory or resources in the Cubyz game engine. The maintainer suggests deleting lines 464-466 in `src/items.zig` as a temporary workaround and indicates that the issue should remain open until a fix is added to the master branch.

## Code Example
```zig
diff
- if(self.texture) |texture| {
- texture.deinit();
- }

```

## Related Questions
- OpenGL vertex attribute array warning
- buffer object usage hint inconsistency
- Cubyz segmentation fault fix
- Zig memory management issues
- OpenGL buffer operations in Cubyz
- vertex attribute array pointer offset

*Source: unknown | chunk_id: github_issue_1366_discussion*
