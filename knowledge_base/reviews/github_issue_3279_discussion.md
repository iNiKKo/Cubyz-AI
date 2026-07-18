# [issues/issue_3279.md] - Issue #3279 discussion

**Type:** review
**Keywords:** Zig cache, Cubyz, disk usage, cleanup script, incremental compilation, memory management
**Symbols:** zig caches, cubyz cache, logs, zig-* folder
**Concepts:** disk space management, compilation speed, incremental compilation

## Summary
Discusses Cubyz's excessive disk usage due to Zig cache files, with suggestions for optional cleanup scripts or relying on Zig compiler improvements.

## Explanation
The issue revolves around Cubyz generating a large amount of cache files during compilation, consuming significant disk space. Users report manually deleting these files regularly. The discussion highlights that while this is not a bug per se, it could be mitigated by adding an optional cleanup script or waiting for improvements in the Zig compiler itself regarding incremental compilation and cache management.

## Related Questions
- What are the potential impacts of excessive disk usage on Cubyz's performance?
- How can optional cleanup scripts be implemented to manage Zig cache files effectively?
- Are there any plans to integrate incremental compilation into Cubyz to reduce cache size?
- What are the trade-offs between compilation speed and disk space in Cubyz?
- How does the Zig compiler plan to address cache management issues in future updates?
- Can Cubyz's architecture be modified to better handle large cache files without impacting performance?

*Source: unknown | chunk_id: github_issue_3279_discussion*
