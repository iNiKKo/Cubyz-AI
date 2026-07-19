# [issues/issue_2300.md] - Issue #2300 discussion

**Type:** review
**Keywords:** X-Ray, spawn inside ground, QD seed, creative mode, cheats enabled, deterministic spawning
**Concepts:** world generation, player spawning, seed-based behavior

## Summary
The issue describes a bug where players spawn inside the ground, enabling X-Ray vision, in worlds created with specific seeds like 'QD'. This behavior persists until movement or pressing ESC.

## Explanation
The issue describes a bug where players spawn inside the ground with X-Ray vision in worlds created with specific seeds like 'QD'. The behavior is consistent for certain seeds but varies based on game mode settings (creative vs. survival) and whether cheats are enabled. For example, with seed 'ReviumReviewloper', spawning inside the ground only occurs in creative mode with cheats enabled, and pressing ESC teleports the player outside the ground. This variability must be preserved. The problem arises from an unexpected interaction between world generation algorithms and player spawning logic. The discussion highlights the need to ensure deterministic player spawning regardless of seed or game configuration.

## Related Questions
- What is the code responsible for player spawning in Cubyz?
- How does world generation handle different seeds in Cubyz?
- Are there any checks to ensure players do not spawn inside solid blocks?
- Can you provide a list of all seeds that cause this issue?
- Is there a way to disable X-Ray vision by default when spawning inside the ground?
- What changes were made to address similar issues in previous versions of Cubyz?
- How does the game handle player movement after initial spawn?
- Are there any plans to add more robust checks for spawn points in future updates?
- Can you explain how the ESC key affects player positioning during world creation?
- Is this issue related to any known bugs with seed-based content generation?

*Source: unknown | chunk_id: github_issue_2300_discussion*
