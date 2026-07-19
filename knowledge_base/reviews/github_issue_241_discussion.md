# [issues/issue_241.md] - Issue #241 discussion

**Type:** review
**Keywords:** rename scripts, user-friendly feedback, progress meters, informational errors, tech support
**Symbols:** run.sh, debug_run.sh, run_release.sh, run_.sh
**Concepts:** user experience, build automation, scripting

## Summary
The build process scripts are being renamed and enhanced with user-friendly feedback messages.

## Explanation
The issue aims to improve the clarity and user-friendliness of the Cubyz build process by renaming the run scripts. Specifically, `run.sh` is renamed to `debug_run.sh`, and `run_release.sh` is renamed to `debug.sh`. This change is intended to make it more obvious which script is for regular users versus developers. Additionally, progress meters and informational error messages are being added during the build process to help users understand common scenarios in `#help-and-questions`. These messages include checking compiler status, installing compiler if necessary, building Cubyz with optimizations, indicating when Cubyz is ready, and launching it. However, due to performance issues on Windows, progress bars for downloading/unzipping are currently disabled.

## Related Questions
- What specific feedback messages will be added during the build process?
- Why was `run_release.sh` renamed to `debug.sh` instead of `run_.sh`?
- How does the lack of progress bars affect the Windows download and unzip processes?

*Source: unknown | chunk_id: github_issue_241_discussion*
