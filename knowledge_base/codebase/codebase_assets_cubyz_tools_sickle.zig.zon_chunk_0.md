# [easy/codebase_assets_cubyz_tools_sickle.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** sickle tool, damage calculation, config settings, properties, source attributes
**Symbols:** disabled, optional, parameters
**Concepts:** configuration data

## Summary
Configuration data for a sickle tool

## Explanation
This chunk contains configuration settings for a sickle tool: `tags = .{.cuttable}`, plus 5x5 `disabled`/`optional` matrices controlling which material-slot combinations are usable. It defines 7 damage/durability/speed parameters:
- `massDamage` -> `damage`, factor `0.06`, method `.sum`
- `massDamage` -> `damage`, factor `0.24`, method `.average`
- `hardnessDamage` -> `damage`, factor `0.2`, method `.average`
- `durability` -> `maxDurability`, factor `0.2`, method `.sum`
- `durability` -> `maxDurability`, factor `0.8`, method `.average`
- `swingSpeed` -> `swingSpeed`, factor `-0.2`, method `.sum`
- `swingSpeed` -> `swingSpeed`, factor `1.2`, method `.average`

## Related Questions
- What are the disabled properties of the sickle tool?
- Which optional properties does the sickle tool have?
- How many parameters are defined for damage calculation in the sickle tool?
- What is the source attribute used to calculate mass damage in the sickle tool?
- What method is used to average the values when calculating hardness damage in the sickle tool?
- What is the factor applied to swing speed when using the sum method in the sickle tool?
- How many parameters are defined for durability calculation in the sickle tool?
- What is the source attribute used to calculate durability in the sickle tool?
- What method is used to average the values when calculating max durability in the sickle tool?
- What is the factor applied to swing speed when using the average method in the sickle tool?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_sickle.zig.zon_chunk_0*
