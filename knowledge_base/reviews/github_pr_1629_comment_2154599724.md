# [src/graphics.zig] - PR #1629 review diff

**Type:** review
**Keywords:** TextRendering, freetypeFace, textureHeight, units_per_EM, fontUnitPerPixel, harfbuzzFace, harfbuzzFont, FT_Set_Pixel_Sizes, hb_ft_face_create_referenced, hb_font_create
**Symbols:** TextRendering, ftError, hbft.FT_Set_Pixel_Sizes, freetypeFace, harfbuzzFace, hbft.hb_ft_face_create_referenced, harfbuzzFont, hbft.hb_font_create, fontUnitPerPixel
**Concepts:** pointer handling, field access, text rendering, font scaling

## Summary
Added calculation of fontUnitPerPixel to handle font scaling correctly.

## Explanation
The change introduces a new variable `fontUnitPerPixel` which calculates the ratio of font units per pixel by dividing the units_per_EM value from the freetypeFace by the textureHeight. This is necessary for accurate text rendering and scaling. The reviewer noted that accessing fields without dereferencing the pointer type `[c]cimport.struct_FT_FaceRec_` leads to an error, highlighting the importance of proper pointer handling in this context.

## Related Questions
- What is the purpose of calculating fontUnitPerPixel in this code?
- Why is proper pointer handling crucial in this context?
- How does the calculation of fontUnitPerPixel affect text rendering?
- What error was reported if field access without dereferencing was attempted?
- Can you explain the role of units_per_EM in font scaling?
- How does the introduction of fontUnitPerPixel prevent potential errors?

*Source: unknown | chunk_id: github_pr_1629_comment_2154599724*
