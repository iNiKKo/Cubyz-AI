# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 2

**Type:** documentation
**Keywords:** items.html, saveItemToProject, stackSize, foodValue, material, matColorBase, durability, swingSpeed, textureRoughness
**Symbols:** itemId, itemStackSize, matDurability, matModifierType

## Summary
Cubyz Addon Creator: Items form (`items.html`) field-to-export mapping.

## Explanation
Block ID (`blockId`) becomes the filename. Base Texture (`topSearch`) exports as `.texture = "{addon}:{tex}"`, only emitted if no directional side textures are set. Render Mode (`blockRotation`) exports as `.rotation = "{value}"`. Up/Bottom/Front/Back/Right/Left texture slots (`upSearch`/`bottomSearch`/`frontSearch`/`backSearch`/`rightSearch`/`leftSearch`) export as `.texture0`..`.texture5` respectively. Texture Slot 6-15 (`tex6`..`tex15`) export as `.texture6`..`.texture15`. Block Health (`blockHealth`) exports as `.blockHealth = {v.toFixed(1)}`. Blast Resistance (`blockResistance`) exports as `.blockResistance = {v.toFixed(1)}`. Collide (`blockCollide`) and Transparent (`blockTransparent`) export as `.collide = {bool}` and `.transparent = {bool}`, omitted entirely for ore blocks. Replaceable/Degradable/ViewThrough/AlwaysViewThrough/HasBackFace/AllowOres export as same-named properties. Friction/Bounciness/Density/Terminal Vel./Mobility (`blockFriction` etc) export as `.friction`/`.bounciness`/`.density`/`.terminalVelocity`/`.mobility`, floats, 1-2 decimal places. Emitted/Absorbed Light Color (hex picker) (`emittedLightColor`/`absorbedLightColor`) exports as `.emittedLight`/`.absorbedLight`, hex → integer via `parseInt(hex, 16)`, only emitted if non-default. Walking on the block (touch type/mode/dps/element) (`logicTouchType`/`logicTouchMode`/`logicTouchDps`/`logicTouchTypeVariant`) exports as `.onTouch = {.type=.hurt, .dps=..., .damageType=...}`, only if touch type is "hurt"; "heal" mode negates dps. Raw Update/Tick/Break hooks + replacement targets (`logicUpdateType`/`logicTickType`/`logicBreakType` + `*ReplaceBlockSearch`) export as `.onUpdate`/`.onTick`/`.onBreak`, shared `compHook()` builder, omitted if type is "none"; "decay" type needs replacement+prevention, "replace_block" needs an auto-namespaced target. onInteract type + UI Window Layout ID (`logicInteractType`/`interactWindowName`) export as `.onInteract = {.type=..., .name="..."}`, `.name` only present for `open_window` type. Mining Drop Item Selection (`dropAuto` (checkbox) + `dropSearch`) exports as `.drops`, auto → `.{.items=.{.auto}}`; manual → specified item, auto-namespaced. Has Item Icon + 2D Inventory Icon Texture (`hasItemIcon`/`itemIconSearch`) export as `.item = {.texture="{icon}.png"}` inline, OR a companion `items/{id}.zig.zon` file with `.block="{addon}:{id}"`, if no icon set, a matching item file is auto-generated referencing the block. Tags (pill UI) (`blockTagsContainer`) export as `.tags = .{.tag1, .tag2}`.

## Related Questions
-  What's the default max stack size a Cubyz item is assumed to have if the field is omitted?
-  What happens if the food saturation value of a Cubyz item is set to 0 in the Addon Creator?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_2*
