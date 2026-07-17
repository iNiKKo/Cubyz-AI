# [src/blocks.zig] - Chunk 1977728718

**Type:** review
**Keywords:** Block, checkEntityTouch, onEntityTouch, entity, callback, stub, placeholder, unused parameters, packed struct, inline, lookup table
**Symbols:** Block, checkEntityTouch, onEntityTouch
**Concepts:** callback hook, placeholder method, entity interaction, packed struct extension, inline lookup table

## Summary
Added two new methods to the Block struct: checkEntityTouch (inline lookup) and onEntityTouch (placeholder callback with unused parameters).

## Explanation
The diff introduces a new inline getter checkEntityTouch that maps block types to entity-touch checks, likely for future collision or interaction logic. It also adds an empty method stub onEntityTouch that accepts an Entity pointer and coordinates but currently ignores all arguments (_ = self; _ = entity; ...). This suggests the author is scaffolding a hook system where other blocks can later implement custom behavior when touched by entities (e.g., mobs, players), while keeping the interface uniform. The reviewer’s comment indicates they only want to provide the needed logic now and are open to refactoring into an optional function pointer if desired, implying awareness that the current stub may be over‑provisioned or need a more flexible callback mechanism later.

## Related Questions
- What is the purpose of checkEntityTouch and how does it differ from onEntityTouch?
- Why are all parameters in onEntityTouch ignored with _ = param;?
- Is there a planned interface for blocks to implement custom entity-touch behavior?
- Could checkEntityTouch be replaced by an optional function pointer as the reviewer suggested?
- What types of entities might trigger onEntityTouch in future code?
- How does adding these methods affect memory layout of the packed Block struct?
- Are there any existing callers that need to handle the new onEntityTouch signature?
- Does checkEntityTouch rely on a global lookup table _checkEntityTouch defined elsewhere?
- What is the expected return type or side effect of onEntityTouch when implemented?
- Could this change introduce ABI incompatibilities for downstream consumers of Block?

*Source: unknown | chunk_id: github_pr_1143_comment_1977728718*
