# [issues/issue_2732.md] - Issue #2732 discussion

**Type:** review
**Keywords:** item drop amounts, .auto block drops, backward compatibility, feature enhancement, block drop system, syntax change
**Symbols:** .auto, .items, .chance
**Concepts:** Backward Compatibility, Feature Enhancement

## Summary
The issue discusses adding the ability to specify item drop amounts for `.auto` block drops in Cubyz.

## Explanation
The user proposes modifying the block drop system to allow specifying an amount for items marked as `.auto`. The maintainer notes that while this feature might change, it already exists with a different syntax: `.{.chance 0.1, .items = .{"5 auto"}}`. The discussion revolves around ensuring backward compatibility and allowing new features without disrupting existing functionality.

## Related Questions
- How does the current block drop system handle item amounts for `.auto` items?
- What is the proposed syntax for specifying item amounts with `.auto` in Cubyz?
- Are there any potential backward compatibility issues with this change?
- How will the existing syntax `.{.chance 0.1, .items = .{"5 auto"}}` be affected by this feature enhancement?
- What is the motivation behind allowing different syntax for specifying item amounts in Cubyz?
- How can we ensure that new features do not disrupt existing functionality in Cubyz?

*Source: unknown | chunk_id: github_issue_2732_discussion*
