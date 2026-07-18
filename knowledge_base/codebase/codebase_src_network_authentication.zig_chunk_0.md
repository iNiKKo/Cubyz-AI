# [medium/codebase_src_network_authentication.zig] - Chunk 0

**Type:** api
**Keywords:** key generation, public key retrieval, signature creation, deterministic seeding, error handling
**Symbols:** wordlist, wordToIndex, init, KeyTypeEnum, KeyCollection, KeyCollection.Storage, KeyCollection.initialized, KeyCollection.init, KeyCollection.getPublicKeys, KeyCollection.getPublicKey, KeyCollection.sign
**Concepts:** network authentication, cryptographic keys, key management, message signing

## Summary
Handles network authentication including key generation, storage, and signing.

## Explanation
This chunk manages the initialization and usage of cryptographic keys for network authentication. It includes functions to read a wordlist from a file, convert words to indices, initialize key pairs with deterministic seeds based on an account code, retrieve public keys in various formats, and sign messages using different cryptographic algorithms. The `KeyCollection` struct encapsulates all key-related operations, ensuring that each key type (ed25519, ecdsaP256Sha256, mldsa44) is handled correctly.

Specifically:
- The wordlist is read from the file 'assets/cubyz/wordlist' and stored in memory as an array of strings. Each string represents a unique word used for indexing purposes.
- Key types supported are `ed25519`, `ecdsaP256Sha256`, and `mldsa44`. These correspond to the cryptographic algorithms: `std.crypto.sign.Ed25519`, `std.crypto.sign.ecdsa.EcdsaP256Sha256`, and `std.crypto.sign.mldsa.MLDSA44` respectively.
- Public keys are retrieved from the `KeyCollection.Storage` struct, which stores key pairs for each supported type. The public keys can be obtained in base64 format using the `getPublicKeys()` function or individually with the `getPublicKey(keyType)` method.
- If an error occurs during message signing (e.g., while generating a signature), it will result in a panic, prompting the user to reconnect or create a new account if necessary.
- Key pairs are generated deterministically using salts derived from keyboard mashing. The salts are concatenated with the account code and hashed multiple times to produce a seed for each key type.

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
- What is the process of initializing the wordlist?
- How do you convert words into indices in the wordlist?
- Which cryptographic algorithms correspond to each key type (ed25519, ecdsaP256Sha256, mldsa44)?
- How are public keys retrieved from KeyCollection.Storage?
- What happens if an error occurs during message signing?
- Describe the deterministic process for generating key pairs.

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_0*
