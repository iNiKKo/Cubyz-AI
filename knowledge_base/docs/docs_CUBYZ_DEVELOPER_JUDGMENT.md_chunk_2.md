# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 2

**Type:** documentation
**Keywords:** concurrency, thread safety, mutex, atomic, load, store, thread sanitizer, shutdown ordering, save-on-disconnect
**Symbols:** .load(), .store()
**Concepts:** Concurrency & Thread Safety

## Summary
Section 2 of Cubyz Developer Judgment: concurrency and thread safety judgment patterns.

## Explanation
Any field touched from more than one thread needs explicit synchronization (mutex, or a genuinely atomic type) -- don't assume "it probably won't race." View-bob player fields (PR #665), gamepad state, and player save-on-disconnect (PR #943) were all flagged for exactly this.

A field is deliberately left non-atomic sometimes, on purpose, specifically so the thread sanitizer will catch a real race during testing rather than the code silently papering over a design flaw with an atomic wrapper (PR #943). Don't reflexively suggest "just make it atomic" -- ask whether the actual fix is proper synchronization of a group of related fields, since atomics only protect the single value they wrap, not cross-field consistency.

Always use `.load()`/`.store()` on atomic values -- direct field access on an atomic is flagged every time it appears (PR #663, #161).

Shutdown/init ordering matters and is a real source of bugs: initialize subsystems in the order their dependents need them (thread pool before audio, since audio's `deinit` touches the thread pool -- PR #3219), and don't drain/nuke a shared resource (a whole thread pool) if other threads may still be using parts of it -- drain only what's actually safe to drain (PR #3219).

Save-on-disconnect must happen after all in-flight updates finish, not concurrently with them -- move save logic into the deinitialization path rather than triggering it eagerly on disconnect notice (PR #943).

## Related Questions
- How should shared fields be synchronized across threads in Cubyz?
- Why would a field be deliberately left non-atomic in Cubyz, on purpose?
- Why is direct field access on an atomic value flagged in Cubyz review?
- How should subsystem shutdown/init ordering be handled in Cubyz?
- When should save-on-disconnect logic run in Cubyz's server?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_2*
