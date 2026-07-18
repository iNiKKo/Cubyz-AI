# [hard/codebase_src_utils.zig] - Chunk 12

**Type:** serialization
**Keywords:** atomic operations, mutex locking, endianness handling, variable-length integers, buffer management
**Symbols:** TimeDifference, TimeDifference.difference, TimeDifference.firstValue, TimeDifference.addDataPoint, Mutex, Mutex.super, Mutex.tryLock, Mutex.lock, Mutex.unlock, Mutex.assertLocked, BinaryReader, BinaryReader.remaining, BinaryReader.AllErrors, BinaryReader.init, BinaryReader.readVec, BinaryReader.readInt, BinaryReader.readVarInt, BinaryReader.readFloat, BinaryReader.readEnum, BinaryReader.readBool, BinaryReader.readUntilDelimiter, BinaryReader.readSlice, BinaryReader.readSliceWithSize
**Concepts:** time tracking, thread synchronization, binary data parsing

## Summary
This chunk defines utility structures and functions for time difference calculation, mutex management, and binary data reading.

## Explanation
The chunk includes a `TimeDifference` struct that tracks the difference between two timestamps using atomic operations. It also provides a `Mutex` wrapper to handle OS-specific locking mechanisms. The `BinaryReader` struct is designed for reading various types of data from a byte slice, including integers, floats, enums, booleans, and variable-length integers. Each method in `BinaryReader` handles specific data types or operations, such as reading vectors, handling endianness, and managing buffer state.

## Code Example
```zig
pub fn readInt(self: *BinaryReader, T: type) error{ OutOfBounds, IntOutOfBounds }!T {
	if (@mod(@typeInfo(T).int.bits, 8) != 0) {
		const fullBits = comptime std.mem.alignForward(u16, @typeInfo(T).int.bits, 8);
		const FullType = std.meta.Int(@typeInfo(T).int.signedness, fullBits);
		const val = try self.readInt(FullType);
		return std.math.cast(T, val) orelse return error.IntOutOfBounds;
	}
	const bufSize = @divExact(@typeInfo(T).int.bits, 8);
	if (self.remaining.len < bufSize) return error.OutOfBounds;
	defer self.remaining = self.remaining[bufSize..];
	return std.mem.readInt(T, self.remaining[0..bufSize], endian);
}
```

## Related Questions
- How does the `TimeDifference` struct calculate time differences?
- What is the purpose of the `Mutex` wrapper in this code?
- How does the `BinaryReader` handle reading variable-length integers?
- What error handling is implemented for integer overflow in `BinaryReader` methods?
- How does the `readEnum` method work in the `BinaryReader` struct?
- What are the different types of errors that can be returned by `BinaryReader` methods?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_12*
