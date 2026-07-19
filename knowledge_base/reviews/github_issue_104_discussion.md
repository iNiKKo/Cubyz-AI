# [issues/issue_104.md] - Issue #104 discussion

**Type:** review
**Keywords:** run.sh, run.bat, zig version, automated installation, workflow improvement, testing
**Symbols:** run.sh, run.bat, zig
**Concepts:** automation, version management, cross-platform compatibility

## Summary
The issue discusses adding a run script that automatically installs the required version of Zig. The maintainer has partially addressed this by implementing a bash script, but the batch file is still pending due to lack of testing.

## Explanation
The issue discusses adding a run script (run.sh/run.bat) that automatically installs the required version of Zig to improve development workflow by reducing manual steps for contributors and developers. The maintainer has partially addressed this by implementing a bash script (commit: 54337f17fd0de57808ddb5ca4e95c05575f35b3c) which automates the installation of the correct Zig version for Unix-like systems. However, the corresponding run.bat file is still pending due to lack of testing on Windows environments.

## Related Questions
- What specific commit addresses the implementation of the run.sh script?
- How does the run.sh script automate the Zig version installation?
- Why has the maintainer not implemented and tested the run.bat file yet?

*Source: unknown | chunk_id: github_issue_104_discussion*
