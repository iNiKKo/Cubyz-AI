# [hard/codebase_src_utils.zig] - Chunk 13

**Type:** serialization
**Keywords:** binary writer, serialization, endianness, variable-length encoding, dynamic list
**Symbols:** BinaryWriter, BinaryWriter.data, BinaryWriter.init, BinaryWriter.initCapacity, BinaryWriter.deinit, BinaryWriter.writeVec, BinaryWriter.writeInt, BinaryWriter.writeVarInt, BinaryWriter.writeFloat, BinaryWriter.writeEnum, BinaryWriter.writeBool, BinaryWriter.writeSlice, BinaryWriter.writeSliceWithSize, BinaryWriter.writeWithDelimiter
**Concepts:** binary serialization, data encoding, variable-length integers

## Summary
Provides a binary writer utility for serializing various data types into a byte buffer.

## Explanation
The BinaryWriter struct manages a dynamic list of bytes and offers methods to serialize different data types, including integers, floats, enums, booleans, slices, and strings with delimiters. It ensures proper alignment and endianness handling for integer writes and uses variable-length encoding for large integers. The writer also supports appending raw byte slices and writing slices prefixed by their length.

- **Handling Non-Standard Bit Sizes**: When writing integers with non-standard bit sizes, the BinaryWriter first checks if the bit size is not a multiple of 8. If so, it calculates the next full byte boundary and writes the integer using that type. This ensures proper alignment and endianness handling.

- **Serializing Variable-Length Integers**: The `writeVarInt` method serializes integers using variable-length encoding. It repeatedly writes 7 bits of the integer value to a byte, setting the 8th bit if there are more bits to write. This process continues until all bits are written, ensuring efficient storage for large integers.

- **Writing Slices of Bytes**: The `writeSlice` method appends a raw byte slice to the internal buffer. The `writeSliceWithSize` method first writes the length of the slice as a variable-length integer followed by the slice itself, allowing for easy deserialization later.

- **Ensuring Proper Alignment**: For integers with non-standard bit sizes, BinaryWriter calculates the next full byte boundary and writes the integer using that type. This ensures proper alignment and endianness handling.

- **Purpose of `writeWithDelimiter` Method**: The `writeWithDelimiter` method appends a delimiter to the internal buffer after writing a slice of bytes. This is useful for separating different data segments within the same buffer, ensuring that each segment can be easily identified and processed later.

## Code Example
```zig
pub fn writeBool(self: *BinaryWriter, value: bool) void {
	self.writeInt(u1, @intFromBool(value));
}
```

## Related Questions
- How does BinaryWriter handle writing integers with non-standard bit sizes?
- What method is used to serialize a variable-length integer in BinaryWriter?
- Can BinaryWriter write slices of bytes directly?
- How does BinaryWriter ensure that the data written is aligned properly?
- What is the purpose of the `writeWithDelimiter` method in BinaryWriter?
- How does BinaryWriter manage memory allocation for its internal buffer?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_13*
