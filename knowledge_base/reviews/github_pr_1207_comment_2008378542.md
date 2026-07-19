# [src/structure_building_blocks.zig] - PR #1207 review diff

**Type:** review
**Keywords:** structure building blocks, blueprints, caching, rotation handling, thread safety, memory optimization, StringHashMap, BpRotKey, BpRotVal, reference counting
**Symbols:** std, main, terrain, ZonElement, Blueprint, List, AliasTable, Neighbor, Block, parseBlock, Degrees, hashInt, NeverFailingAllocator, arena, arena_allocator, structureCache, blueprintCache, BpRotKey, HashContext, BpRotVal, init, incRef, decRef, deinit, rotatedBlueprintCache
**Concepts:** thread safety, memory management, caching, hash maps, blueprint rotation

## Summary
A new Zig file `structure_building_blocks.zig` is introduced, defining structures and functions for managing structure building blocks and blueprints. It includes caches for structures and blueprints, with a focus on handling rotations efficiently.

## Explanation
The code introduces a new module for handling structure building blocks and their blueprints in the Cubyz game engine. It uses `std.StringHashMapUnmanaged` to cache structures and blueprints, optimizing memory usage by avoiding repeated allocations. The `BpRotKey` struct is used as a key for caching rotated blueprints, combining an ID and rotation angle. The `HashContext` in the `BpRotKey` struct provides hash and equality functions for the keys, specifically using `std.hash.Wyhash.hash` to combine the hash of the rotation with the ID's hash, and `std.meta.eql` to compare the IDs along with checking if the rotations are equal.

The `BpRotVal` struct holds the blueprint data along with reference counting and a mutex for thread safety. The `init` method initializes a new instance of `BpRotVal`, setting up the allocator, blueprint, info, reference count, and mutex. The `incRef` method increments the reference count, ensuring that the object is not deallocated prematurely. The `decRef` method decrements the reference count, and if it reaches zero, the `deinit` method is called to properly deinitialize the blueprint and info.

The reviewer suggests using a `StringHashMap([4]BpRotVal)` to cache all four rotations of each blueprint, which could simplify the logic and improve performance by reducing the number of hash map lookups.

## Related Questions
- How does the `BpRotVal` struct handle reference counting and deallocation?
- What is the purpose of the `HashContext` in the `BpRotKey` struct?
- Why is a mutex used in the `BpRotVal` struct methods?
- How does the code ensure that blueprints are not leaked in memory?
- What is the potential impact of caching all four rotations of each blueprint?
- How does the use of `NeverFailingAllocator` affect memory management in this module?

*Source: unknown | chunk_id: github_pr_1207_comment_2008378542*
