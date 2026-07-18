# [issues/issue_1818.md] - Issue #1818 discussion

**Type:** review
**Keywords:** Linux, CachyOS, Arch, kernel 6.16.4-4-cachyos, create world, save files, directory creation, system crash
**Symbols:** Create World, .cubyz/saves/, worldName_number
**Concepts:** file system operations, directory management, system stability

## Summary
The 'Create World' feature in Cubyz creates an excessive number of save files and folders on Linux systems, leading to system crashes.

## Explanation
The issue arises from the 'Create World' functionality creating thousands of directories and files named 'worldName_number' in the .cubyz/saves/ directory. This behavior is observed when attempting to create a new world on CachyOS Linux (Arch) with kernel version 6.16.4-4-cachyos. The maintainer has confirmed the reproducibility of this issue and plans to investigate further, potentially related to improper handling of directory existence checks during world creation.

## Related Questions
- What is the root cause of the excessive directory and file creation in Cubyz?
- How does Cubyz check for directory existence during world creation?
- Is there a known issue with directory management on Linux systems similar to this one?
- What changes were made in commit de0bc4d that might have introduced this bug?
- How can the system stability be improved when handling file and directory operations in Cubyz?
- Are there any existing checks or safeguards in place to prevent such excessive file creation?

*Source: unknown | chunk_id: github_issue_1818_discussion*
