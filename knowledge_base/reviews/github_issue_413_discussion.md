# [issues/issue_413.md] - Issue #413 discussion

**Type:** review
**Keywords:** tp command, player names, color codes, duplicate names, centralized authority, unicode, autocomplete
**Concepts:** player identification, color codes, name uniqueness, autocomplete

## Summary
Discussion on handling player names with color codes in the /tp command. Proposals include ignoring color codes or preventing duplicate names regardless of colors, but these solutions face challenges such as lack of centralized authority and issues with Unicode.

## Explanation
The issue revolves around the difficulty of implementing a /tp (teleport) command that correctly identifies players by name when those names contain color codes. The main proposals are to either ignore color codes during searches or to enforce unique player names regardless of color, but both approaches have significant drawbacks. Ignoring color codes could lead to confusion if multiple players have the same base name but different colors. Enforcing unique names would be impractical due to lack of a centralized authority to manage and verify names globally. Additionally, Unicode complicates these solutions further. The maintainer suggests that autocomplete functionality (#1977) is a more viable solution, as it could provide suggestions based on previously known aliases, potentially addressing the issue without requiring strict name uniqueness.

## Related Questions
- How can the /tp command be modified to handle player names with color codes?
- What are the potential drawbacks of ignoring color codes in player name searches?
- Why is enforcing unique player names regardless of colors impractical?
- How could autocomplete functionality address the issue of handling player names with color codes?
- What challenges does Unicode present when implementing solutions for player name identification?
- Can a centralized authority be established to manage and verify player names globally?

*Source: unknown | chunk_id: github_issue_413_discussion*
