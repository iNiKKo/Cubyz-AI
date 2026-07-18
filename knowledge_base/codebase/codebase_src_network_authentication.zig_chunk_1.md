# [medium/codebase_src_network_authentication.zig] - Chunk 1

**Type:** api
**Keywords:** union, base64 decoding, signature verification, user input validation, random generation, secure deinitialization
**Symbols:** PublicKey, PublicKey.ed25519, PublicKey.ecdsaP256Sha256, PublicKey.mldsa44, PublicKey.initFromBase64, PublicKey.verifySignature, AccountCode, AccountCode.text, AccountCode.printInvalidCharError, AccountCode.initFromUserInput, AccountCode.initRandomly, AccountCode.deinit, EncodingType
**Concepts:** network authentication, public key cryptography, account code validation

## Summary
Defines public key types and account code handling for network authentication.

## Explanation
Defines public key types and account code handling for network authentication. The `PublicKey` union supports three cryptographic algorithms: Ed25519, ECDSA P-256 with SHA-256, and MLDSA44. It provides methods to initialize from base64 strings (`initFromBase64`) and verify signatures (`verifySignature`). Each algorithm has a specific public key type associated with it (e.g., `PublicKey.ed25519` for Ed25519). The `AccountCode` struct handles user input validation, ensuring that the account code contains only ASCII letters and spaces, adheres to a 15-word format, and includes a checksum. It also supports random generation of an AccountCode (`initRandomly`) and secure deinitialization (`deinit`).

## Code Example
```zig
pub fn initFromBase64(base64: []const u8, typ: KeyTypeEnum) !PublicKey {
	switch (typ) {
		inline else => |_typ| {
			const KeyType = @TypeOf(@field(KeyCollection.Storage, @tagName(_typ)).public_key);
			const length = if (@hasDecl(KeyType, "fromBytes")) KeyType.encoded_length else KeyType.uncompressed_sec1_encoded_length;
			var bytes: [length]u8 = undefined;
			try std.base64.standard.Decoder.decode(&bytes, base64);
			if (@hasDecl(KeyType, "fromBytes")) {
				return @unionInit(PublicKey, @tagName(_typ), try KeyType.fromBytes(bytes));
			} else {
				return @unionInit(PublicKey, @tagName(_typ), try KeyType.fromSec1(&bytes));
			}
		},
	}
}
```

## Related Questions
- What are the specific cryptographic algorithms supported by the PublicKey union?
- How does the initFromBase64 method handle different key types?
- What is the exact format required for an AccountCode during user input validation?
- How many words should a valid AccountCode contain and what is the checksum requirement?
- What steps are taken to securely deinitialize an AccountCode instance?

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_1*
