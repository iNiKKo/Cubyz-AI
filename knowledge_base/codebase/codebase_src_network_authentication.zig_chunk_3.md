# [medium/codebase_src_network_authentication.zig] - Chunk 3

**Type:** api
**Keywords:** Argon2, base64 encoding, hashing, serialization, deserialization
**Symbols:** keyFromPassword, fromZon, toZon
**Concepts:** password hashing, Argon2 algorithm, serialization, deserialization, Zon format

## Summary
Handles password encoding and decoding using Argon2 hashing for authentication.

## Explanation
This chunk implements the logic for encoding and decoding passwords using the Argon2 hashing algorithm. It includes functions to derive a key from a password and salt, as well as methods to serialize and deserialize `PasswordEncodedAccountCode` objects to and from Zon format. The `keyFromPassword` function uses Argon2 to hash a password with a given salt, storing the result in a provided buffer. The `fromZon` method constructs a `PasswordEncodedAccountCode` instance from a ZonElement, decoding base64-encoded fields. Conversely, the `toZon` method serializes a `PasswordEncodedAccountCode` into a ZonElement, encoding its fields in base64.

## Code Example
```zig
fn keyFromPassword(typ: EncodingType, salt: []const u8, password: []const u8, key: *[32]u8) void {
	switch (typ) {
		.none => unreachable,
		.argon2_aes_gcm => {
			std.crypto.pwhash.argon2.kdf(main.globalAllocator.allocator, key, password, salt, .{
				.t = 10,
				.m = 32000,
				.p = 1,
			}, .argon2id, main.io) catch unreachable;
		},
	}
}
```

## Related Questions
- How does the `keyFromPassword` function derive a key from a password?
- What is the purpose of the `fromZon` method in this chunk?
- How is the `PasswordEncodedAccountCode` serialized into Zon format?
- What error handling is implemented in the `fromZon` method?
- Which hashing algorithm is used for password encoding?
- How does the chunk handle memory allocation and deallocation?

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_3*
