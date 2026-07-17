# [medium/codebase_src_network_authentication.zig] - Chunk 0

**Type:** api
**Keywords:** ed25519, ecdsaP256Sha256, mldsa44, KeyCollection, PublicKey, signing, base64 encoding, deterministic generation, salted hash, ZonElement
**Symbols:** wordlist, KeyTypeEnum, KeyCollection, PublicKey
**Concepts:** authentication, cryptographic key management, deterministic key generation, public key retrieval, message signing, multi-key storage, base64 encoding, binary serialization

## Summary
This chunk defines the authentication layer for the networking subsystem, providing key type enumeration, a collection of multiple cryptographic keys with deterministic generation and public-key retrieval, and signing functionality.

## Explanation
The chunk declares several top-level symbols: wordlist (a global optional array used internally by wordToIndex), KeyTypeEnum (an enum with three variants ed25519, ecdsaP256Sha256, mldsa44 and a getAlgorithmType method that maps each variant to the corresponding std.crypto.sign type), KeyCollection (a struct containing a Storage substruct with pub fields for each key pair type, an initialized flag, init(accountCode) which deterministically generates all three key pairs using salts derived from accountCode text and fixed strings, getPublicKeys(allocator) returning a ZonElement populated with base64-encoded public keys, getPublicKey(allocator, keyType) returning a tagged base64 string for the requested type, sign(writer, typ, message) which writes the signature bytes to a BinaryWriter), PublicKey (a union over KeyTypeEnum variants holding the respective public key types and an initFromBase64 method that decodes a base64 string into a PublicKey). The code uses main.files.cwd().read(...) in init() to load assets/cubyz/wordlist, splits on newline, trims whitespace, and stores into wordlist. It imports NeverFailingAllocator from main.heap, BinaryWriter/BinaryReader from main.utils, ZonElement from main, and the main module itself for file I/O and random bytes. The init() function also logs errors via std.log.err if reading fails. KeyCollection.init() uses comptime std.meta.declarations(Storage) to iterate over its fields, concatenates accountCode.text with a salt string, hashes repeatedly with Sha512, extracts the seed from the hash, then calls generateDeterministic on each key pair type (via @TypeOf(@field(...).generateDeterministic)). getPublicKeys() asserts initialized, creates a ZonElement via initObject, and for each declared field checks if the public_key type has toBytes; otherwise uses toUncompressedSec1. It encodes with std.base64.standard.Encoder and puts an owned string into result. getPublicKey() similarly asserts initialized, switches on keyType, extracts the appropriate bytes (toBytes or toUncompressedSec1), base64-encodes them, and returns a concatenated string of the type tag and encoded value. sign() asserts initialized, maps typ to AlgorithmType via getAlgorithmType(), generates random noise with main.io.random, calls @field(Storage, @tagName(_typ)).sign(message, randomBytes) catching errors and panicking with a message suggesting reconnect or creating a new account, then writes the signature bytes to writer.

## Related Questions
- What cryptographic algorithms are supported by KeyTypeEnum?
- How does KeyCollection.init generate keys deterministically from an account code?
- Which method should be used to retrieve all public keys as a ZonElement?
- How can I sign a message with the authentication layer and write it to a BinaryWriter?
- What happens if reading assets/cubyz/wordlist fails in init()?
- Does KeyCollection require initialization before calling getPublicKeys or sign?
- How are salts derived for each key pair in KeyCollection.init?
- Which public key encoding method is chosen when toBytes is not available?
- What error message is emitted if signing fails and how does it suggest recovery?
- Is PublicKey a union over the variants of KeyTypeEnum or something else?

*Source: unknown | chunk_id: codebase_src_network_authentication.zig_chunk_0*
