# [issues/issue_1066.md] - Issue #1066 discussion

**Type:** review
**Keywords:** step-down, camera jank, eye height, interpolation, hitbox, motion sickness, see through walls
**Concepts:** camera jank, player model, eye height, hitbox, motion sickness

## Summary
The issue discusses adding a step-down feature to the player model, which was initially rejected due to causing camera jank. The proposed solution involves increasing eye height during the step-down animation to interpolate back to normal, but this introduces concerns about the eyes being outside the player's hitbox, potentially allowing players to see through walls.

## Explanation
The original proposal for adding a step-down feature was met with concerns regarding camera jank. The new solution suggests raising the eye height while the player model steps down and then interpolating it back to normal. However, this approach introduces a new issue where the eyes could be positioned outside the player's hitbox, potentially leading to visual anomalies such as seeing through walls. The maintainer also considers an alternative approach of snapping the step-down with a slight overshoot to avoid interpolation but notes that this might cause motion sickness.

## Related Questions
- What is the proposed solution for adding a step-down feature to the player model?
- Why was the initial proposal for adding step-down rejected?
- What new issue does raising eye height during step-down introduce?
- How could snapping with overshoot be an alternative to interpolation in this scenario?
- What are the potential drawbacks of using snapping with overshoot?
- Is there a way to prevent the eyes from being outside the player's hitbox while stepping down?

*Source: unknown | chunk_id: github_issue_1066_discussion*
