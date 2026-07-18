# [easy/codebase_src_proceduralItem_modifiers_good_at.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, function, modifier, tooltip, block damage
**Symbols:** Data, priority, loadData, combineModifiers, changeBlockDamage, printTooltip
**Concepts:** data structure, modifiers, procedural items

## Summary
This chunk defines a `Data` struct with fields for strength and tag. It provides functions to load data from a ZonElement, combine modifiers based on tags, change block damage based on the item's tag, and print a tooltip. The priority of this chunk is set to 1.

## Explanation
This chunk defines a `Data` struct with fields for strength (a floating-point number) and tag (an enum value). It also includes an unused padding field (`pad`) initialized to undefined.

The `priority` constant is defined as 1, indicating the importance of this procedural item in the system hierarchy.

The `loadData` function initializes a `Data` struct by setting its strength to the maximum of zero and the value retrieved from the ZonElement's 'strength' field (defaulting to 0 if not present). The tag is set based on the value retrieved from the ZonElement's 'tag' field, defaulting to 'incorrect' if not found.

The `combineModifiers` function checks if two Data instances have the same tag. If they do, it combines their strengths using the hypotenuse formula and returns a new Data instance with this combined strength and the common tag. Otherwise, it returns null.

The `changeBlockDamage` function modifies block damage by increasing it based on the item's tag if the block has that tag. The increase is calculated as 1 plus the strength value of the Data struct.

Finally, the `printTooltip` function generates a tooltip string displaying the percentage increase in damage and the name of the relevant block tag.

## Code Example
```zig
pub fn loadData(zon: main.ZonElement) Data { return .{.strength = @max(0, zon.get(f32, "strength") orelse 0), .tag = .find(zon.get([]const u8, "tag") orelse "incorrect")}; }
```

## Related Questions
- What is the purpose of the `Data` struct?
- How does the `loadData` function work?
- What is the `combineModifiers` function used for?
- How does the `changeBlockDamage` function modify block damage based on item tags?
- What information does the `printTooltip` function display?
- What are the fields of the `Data` struct?
- Which functions use the `Data` struct?
- What is the priority of this chunk?
- How is the strength value calculated in the `loadData` function?
- What happens if the tag is not found in the ZonElement?
- What is the purpose of the `find` function used in the `loadData` function?
- How does the `combineModifiers` function handle different tags?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_good_at.zig_chunk_0*
