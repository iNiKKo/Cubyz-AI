# [hard/codebase_src_utils_heap.zig] - Chunk 3

**Type:** documentation
**Keywords:** allocator, unreachable, memory management, error-free operations, arena allocator
**Symbols:** NeverFailingAllocator, NeverFailingAllocator.allocator, NeverFailingAllocator.Alignment, NeverFailingAllocator.math, NeverFailingAllocator.rawAlloc, NeverFailingAllocator.rawResize, NeverFailingAllocator.rawRemap, NeverFailingAllocator.rawFree, NeverFailingAllocator.create, NeverFailingAllocator.destroy, NeverFailingAllocator.alloc, NeverFailingAllocator.allocWithOptions, NeverFailingAllocator.allocWithOptionsRetAddr, NeverFailingAllocator.AllocWithOptionsPayload, NeverFailingAllocator.allocSentinel, NeverFailingAllocator.alignedAlloc, NeverFailingAllocator.allocAdvancedWithRetAddr, NeverFailingAllocator.allocWithSizeAndAlignment, NeverFailingAllocator.allocBytesWithAlignment, NeverFailingAllocator.resize, NeverFailingAllocator.remap, NeverFailingAllocator.realloc, NeverFailingAllocator.reallocAdvanced, NeverFailingAllocator.free, NeverFailingAllocator.dupe, NeverFailingAllocator.dupeZ, NeverFailingAllocator.createArena, NeverFailingAllocator.destroyArena
**Concepts:** Memory Allocation, Error Handling, Wrappers, Allocators

## Summary
Defines a wrapper for an allocator that ensures all operations never fail, using `unreachable` to handle any errors.

## Explanation
The `NeverFailingAllocator` struct wraps another allocator and provides methods that call the underlying allocator's functions. If any operation fails (throws an error), it immediately calls `unreachable`, indicating a programming error. The wrapper includes methods for creating, destroying, allocating, resizing, remapping, reallocating, freeing memory, duplicating arrays, and managing arenas. It ensures that all operations are guaranteed to succeed, simplifying the code that uses this allocator by removing the need for error handling.

### Methods
- **rawAlloc**: Allocates raw memory with a specified length, alignment, and return address. Returns a pointer to the allocated memory or null if allocation fails.
  ```zig
  pub inline fn rawAlloc(a: NeverFailingAllocator, len: usize, alignment: Alignment, ret_addr: usize) ?[*]u8 {
      return a.allocator.vtable.alloc(a.allocator.ptr, len, alignment, ret_addr);
  }
  ```
- **rawResize**: Resizes the specified memory block to a new length. Returns true if resizing is successful, false otherwise.
  ```zig
  pub inline fn rawResize(a: NeverFailingAllocator, allocation: anytype, new_len: usize) bool {
      return self.allocator.resize(allocation, new_len);
  }
  ```
- **rawRemap**: Remaps the specified memory block to a new size, allowing relocation. Returns a pointer to the remapped memory or null if remapping fails.
  ```zig
  pub inline fn rawRemap(a: NeverFailingAllocator, allocation: anytype, new_len: usize) t: {
      const Slice = @typeInfo(@TypeOf(allocation)).pointer;
      break :t ?[]align(Slice.alignment) Slice.child;
  } {
      return self.allocator.remap(allocation, new_len);
  }
  ```
- **rawFree**: Frees the specified memory block.
  ```zig
  pub inline fn rawFree(a: NeverFailingAllocator, memory: anytype) void {
      self.allocator.free(memory);
  }
  ```
- **create**: Creates a new instance of a type using the allocator and returns a pointer to it.
  ```zig
  pub fn create(self: NeverFailingAllocator, comptime T: type) *T {
      const ptr = self.allocator.alloc(T) catch unreachable;
      return @ptrCast(@alignCast(ptr));
  }
  ```
- **destroy**: Destroys an instance of a type by calling its destructor and freeing the memory.
  ```zig
  pub fn destroy(self: NeverFailingAllocator, ptr: anytype) void {
      const T = @TypeOf(ptr);
      ptr.deinit();
      self.allocator.free(@ptrCast(@alignCast(ptr)));
  }
  ```
- **alloc**: Allocates an array of a specified type with the given length.
  ```zig
  pub fn alloc(self: NeverFailingAllocator, comptime T: type, n: usize) []T {
      return self.allocator.alloc(T, n) catch unreachable;
  }
  ```
- **allocWithOptions**: Allocates an array of a specified type with the given length and options.
  ```zig
  pub fn allocWithOptions(self: NeverFailingAllocator, comptime T: type, n: usize, options: Allocator.AllocOptions) []T {
      return self.allocator.alloc(T, n, options) catch unreachable;
  }
  ```
- **allocWithOptionsRetAddr**: Allocates an array of a specified type with the given length, options, and return address.
  ```zig
  pub fn allocWithOptionsRetAddr(self: NeverFailingAllocator, comptime T: type, n: usize, options: Allocator.AllocOptions, ret_addr: usize) []T {
      return self.allocator.alloc(T, n, options, ret_addr) catch unreachable;
  }
  ```
- **allocSentinel**: Allocates an array of a specified type with the given length and sentinel value.
  ```zig
  pub fn allocSentinel(self: NeverFailingAllocator, comptime T: type, n: usize, sentinel: T) []T {
      return self.allocator.alloc(T, n, .{ .sentinel = sentinel }) catch unreachable;
  }
  ```
- **alignedAlloc**: Allocates an array of a specified type with the given length and alignment.
  ```zig
  pub fn alignedAlloc(self: NeverFailingAllocator, comptime T: type, alignment: u29, n: usize) []align(alignment) T {
      return self.allocator.alignedAlloc(T, alignment, n) catch unreachable;
  }
  ```
- **allocAdvancedWithRetAddr**: Allocates an array of a specified type with the given length and return address.
  ```zig
  pub fn allocAdvancedWithRetAddr(self: NeverFailingAllocator, comptime T: type, n: usize, ret_addr: usize) []T {
      return self.allocator.alloc(T, n, .{}, ret_addr) catch unreachable;
  }
  ```
- **allocWithSizeAndAlignment**: Allocates a block of raw memory with the given size and alignment.
  ```zig
  pub fn allocWithSizeAndAlignment(self: NeverFailingAllocator, comptime size: usize, comptime alignment: u29, n: usize, return_address: usize) [*]align(alignment) u8 {
      return self.allocator.allocWithSizeAndAlignment(size, alignment, n, return_address) catch unreachable;
  }
  ```
- **allocBytesWithAlignment**: Allocates a block of raw memory with the given byte count and alignment.
  ```zig
  pub fn allocBytesWithAlignment(self: NeverFailingAllocator, comptime alignment: u29, byte_count: usize, return_address: usize) [*]align(alignment) u8 {
      return self.allocator.allocBytesWithAlignment(byte_count, alignment, return_address) catch unreachable;
  }
  ```
- **resize**: Resizes an existing allocation to a new size.
  ```zig
  pub fn resize(self: NeverFailingAllocator, old_mem: anytype, new_n: usize) t: {
      const Slice = @typeInfo(@TypeOf(old_mem)).pointer;
      break :t []align(Slice.alignment orelse @alignOf(Slice.child)) Slice.child;
  } {
      return self.allocator.realloc(old_mem, new_n) catch unreachable;
  }
  ```
- **remap**: Remaps an existing allocation to a new size, allowing relocation.
  ```zig
  pub fn remap(self: NeverFailingAllocator, old_mem: anytype, new_n: usize) t: {
      const Slice = @typeInfo(@TypeOf(old_mem)).pointer;
      break :t ?[]align(Slice.alignment) Slice.child;
  } {
      return self.allocator.remap(old_mem, new_n) catch unreachable;
  }
  ```
- **realloc**: Resizes an existing allocation to a new size, which can be larger, smaller, or the same size as the old memory allocation.
  ```zig
  pub fn realloc(self: NeverFailingAllocator, old_mem: anytype, new_n: usize) t: {
      const Slice = @typeInfo(@TypeOf(old_mem)).pointer;
      break :t []align(Slice.alignment orelse @alignOf(Slice.child)) Slice.child;
  } {
      return self.allocator.realloc(old_mem, new_n) catch unreachable;
  }
  ```
- **reallocAdvanced**: Resizes an existing allocation to a new size with a specified return address.
  ```zig
  pub fn reallocAdvanced(self: NeverFailingAllocator, old_mem: anytype, new_n: usize, return_address: usize) t: {
      const Slice = @typeInfo(@TypeOf(old_mem)).pointer;
      break :t []align(Slice.alignment) Slice.child;
  } {
      return self.allocator.reallocAdvanced(old_mem, new_n, return_address) catch unreachable;
  }
  ```
- **free**: Frees an existing allocation.
  ```zig
  pub fn free(self: NeverFailingAllocator, memory: anytype) void {
      self.allocator.free(memory);
  }
  ```
- **dupe**: Copies a slice to newly allocated memory.
  ```zig
  pub fn dupe(self: NeverFailingAllocator, comptime T: type, m: []const T) []T {
      return self.allocator.dupe(T, m) catch unreachable;
  }
  ```
- **dupeZ**: Copies a slice to newly allocated memory with a null-terminated element.
  ```zig
  pub fn dupeZ(self: NeverFailingAllocator, comptime T: type, m: []const T) [:0]T {
      return self.allocator.dupeZ(T, m) catch unreachable;
  }
  ```
- **createArena**: Creates a new arena allocator.
  ```zig
  pub fn createArena(self: NeverFailingAllocator) NeverFailingAllocator {
      const arenaPtr = self.create(NeverFailingArenaAllocator);
      arenaPtr.* = NeverFailingArenaAllocator.init(self);
      return arenaPtr.allocator();
  }
  ```
- **destroyArena**: Destroys an existing arena allocator.
  ```zig
  pub fn destroyArena(self: NeverFailingAllocator, arena: NeverFailingAllocator) void {
      const arenaAllocatorPtr: *NeverFailingArenaAllocator = @ptrCast(@alignCast(arena.allocator.ptr));
      arenaAllocatorPtr.deinit();
      self.destroy(arenaAllocatorPtr);
  }
  ```

## Code Example
```zig
fn rawAlloc(a: NeverFailingAllocator, len: usize, alignment: Alignment, ret_addr: usize) ?[*]u8 {
		return a.allocator.vtable.alloc(a.allocator.ptr, len, alignment, ret_addr);
	}
```

## Related Questions
-  How does NeverFailingAllocator handle memory allocation errors?
-  What methods are provided by NeverFailingAllocator for managing memory?
-  Can you explain the purpose of the `createArena` and `destroyArena` methods in NeverFailingAllocator?
-  How does NeverFailingAllocator ensure that all operations never fail?
-  What is the difference between `resize`, `remap`, and `realloc` in NeverFailingAllocator?
-  How does NeverFailingAllocator handle memory duplication with null-termination?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_3*
