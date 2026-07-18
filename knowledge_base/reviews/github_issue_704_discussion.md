# [issues/issue_704.md] - Issue #704 discussion

**Type:** review
**Keywords:** crash, empty name, unicode, validation, multiplayer, camouflage, survival mode, faction system
**Concepts:** game crash, player names, Unicode characters, user input validation

## Summary
Discussion about preventing game crashes when players with empty names join, leading to suggestions and counterarguments regarding the feasibility of enforcing non-empty player names.

## Explanation
The issue revolves around fixing a crash that occurs when a player joins the game with an empty name. The maintainer initially suggests making blank player names impossible but acknowledges the complexity due to various Unicode characters that can appear as blanks. There is a suggestion to require at least one valid character (numbers or letters) in player names, which raises concerns about usability and potential advantages of having a blank name in multiplayer scenarios.

## Related Questions
- How can the game be modified to prevent crashes when players with empty names join?
- What are the potential challenges in making blank player names impossible?
- Why is it suggested to require at least one valid character in player names?
- How could a faction system like in Terraria address visibility issues in multiplayer?
- What are the implications of allowing blank names for gameplay strategies?
- How can the game handle various Unicode characters that appear as blanks?

*Source: unknown | chunk_id: github_issue_704_discussion*
