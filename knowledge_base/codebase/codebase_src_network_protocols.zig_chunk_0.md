# [hard/codebase_src_network_protocols.zig] - Chunk 0

**Type:** networking
**Keywords:** init, onReceive, clientReceiveList, serverReceiveList, HandShakeState, BinaryReader, BinaryWriter, Atomic, condition variable, mutex locking
**Symbols:** bytesReceived, bytesSent, reload, handShake
**Concepts:** network protocol registration, binary serialization, handshake state machine, atomic counters, condition variable synchronization, asset loading, secure channel messaging

## Summary
This chunk defines the core networking protocol machinery for Cubyz, including a generic init() that registers client/server receive handlers by ID, an onReceive() dispatcher that validates handshake state and invokes the appropriate handler, and two public const structs (reload and handShake) containing binary serialization helpers and the full handshake logic with asset loading and server data exchange.

## Explanation
The chunk declares imports from main modules (blocks, chunk, particles, items, ZonElement, game, settings, renderer, utils, vec, heap, network). It defines two atomic counters bytesReceived and bytesSent indexed by protocol ID. The init() function iterates over the type's struct fields; for each field named Protocol it checks that the field has an id and optional clientReceive/serverReceive methods, storing them into global receive lists if those slots are still null, otherwise logging a duplicate error. onReceive(conn, protocolIndex, data) first ensures the connection is fully handshaked unless the index matches handShake.id; it then selects the appropriate handler from the receive lists (serverReceiveList for servers, clientReceiveList for clients), returning Invalid if missing. It creates a BinaryReader over the incoming bytes and calls the selected handler, logging any error that occurs, then atomically adds the received byte count to bytesReceived[protocolIndex]. The reload const struct holds id=0 and provides informClientOfRestart and informServerOfRestart; both allocate a stack-based BinaryWriter, write an int32 restartCounter (client version includes the user state enum), then send the resulting buffer over three channel types (.secure, .lossy, .slow). The handShake const struct holds id=1, an assetsLoadedCondition condition variable, a flag hasFinishedLoadingAssets, and a handshakeZon element. Its clientReceive handler reads a HandShakeState enum; if the new state is strictly greater than the current one it stores the new state atomically and dispatches on newState: userData/.signatureResponse/.reload are rejected as InvalidSide; signatureRequest reads two varInt-length slices (signature1, signature2), writes .signatureResponse to the writer, signs both signatures using network.authentication.KeyCollection.sign with conn.secureChannel.verificationDataForClientSignature.items, then sends the signed data over all three channels. The assets case logs a message, deletes any existing serverAssets tree under main.files.cubyzDir(), opens that directory, and unpacks the remaining reader bytes via utils.Compression.unpack into it. The serverData case parses the remaining bytes as a ZonElement (handshakeZon), broadcasts conn.handShakeWaiting to wake waiting client threads, locks conn.mutex, waits on assetsLoadedCondition until hasFinishedLoadingAssets becomes true, then unlocks and resets the flag. The serverReceive handler begins similarly by reading HandShakeState and storing it if newer; for userData it sets conn.secureChannel.finishedCollectingClientVerificationData = true.

## Related Questions
- How does init() prevent duplicate protocol IDs from being registered in the receive lists?
- What error is returned when onReceive is called before the handshake is complete and the index does not match handShake.id?
- Which channel types are used to send data after a successful signature exchange during the handshake?
- How does clientReceive handle incoming userData or reload states, and what error is produced in those cases?
- What steps are performed when assetsLoadedCondition.wait() returns true inside serverData handling?
- Why is conn.handShakeWaiting broadcast before waiting on assetsLoadedCondition in the serverData case?
- How does the code ensure that signature1 and signature2 are both signed using the secure channel verification data?
- What happens to any existing serverAssets directory when a new asset payload arrives during handshake?
- In what order are bytesReceived[protocolIndex] updated relative to invoking the protocol handler in onReceive?
- How does clientReceive distinguish between a newer HandShakeState and an older or equal one before processing?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_0*
