# [easy/codebase_src_proceduralItem_modifiers_single_use.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, optional value, minimum strength, property setter, durability, single-use, ZonElement, string formatting, modifying items
**Symbols:** Data, priority, loadData, combineModifiers, changeProceduralItemParameters, printTooltip
**Concepts:** single-use modifiers, durability setting, ZON file parsing, packed struct layout, property assignment, tooltip rendering

## Summary
Defines a single-use procedural item modifier that sets the maximum durability of an item, providing data loading from ZON files, combining modifiers via minimum strength, and tooltip rendering.

## Explanation
The chunk declares a packed struct Data with fields strength (f32) and pad (u96), exposing loadData which reads 'strength' from a ZonElement using zon.get returning an optional f32 or defaulting to 1 via orelse, combineModifiers which returns ?Data by taking the minimum of two Data strengths, changeProceduralItemParameters which takes a mutable ProceduralItem and sets its property .maxDurability to data.strength, and printTooltip which formats a tooltip string with '#800000**Single-use**#808080 *Sets durability to **{d:.0}' using outString.print. The chunk also defines priority as 1000.

## Code Example
```zig
pub fn combineModifiers(data1: Data, data2: Data) ?Data {
	return .{.strength = @min(data1.strength, data2.strength)};
}
```

## Related Questions
- What does the loadData function return when zon.get fails to find a strength value?
- How is the priority of this modifier defined and what numeric value is assigned?
- Which property on ProceduralItem is modified by changeProceduralItemParameters?
- What default value is used for the pad field in the Data struct definition?
- Does combineModifiers preserve any fields other than strength when merging two modifiers?
- How does printTooltip format its output string and what color codes are included?
- Is the Data struct marked as packed and why might that be relevant here?
- What optional type is used for the return value of combineModifiers and loadData?
- Does this chunk declare any public constants besides priority?
- Which import statements does this chunk rely on from the main module?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_single_use.zig_chunk_0*
