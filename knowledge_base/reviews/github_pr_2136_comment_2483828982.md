# [src/gui/windows/save_creation.zig] - Chunk 2483828982

**Type:** review
**Keywords:** getWorldSeed, seedStr, u64, time-based entropy, search space, reconstruct seed, random.int, fallback, architectural review, world generation
**Symbols:** getWorldSeed, testingModeCallback, std.crypto.random.int
**Concepts:** seed generation, time-based entropy, search space reduction, reproducibility, cryptographic randomness, world reconstruction attack, fallback behavior, deterministic seeding

## Summary
Added a new `getWorldSeed` function to parse user-provided seeds and fallback to random generation when empty; reviewer argues this is inferior because it relies on time, shrinking the search space for reconstructing a seed from an existing world.

## Explanation
The diff introduces `getWorldSeed(seedStr: []const u8) u64` which returns a random `u64` if the input string is empty. The reviewer’s concern is architectural: using time as entropy source makes it trivial for users to brute‑force or reverse‑engineer the seed from a generated world, because the search space collapses to the current timestamp range. This undermines reproducibility and security of world generation. A better approach would reuse the existing deterministic seeding logic (e.g., combining multiple sources like process ID, monotonic clock ticks with higher entropy, or a cryptographically secure RNG) that does not depend solely on wall‑clock time, thereby preserving a larger effective search space for seed recovery.

## Related Questions
- What existing code path does the reviewer suggest using for seed creation?
- How does relying on time reduce the search space for seed reconstruction?
- Is there a deterministic seeding function already defined in save_creation.zig?
- Does std.crypto.random.int provide sufficient entropy for world seeds?
- What are the security implications of allowing empty seed strings to fall back to random generation?
- Could combining multiple sources (PID, monotonic clock, RNG) mitigate the time dependency concern?
- Is there a way to hash the current time with additional entropy to expand the search space?
- How would one test that the new getWorldSeed function preserves reproducibility across runs?
- What changes are required in the UI or command-line parsing to support non-empty seed strings?
- Does the existing code handle edge cases like overflow when generating seeds from time?

*Source: unknown | chunk_id: github_pr_2136_comment_2483828982*
