# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 7

**Type:** documentation
**Keywords:** PR scope, single concern, explicit return, fallthrough, out-of-scope, backward compatibility, saved data format, migration
**Symbols:** N/A
**Concepts:** PR Scope & Process Discipline, Backward Compatibility & Data Format Stability

## Summary
Sections 7 and 8 of Cubyz Developer Judgment: keeping pull requests focused, and handling backward compatibility for saved/serialized data formats.

## Explanation
Keep PRs to one concern. Bundling an unrelated rename, a style fix, or a new utility function into a PR whose stated purpose is something else gets explicitly split out and deferred, even when the added code is fine on its own merits (PR #2121, #1534, #2427, #2381). If helping someone plan a change, actively flag "this part is unrelated to your stated goal, consider a separate PR" the same way these reviewers do.

Every code path should end with an explicit, obvious return/result -- ambiguous fallthrough is flagged as an invitation for future mistakes even when current behavior is correct (PR #2587).

A legitimately good but out-of-scope suggestion gets deferred to a follow-up issue, not silently dropped and not force-fit into the current PR (PR #2422, #2427, #816).

A change to a serialized/save format must account for existing saved data. Adding a new union case that changes the byte layout, or allowing a previously-invariant field to take a new value (e.g. a "non-null item must have positive amount" invariant being silently broken), is treated as a serious issue requiring either a migration path or a redesign -- not something to patch around after the fact (PR #2247).

Public function signatures are preserved across internal refactors when possible -- several large internal rewrites (thread naming, argument parsing) explicitly note that the external API/command usage stayed the same even though the internals changed completely (PR #3219, #3112). Prefer refactors that don't force every caller to change.

## Related Questions
- Why does Cubyz insist on keeping pull requests to one concern?
- Why is ambiguous fallthrough flagged in Cubyz review even when current behavior is correct?
- What happens to a good but out-of-scope suggestion during a Cubyz PR review?
- What must a change to Cubyz's serialized/save format account for?
- Why does Cubyz try to preserve public function signatures across internal refactors?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_7*
