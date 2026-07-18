# [src/items.zig] - PR #1332 review diff

**Type:** review
**Keywords:** material properties, enum, stringToEnum, memory cost, default replacement, strength, density, grip
**Symbols:** Modifier, MaterialProperty, fromString
**Concepts:** enum, memory cost, default value handling

## Summary
Removed unused material properties and changed the default replacement from 'strength' to 'density'.

## Explanation
The change involves removing two unused material properties ('strength' and 'grip') from the `MaterialProperty` enum in the `items.zig` file. The reviewer notes that this modification could introduce a memory cost due to the use of `std.meta.stringToEnum`, but points out that the fourth enum value results in exactly 0 extra bits, suggesting no additional overhead. The default replacement for unrecognized material properties is changed from 'strength' to 'density', which may affect how materials are handled in the system if such a property is encountered.

## Related Questions
- What is the impact of removing 'strength' and 'grip' from MaterialProperty?
- How does changing the default replacement affect material handling in Cubyz?
- Is there any potential memory overhead with using stringToEnum in this context?
- Can you explain why the fourth enum value results in 0 extra bits?
- What are the implications of this change for backward compatibility?
- How might this modification affect performance in scenarios involving material properties?

*Source: unknown | chunk_id: github_pr_1332_comment_2054644152*
