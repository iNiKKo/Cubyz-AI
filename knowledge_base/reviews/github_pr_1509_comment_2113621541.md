# [src/rotation.zig] - PR #1509 review diff

**Type:** review
**Keywords:** namespace, ID, compatibility, addons, workflow, flexibility
**Symbols:** rotationModes, getByID, main.stackAllocator.allocator
**Concepts:** backwards compatibility, asset management

## Summary
The change introduces a conditional check for namespaces in asset IDs, which could break compatibility by preventing assets from being easily copied between addons.

## Explanation
The reviewer points out that the proposed change would require assets to include their namespace in the ID, even if they share the same namespace as the rotation. This architectural decision could lead to issues for addon creators who might want to copy files between different addons without modifying their IDs. The reviewer emphasizes that this change could disrupt the expected workflow and flexibility of asset management.

The specific code change introduces a conditional check using `std.mem.containsAtLeastScalar(u8, id, 1, ':')` to determine if the ID contains a colon. If not, it constructs a namespaced ID by prepending 'cubyz:' to the original ID. The reviewer suggests that this could be problematic because it means assets cannot just be copied between different addons without modifying their IDs.

Additionally, the reviewer mentions that allowing assets from the same namespace as the rotation to skip the namespace part of ID could improve flexibility and compatibility.

## Related Questions
- What is the impact of requiring namespaces in asset IDs?
- How does this change affect addon creators' workflows?
- Can assets be easily copied between different addons with this new requirement?
- What are the potential backward compatibility issues introduced by this change?
- Is there a way to maintain flexibility while implementing namespace checks?
- How can we ensure that asset IDs remain consistent across different namespaces?

*Source: unknown | chunk_id: github_pr_1509_comment_2113621541*
