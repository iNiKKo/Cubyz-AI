# [issues/issue_704.md] - Issue #704 discussion

**Type:** review
**Keywords:** crash, empty name, unicode, validation, multiplayer, camouflage, survival mode, faction system
**Concepts:** game crash, player names, Unicode characters, user input validation

## Summary
Discussion about preventing game crashes when players with empty names join, leading to suggestions and counterarguments regarding the feasibility of enforcing non-empty player names.

## Explanation
Discussion about preventing game crashes when players with empty names join. The maintainer acknowledges that making blank player names impossible is complex due to various Unicode characters like zero width spaces (​). Suggestions include requiring at least one valid character (numbers or letters) in player names, but this raises concerns about usability and potential advantages of having a blank name for hiding oneself in multiplayer scenarios. Additionally, the maintainer mentions that a faction system similar to Terraria could address visibility issues by allowing players to see only their allies from a distance.

## Related Questions
- How can the game be modified to prevent crashes when players with empty names join?
- What are the potential challenges in making blank player names impossible due to Unicode characters like zero width spaces (​)?
- Why is it suggested to require at least one valid character (numbers or letters) in player names?
- How could a faction system like in Terraria address visibility issues in multiplayer?

*Source: unknown | chunk_id: github_issue_704_discussion*
