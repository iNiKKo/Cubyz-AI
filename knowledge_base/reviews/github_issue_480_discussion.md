# [issues/issue_480.md] - Issue #480 discussion

**Type:** review
**Keywords:** removal, Version 0.0.0, backwards compatibility, development versions, world saves
**Symbols:** bioem/height maps, json to zig.zon conversion code, json.zig, assets/backgrounds migration
**Concepts:** backwards compatibility

## Summary
The maintainer plans to remove certain code and assets after the Version 0.0.0 release, aiming for full backwards compatibility with previous development versions.

## Explanation
The maintainer plans to remove specific functionalities and files that are no longer needed post-release, aiming for full backwards compatibility with previous development versions. These include code for generating bioem/height maps from saves without stored data, JSON to Zig.Zon conversion utilities, the json.zig file, and assets/backgrounds migration. The primary goal is to ensure that the upcoming first release (Version 0.0.0) can load world saves from any development version up until the previous release, maintaining full backwards compatibility. Until then, these changes cannot be made as they would break compatibility with earlier versions.

## Related Questions
- What specific code is planned for removal after Version 0.0.0?
- Why is full backwards compatibility important for the first release?
- How will the removal of JSON to Zig.Zon conversion affect existing saves?
- Can you explain the purpose of assets/backgrounds migration and its future relevance?
- What are the potential impacts on performance or correctness with these changes?
- How does the maintainer ensure that world saves from previous versions remain compatible?

*Source: unknown | chunk_id: github_issue_480_discussion*
