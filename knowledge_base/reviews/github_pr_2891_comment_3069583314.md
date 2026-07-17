# [src/items.zig] - Chunk 3069583314

**Type:** review
**Keywords:** ProceduralItem, getProperty, getPropertyPtr, properties array, intFromEnum, dangling pointers, tool initialization, ABI stability, field access, enum indexing
**Symbols:** ProceduralItem, getProperty, getPropertyPtr, ProceduralItemProperty
**Concepts:** enum-to-array indexing, pointer safety, ABI stability, mutable access patterns, field vs property storage

## Summary
Refactored ProceduralItem.getProperty from an inline switch returning field pointers to a direct array lookup returning f32 values, and introduced getPropertyPtr for pointer access.

## Explanation
The original implementation used a switch on the enum to return &@field(self, @tagName(field)), which implicitly relied on the struct layout and could be fragile if fields were reordered or renamed. The reviewer flagged two concerns: (1) dangling pointers – returning field addresses directly is unsafe because the struct’s memory layout isn’t guaranteed stable across ABI changes; (2) misuse after tool initialization – callers might assume they can overwrite a returned pointer, but the property storage is actually an array of f32 values indexed by enum. The new getProperty returns self.properties[@intFromEnum(prop)], which is safe as long as the enum maps to valid indices and the properties array remains allocated. This change also removes any implicit pointer semantics from getProperty, preventing accidental overwrites. A new getPropertyPtr was added for cases where callers need mutable access (e.g., *= operations), keeping arithmetic expressions clean while preserving explicit ownership semantics.

## Related Questions
- What is the type of self.properties in ProceduralItem?
- How does @intFromEnum map a ProceduralItemProperty to an array index?
- Why was the original getProperty implementation considered unsafe regarding dangling pointers?
- Under what circumstances would getPropertyPtr be preferred over getProperty?
- Does changing getProperty to return f32 affect any existing code that expects a pointer?
- What guarantees must hold for self.properties to remain valid after tool initialization?
- How does the new implementation handle enum values outside the defined range?
- Is there any documentation or comment explaining why properties are stored in an array instead of fields?
- Could getPropertyPtr be implemented using @ptrCast on a field pointer, and what risks would that entail?
- What changes to the ProceduralItemProperty enum might be required if we add new property types?

*Source: unknown | chunk_id: github_pr_2891_comment_3069583314*
