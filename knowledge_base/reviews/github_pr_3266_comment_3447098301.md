# [mods/cubyz/rotations.zig] - Chunk 3447098301

**Type:** review
**Keywords:** rotations, modular, parsing, registration, subfolder, sentinel, public const, helper struct, termination, visibility
**Symbols:** stairs, no_rotation, texture_pile, ore, hanging, torch, decayable, direction, planar, log, carpet, branch, fence, sign, cubyz, a_sub_folder, exmple, init, deinit, Helper
**Concepts:** modular architecture, recursive module parsing, feature registration, sentinel markers, public vs private exports, termination conditions in AST traversal, developer feedback clarity

## Summary
The reviewer questions the parsing logic of a modular rotation system, specifically how to determine when a nested module (e.g., `a_sub_folder`) contains no further registrable features and should be treated as terminal.

## Explanation
The core architectural concern is distinguishing between modules that define public constants (like `pub const stairs = @import(...)`) versus those that only contain implementation details or helper structs. The reviewer points out that a file may expose functions like `init()`/`deinit()` and internal helpers, but these should not be automatically registered as features unless explicitly marked. Simply ignoring unparsable modules is insufficient because it obscures the reason for failure to mod creators. A robust solution requires an explicit marker (e.g., a sentinel constant or attribute) that signals 'this module has no further registrable content', allowing the parser to stop recursing and avoid false positives.

## Related Questions
- What sentinel constant should be added to a module file to indicate it contains no further registrable features?
- How can the parser distinguish between a module that only defines internal helpers and one that exports public constants for registration?
- If a nested folder like `a_sub_folder` has no `pub const` entries, what logic should trigger its termination in the traversal?
- Should the parser treat any file with only `init()`/`deinit()` functions as non-registrable by default?
- What error message or hint would best inform a mod creator why their module was ignored during feature registration?
- Can we use attribute-based metadata (e.g., `#[feature]`) instead of relying solely on public constants to mark registrable items?
- How does the current design handle cases where a subfolder mixes both registrable constants and internal helpers?
- Is there a risk that ignoring unparsable modules silently could lead to missing features in edge cases?
- What is the recommended pattern for exposing only top-level rotation types while hiding implementation details from the parser?
- Should the parser validate that every imported module either exports a `pub const` or explicitly marks itself as terminal?

*Source: unknown | chunk_id: github_pr_3266_comment_3447098301*
