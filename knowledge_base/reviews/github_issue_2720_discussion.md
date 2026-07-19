# [issues/issue_2720.md] - Issue #2720 discussion

**Type:** review
**Keywords:** consolidation, frame block, transparent, validation, torch lighting, lanterns, lamps, fuels, materials, design
**Symbols:** lantern frame, lamp, fuel, torch
**Concepts:** block design, fuel validation, lighting mechanism

## Summary
Discussion on consolidating lantern and lamp blocks into a single frame block that accepts different fuels, with considerations for transparency and lighting mechanisms.

## Explanation
Discussion on consolidating lantern and lamp blocks into a single 'lantern frame' block that accepts various fuels. The maintainer notes that lamps are not transparent, unlike lanterns. A method is proposed for transforming fuel into another block type upon placement to match the model with handmade textures. Using a torch instead of direct fuel insertion is suggested as it clarifies what can be used to light lanterns and reduces costs.

## Related Questions
- How will the 'lantern frame' block transform fuels into different block types on placement?
- Why was using a torch chosen over directly inserting fuel for lighting lanterns?

*Source: unknown | chunk_id: github_issue_2720_discussion*
