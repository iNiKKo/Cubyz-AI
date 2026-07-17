# [src/blocks.zig] - Chunk 3292784532

**Type:** review
**Keywords:** SelectionCapabilities, enum, union, always, custom, BackingType, toolEffective, packed struct, refactor, hardcoded logic
**Symbols:** SelectionCapabilities, Capability, BackingType, toolEffective
**Concepts:** union enum pattern, feature flagging, code clarity, refactoring for extensibility, hardcoded logic removal

## Summary
Refactor of SelectionCapabilities from a flat enum into a union(enum) to separate always-true cases from custom capability flags.

## Explanation
The original code defined SelectionCapabilities as an enum with a single Capability variant and a capabilities field holding ?[]const Capability. Reviewers noted that the logic for checking whether a selection is allowed by item was hard‑coded inside the enum, making it unclear which features were configurable versus what was always true. The change introduces a union(enum) where one branch is 'always' (void) representing cases that never need capability checks, and another branch is 'custom', a packed struct holding BackingType flags including toolEffective. This design moves the per‑condition logic into the custom variant so each feature can be expressed with explicit if statements inside its own struct, improving readability and allowing future extensions without modifying the enum definition. Architecturally this reduces coupling between the capability list and the selection logic, prevents regressions by isolating always-true behavior in a dedicated union branch, and aligns with Zig best practices for representing optional or mutually exclusive states via unions.

## Related Questions
- What does the BackingType u1 represent in the custom variant?
- How is toolEffective used after this refactor?
- Where are the always-true cases now stored?
- Does this change affect any existing API that expects SelectionCapabilities to be an enum?
- Is there a migration path for code that currently inspects capabilities via the old enum fields?
- What performance implications arise from using a packed struct instead of a plain enum field?
- How does the union(enum) pattern impact serialization or reflection on SelectionCapabilities?
- Are there any tests that need updating to cover the new always and custom branches?
- Could BackingType be extended with more flags without breaking binary compatibility?
- What is the intended lifecycle of the old Capability enum after this change?

*Source: unknown | chunk_id: github_pr_3060_comment_3292784532*
