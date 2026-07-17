# Cubyz Engine-Side Addon Validation Reference

This is the companion to `FIELD_REFERENCE.md`. That document covers what the Addon Creator
*website* exports; this one covers what the *game engine* actually reads back when loading a
`.zig.zon` addon file, compiled by reading the real Zig loader functions in full:
`blocks.zig:register()`, `items.zig:BaseItem.init()`/`Material.init()`/`registerProceduralItem()`,
`items/recipes.zig:parseRecipe()`, `server/terrain/biomes.zig:Biome.init()`,
`entityModel.zig:EntityModel.init()`, and `particles.zig:register()`/`EmitterProperties`/
`SpawnShape`/`DirectionMode`.

Two things this reference is good for:
1. **Exact error messages** the engine logs for specific mistakes -- useful for matching a
   real error/log line back to its cause.
2. **What happens when a field is missing** -- the engine's own fallback default, which is not
   always the same as the website's form default (the website always writes a value, so this
   only matters for hand-edited files).

## Precedence rule

Where this document and `FIELD_REFERENCE.md` disagree (field names, defaults, formats), **the
engine is the source of truth, not the website.** The website is a convenience tool and can have
bugs (two are documented below); the engine's parsing code is what actually determines in-game
behavior. When generating new example addon code, use the engine-expected field name/format
even where it differs from what the website currently produces -- e.g. write `.validPlayerSpawn`,
not the website's `.isValidPlayerSpawn`. Only describe the website's actual (buggy) behavior when
specifically explaining why something exported from the website isn't working.

## ⚠️ Two likely real bugs found while reading this

**1. Biome player-spawn flag field name mismatch.** The website's `saveBiomeToProject`
(`app-save.js`) exports the spawn checkbox as `.isValidPlayerSpawn`. The engine's
`Biome.init()` (`server/terrain/biomes.zig` line 297) reads `zon.get(bool, "validPlayerSpawn")`
-- a **different field name**. Because `ZonElement.get` returns the `orelse` default (`false`)
when a field isn't present, a biome exported from the website with "spawn" checked will still
load with `isValidPlayerSpawn = false` in-game. This should be verified against a real exported
file and reported/fixed in `app-save.js` (rename the exported field to `validPlayerSpawn`).

**2. Biome sky/fog color format mismatch (likely, not fully confirmed).** The website exports
`.skyColor`/`.fogColor` as a 3-component float vector (`.{r, g, b}`, values 0-1) via
`getHexColorAsRGBVector()`. The engine reads them with `zon.get(u32, "fogColor")` /
`zon.get(u32, "skyColor")` -- a **packed integer** (e.g. the fallback default is literally
`0xffbfe2ff`), then converts to a vector internally via a separate `u32ToVec3()` helper. A
vector literal being read through a `u32` getter looks very likely to fail to parse and silently
fall back to the default color rather than crash. This is inferred from the type mismatch and
the existence of the u32→vec3 conversion helper (implying u32 is the canonical stored format),
not from reading `ZonElement.get`'s implementation directly -- worth confirming with a real
in-game test (set a distinctive sky color via the website, export, check if it actually shows)
before treating this as certain.

---

## Blocks (`blocks.zig: register()`)

| Field | Type | Engine default if missing | Notes |
|---|---|---|---|
| `.rotation` | string | `"cubyz:no_rotation"` | website defaults form to `"cubyz:stairs"` -- different, but website always writes a value |
| `.blockHealth` | f32 | `1` | |
| `.blockResistance` | f32 | `0` | |
| `.tags` | tag list | -- | **if the resulting tag list is empty, logs `"Block {id} is missing 'tags' field"`** -- every block needs at least one tag |
| `.emittedLight` | u32 | `0` | |
| `.absorbedLight` | u32 | `0xffffff` (16777215) | matches website's decimal default |
| `.degradable` | bool | `false` | |
| `.selectionCapabilities` | object | `.always` (any tool can select it) | **not exposed anywhere in the website UI** -- hand-edit only |
| `.replaceable` | bool | `false` | |
| `.transparent` | bool | `false` | |
| `.collide` | bool | **`true`** | note the default is "does collide", opposite of leaving it off meaning no collision |
| `.viewThrough` | bool | `false`, but forced `true` if `transparent` or `alwaysViewThrough` is true | derived value, not just a raw default |
| `.friction` | f32 | `20` | |
| `.bounciness` | f32 | `0.0` | |
| `.density` | f32 | `main.physics.airDensity` (a named engine constant, not a literal number) | website form defaults to `1.2` |
| `.terminalVelocity` | f32 | `90` | |
| `.mobility` | f32 | `1.0` | |
| `.allowOres` | bool | `false` | |
| `.blockEntity` | string id | none | looked up via `block_entity.getByID` |
| `.ore` | object | -- | **only processed if `.rotation == "cubyz:ore"`; if an `.ore` block exists but rotation isn't `"cubyz:ore"`, logs `"Ore must have rotation mode \"cubyz:ore\"!"` and the ore properties are silently dropped**. Within `.ore`, engine-side raw fallbacks if sub-fields are missing: `veins=0`, `size=0`, `maxHeight=i32 max`, `minHeight=i32 min`, `density=0.5` -- **very different from the website's own hardcoded ore defaults** (`veins=4.5, size=20, maxHeight=-600, density=0.25`), which only matters for hand-written ore blocks that omit fields |
| `.onInteract`/`.onBreak`/`.onUpdate`/`.onTick` | callback object | `.noop` | **if present but malformed, logs `"Failed to load onX event for block {id}"`** and falls back to no-op -- exact message per callback type |
| `.onTouch` | callback object | `.noop` | same pattern, message is `"Failed to load onTouch event for block {id}"` |
| `.drops` | array | -- | parsed via `loadBlockDrop()`; each entry's item string supports `"auto"` (drops the block itself) or `"{count} {item}"`; unknown item ids are silently skipped (`continue`), not errored |
| referencing a nonexistent block id anywhere (`.blockPlacement`, drop items, etc., via `getTypeById`) | -- | -- | **logs `"Couldn't find block {id}. Replacing it with air..."` and substitutes air** -- doesn't crash, just silently becomes air. This is the single most useful diagnostic line in the whole engine for "my block reference doesn't seem to work" |

## Items (`items.zig`)

**Simple items** (`BaseItem.init()`):

| Field | Type | Engine default if missing | Notes |
|---|---|---|---|
| `.name` | string | **the item's own `id`** | website never sets this field at all -- items exported via the website always display their raw id as the tooltip name |
| `.tags` | tag list | empty | |
| `.stackSize` | u16 | `120` | matches website |
| `.material` | object | `null` (no material) | engine checks whether this is an **object**, not whether a `.material` tag is present -- in practice these are coupled by the website's own logic |
| `.block` | string id | `null` | looked up via `blocks.getTypeById` -- same "Couldn't find block..." fallback-to-air behavior as above if the reference is bad |
| `.food` | f32 | `0` | |

**Material sub-object** (`Material.init()`, only runs if `.material` is present) -- **these four
have NO silent default**, a missing field logs an explicit error and falls back to `0`, which for
durability effectively means the item breaks instantly:
- `.massDamage` -- missing → `"Couldn't find material attribute 'massDamage'"`, becomes `0`
- `.hardnessDamage` -- missing → `"Couldn't find material attribute 'hardnessDamage'"`, becomes `0`
- `.durability` -- missing → `"Couldn't find material attribute 'durability'"`, becomes `0`
- `.swingSpeed` -- missing → `"Couldn't find material attribute 'swingSpeed'"`, becomes `0`
- `.textureRoughness` -- **does** have a soft default: `1.0` if missing (website form defaults to `0.0` -- different)
- `.modifiers[].id` -- **if the id doesn't match a known modifier, logs `"Couldn't find modifier with id '{id}'. Replacing it with 'durable'"`** and silently substitutes the "durable" modifier

**Procedural items** (`registerProceduralItem()`): a completely separate, more advanced system
(weighted parameter matrices mapping material properties to tool stats, `disabled`/`optional`
slot arrays) that **the website does not support at all**. Only reachable by hand-writing the
zon file.

## Recipes (`items/recipes.zig: parseRecipe()`)

The website's simple `.inputs = .{...}, .output = "..."` format maps directly and works as-is.
Two things the website doesn't expose:
- **`.reversible`** (bool, default `false`) -- if true, auto-generates the reverse recipe
  (output becomes an input and vice versa), but **requires the recipe have exactly 2 items
  total** (1 input + 1 output) or parsing fails with `error.InvalidReversibleRecipe`.
- A much more powerful **symbolic pattern-matching system** (`{symbol}` wildcards in item ids,
  e.g. `"foo:{bar}/{baz}"`) for recipes that match families of items rather than one exact item.
  Entirely hand-edit only.

## Biomes (`server/terrain/biomes.zig: Biome.init()`)

| Field | Type | Engine default if missing | Notes |
|---|---|---|---|
| `.minRadius`/`.maxRadius` (or legacy `.radius`) | f32 | `256` for min, `= minRadius` for max if unset | engine derives internal `radius`/`radiusVariation` from these, not stored raw |
| `.stoneBlock` | block ref | `"cubyz:slate/smooth"` | |
| `.fogColor`/`.skyColor` | **u32** | `0xffbfe2ff` / a hardcoded light-blue vector | see bug note above -- website exports a vector, not a packed int |
| `.fogDensity` | f32 | `1.0` (then internally divided by `15.0*128.0`) | website's raw value is what's stored; the division is purely internal math, not a format concern |
| `.roughness`/`.hills`/`.mountains`/`.keepOriginalTerrain` | f32 | `0` each | |
| `.interpolation` | enum string | `"square"` if missing or invalid | |
| `.caveSmoothness` | f32 | `4.0`, clamped to `[0.00001, 4.0]` | **not exposed by the website form at all** |
| `.caveNoiseStrength` | f32 | `8` | **not exposed by the website form** |
| `.caveRadiusFactor` | f32 | `1`, clamped to `[-2, 2]` | website field name matches |
| `.crystals` | u32 | `0` | |
| `.soilCreep` | f32 | `0.5` | website form default is `1.0` -- different |
| `.minHeight`/`.maxHeight` | i32 | full i32 range | **logs `"Biome {id} has invalid height range ({min}, {max})"` if min > max** |
| `.minHeightLimit`/`.maxHeightLimit` | i32 | full i32 range | |
| `.smoothBeaches` | bool | `false` | |
| `.rivers` | bool | `false` | field name is `rivers`, **not exposed by the website form at all** |
| `.music` | string | `"cubyz:totaldemented/cubyz"` | website form default is `'cubyz:sunrise'` -- different, only matters if hand-omitted |
| `.validPlayerSpawn` | bool | `false` | **see bug note above -- website writes `.isValidPlayerSpawn` instead** |
| `.chance` | f32 | `1` normally, `0` if the whole biome entry is null | |
| `.tags` | tag list | empty | **cave biomes (`isCave = true`) specifically require a tag ending in `"_layer"`, or logs `"Cave biome {id} is missing a '_layer' tag to assign it to a cave layer."`** -- the website's generic tag-pill UI doesn't prompt for or validate this |
| radius sanity check | -- | -- | **logs `"Biome {id} has invalid radius range ({min}, {max})"` if minRadius > maxRadius**, and **`"Biome {id} has radius {r}, smaller than grid resolution..."` if minRadius is too small relative to the world's biome grid size** |
| `.parentBiomes`, `.transitionBiomes` | array | none | sub-biome nesting and biome-transition-blending systems, **entirely unexposed by the website** |
| `.ground_structure` | array | -- | matches website's `.{"{surface}", "0 to 3 {sub}"}` format |
| `.structures` | array | -- | matches website's dynamic structure-row UI |
| `.caveModels`, `.stripes` | array | none | additional advanced generation features, **hand-edit only** |

## Entities (`entityModel.zig: EntityModel.init()`)

| Field | Type | Engine default if missing | Notes |
|---|---|---|---|
| `.model` | string | `null` (no error logged) | |
| `.height` | f32 | `1` | website form defaults to `2.0` -- different |
| `.coordinateSystem` | enum string | `.right_handed_z_up` | matches website default |
| `.tags` | tag list | empty | a special `playerModel` tag exists (registers the entity as a selectable player skin) -- **not exposed by the website form** |
| `.defaultTexture` | string `"mod:name"` | empty path | split on `:`; texture path resolved as `{assetFolder}/{mod}/entity_models/textures/{name}.png`, falling back to `assets/{mod}/entity_models/textures/{name}.png` if the first doesn't exist. No error logged here if both are missing -- the failure surfaces later when the model actually tries to load |

## Particles (`particles.zig: register()` + `EmitterProperties`/`SpawnShape`/`DirectionMode`)

| Field | Type | Engine default if missing | Notes |
|---|---|---|---|
| `.texture` | string | **required** | **missing → `"Particle texture id was not specified for {id}"` and the particle type fails to register entirely** (hard failure, not a soft fallback) |
| texture dimensions | -- | -- | **base texture height must be an exact multiple of its width** (used to slice animation frames) or logs `"Particle base texture has incorrect dimensions ({w}x{h}) expected height to be multiple of width..."`; if an emission texture (`_emission.png`) is present, **its frame count must match the base texture's** or logs a frame-count-mismatch error |
| `.rotationVelocity` | `{min, max}` | `{20, 60}` | matches website; **values are interpreted as degrees and converted to radians internally** |
| `.density` | `{min, max}` | `{2, 3}` | matches website |
| `.dragCoefficient` | `{min, max}` | `{0.5, 0.6}` | matches website |
| `.loopTime` | `{min, max}` | none | **not exposed by the website form** |
| `.speed` | `{min, max}` | `{1, 1.5}` | matches website; parsed separately via `EmitterProperties.parse`, not in `register()` -- see note below |
| `.lifeTime` | `{min, max}` | `{0.75, 1}` | matches website; same note |
| `.randomRotate` | bool | `true` | website always writes an explicit value from the checkbox, so this default rarely applies in practice |
| `.mode` | enum string: `spread`/`scatter`/`direction` | `spread` if missing; **invalid string → `"Error while parsing direction mode"`, falls back to `spread`** | |
| `.direction` | Vec3f | `{0, 0, 1}` | matches website default (dirZ=1.0) |
| `.shape` | enum string: `point`/`sphere`/`cube` | `point` if missing; **invalid string → `"Error while parsing particle spawn data"`, falls back to a point shape** | |

Important structural note: `.texture`/`.rotationVelocity`/`.density`/`.dragCoefficient` are
validated once, at particle-*type* registration time (`register()`, called when the addon
loads). `.speed`/`.lifeTime`/`.shape`/`.mode`/`.direction` are **emitter** properties, parsed
separately (`EmitterProperties.parse`/`SpawnShape.parse`/`DirectionMode.parse`) whenever
something actually spawns this particle type. So a broken emitter-side field won't cause an
error at world-load time -- it only surfaces when something in the world actually triggers that
particle effect, which makes it a harder class of bug to catch just from load-time logs.
