# [issues/issue_3314.md] - Issue #3314 discussion

**Type:** review
**Keywords:** clear inventory, bag, flag, mods, inventory handling
**Concepts:** inventory management, command implementation, mod compatibility

## Summary
The /clear inventory command does not clear items in the player's bag. The discussion suggests a need for an additional flag to clear the bag as well.

## Explanation
The issue report indicates that the current implementation of the /clear inventory command only clears the main inventory but leaves items in the bag untouched. This behavior might be intentional, but it has raised concerns about the lack of flexibility for users and mod developers who may have added their own inventories. The maintainer is seeking input on how to address this issue while considering the potential impact on existing mods that might rely on specific inventory handling.

## Related Questions
- How does the current /clear inventory command interact with mod-added inventories?
- What are the potential side effects of adding a flag to clear the bag?
- Can you provide examples of how other games handle similar inventory clearing commands?
- Is there a way to make the behavior configurable without introducing new flags?
- How would changing this behavior affect existing mods that rely on the current implementation?
- What are the performance implications of modifying the inventory clearing logic?

*Source: unknown | chunk_id: github_issue_3314_discussion*
