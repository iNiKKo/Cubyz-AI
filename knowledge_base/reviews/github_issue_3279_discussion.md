# [issues/issue_3279.md] - Issue #3279 discussion

**Type:** review
**Keywords:** Zig cache, Cubyz, disk usage, cleanup script, incremental compilation, memory management
**Symbols:** zig caches, cubyz cache, logs, zig-* folder
**Concepts:** disk space management, compilation speed, incremental compilation

## Summary
Discusses Cubyz's excessive disk usage due to Zig cache files, with suggestions for optional cleanup scripts or relying on Zig compiler improvements.

## Explanation
The issue revolves around Cubyz generating a large amount of Zig cache files during compilation, consuming significant disk space. Users report manually deleting these files regularly to reclaim memory. Before deleting the caches and logs, available memory on the hard drive was reduced by approximately 2GB due to Cubyz cache files. After deleting all logs and zig-* folders, available memory increased significantly as shown in attached images. The discussion highlights that while this is not a bug per se, it could be mitigated by adding an optional cleanup script or waiting for improvements in the Zig compiler itself regarding incremental compilation and cache management.

## Related Questions
- What are the exact amounts of disk space consumed by Cubyz caches before and after deletion?
- How does deleting specific folders like logs and zig-* impact available memory?

*Source: unknown | chunk_id: github_issue_3279_discussion*
