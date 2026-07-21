# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 9

**Type:** documentation
**Keywords:** review checklist, how to apply, allocation, synchronization, tagged union, abstraction, naming, boundaries, PR scope, saved format
**Symbols:** N/A
**Concepts:** How to apply this document when reviewing or writing Cubyz code

## Summary
The document's closing checklist: the specific questions to run through, in order, when reviewing or writing Cubyz code.

## Explanation
When asked to review pasted code or write new Cubyz code, run through these questions in order, the way Cubyz's reviewers implicitly do:
1. Does every allocation have a clear, matching, correctly-scoped deallocation? Is the allocator choice appropriate to the data's actual lifetime?
2. Is anything here touched from more than one thread without synchronization?
3. Could this have used a tagged union instead of an enum-plus-optional-fields? Is a fallible case using `unreachable`/panic where it should return an error, or vice versa?
4. Is there a new abstraction/struct/indirection layer here that isn't earning its complexity yet?
5. Do the names still accurately describe current behavior? Is any bare number's unit unclear?
6. Are inclusive/exclusive bounds and untrusted input sizes handled carefully?
7. Is this PR-sized change actually one concern, or does it bundle something unrelated?
8. If this touches a saved/serialized format, does it handle existing data?

This is the actual texture of how this project's maintainer reviews code -- not a generic checklist, but a specific, consistent, opinionated engineering culture that has now been applied across hundreds of real PRs.

## Related Questions
- What checklist should you run through when reviewing or writing Cubyz code?
- What's the first question a Cubyz reviewer implicitly asks about a new allocation?
- What's the last question on Cubyz's code-review checklist, about saved/serialized formats?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_9*
