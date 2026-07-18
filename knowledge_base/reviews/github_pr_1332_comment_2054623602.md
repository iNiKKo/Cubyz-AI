# [src/items.zig] - PR #1332 review diff

**Type:** review
**Keywords:** MaterialProperty, strength, grip, density, enum, default, replacement, ignored, asset designer, scaling
**Symbols:** Modifier, MaterialProperty, fromString
**Concepts:** enum handling, error handling, default values

## Summary
Removed 'strength' and 'grip' from MaterialProperty enum and changed the default replacement from 'strength' to 'density'.

## Explanation
The reviewer suggests that invalid material properties should be ignored instead of replaced with a default value, as there is no universally appropriate default. The current change replaces 'strength' with 'density' when an unknown property is encountered, but the reviewer argues that this is arbitrary and could lead to incorrect scaling assumptions by asset designers. The reviewer proposes adding an 'ignored' enum value to handle such cases more appropriately.

## Related Questions
- What is the purpose of the 'fromString' function in the MaterialProperty enum?
- Why was 'strength' removed from the MaterialProperty enum?
- How does the current implementation handle unknown material properties?
- What are the potential issues with using 'density' as a default replacement for unknown properties?
- How would adding an 'ignored' enum value improve error handling?
- What considerations should be made when choosing a default value for invalid material properties?

*Source: unknown | chunk_id: github_pr_1332_comment_2054623602*
