# [issues/issue_1481.md] - Issue #1481 discussion

**Type:** review
**Keywords:** Mossmans, burrowing, attack mode, spit, visual design, scraping
**Concepts:** creature design, behavior modeling

## Summary
The discussion revolves around a creature called 'Mossmans' with unique burrowing and attacking behaviors, but ultimately, the maintainer decides to scrap it.

## Explanation
The Mossmans creature was designed with unique burrowing and attacking behaviors. They spawn individually and cannot move traditionally; instead, they burrow into the ground and pop out up to 16 blocks away from their initial position. Their idle behavior includes observing other entities, wiggling, and self-grooming, occasionally relocating within their chunk. When an entity approaches that they are uncomfortable with, Mossmans enter attack mode: unburrowing near the target, looking at it for about three seconds, spitting, then burrowing again to relocate before repeating the cycle. They will always try to relocate to a spot within line-of-sight of their target and may give up if the target is out of range or moves too far away from their territory. Mossmans also join in attacks on other targets they observe being attacked for fun. The purpose of this enemy is to be a bother at long distances but easy to deal with otherwise, incidentally supporting other enemies by knocking down fleeing targets. However, despite having well-defined behavior, the visual design was lacking, leading to the decision to scrap the Mossmans for now, although its behavior might be reused in future designs.

## Related Questions
- What specific behaviors were implemented for the Mossmans creature?
- Why was the visual design of the Mossmans considered lacking?
- How does the attack mode of Mossmans work?
- Was there any consideration given to reusing the behavior of Mossmans in future designs?
- What is the purpose of the Mossmans creature in the game?
- How does the Mossmans' spit interact with other enemies?
- Is there a limit to how far Mossmans will follow their target?
- Can Mossmans be influenced by observing other entities being targeted?
- What are the health and damage characteristics of Mossmans?

*Source: unknown | chunk_id: github_issue_1481_discussion*
