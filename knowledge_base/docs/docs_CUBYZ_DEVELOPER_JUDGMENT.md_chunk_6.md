# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 6

**Type:** documentation
**Keywords:** inclusive exclusive boundaries, min max convention, integer overflow, wrapping subtraction, entropy, double-free, ownership
**Symbols:** -%
**Concepts:** Correctness & Defensive Detail

## Summary
Section 6 of Cubyz Developer Judgment: correctness and defensive-coding judgment patterns, including the project-wide min/max boundary convention.

## Explanation
Inclusive/exclusive boundary conventions must be applied consistently and are a recurring source of real bugs: `>` vs `>=` creating a dead zone between UI elements (PR #1478), min being inclusive while max is exclusive as an established project-wide convention that new code must match (PR #3111, #2825). In Cubyz's Blueprint capture code specifically, this convention means min is inclusive and max is exclusive, mirroring how `size()` elsewhere in the codebase adds one and avoids bounds failures.

Never trust a declared size/count from network or file input without checking there's actually enough remaining data to back it -- reading a varint count and then allocating based on it without verifying the reader has that many bytes left is a real flagged vulnerability class (an attacker can claim a huge count with a short payload and force a large allocation or crash) (PR #2469).

Watch for integer overflow in timestamp/counter arithmetic; use wrapping-safe subtraction (`-%`) where a value could legitimately wrap (PR #2010).

Don't use a predictable/low-entropy source (wall-clock time) for anything where unpredictability actually matters -- a world-seed generator that fell back to time-based entropy was flagged as trivially brute-forceable (PR #2136).

A double-free from mismatched ownership after a conditional reassignment is a real, repeatedly-found bug shape: assign a new value over a variable that still has a pending `defer` cleanup pointing at the old value, and that old value gets freed twice or the new one never gets freed. Trace ownership through every branch, not just the common path (PR #1719).

## Related Questions
- In Cubyz's Blueprint capture code, what convention does min/max follow architecturally?
- Why must inclusive/exclusive boundary conventions be applied consistently in Cubyz?
- What vulnerability class does Cubyz guard against when reading a declared size/count from network or file input?
- When should wrapping-safe subtraction (`-%`) be used in Cubyz?
- Why does Cubyz avoid wall-clock time as an entropy source for world seeds?
- How does a double-free from mismatched ownership typically happen in Cubyz code?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_6*
