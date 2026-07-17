# [hard/codebase_src_items.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct initialization, hashing, property access, polymorphism, tooltip formatting
**Symbols:** Material, Material.massDamage, Material.hardnessDamage, Material.durability, Material.swingSpeed, Material.textureRoughness, Material.colorPalette, Material.modifiers, Material.init, Material.hashCode, Material.getProperty, Material.printTooltip, ModifierRestriction, ModifierRestriction.vTable, ModifierRestriction.data, ModifierRestriction.VTable, ModifierRestriction.satisfied, ModifierRestriction.loadFromZon, ModifierRestriction.printTooltip, recipes, Inventory
**Concepts:** item properties, material attributes, modifier restrictions, tooltip generation

## Summary
Defines the Material and ModifierRestriction structures for item properties and restrictions in Cubyz.

## Explanation
This chunk defines two main structures: Material and ModifierRestriction. The Material structure encapsulates various attributes of an item's material, such as mass damage, hardness damage, durability, swing speed, texture roughness, color palette, and modifiers. It includes methods for initialization from a ZonElement, computing a hash code, retrieving properties, and printing tooltips. The ModifierRestriction structure represents restrictions that can be applied to modifiers, with a vTable for polymorphic behavior in loading data, checking satisfaction, and printing tooltips.

## Code Example
```zig
pub fn hashCode(self: Material) u32 {
	var hash: u32 = 0;
	hash = 101*%hash +% @as(u32, @bitCast(self.massDamage));
	hash = 101*%hash +% @as(u32, @bitCast(self.hardnessDamage));
	hash = 101*%hash +% @as(u32, @bitCast(self.durability));
	hash = 101*%hash +% @as(u32, @bitCast(self.swingSpeed));
	hash = 101*%hash +% @as(u32, @bitCast(self.textureRoughness));
	hash ^= hash >> 24;
	return hash;
}
```

## Related Questions
- What are the attributes of a Material in Cubyz?
- How does the Material structure initialize from a ZonElement?
- What is the purpose of the hashCode method in Material?
- How are ModifierRestrictions loaded from a ZonElement?
- What methods does ModifierRestriction provide for checking satisfaction and printing tooltips?
- How does the getProperty method work in the Material structure?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_0*
