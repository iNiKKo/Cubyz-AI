# [easy/docs_CONTENT_SUGGESTIONS.md] - Chunk 0

**Type:** configuration
**Keywords:** texture, resolution, lighting, color palette, tiling, hue shifting, outlines, contrast, structure building blocks, underground, roots, void blocks, degradable variants, volume capture, randomization
**Symbols:** /toggledecay, cubyz:void
**Concepts:** Content Suggestion Requirements, Texture Guidelines, Structure Building Block Rules

## Summary
The document outlines strict requirements for content suggestions, specifically detailing texture style guidelines and structure building block rules.

## Explanation
Content suggestions must adhere to Game Design Principles and include a reference implementation; textures require specific resolution (16x16), lighting direction (top-left), limited color palettes (~4-6 colors), smooth tiling, conservative hue shifting, full colored outlines on items with appropriate shading, and higher contrast than blocks. Structure Building Blocks must extend underground with roots where applicable, be filled with cubyz:void before saving unless replacing terrain with air, use degradable variants via /toggledecay for trees, capture the smallest possible volume to avoid cost penalties, split bulk appearances into randomized parts, and include rare fun variants.

## Related Questions
- What is the required resolution for new textures in Cubyz?
- How should lighting direction be handled when creating item and block textures?
- Which command must be used to convert degradable blocks like leaves before saving structures?
- What block type should fill structures before saving unless replacing terrain with air?
- Why is capturing the smallest volume important for structure building blocks?
- How can bulk-appearing structures avoid visible repetition according to the guidelines?
- Who created the majority of the art for Cubyz and where can they be contacted on Discord?
- What specific shading rule applies to item outlines in Cubyz textures?
- Are near-duplicate colors allowed in Cubyz texture palettes?
- Do structure building blocks need to extend underground with roots when generating on slopes?
- Can noise, filters, or brushes be used to create unnecessary amounts of colors for Cubyz textures?
- What is the recommended approach for handling rare fun variants in structure suggestions?

*Source: unknown | chunk_id: docs_CONTENT_SUGGESTIONS.md_chunk_0*
