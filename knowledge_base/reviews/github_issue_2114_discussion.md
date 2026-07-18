# [issues/issue_2114.md] - Issue #2114 discussion

**Type:** review
**Keywords:** standardization, metadata, addons, discovery, unpacking, friction, registries, human-readable, web links, internal structure
**Symbols:** addon.zig.zon, addon metadata file
**Concepts:** programmatic discovery, metadata management, user experience, registry integration

## Summary
The proposal aims to standardize addon metadata by introducing an `addon.zig.zon` file to simplify addon discovery and management within Cubyz.

## Explanation
The issue highlights the current friction in managing addon archives, where users often struggle with unpacking and placing assets correctly. The proposed metadata file would serve as a clear reference point for addon root directories, enabling automated and correct extraction. Additionally, it could inform registries, reduce manual updates, and include more human-readable information such as descriptions and images. However, there are concerns about relying too much on web links and the potential disadvantage of enforcing a uniform internal structure for addons.

## Related Questions
- How would the `addon.zig.zon` file be used to programmatically discover and unpack addons?
- What are the potential benefits of integrating metadata files with registries?
- How could the proposed metadata file reduce manual updates for addon information?
- What are the concerns regarding the reliance on web links in the metadata file?
- How might enforcing a uniform internal structure for addons impact user experience?
- What additional keys should be included in the `addon.zig.zon` file to enhance usability?

*Source: unknown | chunk_id: github_issue_2114_discussion*
