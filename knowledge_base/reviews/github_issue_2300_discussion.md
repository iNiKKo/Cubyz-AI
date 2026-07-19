# [issues/issue_2300.md] - Issue #2300 discussion

**Type:** review
**Keywords:** X-Ray, spawn inside ground, QD seed, creative mode, cheats enabled, deterministic spawning
**Concepts:** world generation, player spawning, seed-based behavior

## Summary
The issue describes a bug where players spawn inside the ground, enabling X-Ray vision, in worlds created with specific seeds like 'QD'. This behavior persists until movement or pressing ESC.

## Explanation
The issue describes a bug where players spawn inside the ground with X-Ray vision in worlds created with specific seeds like 'QD' and 'ReviumReviewloper'. For seed 'QD', this behavior is consistent regardless of game mode or cheat settings. However, for seed 'ReviumReviewloper', spawning inside the ground only occurs in creative mode with cheats enabled, and pressing ESC teleports the player outside the ground. This variability must be preserved. The problem arises from an unexpected interaction between world generation algorithms and player spawning logic.

## Related Questions
- Is there a way to disable X-Ray vision by default when spawning inside the ground?

*Source: unknown | chunk_id: github_issue_2300_discussion*
