# [issues/issue_2720.md] - Issue #2720 discussion

**Type:** review
**Keywords:** consolidation, frame block, transparent, validation, torch lighting, lanterns, lamps, fuels, materials, design
**Symbols:** lantern frame, lamp, fuel, torch
**Concepts:** block design, fuel validation, lighting mechanism

## Summary
Discussion on consolidating lantern and lamp blocks into a single frame block that accepts different fuels, with considerations for transparency and lighting mechanisms.

## Explanation
The discussion revolves around the idea of creating a unified 'lantern frame' block that can be filled with various fuels to produce differently colored lanterns. This approach aims to reduce the number of separate blocks needed for each combination of fuel and material. The maintainer notes that lamps, unlike lanterns, are not transparent, which is an important distinction. There's also a discussion on how to validate fuel types and whether using a torch to light the lanterns would be more practical in terms of cost and clarity.

## Related Questions
- How can the fuel validation be implemented to ensure only valid fuels are used in the lantern frame?
- What is the proposed method for transforming the fuel into a block type that matches the model and has a handmade texture?
- Why was it decided to use a torch for lighting the lanterns instead of directly using the fuel?
- How will the transparency difference between lanterns and lamps be handled in the game mechanics?
- What are the potential performance implications of consolidating multiple block types into one frame block?
- How can the design ensure that different metals used as fuels do not conflict with each other in terms of properties?

*Source: unknown | chunk_id: github_issue_2720_discussion*
