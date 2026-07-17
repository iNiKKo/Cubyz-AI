# [src/migrations.zig] - Chunk 1980129103

**Type:** review
**Keywords:** migrations, registerBlockMigrations, addonName, stackAllocator, NeverFailingAllocator, localAllocator, heap fallback, memory management, ZonElement, collection, assetType
**Symbols:** registerBlockMigrations, register, main.stackAllocator, NeverFallingAllocator
**Concepts:** stack allocator, global fallback, addon isolation, memory pressure reduction, deterministic allocation

## Summary
Refactor of registerBlockMigrations signature to use addonName instead of name, introducing a local stack allocator reference for migration registration.

## Explanation
The change replaces the generic 'name' parameter with 'addonName', likely to better reflect that migrations are registered per addon rather than a single monolithic name. A new local variable 'localAllocator = main.stackAllocator' is introduced inside the register function, indicating an intent to use stack allocation where possible while still falling back to the global allocator via NeverFailingAllocator semantics. This aligns with the architectural philosophy of minimizing heap pressure and ensuring deterministic memory behavior in migrations.

## Related Questions
- What is the purpose of main.stackAllocator in this context?
- How does NeverFailingAllocator handle fallback to global allocator?
- Why was the parameter renamed from name to addonName?
- Does localAllocator shadow any existing variable in registerBlockMigrations?
- Is there a risk of stack overflow if migrationZon is large?
- What happens if main.stackAllocator is null or uninitialized?
- How does this change affect migrations registered by other addons?
- Are there any performance implications of using localAllocator vs global allocator?
- Does the diff show any changes to the return type of registerBlockMigrations?
- Is addonName used elsewhere in the codebase for similar purposes?

*Source: unknown | chunk_id: github_pr_1125_comment_1980129103*
