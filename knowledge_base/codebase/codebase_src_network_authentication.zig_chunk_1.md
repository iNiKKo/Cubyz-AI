# [medium/codebase_src_network_authentication.zig] - Chunk 1

**Type:** api
**Keywords:** signing, verification, seed phrase, BIP39, crypto, checksum, random bytes, base64 decode, UTF8 iterator, bit manipulation, SHA256 hash, union dispatch, error panic, account init, wordlist validation
**Symbols:** sign, PublicKey, ed25519, ecdsaP256Sha256, mldsa44, initFromBase64, verifySignature, AccountCode, printInvalidCharError, initFromUserInput, initRandomly
**Concepts:** public key cryptography, BIP39 seed phrase parsing, crypto checksum validation, random byte generation, binary serialization, union type dispatching, error handling with panic fallbacks, base64 decoding, UTF8 codepoint iteration, bit manipulation for word indexing, SHA256 hashing, account initialization flow

## Summary
This chunk defines the network authentication layer, providing public-key cryptography utilities (signing/verification), BIP39-style account code parsing with checksum validation, and random seed generation for key derivation.

## Explanation
The chunk declares a pub fn sign that asserts initialization state, dispatches on KeyTypeEnum via an inline switch to extract the algorithm type, allocates a noise buffer of the required length, fills it with cryptographically secure random bytes from main.io.random, delegates to the Storage field's sign method (typed per key variant), and writes the resulting signature bytes. It also defines PublicKey as a union over three algorithms: ed25519, ecdsaP256Sha256, mldsa44, each mapped to their respective std.crypto.sign types; it provides initFromBase64 that decodes base64 input into the correct byte length (using encoded_length or uncompressed_sec1_encoded_length), then either calls fromBytes if declared or fromSec1 otherwise, returning a union-initialized PublicKey. The verifySignature method reads exactly Signature.encoded_length bytes via BinaryReader.readSlice, casts to an error-wrapped signature type, and invokes the algorithm's verify function with the message and self key field. A separate AccountCode struct holds a text slice representing a seed phrase; it includes printInvalidCharError for non-ASCII characters, initFromUserInput that trims whitespace, iterates UTF8 codepoints, rejects >0x7F, lowercases alphabetic chars, preserves single spaces between words, validates exactly 15 words against an external wordlist via wordToIndex (not shown here), accumulates bits into a [21]u8 array using bit-shifting math to reconstruct the original index range, checks that the final checksum byte matches sha256Result[0]>>3, and returns a duplicated text slice. initRandomly generates 20 random bytes, hashes them with Sha256, sets bits[20] to the hash's first byte (the checksum), then begins iterating over the 15 word slots using identical bit-index math as in initFromUserInput.

## Code Example
```zig
	pub fn sign(writer: *BinaryWriter, typ: KeyTypeEnum, message: []const u8) void {
		std.debug.assert(initialized);
		switch (typ) {
			inline else => |_typ| {
				const AlgorithmType = _typ.getAlgorithmType();
				var randomBytes: [AlgorithmType.noise_length]u8 = undefined;
				main.io.random(&randomBytes);
				const signature = @field(Storage, @tagName(_typ)).sign(message, randomBytes) catch |err| {
					std.debug.panic("Failed to sign message with error {s}. Maybe try reconnecting, if the error persists, I'd suggest creating a new account", .{@errorName(err)});
				};
				writer.writeSlice(&signature.toBytes());
			},
		}
	}
```

## Related Questions
- How does sign handle the case where the Storage field's sign method fails?
- What is the exact byte length used when decoding a base64 public key for ed25519 versus ecdsaP256Sha256?
- Which std.crypto.sign types are exposed inside PublicKey and how are they mapped to union tags?
- How does verifySignature read the signature bytes from BinaryReader without leaking partial data?
- What happens in initFromUserInput if a codepoint is greater than 0x7F?
- How does AccountCode enforce exactly 15 words before attempting checksum validation?
- Where is the BIP39 wordlist referenced and how is it accessed during wordToIndex?
- Does initRandomly require the global wordlist to be initialized, and what panic occurs if not?
- What is the purpose of bits[20] in AccountCode and how is its value derived from SHA256?
- How does the bit-shifting math reconstruct a 11-bit word index from the [21]u8 bits array?
- Is there any validation that the trimmed text contains only ASCII letters and whitespace before wordlist lookup?
- What error type is returned by initFromBase64 if the base64 decoder fails to fill the buffer?

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_1*
