# [issues/issue_345.md] - Issue #345 discussion

**Type:** review
**Keywords:** Block inventory item textures, non-cube blocks, cross models, torches, fences, item texture, oak_fence.json, wood class, hardness attribute, drops array, absorbedLight property, rotation setting, model specification, texture field, texture_top field
**Symbols:** oak_fence.json, wood, hardness, drops, absorbedLight, rotation, model, texture, texture_top, texture_bottom, item, materials/stick.png
**Concepts:** block definition, inventory representation, texture mapping

## Summary
Allow blocks to specify a 2D item texture for inventory display, particularly useful for non-cube block models.

## Explanation
This change introduces a new feature that enables blocks to define a specific texture for their item representation in the inventory. This is beneficial for blocks with complex geometries like fences and torches, which cannot be accurately represented by default cube textures. The maintainer provides an example configuration for an oak fence block as follows:

```json
{
    "class" : "wood",
    "hardness" : 7,
    "drops" : [
        "auto"
    ],
    "absorbedLight" : 0x202830,
    "rotation" : "fence",
    "model" : "fence",
    "texture" : "cubyz:oak_fence",
    "texture_top" : "cubyz:oak_fence_top",
    "texture_bottom" : "cubyz:oak_fence_top",
    "item": {
        "texture" : "materials/stick.png"
    }
}
```
The example demonstrates how to specify both general block textures and a separate item texture. The `item` field contains the path to the 2D texture used for inventory display, which must be placed within the 'items' folder to ensure proper loading. Additionally, the configuration includes specific attributes such as hardness (7), drops array with auto value, absorbed light property (0x202830), and rotation setting ('fence').

## Related Questions
- What is the purpose of specifying a separate item texture for blocks?
- Where should the item textures be placed according to the maintainer's comment?
- How does this change affect the representation of non-cube blocks in the inventory?
- Can you provide an example of how to define an item texture for a block in the JSON configuration?
- What is the significance of the 'items' folder mentioned in the discussion?
- How might this feature impact the loading performance of block textures?

*Source: unknown | chunk_id: github_issue_345_discussion*
