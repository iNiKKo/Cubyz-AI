# [issues/issue_1545.md] - Issue #1545 discussion

**Type:** review
**Keywords:** mod registry, dependency tree, GitHub, source code verification, mod versioning, launcher integration, mod distribution, modpack stability
**Concepts:** mod registry, dependency management, versioning, caching, trust

## Summary
The discussion revolves around designing an online mod registry for Cubyz, focusing on trust, versioning, caching, and dependency management. The maintainers suggest resolving dependencies at the modpack creator level and using GitHub for hosting the registry due to its existing infrastructure.

## Explanation
The issue discusses the design of a mod registry for Cubyz, emphasizing the need for trust in third-party verifiers and the inclusion of metadata such as version compatibility, source code hashes, and download links. The maintainers propose that dependencies should be managed by modpack creators, similar to Minecraft's approach, where mods specify their dependencies and fail to load if they are not met. They also suggest using GitHub for hosting the registry due to its established infrastructure for source code management and distribution. The discussion includes considerations for versioning, caching, and ensuring the stability of mod packs by preventing re-publishing of versions with different sources.

## Related Questions
- What is the proposed method for resolving mod dependencies?
- Why is GitHub suggested as the hosting platform for the registry?
- How does the registry ensure the integrity of mod sources?
- What are the considerations for versioning and caching in the mod registry?
- How will the launcher handle mods from third-party registries?
- What measures are in place to prevent supply chain attacks through mod versions?

*Source: unknown | chunk_id: github_issue_1545_discussion*
