# [easy/docs_CONTENT_SUGGESTIONS.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz, texture guidelines, structure building blocks, game design principles, reference implementation, color palettes, contrast, tiling, hue shifting, item outlines, volume optimization
**Symbols:** cubyz:void, /toggledecay
**Concepts:** Game Design Principles, Texture Requirements, Structure Building Blocks

## Summary
Provides guidelines for suggesting content additions to Cubyz, including texture requirements and structure building block considerations.

## Explanation
Cubyz does not accept low-effort content suggestions. Before suggesting: check the suggestion follows the Game Design Principles, build a reference implementation as an addon/mod/fork (no content copied from other games), follow the requirements below if applicable, and open a PR or a blank-template issue with screenshots. Texture requirements (a rejected texture if any are ignored): resolution must be 16 x 16; lighting direction must be top-left for items and blocks; keep color palettes small (~4-6 colours per block, no near-duplicate colours, no noise/filter/brush artifacts); reference other block textures for colour/contrast consistency and test in-game; blocks must tile smoothly with no seams/repetition; use hue shifting conservatively, accounting for the material; items need a full 1-pixel coloured outline, shaded so the top-left (lit) side is brighter and bottom-right (shadow) side darker; items should have higher contrast than their block counterparts. Textures may be edited or replaced by the team to keep a consistent art style. careeoki has made the majority of Cubyz's art and is the contact point (via Discord) for further texture questions. Structure Building Blocks (SBBs): **structures often generate on a slope or above a cave, exposing their underside -- so the structure should continue underground and include roots where applicable;** fill structures with `cubyz:void` blocks before saving unless terrain replacement is actually wanted; convert degradable blocks (leaves, branches) using `/toggledecay`; capture the smallest volume possible, since these structures aren't cheap; split bulk-appearing structures into multiple randomized parts to avoid visible repetition; rare fun variants (e.g. inspired by the bolete mushroom base) are encouraged.

## Related Questions
- What texture resolution does Cubyz require for new textures?
- What lighting direction should Cubyz item and block textures use?
- Who made the majority of the art for Cubyz?
- What is the recommended color palette size for textures in Cubyz?
- What are some guidelines for creating smooth block tiling in Cubyz?
- What is the purpose of hue shifting in Cubyz textures?
- What is the recommended contrast level for items compared to blocks in Cubyz?
- How should rare fun variants be encouraged in Cubyz structures?
- What command toggles decay on structure building blocks in Cubyz?
- What are some tips for capturing the smallest volume possible when creating structures in Cubyz?
- How can I split a large structure into multiple randomized parts to avoid repetition in Cubyz?

*Source: unknown | chunk_id: docs_CONTENT_SUGGESTIONS.md_chunk_0*
