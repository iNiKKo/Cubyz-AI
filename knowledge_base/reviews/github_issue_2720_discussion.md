# [issues/issue_2720.md] - Issue #2720 discussion

**Type:** review
**Keywords:** consolidation, frame block, transparent, validation, torch lighting, lanterns, lamps, fuels, materials, design
**Symbols:** lantern frame, lamp, fuel, torch
**Concepts:** block design, fuel validation, lighting mechanism

## Summary
Discussion on consolidating lantern and lamp blocks into a single frame block that accepts different fuels, with considerations for transparency and lighting mechanisms.

## Explanation
### Summary
Discussion on consolidating lantern and lamp blocks into a single frame block that accepts different fuels, with considerations for transparency and lighting mechanisms.

### Explanation
The discussion revolves around replacing separate blocks for sulfur and coal lanterns with a single 'lantern frame' block that can accept various fuels to light them in different colors. This approach would also apply to lamps. The maintainer notes that while frame blocks are familiar, lamps differ because they are not transparent. A user suggests using a torch to light the lanterns instead of inserting fuel directly, arguing that this makes it clearer what can be used and is more cost-effective. Another user points out that each metal that can be used as fuel needs to have another property defined by the lamp to ensure valid fuel is inserted. The maintainer proposes transforming the fuel into another block type upon placement that matches the model with handmade textures. This includes metals like copper, gold, silver, and uranium.

*Source: unknown | chunk_id: github_issue_2720_discussion*

## Related Questions
- How will the 'lantern frame' block transform fuels into different block types on placement?
- Why was using a torch chosen over directly inserting fuel for lighting lanterns?

*Source: unknown | chunk_id: github_issue_2720_discussion*
