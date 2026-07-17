# [hard/codebase_src_utils_heap.zig] - Chunk 2

**Type:** api
**Keywords:** never failing allocator, vtable alloc, raw resize, aligned alloc, sentinel slice, catch unreachable, allocator interface, memory alignment, alloc with options, create destroy
**Symbols:** NeverFailingAllocator, NeverFailingAllocator.allocator, NeverFailingAllocator.IAssertThatTheProvidedAllocatorCantFail, NeverFailingAllocator.Alignment, NeverFailingAllocator.rawAlloc, NeverFailingAllocator.rawResize, NeverFailingAllocator.rawRemap, NeverFailingAllocator.rawFree, NeverFailingAllocator.create, NeverFailingAllocator.destroy, NeverFailingAllocator.alloc, NeverFailingAllocator.allocWithOptions, NeverFailingAllocator.AllocWithOptionsPayload, NeverFailingAllocator.allocSentinel, NeverFailingAllocator.alignedAlloc
**Concepts:** allocator interface, vtable delegation, sentinel allocation, alignment handling, error suppression via unreachable

## Summary
This chunk defines the `NeverFailingAllocator` interface and its associated helper types, providing a set of public methods that delegate to an underlying allocator's vtable while guaranteeing no failures via `catch unreachable`. It also includes internal inline wrappers for raw operations (`rawAlloc`, `rawResize`, `rawRemap`, `rawFree`) intended solely for use within the implementation of other allocators.

## Explanation
The chunk declares a public const struct named NeverFailingAllocator containing an allocator field and an IAssertThatTheProvidedAllocatorCantFail void field. It defines an inline type Alignment as std.mem.Alignment, then provides several pub inline functions: rawAlloc, rawResize, rawRemap, and rawFree, each forwarding to the corresponding vtable method on self.allocator.ptr with optional ret_addr handling. The create function wraps self.allocator.create(T) with a catch unreachable; destroy simply forwards to self.allocator.destroy(ptr). alloc wraps self.allocator.alloc(T,n) with catch unreachable; allocWithOptions returns an AllocWithOptionsPayload type constructed from self.allocator.allocWithOptions, also catching unreachable; the payload type is defined inline as either a sentinel-aligned slice or a plain aligned slice depending on whether a sentinel is provided. allocSentinel wraps self.allocator.allocSentinel(Elem,n,sentinel) with catch unreachable. alignedAlloc wraps self.allocator.alignedAlloc(T,alignment,n) with catch unreachable and computes the resulting alignment using alignment.toByteUnits() if present else @alignOf(T). The chunk also defines a private inline function allocAdvancedWithRetAddr (signature truncated in the provided snippet), which is not public and therefore excluded from symbols.

## Related Questions
- What is the purpose of the IAssertThatTheProvidedAllocatorCantFail field in NeverFailingAllocator?
- How does rawAlloc delegate to the underlying allocator's vtable?
- Under what conditions does allocWithOptions return an AllocWithOptionsPayload with a sentinel versus without one?
- Why are all public methods on NeverFailingAllocator wrapped with catch unreachable?
- What is the exact signature of the private function allocAdvancedWithRetAddr and why is it not exposed publicly?
- How does alignedAlloc compute its resulting alignment when an optional alignment parameter is provided versus omitted?
- Does create or destroy ever propagate errors from the underlying allocator in this interface?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_2*
