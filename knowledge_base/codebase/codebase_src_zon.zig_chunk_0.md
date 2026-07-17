# [hard/codebase_src_zon.zig] - Chunk 0

**Type:** api
**Keywords:** union, ZonElement, initObject, initArray, getAtIndex, getChildAtIndex, clone, joinGetNew, JoinPriority, join, as
**Symbols:** ZonElement, JoinPriority
**Concepts:** union type variants, object/array containers, deep cloning, priority-based joining, allocator assertions, error logging, public API surface

## Summary
Defines the ZonElement union type and its public API for constructing objects/arrays, indexing children, cloning, joining with priority, and casting to concrete types.

## Explanation
The chunk declares a top-level pub const ZonElement union containing variants: int (i128), float (f64), string ([]const u8), stringOwned ([]const u8), bool, null, array (*ListManaged(ZonElement)), and object (*std.StringHashMap(ZonElement)). It provides public factory functions initObject and initArray that allocate the respective container via NeverFailingAllocator. Public accessors getAtIndex (returns T or replacement if type mismatch/out of bounds) and getChildAtIndex (returns .null on non-array). For objects, it exposes get (typed lookup returning ?T), getChild (non-optional wrapper around getChildOrNull), getChildOrNull (?ZonElement), removeChild (?ZonElement), and clone (deep copy using switch over variants; stringOwned is duplicated via allocator.dupe with unreachable catch, arrays are cloned recursively, objects iterate and put cloned values). JoinPriority enum defines preferLeft/Right. The joinGetNew helper returns a new element based on priority: for primitives it clones left or right, for arrays it appends right's items to left's clone, for objects it calls left.clone then invokes the public join method. The join method itself is pub fn; it guards against null right and non-object types (emitting an error log if not in test mode), iterates over right.object, and for each entry either joins with existing key via joinGetNew or clones directly using a closure that supplies left.object.allocator and asserts the allocator cannot fail. The chunk also begins defining pub fn as (cast to ?T) but does not include its body.

## Related Questions
- What variants does the ZonElement union support and how are they represented?
- How do initObject and initArray allocate their containers using NeverFailingAllocator?
- Describe the behavior of getAtIndex when the requested type differs from the stored variant.
- Explain how clone handles each ZonElement variant, especially stringOwned duplication.
- What does joinGetNew return for primitive variants versus array/object variants given a JoinPriority?
- Under what conditions does join emit an error log and why is it guarded by builtin.is_test?
- How does the closure inside join supply allocator information to clone operations?
- What is the purpose of pub fn as and how would it be used for type casting?

*Source: unknown | chunk_id: codebase_src_zon.zig_chunk_0*
