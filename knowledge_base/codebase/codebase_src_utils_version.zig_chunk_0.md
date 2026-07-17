# [easy/codebase_src_utils_version.zig] - Chunk 0

**Type:** api
**Keywords:** SemanticVersion, major, minor, patch, dev suffix, parse, expect, build_options
**Symbols:** version, isCompatibleClientVersionImpl, isCompatibleClientVersion
**Concepts:** semantic versioning, build options, API surface, compatibility checks, dev mode handling

## Summary
This chunk defines the version handling utilities for the Cubyz engine, exposing a public version constant derived from build options and providing compatibility checks between client and server versions.

## Explanation
The chunk imports std and build_options to obtain the current build version. It declares pub const version = build_options.version, making the version available as part of the module's API surface. The core logic resides in isCompatibleClientVersionImpl, which first treats any server version ending with '-dev' as compatible (returning true) and rejects any client version ending with '-dev' (returning false). For non-dev versions it parses both strings into SemanticVersion structs using std.SemanticVersion.parse, then compares major and minor fields only—ignoring patch differences. The public wrapper isCompatibleClientVersion simply calls the impl with the module's own version constant as the server argument. Two test functions verify correctness: one ensures the stored version string can be parsed by the semantic parser, and another runs a suite of expectations covering dev-server compatibility, release-version incompatibility between mismatched minors, exact-match acceptance, and patch-level tolerance (e.g., 4.5.0 and 4.5.10 are compatible with server 4.5.6 while 4.6.6 is not).

## Code Example
```zig
fn isCompatibleClientVersionImpl(clientVersion: []const u8, serverVersion: []const u8) !bool {
	if (std.mem.endsWith(u8, serverVersion, "-dev")) return true;
	if (std.mem.endsWith(u8, clientVersion, "-dev")) return false;

	const client = try std.SemanticVersion.parse(clientVersion);
	const server = try std.SemanticVersion.parse(serverVersion);

	return client.major == server.major and client.minor == server.minor;
}
```

## Related Questions
- What does the version constant represent in this module?
- How is a dev suffix handled for server versions during compatibility checks?
- Why are patch-level differences ignored when comparing semantic versions?
- Which function should be called to check if a client version is compatible with the current build?
- What happens if a client version string ends with '-dev'?
- How does the test suite verify that the stored version can be parsed correctly?
- Are there any constraints on major or minor version mismatches for compatibility?

*Source: unknown | chunk_id: codebase_src_utils_version.zig_chunk_0*
