# Cubyz Addon Creator: UI → Export Field Reference

This document maps every Addon Creator Studio form field to its internal `projectData` property
and its exact serialized `.zig.zon` output. Compiled by reading `app-save.js` (the save/export
logic) in full, cross-checked against `app-io.js`'s import logic (which parses the same
`.zig.zon` fields back out via regex to repopulate the form -- confirming these mappings are
stable and bidirectional).

## How it works, end to end

1. User fills in a form (`blocks.html`, `items.html`, etc.).
2. Clicking "Save to Project" calls the matching `saveXToProject()` function in `app-save.js`,
   which reads the DOM fields by ID and pushes a plain object into `window.projectData.X`.
3. Clicking "Export Full Addon" calls `exportFullAddon()`, which walks every object in
   `window.projectData` and writes it out as a `.zig.zon` file (via template-string
   concatenation) inside a zip, organized into the standard Cubyz addon folder layout
   (`blocks/`, `items/`, `biomes/`, `entityModels/`, `particles/`, `recipes/`).
4. Importing an existing addon (`importExistingAddon()` in `app-io.js`) does the exact reverse:
   regex-parses the `.zig.zon` text of each file back into the same internal field names,
   repopulating `window.projectData` and the form.

Two conventions apply almost everywhere:
- **Namespace auto-prefixing**: cross-references (a block's drop item, a biome's surface block,
  a recipe's ingredients) get auto-prefixed with `{addonName}:` if the referenced ID matches
  something already defined in the current project, or `cubyz:` otherwise (assumed vanilla
  asset). An explicit `:` in the input bypasses this entirely.
- **ID sanitization**: ID fields are lowercased and stripped to `[a-z0-9_]` before use as a
  filename.

---

## Blocks (`blocks.html` → `saveBlockToProject` → `blocks/{id}.zig.zon`)

| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| (Block ID, in toolbar) | `blockId` | `id` | filename | sanitized |
| Base Texture (Default/Back) | `topSearch` | `baseTexture` | `.texture = "{addon}:{tex}"` | only emitted if no directional side textures are set |
| Render Mode | `blockRotation` | `rotation` | `.rotation = "{value}"` | `"cubyz:ore"` triggers a separate `.ore = {...}` block with fixed vein params, and requires an item icon |
| Up/Bottom/Front/Back/Right/Left texture slots | `upSearch`/`bottomSearch`/`frontSearch`/`backSearch`/`rightSearch`/`leftSearch` | `sides.{up,bottom,front,back,right,left}` | `.texture0`..`.texture5` respectively | index order is up=0, bottom=1, front=2, back=3, right=4, left=5 -- **not** alphabetical or form order |
| Texture Slot 6-15 | `tex6`..`tex15` | `sides.tex6`..`tex15` | `.texture6`..`.texture15` | extra material slots for custom models |
| Block Health | `blockHealth` | `health` | `.blockHealth = {v.toFixed(1)}` | |
| Blast Resistance | `blockResistance` | `resistance` | `.blockResistance = {v.toFixed(1)}` | |
| (checkbox) Collide | `blockCollide` | `collide` | `.collide = {bool}` | omitted entirely for ore blocks |
| (checkbox) Transparent | `blockTransparent` | `transparent` | `.transparent = {bool}` | omitted entirely for ore blocks |
| (checkbox) Replaceable/Degradable/ViewThrough/AlwaysViewThrough/HasBackFace/AllowOres | matching IDs | same-named property | same-named field | direct boolean passthrough |
| Friction/Bounciness/Density/Terminal Vel./Mobility | `blockFriction` etc | same-named | `.friction`/`.bounciness`/`.density`/`.terminalVelocity`/`.mobility` | floats, 1-2 decimal places |
| Emitted/Absorbed Light Color (hex picker) | `emittedLightColor`/`absorbedLightColor` | parsed to int | `.emittedLight`/`.absorbedLight` | hex → integer via `parseInt(hex, 16)`; only emitted if non-default |
| Walking on the block (touch type/mode/dps/element) | `logicTouchType`/`logicTouchMode`/`logicTouchDps`/`logicTouchTypeVariant` | `callbacks.touch*` | `.onTouch = {.type=.hurt, .dps=..., .damageType=...}` | only if touch type is "hurt"; "heal" mode negates dps |
| Raw Update/Tick/Break hooks + replacement targets | `logicUpdateType`/`logicTickType`/`logicBreakType` + `*ReplaceBlockSearch` | `callbacks.updateType` etc | `.onUpdate`/`.onTick`/`.onBreak` | shared `compHook()` builder; omitted if type is "none"; "decay" type needs replacement+prevention, "replace_block" needs an auto-namespaced target |
| onInteract type + UI Window Layout ID | `logicInteractType`/`interactWindowName` | `callbacks.interactType`/`interactWindowName` | `.onInteract = {.type=..., .name="..."}` | `.name` only present for `open_window` type |
| Mining Drop Item Selection | `dropAuto` (checkbox) + `dropSearch` | `dropAuto`/`dropSearch` | `.drops` | auto → `.{.items=.{.auto}}`; manual → specified item, auto-namespaced |
| (checkbox) Has Item Icon + 2D Inventory Icon Texture | `hasItemIcon`/`itemIconSearch` | same | `.item = {.texture="{icon}.png"}` inline, OR a companion `items/{id}.zig.zon` file with `.block="{addon}:{id}"` | if no icon set, a matching item file is auto-generated referencing the block |
| Tags (pill UI) | `blockTagsContainer` | `tags[]` | `.tags = .{.tag1, .tag2}` | |

## Items (`items.html` → `saveItemToProject` → `items/{id}.zig.zon`)

| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| (Item ID) | `itemId` | `id` | filename | |
| Item Sprite Texture | `itemTextureSearch` | `texture` | `.texture = "{basename}.png"` | path stripped to basename |
| Max Stack Size | `itemStackSize` | `stackSize` | `.stackSize = {v}` | only emitted if ≠ 120 (default) |
| Food Saturation Value | `itemFoodValue` | `foodValue` | `.food = {v.toFixed(1)}` | only if > 0 |
| (linked block, no direct label) | `itemBlockPlacementSearch` | `blockPlacement` | `.block = "{ref}"` | auto-namespaced |
| Tags | `itemTagsContainer` | `tags[]` | `.tags = .{...}` | |
| Material Color (hex picker) | `matColorBase` | `baseColor`, expanded to `colors[]` | `.colors = .{0xff..., ...}` | base hex is converted to HSL, then re-sampled at 5 lightness steps (0.22/0.38/0.52/0.72/0.88) to generate a shading gradient; only emitted if item has the `.material` tag |
| Durability | `matDurability` | `material.durability` | `.material.durability` | only emitted if `.material` tag present |
| Swing Speed | `matSwingSpeed` | `material.swingSpeed` | `.material.swingSpeed` | " |
| Texture Roughness | `matTexRoughness` | `material.textureRoughness` | `.material.textureRoughness` | " |
| Mass Damage | `matMassDamage` | `material.massDamage` | `.material.massDamage` | " |
| Hardness Damage | `matHardnessDamage` | `material.hardnessDamage` | `.material.hardnessDamage` | " |
| (modifier type/strength, no direct label) | `matModifierType`/`matModifierStrength` | `material.modifierType`/`modifierStrength` | `.material.modifiers = .{.{.id=.type, .strength=v}}` | only if modifier type ≠ "none" |

## Recipes (`recipes.html` → `saveRecipeToProject` → `recipes/{filename}_recipes.zig.zon`)

| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| Recipe ID (Filename) | `recipeFilename` | key in `projectData.recipes{}` | filename | multiple recipes can share a file (array per filename) |
| What item does this craft? + Amount Made | `recipeOutputSearch`/`recipeOutputCount` | `output` | `.output = "{count} {item}"` | count prefix omitted if 1; auto-namespaced |
| Ingredient slots 1-4 + counts | `recipeInputSearch1-4`/`recipeInputCount1-4` | `inputs[]` | `.inputs = .{"{count} {item}", ...}` | empty slots skipped; up to 4 ingredients |

## Biomes (`biomes.html` → `saveBiomeToProject` → `biomes/{id}.zig.zon`)

| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| (Biome ID) | `biomeId` | `id` | filename | |
| Generation Chance | `biomeChance` | `chance` | `.chance = {v.toFixed(2)}` | |
| Border Interpolation | `bioInterpolation` | `interpolation` | `.interpolation = {v}` | raw enum passthrough |
| Min/Max Cluster Radius | `bioMinRadius`/`bioMaxRadius` | same | `.minRadius`/`.maxRadius` | no decimal formatting |
| Min/Max Height, Min Floor/Max Ceiling Limit | `bioMinHeight`/`bioMaxHeight`/`bioMinHeightLimit`/`bioMaxHeightLimit` | same | matching fields | raw passthrough |
| Roughness/Hills/Mountains/Soil Creep/Keep Original Mix Factors | `bioRoughness` etc | same | `.roughness` etc | `.toFixed(2)` |
| Top Surface / Subsurface / Bottom Stone Layer | `bioSurfaceBlock`/`bioSubBlock`/`bioStoneBlock` | via `autoNamespaceBlock()` | `.ground_structure = .{"{surface}", "0 to 3 {sub}"}` + separate `.stoneBlock` | surface/sub combined into one field, stone separate |
| (checkbox) Is Cave | `bioIsCave` | `isCave` | `.isCave = {bool}` | gates whether cave-only fields below are emitted at all |
| Cave Density Scale / Openness Radius Factor / Glow Crystal Frequency | `bioCaves`/`bioCaveRadiusFactor`/`bioCrystals` | same | `.caves`/`.caveRadiusFactor`/`.crystals` | **only emitted if `isCave` is checked** |
| Ambient Music Track | `bioMusic` | `music` | `.music = "{track}"` | default `cubyz:sunrise` |
| Fog Thickness Density | `bioFogDensity` | `fogDensity` | `.fogDensity = {v.toFixed(2)}` | |
| Sky Tint / Fog Atmospheric Tint (hex pickers) | `bioSkyColor`/`bioFogColor` | converted to normalized RGB | `.skyColor`/`.fogColor = .{r, g, b}` | hex → 0-1 float vector |
| (checkbox, no visible label found) | `bioSpawn` | `isValidPlayerSpawn` | `.isValidPlayerSpawn = {bool}` | |
| Climate/Humidity/Zone/Growth/Elevation radio groups | `bioTemp`/`bioWet`/`bioZone`/`bioGrowth`/`bioHeightProp` (radio inputs, `name=` not `id=`) | `properties[]` | `.properties = .{.val1, .val2, ...}` | **all 5 groups' checked values are flattened into one combined list**, not kept separate |
| Structure rows (dynamic list, `.structure-row-entry`) | per-row `.struct-type-selector` + type-specific fields | `structures[]` | `.structures = .{...}` | most complex mapping -- schema depends entirely on selected type: `simple_tree` needs log/leaves/top/height/height_variation/leafRadius; `simple_vegetation`/`flower_patch`/`boulder`/`ground_patch` each need a `block` plus different size fields; `fallen_tree` needs log/top/height; `sbb` needs structure+placeMode |

## Entities (`entities.html` → `saveEntityToProject` → `entityModels/{id}.zig.zon`)

| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| (Entity ID) | `entityId` | `id` | filename | |
| Height | `entityHeight` | `height` | `.height = {v.toFixed(1)}` | |
| Coordinate System | `entityCoordSystem` | `coordinateSystem` | `.coordinateSystem = {v}` | default `.right_handed_z_up` |
| Model | `entityModelSearch` | `model` | `.model = "{addon}:{model}"` | |
| Texture | `entityTextureSearch` | `defaultTexture` | `.defaultTexture = "{addon}:{tex}"` | |
| Tags | `entityTagsContainer` | `tags[]` | `.tags = .{...}` | block omitted entirely if no tags |

## Particles (`particles.html` → `saveParticleToProject` → `particles/{id}.zig.zon`)

| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| (Particle ID) | `particleId` | `id` | filename | |
| Particle Texture | `particleTextureSearch` | `texture` | `.texture = "{ref}"` | auto-namespaced |
| (checkbox, has emission) | `particleHasEmission` | `hasEmission` | -- | doesn't write a field directly; controls whether a companion `{texture}_emission` texture file is also bundled into the export |
| Speed/Life/Density/Rotation Velocity/Drag min+max pairs | `particleSpeedMin/Max` etc | matching min/max properties | `.speed`/`.lifeTime`/`.density`/`.rotationVelocity`/`.dragCoefficient = {.min=..., .max=...}` | |
| (checkboxes) Random Rotate / Collides | `particleRandomRotate`/`particleCollides` | same | `.randomRotate`/`.collides` | direct boolean passthrough |
| Spawn Shape | `particleSpawnShape` | `shape` | `.shape = .{shape}` | `sphere` adds `.radius` (from `particleShapeRadius`); `cube` adds `.size` (from `particleShapeSize`) |
| Spawn Direction | `particleDirectionMode` | `mode` | `.mode = .{mode}` | `direction` mode adds `.direction = .{x, y, z}` from `particleDirX/Y/Z` |
