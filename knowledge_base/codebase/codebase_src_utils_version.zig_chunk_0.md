# [easy/codebase_src_utils_version.zig] - Chunk 0

**Type:** api
**Keywords:** semantic versioning, version comparison, development version, release version, compatibility
**Symbols:** version, isCompatibleClientVersionImpl, isCompatibleClientVersion
**Concepts:** versioning, compatibility check

## Summary
Handles version compatibility checks between client and server versions.

## Explanation
Handles version compatibility checks between client and server versions.

The chunk defines a function `isCompatibleClientVersion` that checks if a given client version is compatible with the server version, via `isCompatibleClientVersionImpl`. If the server version ends with `"-dev"`, it's always compatible (returns `true` immediately, before parsing anything). Otherwise, if the *client* version ends with `"-dev"`, it's always incompatible (`false`). Otherwise, both are parsed as `std.SemanticVersion` and compared: compatible only if `major` and `minor` both match exactly (patch version is ignored).

**Test Cases for `-dev` Server Version (`"1054.11.423-dev"`):**
- Client version `"0.3.1"`: Compatible (`true`)
- Client version `"100.0.0-dev"`: Compatible (`true`)
- Client version `"0.0.0-dev"`: Compatible (`true`)
- Client version `"1055.12.424"`: Incompatible (`false`)
- Client version `"1054.11.423-dev"`: Compatible (`true`)

**Test Cases for Release Server Version (`"4.5.6"`):**
- Client version `"0.3.1"`: Incompatible (`false`)
- Client version `"100.0.0-dev"`: Incompatible (`false`)
- Client version `"0.0.0-dev"`: Incompatible (`false`)
- Client version `"1055.12.424"`: Incompatible (`false`)
- Client version `"4.5.6"`: Compatible (`true`)
- Client version `"4.5.0"`: Compatible (`true`)
- Client version `"4.5.10"`: Compatible (`true`)
- Client version `"4.6.6"`: Incompatible (`false`)
- Client version `"4.4.6"`: Incompatible (`false`)
- Client version `"3.5.6"`: Incompatible (`false`)
- Client version `"5.5.6"`: Incompatible (`false`)

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
