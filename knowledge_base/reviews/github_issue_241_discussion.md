# [issues/issue_241.md] - Issue #241 discussion

**Type:** review
**Keywords:** rename scripts, user-friendly feedback, progress meters, informational errors, tech support
**Symbols:** run.sh, debug_run.sh, run_release.sh, run_.sh
**Concepts:** user experience, build automation, scripting

## Summary
The build process scripts are being renamed and enhanced with user-friendly feedback messages.

## Explanation
The issue aims to improve the clarity and user-friendliness of the Cubyz build process by renaming the run scripts. The `run.sh` is renamed to `debug_run.sh`, and `run_release.sh` is renamed to `run_.sh`. This change is intended to make it more obvious which script is for regular users versus developers. Additionally, progress meters and informational error messages are being added to help users understand the build process better, reduce impatience, and assist tech support in diagnosing common issues.

## Related Questions
- What is the purpose of renaming `run.sh` to `debug_run.sh`?
- Why was `run_release.sh` renamed to `run_.sh`?
- How will the progress meters and informational error messages improve user experience?
- What are the potential drawbacks of adding progress bars for downloading/unzipping on Windows?
- When is the implementation of a progress bar in the launcher expected?
- How can the build process be further optimized to reduce impatience among newcomers?

*Source: unknown | chunk_id: github_issue_241_discussion*
