# [src/rotation.zig] - Chunk 2113621541

**Type:** review
**Keywords:** rotation mode, namespace, cubyz:, getByID, containsAtLeastScalar, allocPrint, stackAllocator, asset copying, addon creation
**Symbols:** deinit, getByID, RotationMode, rotationModes, std.log.err, std.mem.containsAtLeastScalar, std.fmt.allocPrint, main.stackAllocator.allocator
**Concepts:** namespace resolution, ID prefixing, memory allocation, backwards compatibility, asset loading, reviewer feedback integration

## Summary
The change introduces a check for colons in rotation mode IDs and prepends the 'cubyz:' namespace prefix when none is present, addressing a reviewer's concern about allowing assets from the same namespace to skip the ID namespace part.

## Explanation
The original code logged an error if a requested rotation mode was not found and defaulted to 'no_rotation'. The reviewer pointed out that this behavior is problematic because it prevents copying files between addons when they share the same namespace, which is a common practice for new addon creators. To resolve this, the implementation now checks whether the provided ID contains a colon (indicating an explicit namespace). If no colon is present, it constructs a namespaced ID by prepending 'cubyz:' to the original ID using the main stack allocator. This ensures that lookups are performed against the fully qualified namespace path, allowing assets within the same namespace to be correctly resolved without requiring manual namespace specification in the ID.

## Related Questions
- What happens if a rotation mode ID contains multiple colons?
- Does the new namespacedId allocation handle out-of-memory gracefully or is unreachable assumed?
- Is there any validation that the original id does not already start with 'cubyz:' before prepending?
- How does this change affect existing code that passes unqualified IDs like 'no_rotation'?
- What is the expected behavior when getByID is called with an empty string after this modification?
- Does rotationModes.getPtr return a pointer to a static or dynamically allocated RotationMode struct?
- Is there any documentation update required for the new namespace prefix convention?
- Could this change introduce a regression in addons that rely on exact ID matching without namespaces?
- What is the lifetime of the returned RotationMode pointer from getByID after this modification?
- Are there any other places in rotation.zig where similar namespace handling should be applied?

*Source: unknown | chunk_id: github_pr_1509_comment_2113621541*
