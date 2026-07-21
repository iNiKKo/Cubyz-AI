# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 8

**Type:** documentation
**Keywords:** namespace auto-prefixing, ID sanitization, cross-references, addonName, cubyz namespace
**Symbols:** window.projectData

## Summary
The two ID-handling conventions that apply almost everywhere in the Cubyz Addon Creator Studio: namespace auto-prefixing and ID sanitization.

## Explanation
**Namespace auto-prefixing:** cross-references (a block's drop item, a biome's surface block, a recipe's ingredients) get auto-prefixed with `{addonName}:` if the referenced ID matches something already defined in the current project, or `cubyz:` otherwise (assumed vanilla asset); an explicit `:` in the input bypasses this entirely.

**ID sanitization:** ID fields are lowercased and stripped to `[a-z0-9_]` before use as a filename.

## Related Questions
- What two ID-handling conventions does the Cubyz Addon Creator apply almost everywhere?
- What does an explicit colon in a Cubyz Addon Creator ID input field do?
- How does the Cubyz Addon Creator decide whether to prefix a cross-reference with the addon's own namespace or `cubyz:`?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_8*
