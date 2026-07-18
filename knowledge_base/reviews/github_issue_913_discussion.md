# [issues/issue_913.md] - Issue #913 discussion

**Type:** review
**Keywords:** item stacks, quantity, inventory slots, save, reload, bug
**Concepts:** inventory management, serialization, deserialization

## Summary
The issue involves item stacks showing incorrect quantities (0 or 64) in specific inventory slots after saving and reloading the world.

## Explanation
The user reports that items placed in previously occupied slots show a quantity of 0 when reloaded, while new slots display the correct quantity. The maintainer asks for detailed steps to reproduce the issue. This could indicate a bug related to inventory serialization or deserialization, where the state of certain slots is not correctly saved or loaded.

## Related Questions
- What is the current state of inventory serialization in Cubyz?
- Are there any known issues with deserializing specific inventory slots?
- How does Cubyz handle item stack quantities during save and load operations?
- Can you provide a detailed log of the steps taken to reproduce this issue?
- Is there any code related to inventory management that might be causing this bug?
- Have there been any recent changes in the inventory system that could affect serialization/deserialization?

*Source: unknown | chunk_id: github_issue_913_discussion*
