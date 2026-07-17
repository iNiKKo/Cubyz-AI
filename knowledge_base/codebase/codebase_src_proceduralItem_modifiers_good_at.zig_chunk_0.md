# [easy/codebase_src_proceduralItem_modifiers_good_at.zig] - Chunk 0

**Type:** implementation
**Keywords:** packed struct, hypot, tag matching, clamp to zero, default value
**Symbols:** Data, priority, loadData, combineModifiers, changeBlockDamage, printTooltip
**Concepts:** procedural item modifiers, damage scaling, tag-based filtering, tooltip rendering

## Summary
Defines a procedural item modifier for 'Good at' that increases damage on specific block tags.

## Explanation
The chunk declares a packed struct Data holding strength (f32), tag (main.Tag), and padding. loadData reads strength from the ZonElement, clamping to >=0, and resolves the tag name, defaulting to 'incorrect'. combineModifiers merges two modifiers only if their tags match; otherwise returns null, using hypot for combined strength. changeBlockDamage iterates over a block's tags and multiplies damage by (1 + data.strength) when a matching tag is found. printTooltip formats a tooltip string with the percentage increase and the block name.

## Code Example
```zig
pub fn combineModifiers(data1: Data, data2: Data) ?Data {
	if (data1.tag != data2.tag) return null;
	return .{.strength = std.math.hypot(data1.strength, data2.strength), .tag = data1.tag};
}
```

## Related Questions
- What is the default tag value when loadData cannot find a 'tag' field in the ZonElement?
- How does combineModifiers handle mismatched tags between two modifiers?
- Does changeBlockDamage modify damage for multiple matching block tags or only the first one encountered?
- Is the strength field in Data signed or unsigned, and how is it used in calculations?
- What happens to the padding field in the packed struct Data when loadData assigns values?
- Can printTooltip be called with a null outString pointer without causing undefined behavior?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_good_at.zig_chunk_0*
