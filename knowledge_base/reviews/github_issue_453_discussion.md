# [issues/issue_453.md] - Issue #453 discussion

**Type:** review
**Keywords:** world.dat, biomeChecksum, commit, exclude, tracking, master copy
**Concepts:** Git, version control, file tracking

## Summary
The issue arises because Git does not ignore changes in `world.dat` due to updates made by Cubyz, specifically the addition of `biomeChecksum`. This necessitates manual exclusion during commits.

## Explanation
The problem stems from Cubyz's behavior of updating the master copy of the world file, which includes changes to `biomeChecksum`. As a result, Git tracks these changes and requires explicit exclusion when committing. The maintainer suggests exploring options to exclude certain files from being tracked by Git, potentially addressing this issue.

## Related Questions
- How can we modify Cubyz to prevent updates to `world.dat` during commits?
- What are the potential impacts of excluding `world.dat` from Git tracking?
- Are there any other files in Cubyz that should be excluded from version control?
- Can we implement a feature to automatically exclude certain files from being committed?
- How does the current implementation of `biomeChecksum` affect file tracking in Git?
- What are the best practices for managing world data files in version control systems?

*Source: unknown | chunk_id: github_issue_453_discussion*
