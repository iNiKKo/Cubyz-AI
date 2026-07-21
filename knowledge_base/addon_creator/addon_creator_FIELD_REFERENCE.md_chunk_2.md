# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 2

**Type:** documentation
**Keywords:** items.html, saveItemToProject, stackSize, foodValue, material, matColorBase, durability, swingSpeed, textureRoughness
**Symbols:** itemId, itemStackSize, matDurability, matModifierType

## Summary
Cubyz Addon Creator: Items form (`items.html`) field-to-export mapping.

## Explanation
Item ID (`itemId`) becomes the filename. Item Sprite Texture (`itemTextureSearch`) exports as `.texture = "{basename}.png"`, path stripped to basename. Max Stack Size (`itemStackSize`) exports as `.stackSize`, only emitted if not equal to 120 (the default). Food Saturation Value (`itemFoodValue`) exports as `.food`, **only emitted if greater than 0**. The linked block field exports as `.block = "{ref}"`, auto-namespaced. Tags export as `.tags = .{...}`.

Material Color hex picker (`matColorBase`) is converted to HSL, then re-sampled at 5 lightness steps (0.22/0.38/0.52/0.72/0.88) to generate a shading gradient, exported as `.colors = .{0xff..., ...}` -- **only emitted if the item has the `.material` tag**. Durability (`matDurability`), Swing Speed (`matSwingSpeed`), Texture Roughness (`matTexRoughness`), Mass Damage (`matMassDamage`), and Hardness Damage (`matHardnessDamage`) all export as their matching `.material.*` fields, and are **all only emitted if the `.material` tag is present**. Modifier type/strength export as `.material.modifiers = .{.{.id=.type, .strength=v}}`, only if the modifier type isn't "none".

## Related Questions
- When is a Cubyz item's food value field emitted in the Addon Creator's export?
- How does the Cubyz Addon Creator generate an item's shading gradient from its material color?
- When are a Cubyz item's material fields (durability, swingSpeed, etc.) emitted by the Addon Creator?
- What's the default max stack size a Cubyz item is assumed to have if the field is omitted?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_2*
