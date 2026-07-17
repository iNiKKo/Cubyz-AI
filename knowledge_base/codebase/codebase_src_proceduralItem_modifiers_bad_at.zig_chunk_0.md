# [easy/codebase_src_proceduralItem_modifiers_bad_at.zig] - Chunk 0

**Type:** implementation
**Keywords:** strength, tag, clamp, hypot, combineModifiers, changeBlockDamage, printTooltip, packed struct, modifier priority, block tags
**Symbols:** Data, priority, loadData, combineModifiers, changeBlockDamage, printTooltip
**Concepts:** procedural item modifiers, damage reduction, tag matching, packed struct storage, modifier combination, tooltip rendering

## Summary
Defines a procedural item modifier that reduces damage on specific block tags using packed struct storage and combines modifiers via tag matching with strength blending.

## Explanation
The chunk declares a public packed struct Data holding an f32 strength, a main.Tag, and a u64 pad. It exposes a priority constant of 1. loadData reads strength from a zon element (clamped to [0,1]) and resolves the tag via string lookup with a fallback 'incorrect'. combineModifiers returns null if tags differ; otherwise it computes blended strength using an inverse-hypot formula that maps two strengths into a combined value while preserving the original tag. changeBlockDamage iterates over block.tags() and applies damage reduction (damage*(1 - data.strength)) when the block's tag matches data.tag, returning unchanged damage otherwise. printTooltip formats a tooltip string with the percentage reduction and block name using outString.print.

## Code Example
```zig
pub fn combineModifiers(data1: Data, data2: Data) ?Data {
	if (data1.tag != data2.tag) return null;
	return .{.strength = 1.0 - 1.0/(1.0 + std.math.hypot(1.0/(1.0 - data1.strength) - 1.0, 1.0/(1.0 - data2.strength) - 1.0)), .tag = data1.tag};
}
```

## Related Questions
- What is the priority value assigned to this modifier?
- How does loadData handle missing strength or tag values from a zon element?
- Under what condition does combineModifiers return null instead of a merged Data?
- Which formula is used to blend two strengths in combineModifiers and why use hypot?
- What fallback tag string is returned when the zon lacks a 'tag' field?
- How does changeBlockDamage iterate over block tags and apply damage reduction?
- Does printTooltip modify the outString buffer or just write into it?
- Is the Data struct packed and what fields are declared in that packing?
- What happens to the strength value if both modifiers have identical tags?
- Can a modifier with tag 'incorrect' ever match any block tag during damage calculation?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_bad_at.zig_chunk_0*
