# [hard/codebase_src_items.zig] - Chunk 9

**Type:** api
**Keywords:** item stack, recipe validation, binary serialization, ZonElement, global item list
**Symbols:** ItemStack, ItemStack.item, ItemStack.amount, ItemStack.load, ItemStack.deinit, ItemStack.clone, ItemStack.empty, ItemStack.storeToZon, ItemStack.fromBytes, ItemStack.toBytes, Recipe, Recipe.sourceItems, Recipe.sourceAmounts, Recipe.resultItem, Recipe.resultAmount, Recipe.getValidRecipe, Recipe.toBytes, Recipe.fromBytes, proceduralItemTypeList, proceduralItemTypeIdToIndex, reverseIndices, modifiers, modifierRestrictions, itemList, itemListSize, itemDeduplicationMap, recipeList, hasRegistered, hasRegisteredProceduralItem, iterator, getRecipes
**Concepts:** inventory management, crafting recipes, serialization, deserialization

## Summary
Defines item stack and recipe structures with serialization, deserialization, and registration functionalities.

## Explanation
This chunk defines two primary structures: `ItemStack` and `Recipe`. The `ItemStack` structure manages an item and its quantity, providing methods for loading from a ZonElement, deinitializing resources, cloning the stack, checking if it's empty, storing to a ZonElement, and serializing/deserializing to/from binary formats. Specifically, `ItemStack` has fields:
- `item: Item = .null`
- `amount: u16 = 0`
The methods include:
- `load(zon: ZonElement) !ItemStack`: Loads an ItemStack from a ZonElement.
- `deinit(self: *ItemStack) void`: Deinitializes the item stack resources.
- `clone(self: *const ItemStack) ItemStack`: Clones the item stack.
- `empty(self: *const ItemStack) bool`: Checks if the amount is zero.
- `storeToZon(self: *const ItemStack, allocator: NeverFailingAllocator, zonObject: ZonElement) void`: Stores the item stack to a ZonElement.
- `fromBytes(reader: *BinaryReader) !ItemStack`: Deserializes an ItemStack from binary format.
- `toBytes(self: *const ItemStack, writer: *BinaryWriter) void`: Serializes an ItemStack to binary format.
The `Recipe` structure represents crafting recipes and includes methods for validating recipes, serializing to binary format, and deserializing from binary format. Specifically, `Recipe` has fields:
- `sourceItems: []BaseItemIndex`
- `sourceAmounts: []u16`
- `resultItem: BaseItemIndex`
- `resultAmount: u16`
The methods include:
- `getValidRecipe(self: Recipe) error{Invalid}!*Recipe`: Validates the recipe against existing recipes.
- `toBytes(self: *const Recipe, writer: *BinaryWriter) void`: Serializes a Recipe to binary format.
- `fromBytes(reader: *BinaryReader) !*Recipe`: Deserializes a Recipe from binary format. Additionally, the chunk declares several global variables related to item management:
- `proceduralItemTypeList: List(ProceduralItemType) = .empty`
- `proceduralItemTypeIdToIndex: std.StringHashMapUnmanaged(ProceduralItemTypeIndex) = .{}`
- `reverseIndices: std.StringHashMapUnmanaged(BaseItemIndex) = .{}`
- `modifiers: std.StringHashMapUnmanaged(*const Modifier.VTable) = .{}`
- `modifierRestrictions: std.StringHashMapUnmanaged(*const ModifierRestriction.VTable) = .{}`
- `itemList: [65536]BaseItem = undefined`
- `itemListSize: u16 = 0`
- `itemDeduplicationMap: [65536]BaseItemIndex = undefined`
- `recipeList: main.ListManaged(Recipe) = .init(main.worldArena)`
The chunk also provides functions for checking if an item has been registered and handling multiple indices mapping to the same item.

## Code Example
```zig
pub fn empty(self: *const ItemStack) bool {
	return self.amount == 0;
}
```

## Related Questions
- How does an `ItemStack` load data from a ZonElement?
- What methods are available for managing an `ItemStack`?
- How is a `Recipe` validated against existing recipes?
- What global variables are used for item management?
- How do you check if an item has been registered?
- How does the engine handle multiple indices mapping to the same item?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_9*
