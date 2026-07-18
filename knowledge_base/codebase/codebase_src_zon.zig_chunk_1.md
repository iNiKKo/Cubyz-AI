# [hard/codebase_src_zon.zig] - Chunk 1

**Type:** serialization
**Keywords:** union, enum, memory management, type casting, error handling
**Symbols:** ZonElement, ZonElement.int, ZonElement.float, ZonElement.string, ZonElement.stringOwned, ZonElement.bool, ZonElement.null, ZonElement.array, ZonElement.object, ZonElement.initObject, ZonElement.initArray, ZonElement.getAtIndex, ZonElement.getChildAtIndex, ZonElement.get, ZonElement.getChild, ZonElement.getChildOrNull, ZonElement.removeChild, ZonElement.clone, ZonElement.JoinPriority, ZonElement.joinGetNew, ZonElement.join, ZonElement.as
**Concepts:** data serialization, dynamic data structures, type handling

## Summary
Defines the ZonElement union and its associated methods for handling different data types, including initialization, access, cloning, joining, and type conversion.

## Explanation
The ZonElement union in this chunk represents various data types such as integers, floats, strings, booleans, nulls, arrays, and objects. It includes methods for initializing objects and arrays, accessing elements by index or key, cloning the entire structure, joining two ZonElements with a specified priority, and converting the element to a specific type if possible. The chunk also defines an enumeration JoinPriority to determine how conflicts are resolved during the join operation.

## Code Example
```zig
pub fn initObject(allocator: NeverFailingAllocator) ZonElement {
	const map = allocator.create(std.StringHashMap(ZonElement));
	map.* = .init(allocator.allocator);
	return .{.object = map};
}
```

## Related Questions
- How do you initialize a ZonElement object?
- What methods are available for accessing elements in a ZonElement array?
- How does the clone method work for ZonElements?
- What is the purpose of the JoinPriority enum?
- How are conflicts resolved during the join operation?
- How does the as method handle type conversion?

*Source: unknown | chunk_id: codebase_src_zon.zig_chunk_1*
