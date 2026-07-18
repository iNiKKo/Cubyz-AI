# [medium/codebase_src_network_authentication.zig] - Chunk 0

**Type:** api
**Keywords:** key generation, public key retrieval, signature creation, deterministic seeding, error handling
**Symbols:** wordlist, wordToIndex, init, KeyTypeEnum, KeyCollection, KeyCollection.Storage, KeyCollection.initialized, KeyCollection.init, KeyCollection.getPublicKeys, KeyCollection.getPublicKey, KeyCollection.sign
**Concepts:** network authentication, cryptographic keys, key management, message signing

## Summary
Handles network authentication including key generation, storage, and signing.

## Explanation
This chunk manages the initialization and usage of cryptographic keys for network authentication. It includes functions to read a wordlist from a file, convert words to indices, initialize key pairs with deterministic seeds based on an account code, retrieve public keys in various formats, and sign messages using different cryptographic algorithms. The `KeyCollection` struct encapsulates all key-related operations, ensuring that each key type (ed25519, ecdsaP256Sha256, mldsa44) is handled correctly.

## Code Example
```zig
fn wordToIndex(word: []const u8) ?u11 {
	if (wordlist == null) return null;
	for (wordlist.?, 0..) |other, i| {
		if (std.mem.eql(u8, word, other)) {
			return @intCast(i);
		}
	}
	return null;
}
```

## Related Questions
- How is the wordlist initialized?
- What types of keys are supported for network authentication?
- How are public keys retrieved from the KeyCollection?
- What happens if an error occurs during message signing?
- How are key pairs generated deterministically?
- What is the purpose of the `wordToIndex` function?

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_0*
