# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 8

**Type:** documentation
**Keywords:** doc comments, ownership semantics, attribution, ported algorithms, log message severity, redundant comments
**Symbols:** argparse
**Concepts:** Comments, Documentation & Attribution

## Summary
Section 9 of Cubyz Developer Judgment: comments, documentation, and attribution judgment patterns.

## Explanation
New public API surface needs a doc comment explaining purpose and, where relevant, ownership semantics -- who frees what, what a null return means (PR #1425, the same PR that added a doc-comment for the new `argparse` module).

When porting an algorithm from elsewhere (e.g. a ray-triangle intersection routine), link back to the source -- this is about both transparency and licensing, not just courtesy (PR #2133).

Log message severity and wording must match reality. Calling an expected, already-handled control-flow path an "Internal error" is flagged as actively misleading during future debugging -- the fix renamed it to describe what actually happened (PR #2195).

Redundant comments that just restate the following line are removed, not kept for "clarity" (PR #1118).

## Related Questions
- What does a new public API surface need in Cubyz, per PR #1425?
- Why must Cubyz link back to the source when porting an algorithm from elsewhere?
- Why is calling an expected, already-handled path an "Internal error" flagged in Cubyz?
- Why are redundant comments that just restate the following line removed in Cubyz?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_8*
