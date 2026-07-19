# [issues/issue_1788.md] - Issue #1788 discussion

**Type:** review
**Keywords:** sky appearance, high altitude, fog density, atmosphere height, spherical curvature
**Concepts:** atmospheric rendering, spherical geometry

## Summary
The sky appears unusual from high altitudes due to atmospheric rendering issues.

## Explanation
The sky appears unusual from high altitudes due to the current atmospheric rendering model, which does not account for spherical curvature. The maintainer notes that this is what the atmosphere would look like if we were living on a non-globular world and suggests exploring different combinations of fog density and atmosphere height settings. A user proposes simulating a spherical atmosphere around the player to correct the visual anomaly.

## Related Questions
- What is the current atmospheric rendering model in Cubyz?
- How does changing fog density and atmosphere height affect sky appearance?
- Can simulating a spherical atmosphere resolve high-altitude sky issues?
- Are there any existing settings that can improve the sky's appearance from high up?
- What are the potential performance implications of implementing a spherical atmosphere model?
- How might this change impact compatibility with existing Cubyz worlds?

*Source: unknown | chunk_id: github_issue_1788_discussion*
