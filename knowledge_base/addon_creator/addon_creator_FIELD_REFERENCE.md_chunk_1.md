# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 1

**Type:** documentation
**Keywords:** blocks.html, saveBlockToProject, texture slots, render mode, ore, blockHealth, blockResistance, onTouch, onInteract, drops, item icon
**Symbols:** blockId, blockRotation, upSearch, dropAuto, hasItemIcon

## Summary
Cubyz Addon Creator: Blocks form (`blocks.html`) field-to-export mapping.

## Explanation
Block ID (form field `blockId`) becomes the filename, sanitized. Base Texture (`topSearch`) exports as `.texture = "{addon}:{tex}"`, only emitted if no directional side textures are set. Render Mode (`blockRotation`) exports as `.rotation = "{value}"` -- setting it to `"cubyz:ore"` triggers a separate `.ore = {...}` block with fixed vein params, and requires an item icon. The six directional texture slots (up/bottom/front/back/right/left, fields `upSearch`/`bottomSearch`/`frontSearch`/`backSearch`/`rightSearch`/`leftSearch`) export as `.texture0` through `.texture5` respectively -- index order is up=0, bottom=1, front=2, back=3, right=4, left=5, **not** alphabetical or form order. Texture slots 6-15 (`tex6`..`tex15`) export as `.texture6`..`.texture15`, extra material slots for custom models.

Block Health (`blockHealth`) exports as `.blockHealth`. Blast Resistance (`blockResistance`) exports as `.blockResistance`. The Collide and Transparent checkboxes export as `.collide`/`.transparent` -- **both are omitted entirely for ore blocks**. Replaceable/Degradable/ViewThrough/AlwaysViewThrough/HasBackFace/AllowOres checkboxes are direct boolean passthroughs. Friction/Bounciness/Density/Terminal Velocity/Mobility export as floats. Emitted/Absorbed Light Color hex pickers convert hex to an integer via `parseInt(hex, 16)`, only emitted if non-default.

Touch callback (type/mode/dps/element) exports as `.onTouch = {.type=.hurt, .dps=..., .damageType=...}`, only if touch type is "hurt"; "heal" mode negates the dps value. Update/Tick/Break hooks export as `.onUpdate`/`.onTick`/`.onBreak`, omitted if type is "none"; the "decay" type needs a replacement block plus a prevention setting, "replace_block" needs an auto-namespaced target. onInteract type + UI Window Layout ID export as `.onInteract = {.type=..., .name="..."}` -- `.name` is only present for the `open_window` type.

Mining Drop (checkbox `dropAuto` + `dropSearch`) exports as `.drops` -- **auto exports the literal syntax `.{.items=.{.auto}}`** (drops the block itself); **manual** exports the specified item, and that item reference is **auto-namespaced** (same namespace-prefixing convention as every other cross-reference). Has Item Icon + texture: if set, exports `.item = {.texture="{icon}.png"}` inline; **if no icon is set, a companion `items/{id}.zig.zon` file is auto-generated instead, referencing the block via `.block="{addon}:{id}"`**. Tags (pill UI) export as `.tags = .{.tag1, .tag2}`.

## Related Questions
- Which texture slot index corresponds to the block's 'left' side in the Cubyz Addon Creator?
- What does setting a Cubyz block's render mode to "cubyz:ore" trigger, and what else does it require?
- What two block boolean fields does the Cubyz Addon Creator omit entirely for ore blocks?
- How does the Cubyz Addon Creator convert a block's emitted/absorbed light color for export?
- What does the "heal" touch mode do to the dps value for a Cubyz block's onTouch callback?
- What does the "decay" onUpdate/onTick/onBreak hook type need?
- What does the "replace_block" hook type need?
- When is the .name field present in a Cubyz block's onInteract export?
- What's the difference between "auto" and manual drop selection for a Cubyz block?
- What happens if a Cubyz block has no item icon set in the Addon Creator?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_1*
