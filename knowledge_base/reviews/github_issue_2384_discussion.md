# [issues/issue_2384.md] - Issue #2384 discussion

**Type:** review
**Keywords:** infinite apples, oak leaves, undecaying variant, leaf-breaking mechanism, commit #856
**Concepts:** bug, regression

## Summary
The bug causes oak leaves to drop apples even when they are undecaying, allowing for infinite apple generation through repeated breaking.

## Explanation
The issue arises from the logic in the leaf-breaking mechanism, where apples are dropped regardless of the leaf variant's decay status. The maintainer notes that with commit #856, leaves should drop apples when broken by hand and leaves when broken with a sickle, indicating a potential regression or misconfiguration in handling different leaf variants.

## Related Questions
- What changes were made in commit #856 that might have caused this bug?
- How does the leaf-breaking mechanism differentiate between decaying and undecaying variants?
- Are there any other items or resources that can be infinitely generated through similar mechanisms?
- Can you provide a code snippet showing how the leaf variant is checked before dropping apples?
- What tests are in place to ensure that different leaf variants behave as expected when broken?
- How does this bug affect gameplay balance and player experience?

*Source: unknown | chunk_id: github_issue_2384_discussion*
