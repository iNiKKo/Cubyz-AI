# [src/blocks.zig] - Chunk 3196803123

**Type:** review
**Keywords:** SelectionRule, .always, .all, default case, redundant, config, unspecified, nullable, array, clarity
**Symbols:** register, _selectionRule, SelectionRule, zon.get, selectionCapabilities
**Concepts:** default behavior, config redundancy, nullable fields, architectural clarity, backward compatibility

## Summary
Replaced a direct assignment of a default `SelectionRule(.always)` with a nullable array field and introduced an explicit comment clarifying that the default case should be treated as `.all`, addressing reviewer concerns about redundancy and clarity.

## Explanation
The original code unconditionally set `_selectionRule[size]` to `zon.get(SelectionRule, "selectionRule", .always)`. This means even if the configuration omitted a selection rule, it would still default to `.always`, which could be misleading or redundant if the user explicitly wants no restriction. The reviewer pointed out that making the default case clearer as `.all` (i.e., allowing any selection) is preferable, and suggested adding `.all` to the config when unspecified rather than hard‑coding `.always`. To implement this, the change introduces a new variable `selectionCapabilities: ?[]SelectionCapability = null`, which will hold an optional slice of capabilities. This shift from a single default enum value to a nullable array allows the system to represent “no specific rule” more flexibly and aligns with the architectural goal of separating defaults from explicit configuration entries, preventing redundant `.all` entries in user configs while preserving backward compatibility.

## Related Questions
- What is the current default value of `_selectionRule` before this change?
- How does `zon.get` handle missing keys for a union type like `SelectionRule`?
- Why would storing `.all` in the config be preferable to hard‑coding it as the default?
- Does introducing a nullable array affect memory layout or alignment of `_selectionRule`?
- What happens at runtime if `selectionCapabilities` remains null after initialization?
- Is there any existing code that assumes `_selectionRule` is always non‑null?
- How does this change impact serialization/deserialization of block definitions?
- Could the new field cause issues with older binary formats expecting a single enum?
- What tests should be added to verify the default behavior when no rule is specified?
- Does the reviewer’s comment imply that `.all` should be an explicit config entry in all cases?

*Source: unknown | chunk_id: github_pr_2987_comment_3196803123*
