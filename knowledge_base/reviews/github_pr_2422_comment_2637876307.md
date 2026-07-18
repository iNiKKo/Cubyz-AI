# [src/server/world.zig] - PR #2422 review diff

**Type:** review
**Keywords:** world configuration, data initialization, zon files, renaming functions, codebase inconsistency
**Symbols:** ServerWorld, loadWorldData, loadWorldConfig, ZonElement
**Concepts:** naming conventions, code clarity, architectural consistency

## Summary
The function `loadWorldData` was renamed to `loadWorldConfig` to clarify its purpose of loading world configuration data.

## Explanation
The reviewer suggests renaming the function `loadWorldData` to `loadWorldConfig` to more accurately reflect its role in loading configuration data specific to the world, rather than a broad category of world data. The reviewer notes that the term 'data' is too generic and could encompass various types of information, including entity data. Additionally, there is inconsistency in how initialization from Zon files is handled across the codebase, but this PR does not address those issues. Instead, the reviewer plans to create an issue to discuss potential improvements.

## Related Questions
- What is the purpose of renaming `loadWorldData` to `loadWorldConfig`?
- Why does the reviewer consider 'data' too broad a term for this function?
- How does the inconsistency in initialization from Zon files affect the codebase?
- What steps will be taken to address the identified inconsistencies?
- Can you provide more details on the issue created by the reviewer regarding Zon file initialization?
- How might renaming `loadWorldData` impact other parts of the codebase?

*Source: unknown | chunk_id: github_pr_2422_comment_2637876307*
