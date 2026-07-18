# [issues/issue_2005.md] - Issue #2005 discussion

**Type:** review
**Keywords:** block migrations, blueprint palette, re-applies migrations, quick solution, workaround, frequent refactoring, change in mindset
**Symbols:** migrations.zig, Palette
**Concepts:** block migrations, blueprint palette, quick solution, workaround

## Summary
The discussion revolves around applying block migrations to blocks in the blueprint palette during loading. The maintainer suggests a quick solution that re-applies migrations each time a blueprint is loaded and emphasizes the need for a change in mindset towards workarounds.

## Explanation
The issue arises because migrations are not applied to blueprints when they are loaded, which could lead to problems if old migrations are removed. The user proposes constructing a Palette object for use in migrations, applying them, and then continuing. The maintainer decides on a quick solution that re-applies migrations each time the blueprint is loaded, arguing that this should be addressed soon as it affects the base game. There is a discussion about whether blueprints should be automatically saved after migration if they have changed. The maintainer also emphasizes the need for a change in mindset towards workarounds and suggests frequent refactoring to clean up these solutions once more complete requirements are established.

## Related Questions
- What is the purpose of re-applying migrations each time a blueprint is loaded?
- How does the quick solution address the issue of old migrations being removed?
- Why is there a discussion about automatically saving blueprints after migration if they have changed?
- What are the potential drawbacks of using a quick solution for block migrations?
- How does the maintainer suggest addressing the problem of blueprint compatibility across different versions?
- What is the timeline for removing old migrations, and how does this affect the current implementation?
- How can developers ensure that their blueprints remain compatible with older versions after migration?
- What are the potential performance implications of re-applying migrations each time a blueprint is loaded?
- How can the project maintain a balance between meeting deadlines and implementing clean solutions?
- What steps should be taken to refactor and clean up workarounds in the future?

*Source: unknown | chunk_id: github_issue_2005_discussion*
