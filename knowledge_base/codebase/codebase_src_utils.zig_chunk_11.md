# [hard/codebase_src_utils.zig] - Chunk 11

**Type:** implementation
**Keywords:** mutex locking, atomic operations, hashing, LRU, set associative
**Symbols:** Cache, Bucket, Bucket.mutex, Bucket.items, Bucket.find, Bucket.add, Bucket.findOrCreate, Bucket.clear, Bucket.foreach
**Concepts:** cache, LRU eviction, set-associative hashing, thread safety

## Summary
Implements a simple set associative cache with LRU replacement strategy.

## Explanation
This chunk defines a generic cache implementation using set-associative hashing and Least Recently Used (LRU) eviction policy. The `Cache` function template creates a type that manages a fixed number of buckets, each containing a fixed number of items. Each bucket is protected by a mutex to ensure thread safety during operations like finding or adding items. The cache supports operations such as finding an item, adding an item, clearing the cache, and iterating over all items. It also tracks cache requests and misses using atomic counters.

## Code Example
```zig
fn find(self: *@This(), compare: anytype) ?*T {
	self.mutex.assertLocked();
	for (self.items, 0..) |item, i| {
		if (compare.equals(item)) {
			if (i != 0) {
				std.mem.copyBackwards(?*T, self.items[1..], self.items[0..i]);
				self.items[0] = item;
			}
			return item;
		}
	}
	return null;
}
```

## Related Questions
- How does the cache handle collisions?
- What is the purpose of the `mutex` in each bucket?
- How are cache requests and misses tracked?
- What happens when an item is added to a full bucket?
- How does the cache ensure thread safety during operations?
- What function is used to initialize new items in the cache?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_11*
