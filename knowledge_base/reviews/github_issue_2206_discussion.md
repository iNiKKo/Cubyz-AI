# [issues/issue_2206.md] - Issue #2206 discussion

**Type:** review
**Keywords:** multiple keybinds, escape key, E key, inventory access, HUD, text fields, F1/F2 state
**Concepts:** user experience, keybindings, backward compatibility

## Summary
Discussion on allowing multiple keybinds for a single control to accommodate user preferences.

## Explanation
The issue revolves around the introduction of changes in commit #2036, which altered keybindings. Users expressed frustration with needing to relearn that the 'escape' key now accesses the inventory, while the 'E' key does nothing. The maintainer suggests exploring the possibility of allowing multiple keybinds for a single control, such as binding both 'escape' and 'E' to open the HUD. This would cater to users who are resistant to change. The maintainer also notes that there are subtle differences between using 'escape' and 'E', such as 'E' not leaving text fields and its behavior with commit #2343 regarding F1/F2 state.

## Related Questions
- What are the specific differences between using 'escape' and 'E' keys?
- How does commit #2343 affect the behavior of the 'E' key?
- What is the impact on user experience with multiple keybinds?
- Are there any potential backward compatibility issues with allowing multiple keybinds?
- How can we implement multiple keybinds without introducing new bugs?
- What are the performance implications of supporting multiple keybinds?

*Source: unknown | chunk_id: github_issue_2206_discussion*
