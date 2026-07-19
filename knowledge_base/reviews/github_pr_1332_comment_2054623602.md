# [src/items.zig] - PR #1332 review diff

**Type:** review
**Keywords:** MaterialProperty, strength, grip, density, enum, default, replacement, ignored, asset designer, scaling
**Symbols:** Modifier, MaterialProperty, fromString
**Concepts:** enum handling, error handling, default values

## Summary
Removed 'strength' and 'grip' from MaterialProperty enum and changed the default replacement from 'strength' to 'density'.

## Explanation
The reviewer suggests that invalid material properties should be ignored instead of replaced with a default value, as there is no universally appropriate default. The current change removes both 'strength' and 'grip' from the MaterialProperty enum and changes the default replacement from 'strength' to 'density' when an unknown property is encountered. The reviewer argues that this is arbitrary and could lead to incorrect scaling assumptions by asset designers. The reviewer proposes adding an 'ignored' enum value to handle such cases more appropriately.

## Related Questions
- Why were 'strength' and 'grip' removed from the MaterialProperty enum?

*Source: unknown | chunk_id: github_pr_1332_comment_2054623602*
