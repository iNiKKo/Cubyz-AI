# [issues/issue_3310.md] - Issue #3310 discussion

**Type:** review
**Keywords:** JumpCooldown, negative value, workbench, chest, F3 debug, right click
**Concepts:** gameplay, bug handling

## Summary
The JumpCooldown variable can go negative when interacting with block entities like a workbench or chest.

## Explanation
The issue arises because the JumpCooldown mechanism does not properly handle interactions within specific block entities, leading to an unexpected decrement below zero. The maintainer suggests that such issues should be reported only if they impact gameplay, implying that this particular bug may not significantly affect player experience.

## Related Questions
- What is the expected behavior of JumpCooldown when interacting with block entities?
- How does the current implementation handle interactions within block entities like a workbench or chest?
- Are there any checks in place to prevent JumpCooldown from going negative?
- Why did the maintainer suggest only reporting issues that impact gameplay?
- Is there a plan to address this bug, and if so, what is the proposed fix?
- How can we ensure that similar issues do not occur with other block entities?

*Source: unknown | chunk_id: github_issue_3310_discussion*
