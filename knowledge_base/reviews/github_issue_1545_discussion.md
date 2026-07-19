# [issues/issue_1545.md] - Issue #1545 discussion

**Type:** review
**Keywords:** mod registry, dependency tree, GitHub, source code verification, mod versioning, launcher integration, mod distribution, modpack stability
**Concepts:** mod registry, dependency management, versioning, caching, trust

## Summary
The discussion revolves around designing an online mod registry for Cubyz, focusing on trust, versioning, caching, and dependency management. The maintainers suggest resolving dependencies at the modpack creator level and using GitHub for hosting the registry due to its existing infrastructure.

## Explanation
The discussion revolves around designing an online mod registry for Cubyz, focusing on trust, versioning, caching, dependency management, and ensuring source code integrity. The maintainers suggest resolving dependencies at the modpack creator level and using GitHub for hosting the registry due to its established infrastructure for source code management and distribution.

Key points include:
- Players should be able to add trusted online registries in the launcher, merging them into a single catalogue of mods.
- Each registry entry must contain information about supported Cubyz versions, author details, download links, and hash values for verifying source code integrity.
- The registry should support multiple versions of the same modification with a version resolution algorithm to pick the latest compatible version.
- Registry entries do not include mod source code but provide links to it.
- Local caching is required for efficient access.
- Versioning ensures that modifications are tracked and updated properly.
- Launcher features allow viewing changes in registry content, including additions and removals.
- Mod distribution format should identify both assets and source code separately.
- Adding a mod with version X disallows re-publishing the same version with different sources to ensure stability for mod packs and reduce supply chain risks.
- Players joining modded servers must be informed about installed mods, their origins, and given an option to automatically download them.
- For third-party registries not in trusted lists, a warning message should inform players of potential security risks.
- A default 1st party registry is included by the launcher with limited features for core game content.
- Registry maintainers must ensure source code linked does not disappear and provide tools to manage it independently from metadata.
- Direct installation of mods from zip archives in a predefined format is supported, possibly with dedicated file extensions and metadata attached.

The discussion also addresses specific questions:
- Dependencies should be resolved by modpack creators rather than the launcher or registry itself.
- GitHub is suggested due to its existing infrastructure for source code management and distribution.
- Source integrity is ensured through hash values provided in registry entries.
- Versioning ensures stability and security, while caching improves performance.
- The launcher handles third-party mods with warnings about potential risks.

## Related Questions
-  Do we want to allow proper dependency trees to allow library mods or should people figure that out on their own?
-  Why is GitHub suggested as the hosting platform for the registry?
-  How does the registry ensure the integrity of mod sources?
-  What are the considerations for versioning and caching in the mod registry?
-  How will the launcher handle mods from third-party registries?
-  What measures are in place to prevent supply chain attacks through mod versions?

*Source: unknown | chunk_id: github_issue_1545_discussion*
