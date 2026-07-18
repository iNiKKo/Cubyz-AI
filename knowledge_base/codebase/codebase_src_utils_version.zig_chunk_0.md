# [easy/codebase_src_utils_version.zig] - Chunk 0

**Type:** api
**Keywords:** semantic versioning, version comparison, development version, release version, compatibility
**Symbols:** version, isCompatibleClientVersionImpl, isCompatibleClientVersion
**Concepts:** versioning, compatibility check

## Summary
Handles version compatibility checks between client and server versions.

## Explanation
The chunk defines a function `isCompatibleClientVersion` that checks if a given client version is compatible with the server version. It uses semantic versioning to compare major and minor version numbers, allowing any `-dev` server version to be considered compatible. The chunk also includes tests for both development and release versions to ensure correctness.

## Code Example
```zig
pub fn isCompatibleClientVersion(clientVersion: []const u8) !bool {
	return isCompatibleClientVersionImpl(clientVersion, version);
}
```

## Related Questions
- What is the purpose of the `isCompatibleClientVersion` function?
- How does the chunk handle `-dev` versions in compatibility checks?
- What tests are provided to verify the correctness of version comparisons?
- Where does the server version come from in this chunk?
- How many different types of version checks are implemented in the tests?
- What is the role of semantic versioning in this chunk?

*Source: unknown | chunk_id: codebase_src_utils_version.zig_chunk_0*
