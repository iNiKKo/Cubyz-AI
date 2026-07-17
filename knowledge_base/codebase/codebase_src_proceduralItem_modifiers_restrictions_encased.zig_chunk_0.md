# [easy/codebase_src_proceduralItem_modifiers_restrictions_encased.zig] - Chunk 0

**Type:** implementation
**Keywords:** Encased, satisfied, loadFromZon, printTooltip, tag, amount, neighborhood, hasTag, getItemAt, default value
**Symbols:** Encased, Encased.tag, Encased.amount, Encased.satisfied, Encased.loadFromZon, Encased.printTooltip
**Concepts:** modifier restrictions, encased item validation, neighborhood checking, tag matching, zon element parsing, tooltip generation

## Summary
Defines the Encased modifier restriction that validates a procedural item is surrounded by a required number of matching tags within its immediate 3x3 neighborhood.

## Explanation
The chunk declares a public struct Encased with fields tag (main.Tag) and amount (usize). It provides satisfied(self, proceduralItem, x, y) which iterates over the 3x3 grid centered at (x,y), skips cells outside bounds via getItemAt returning null, counts neighbors whose hasTag matches self.tag, and returns true only if count >= self.amount. loadFromZon(allocator, zon) parses a ZonElement: it reads 'tag' as a string and resolves it via main.Tag.find, logging an error and returning the sentinel 'not specified' if missing; it reads 'amount' as usize with a default of 8 on failure. printTooltip(self, outString) formats a tooltip string showing the amount and tag name.

## Code Example
```zig
pub fn printTooltip(self: *const Encased, outString: *main.ListManaged(u8)) void {
	outString.print("encased in {} .{s}", .{self.amount, self.tag.getName()});
}
```

## Related Questions
- What does the satisfied function return when fewer than amount neighbors have the required tag?
- How is a missing 'tag' field handled during loadFromZon and what sentinel value is used?
- What default amount is applied if parsing fails in loadFromZon?
- Which main.Tag method is invoked to resolve the string tag name inside Encased?
- Does satisfied check only orthogonal neighbors or all eight surrounding cells?
- How does getItemAt signal an out-of-bounds coordinate within the neighborhood loop?
- What exact tooltip text format is produced by printTooltip for a given amount and tag?
- Is Encased marked as pub so other modules can instantiate it directly?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_encased.zig_chunk_0*
