# [issues/issue_1746.md] - Issue #1746 discussion

**Type:** review
**Keywords:** item migrations, binary storage, item drops, migration path, version 0
**Concepts:** data migration, binary storage

## Summary
The discussion revolves around whether item drops should use binary storage and if a migration path is necessary for existing data.

## Explanation
The issue highlights that the current system for handling item migrations does not work properly when items are dropped. The proposed solution suggests using binary storage for item drops, with the maintainer arguing that no migration path is needed for old data because item drops are temporary and unlikely to be of concern before version 0.

## Related Questions
- What is the current system for handling item migrations?
- Why is binary storage proposed for item drops?
- Why does the maintainer believe no migration path is necessary?
- How are item drops defined in this context?
- What version number is mentioned as a cutoff point?
- Are there any potential implications of not migrating old data?

*Source: unknown | chunk_id: github_issue_1746_discussion*
