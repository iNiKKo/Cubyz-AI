# [src/graphics/Window.zig] - PR #2026 review diff

**Type:** review
**Keywords:** Window.zig, Key struct, isToggling field, ZonElement, Zig standard library, migration
**Symbols:** GamepadAxis, Key, isToggling
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added `isToggling` field to `Key` struct in `Window.zig`. Proposed migration of Cubyz's ZonElement to Zig's standard library.

## Explanation
The change introduces a new field `isToggling` in the `Key` struct, which is intended to track whether a key is toggling. The reviewer also raises a critical architectural review about potentially migrating Cubyz's custom ZonElement implementation to the Zon parser/serializer available in Zig's standard library. This suggestion aims to leverage improvements and optimizations from the standard library while ensuring compatibility and correctness.

## Related Questions
- What is the purpose of the `isToggling` field in the `Key` struct?
- How does the addition of `isToggling` affect key handling in Cubyz?
- Why was there a suggestion to migrate ZonElement to Zig's standard library?
- What are the potential benefits and drawbacks of migrating to Zig's standard library for ZonElement?
- How would the migration of ZonElement impact existing Cubyz projects?
- Are there any compatibility issues to consider when migrating ZonElement?

*Source: unknown | chunk_id: github_pr_2026_comment_2441904390*
