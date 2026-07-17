# [hard/codebase_src_items.zig] - Chunk 1

**Type:** api
**Keywords:** vTable, dynamic method dispatch, enum, struct, item attributes
**Symbols:** ModifierRestriction, ModifierRestriction.vTable, ModifierRestriction.data, ModifierRestriction.VTable, ModifierRestriction.VTable.satisfied, ModifierRestriction.VTable.loadFromZon, ModifierRestriction.VTable.printTooltip, Modifier, Modifier.data, Modifier.restriction, Modifier.vTable, Modifier.VTable, Modifier.VTable.Data, Modifier.VTable.combineModifiers, Modifier.VTable.changeProceduralItemParameters, Modifier.VTable.changeBlockDamage, Modifier.VTable.printTooltip, Modifier.VTable.loadData, Modifier.VTable.priority, Modifier.VTable.Defaults, Modifier.VTable.Defaults.changeProceduralItemParameters, Modifier.VTable.Defaults.changeBlockDamage, MaterialProperty, BaseItemIndex, BaseItem
**Concepts:** item management, modifier system, material properties, base item index

## Summary
Defines item-related structures and enums for Cubyz, including ModifierRestriction, Modifier, MaterialProperty, BaseItemIndex, and BaseItem.

## Explanation
The chunk defines several key structures and enums related to items in the Cubyz game engine. The `ModifierRestriction` struct manages restrictions on modifiers with a vTable for dynamic method calls. The `Modifier` struct represents item modifiers with similar dynamic method handling. The `MaterialProperty` enum lists properties like mass damage, hardness, etc., and includes a method to convert strings to enum values. The `BaseItemIndex` enum provides an index for base items with methods to retrieve various item attributes such as image, texture, ID, name, tags, stack size, material, block type, and tooltip. The `BaseItem` struct represents the basic properties of an item including its image, texture, ID, name, and tags.

## Code Example
```zig
pub fn fromId(_id: []const u8) ?BaseItemIndex {
	return reverseIndices.get(_id);
}
```

## Related Questions
- How does ModifierRestriction handle loading data from ZonElement?
- What is the purpose of the VTable in Modifier and ModifierRestriction?
- How are MaterialProperty values converted from strings?
- What methods does BaseItemIndex provide to retrieve item attributes?
- How do Modifiers combine with each other?
- What is the structure of the Modifier.VTable.Data field?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_1*
