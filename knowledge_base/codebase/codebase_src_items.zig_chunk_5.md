# [hard/codebase_src_items.zig] - Chunk 5

**Type:** api
**Keywords:** enum, struct, serialization, iteration, attribute access
**Symbols:** ProceduralItemTypeIndex, ProceduralItemTypeIndex.ProceduralItemTypeIterator, ProceduralItemTypeIndex.next, ProceduralItemTypeIndex.toBytes, ProceduralItemTypeIndex.fromBytes, ProceduralItemTypeIndex.iterator, ProceduralItemTypeIndex.fromId, ProceduralItemTypeIndex.id, ProceduralItemTypeIndex.tags, ProceduralItemTypeIndex.properties, ProceduralItemTypeIndex.slotInfos, ProceduralItemTypeIndex.pixelSources, ProceduralItemTypeIndex.pixelSourcesOverlay, ProceduralItemProperty, ProceduralItemProperty.fromString
**Concepts:** item management, serialization, enumeration

## Summary
Defines the structure and methods for procedural item types in Cubyz.

## Explanation
This chunk defines an enum `ProceduralItemTypeIndex` representing indices of procedural item types, along with a struct `ProceduralItemProperty` for properties of items. It includes methods for serialization (`toBytes`, `fromBytes`), iteration (`iterator`, `next`), and accessing various attributes of items such as ID, tags, properties, slot information, pixel sources, and overlays. The chunk also defines a struct `ProceduralItemType` that holds detailed data about each item type.

## Code Example
```zig
pub fn next(self: *ProceduralItemTypeIterator) ?ProceduralItemTypeIndex {
	if (self.i >= proceduralItemTypeList.items.len) return null;
	defer self.i += 1;
	return @enumFromInt(self.i);
}
```

## Related Questions
- How do you iterate over all procedural item types?
- What methods are available for serializing and deserializing procedural item types?
- How is the ID of a procedural item type accessed?
- What properties can be retrieved from a procedural item type?
- How does the code handle invalid enum tags during deserialization?
- What is the structure of the `ProceduralItemType` struct?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_5*
