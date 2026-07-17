# [medium/codebase_src_network_authentication.zig] - Chunk 2

**Type:** api
**Keywords:** AccountCode, PasswordEncodedAccountCode, Argon2, AES-GCM, base64, SHA-256, random generation, secure deinitialization
**Symbols:** AccountCode, AccountCode.text, AccountCode.initFromUserInput, AccountCode.initRandomly, AccountCode.deinit, EncodingType, PasswordEncodedAccountCode, PasswordEncodedAccountCode.typ, PasswordEncodedAccountCode.salt, PasswordEncodedAccountCode.nonce, PasswordEncodedAccountCode.data, PasswordEncodedAccountCode.authenticationTag, PasswordEncodedAccountCode.empty, PasswordEncodedAccountCode.initFromPassword, PasswordEncodedAccountCode.initUnencoded, PasswordEncodedAccountCode.deinit, PasswordEncodedAccountCode.decryptFromPassword, keyFromPassword, fromZon
**Concepts:** account code generation, password encoding, encryption, checksum validation, secure memory management, data serialization

## Summary
Handles account code generation, encoding with passwords, and decoding from encoded data.

## Explanation
This chunk defines the `AccountCode` struct for generating and validating account codes. It includes methods to initialize an account code randomly or from user input, check its checksum, and deinitialize it securely. The `PasswordEncodedAccountCode` struct manages encoding account codes with passwords using Argon2 hashing and AES-GCM encryption. It provides functions to initialize encoded account codes from a password or without encoding, decrypt them back to the original account code, and handle serialization from ZON format.

## Code Example
```zig
pub fn initRandomly() AccountCode {
	if (wordlist == null) @panic("Cannot generate new Account without a valid wordlist.");
	var bits: [21]u8 = undefined;
	defer std.crypto.secureZero(u8, &bits);
	main.io.random(bits[0..20]);
	var sha256Result: [32]u8 = undefined;
	defer std.crypto.secureZero(u8, &sha256Result);
	std.crypto.hash.sha2.Sha256.hash(bits[0..20], &sha256Result, .{});
	bits[20] = sha256Result[0];

	var result: main.List(u8) = .empty;
	defer result.deinit(main.stackAllocator);
	defer std.crypto.secureZero(u8, result.items);

	for (0..15) |i| {
		const bitIndex = i*11;
		const byteIndex = bitIndex/8;

		const containingRegion = @as(usize, bits[byteIndex]) << 16 | @as(usize, bits[byteIndex + 1]) << 8 | if (byteIndex + 2 < bits.len) bits[byteIndex + 2] else 0;
		const wordIndex: u11 = @truncate(containingRegion >> @intCast(8*3 - 11 - bitIndex%8));

		if (i != 0) result.append(main.stackAllocator, ' ');
		result.appendSlice(main.stackAllocator, wordlist.?[wordIndex]);
	}

	return .{
		.text = main.globalAllocator.dupe(u8, result.items),
	};
}
```

## Related Questions
- How is an AccountCode initialized from user input?
- What method generates a new AccountCode randomly?
- How does the chunk validate the checksum of an AccountCode?
- What encryption algorithm is used to encode account codes with passwords?
- How is memory securely managed in this chunk?
- What format is used for serializing PasswordEncodedAccountCodes?
- How are keys derived from passwords in this chunk?
- What error handling is implemented when decoding encoded account codes?
- How does the chunk handle invalid ZON elements during deserialization?
- What methods are available to deinitialize AccountCode and PasswordEncodedAccountCode instances?

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_2*
