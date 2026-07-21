# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 4

**Type:** documentation
**Keywords:** biomes.html, saveBiomeToProject, isCave, ground_structure, isValidPlayerSpawn, properties radio groups, structures
**Symbols:** biomeId, bioMinRadius, bioIsCave, bioSpawn, bioTemp

## Summary
Cubyz Addon Creator: Biomes form (`biomes.html`) field-to-export mapping.

## Explanation
Biome ID (`biomeId`) becomes the filename. Generation Chance (`biomeChance`) exports as `.chance`. Border Interpolation (`bioInterpolation`) is a raw enum passthrough to `.interpolation`. Min/Max Cluster Radius (`bioMinRadius`/`bioMaxRadius`), Min/Max Height, Min Floor/Max Ceiling Limit all export as their matching fields, raw passthrough, no decimal formatting for radius. Roughness/Hills/Mountains/Soil Creep/Keep Original Mix Factors export with `.toFixed(2)`.

Top Surface / Subsurface / Bottom Stone Layer (`bioSurfaceBlock`/`bioSubBlock`/`bioStoneBlock`) map to **two separate output fields**, not three: (1) surface and subsurface are combined into one field, `.ground_structure = .{"{surface}", "0 to 3 {sub}"}`; (2) the stone layer is kept as its own, separate `.stoneBlock` field. So: surface+subsurface -> `.ground_structure`, and stone layer -> `.stoneBlock`. The "Is Cave" checkbox (`bioIsCave`) exports as `.isCave`, and **gates whether the cave-only fields below are emitted at all**: Cave Density Scale / Openness Radius Factor / Glow Crystal Frequency (`bioCaves`/`bioCaveRadiusFactor`/`bioCrystals`) are only emitted if `isCave` is checked.

Ambient Music Track (`bioMusic`) exports as `.music`, website default `cubyz:sunrise`. Fog Thickness Density (`bioFogDensity`) exports with `.toFixed(2)`. Sky Tint / Fog Atmospheric Tint hex pickers (`bioSkyColor`/`bioFogColor`) convert hex to a normalized 0-1 float RGB vector, exported as `.skyColor`/`.fogColor`. The player-spawn checkbox (`bioSpawn`, no visible label found in the UI) exports as `.isValidPlayerSpawn`.

The Climate/Humidity/Zone/Growth/Elevation radio groups (`bioTemp`/`bioWet`/`bioZone`/`bioGrowth`/`bioHeightProp`, radio inputs using `name=` not `id=`) export as `.properties = .{.val1, .val2, ...}` -- **all 5 groups' checked values are flattened into one combined list**, not kept separate. Structure rows (dynamic list) export as `.structures = .{...}` -- schema depends entirely on the selected type: `simple_tree` needs log/leaves/top/height/height_variation/leafRadius; `simple_vegetation`/`flower_patch`/`boulder`/`ground_patch` each need a `block` plus different size fields; `fallen_tree` needs log/top/height; `sbb` needs structure+placeMode.

## Related Questions
- What two fields does the Cubyz Addon Creator combine a biome's surface and subsurface blocks into?
- What gates whether a Cubyz biome's cave-specific fields are exported at all?
- How does the Cubyz Addon Creator handle a biome's five climate/humidity/zone/growth/elevation radio groups on export?
- What fields does a Cubyz "simple_tree" structure row need in the Addon Creator?
- What fields does a Cubyz "fallen_tree" structure row need in the Addon Creator?
- What fields does an "sbb" structure row need in the Cubyz Addon Creator?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_4*
