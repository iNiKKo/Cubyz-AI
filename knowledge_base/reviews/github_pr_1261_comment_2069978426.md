# [src/blocks.zig] - Chunk 2069978426

**Type:** review
**Keywords:** healingRatio, Block, inline, f32, 0.05, member function, customizable, misleading, optimization, opt out
**Symbols:** Block, healingRatio
**Concepts:** inline function, compile-time constant, misleading API surface, optimization opt-out, struct member semantics, function visibility, API design clarity, runtime vs compile-time configuration

## Summary
Added a `healingRatio` inline function returning 0.05 to the Block struct, but reviewers flagged that exposing it as a member method misleadingly suggests customizability and contradicts the intent of making healing an unopt-out optimization.

## Explanation
The diff introduces a new constant-like value for healing ratio (0.05) via an inline function on the Block struct. Reviewers argue that placing this in a member function implies the value could be overridden per instance, which is not desired; it should be a compile-time constant or a non-member to clearly signal that no opt-out path exists. Architecturally, this change affects how healing logic is invoked and may impact performance expectations if callers assume they can tune the ratio at runtime. The reviewer also hints that the current design could lead to subtle bugs where developers think they are customizing behavior when they are not, violating the principle of least surprise.

## Related Questions
- What is the current signature of healingRatio in blocks.zig?
- Where else in the codebase does healingRatio get called or referenced?
- Is there a constant definition for healing ratio elsewhere that could replace this function?
- How does exposing healingRatio as a member affect binary compatibility?
- What callers assume about healingRatio being tunable at runtime?
- Does any documentation claim healingRatio is configurable per block instance?
- Are there tests that verify the exact 0.05 value returned by healingRatio?
- Could moving healingRatio to a non-member constant break existing call sites?
- What performance implications arise from inlining vs calling a member function?
- Is there a pattern in Cubyz for representing fixed optimization constants?

*Source: unknown | chunk_id: github_pr_1261_comment_2069978426*
