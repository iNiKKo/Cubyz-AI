# [hard/codebase_src_items.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct definition, method implementation, error handling, property access, string manipulation
**Symbols:** Material, Material.massDamage, Material.hardnessDamage, Material.durability, Material.swingSpeed, Material.textureRoughness, Material.colorPalette, Material.modifiers, Material.init, Material.hashCode, Material.getProperty, Material.printTooltip, recipes, Inventory
**Concepts:** item properties, material initialization, hashing mechanism, tooltip generation

## Summary
Defines the Material struct and its methods for initialization with default fallbacks, hashing, property retrieval, and tooltip printing. Initialization includes setting massDamage, hardnessDamage, durability, swingSpeed, textureRoughness, colorPalette, and modifiers from a ZonElement, handling missing attributes by logging errors.

## Explanation
The chunk defines a `Material` struct with fields such as massDamage, hardnessDamage, durability, swingSpeed, textureRoughness, colorPalette, and modifiers. It includes methods like `init`, which initializes the material from a ZonElement, setting default values for missing attributes; `hashCode`, which computes a hash code for the material based on its properties; `getProperty`, which retrieves a property value based on an enum; and `printTooltip`, which appends a tooltip string to a list managed by the main module. During initialization (`init` method), the `massDamage`, `hardnessDamage`, `durability`, and `swingSpeed` fields are set from the ZonElement, with a default value of 0 if they are not found. The `textureRoughness` field is set to a maximum of 1.0 if it is not found. The `colorPalette` is initialized by reading color values from the ZonElement and converting them into Color structs. The `modifiers` are loaded by iterating over the modifiers in the ZonElement, retrieving their vTable, and loading their data. If a modifier's ID is not found, it defaults to 'durable'. The `hashCode` method computes a hash code for the material based on its properties using a specific formula. The `getProperty` method retrieves a property value based on an enum. The `printTooltip` method appends a tooltip string to a list managed by the main module, including information about modifiers if they exist.

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
- How is the Material struct initialized with error handling for missing attributes?
- What specific properties and their types are included in the Material struct?
- How does the hashCode method compute a hash code for a Material instance?
- What happens if a required attribute is missing during initialization?
- How are tooltips generated for materials with modifiers?
- What is the purpose of the colorPalette field in Material?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_0*
