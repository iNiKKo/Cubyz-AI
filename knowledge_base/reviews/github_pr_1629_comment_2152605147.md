# [src/graphics.zig] - PR #1629 review diff

**Type:** review
**Keywords:** TextRendering, FT_Set_Pixel_Sizes, freetypeFace, units_per_EM, textureHeight, fontUnitPerPixel, dereference, suggestion
**Symbols:** TextRendering, ftError, hbft.FT_Set_Pixel_Sizes, freetypeFace, harfbuzzFace, hbft.hb_ft_face_create_referenced, harfbuzzFont, hbft.hb_font_create, fontUnitPerPixel
**Concepts:** memory safety, code readability

## Summary
A reviewer suggests removing the explicit dereference of `freetypeFace` in the calculation of `fontUnitPerPixel`. The reviewer believes it is unnecessary.

## Explanation
The change involves modifying the line where `fontUnitPerPixel` is calculated. The original code explicitly dereferences `freetypeFace` using `.*`, which is not necessary according to the reviewer. The reviewer's suggestion simplifies the expression by directly accessing the field without the dereference, potentially improving readability and reducing potential errors.

## Related Questions
- What is the purpose of `ftError` in this code snippet?
- How does `hbft.FT_Set_Pixel_Sizes` function relate to font rendering?
- Why was the explicit dereference removed from `freetypeFace`?
- Can you explain the role of `units_per_EM` in font metrics?
- What is the impact of removing the dereference on performance?
- How does this change affect memory safety in the code?

*Source: unknown | chunk_id: github_pr_1629_comment_2152605147*
