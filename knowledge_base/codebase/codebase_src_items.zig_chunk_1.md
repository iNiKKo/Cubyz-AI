# [hard/codebase_src_items.zig] - Chunk 1

**Type:** api
**Keywords:** vTable, dynamic method dispatch, enum, struct, item attributes, modifier restrictions
**Symbols:** ModifierRestriction, ModifierRestriction.vTable, ModifierRestriction.data, ModifierRestriction.VTable, ModifierRestriction.VTable.satisfied, ModifierRestriction.VTable.loadFromZon, ModifierRestriction.VTable.printTooltip, Modifier, Modifier.data, Modifier.restriction, Modifier.vTable, Modifier.VTable, Modifier.VTable.Data, Modifier.VTable.combineModifiers, Modifier.VTable.changeProceduralItemParameters, Modifier.VTable.changeBlockDamage, Modifier.VTable.printTooltip, Modifier.VTable.loadData, Modifier.VTable.priority, Modifier.VTable.Defaults, Modifier.VTable.Defaults.changeProceduralItemParameters, Modifier.VTable.Defaults.changeBlockDamage, MaterialProperty, BaseItemIndex, BaseItemIndex._
**Concepts:** item management, modifier system, material properties, base item indexing

## Summary
Defines item-related structures and enums, including ModifierRestriction, Modifier, MaterialProperty, and BaseItemIndex.

## Explanation
This chunk defines several key structures and enums for handling items in the game. The `ModifierRestriction` struct manages restrictions on modifiers with a vTable for dynamic method calls. The `Modifier` struct represents item modifiers with similar dynamic method handling. The `MaterialProperty` enum lists properties like mass damage, hardness, etc., and includes a method to convert strings to these properties. The `BaseItemIndex` enum provides an index for base items, with methods to retrieve various attributes of the items such as image, texture, ID, name, tags, stack size, material, block type, and more.

## Code Example
```zig
pub fn satisfied(self: ModifierRestriction, proceduralItem: *const ProceduralItem, x: i32, y: i32) bool {
	return self.vTable.satisfied(self.data, proceduralItem, x, y);
}
```

## Related Questions
- What is the purpose of the `ModifierRestriction` struct?
- How does the `Modifier` struct handle dynamic method calls?
- What properties are listed in the `MaterialProperty` enum?
- How do you retrieve an item's image using the `BaseItemIndex` enum?
- What methods are available for the `BaseItemIndex` enum?
- How is the `loadFromZon` function implemented for `ModifierRestriction`?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_1*
