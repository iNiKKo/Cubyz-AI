# [hard/codebase_src_server_world.zig] - Chunk 5

**Type:** implementation
**Keywords:** ZON file, thread pool, mutex locking, Level of Detail (LOD), chunk generation
**Symbols:** ServerWorld, worldData.put, loadPlayerLoginInfo, RegenerateLODTask, RegenerateLODTask.schedule, RegenerateLODTask.getPriority, RegenerateLODTask.isStillNeeded, RegenerateLODTask.run, RegenerateLODTask.clean, regenerateLOD
**Concepts:** world data serialization, player login info loading, chunk LOD regeneration

## Summary
Handles world data serialization, player login info loading, and LOD regeneration tasks.

## Explanation
This chunk manages various aspects of the server world's state, including saving world data to a ZON file, loading player login information from files, and scheduling tasks to regenerate Level of Detail (LOD) for chunks. The `RegenerateLODTask` struct defines a task that can be added to a thread pool to update LODs asynchronously. This involves locking region mutexes, generating or retrieving chunks, and updating higher-resolution chunks based on lower-resolution ones.

**World Data Serialization:**
The world data is serialized using the `worldData.put` method, which stores various properties such as `biomeChecksum`, `name`, `lastUsedTime`, `tickSpeed`, and `localPlayer`. These values are then written to a ZON file using `files.cubyzDir().writeZon(path, worldData)`.

**Player Login Info Loading:**
The player login information is loaded from files in the `players` directory. Each player file is read as a ZON file, and if it contains a valid public key or name, it is added to the player database. If a player file contains leading zeroes or an invalid key type, an error message is logged, and the file is skipped.

**LOD Regeneration Tasks:**
The LOD regeneration tasks are scheduled using `RegenerateLODTask.schedule`, which creates a new task and adds it to the thread pool. The task runs asynchronously, updating higher-resolution chunks based on lower-resolution ones. Mutex locking is used to ensure that region data is accessed safely.

**Error Handling:**
When deleting old LOD directories, any errors other than `error.FileNotFound` are logged. If a player file contains leading zeroes or an invalid key type, an error message is logged, and the file is skipped.

## Code Example
```zig
pub fn getPriority(_: *RegenerateLODTask) f32 {
			return std.math.floatMax(f32);
		}
```

## Related Questions
- How does the world data get serialized to a ZON file?
- What is the process for loading player login information?
- How are LOD regeneration tasks scheduled and executed?
- What happens if a player file contains leading zeroes?
- How is mutex locking used in LOD regeneration?
- What error handling is implemented when deleting old LOD directories?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_5*
