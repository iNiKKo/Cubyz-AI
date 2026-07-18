# [issues/issue_104.md] - Issue #104 discussion

**Type:** review
**Keywords:** run.sh, run.bat, zig version, automated installation, workflow improvement, testing
**Symbols:** run.sh, run.bat, zig
**Concepts:** automation, version management, cross-platform compatibility

## Summary
The issue discusses adding a run script that automatically installs the required version of Zig. The maintainer has partially addressed this by implementing a bash script, but the batch file is still pending due to lack of testing.

## Explanation
The discussion revolves around improving the development workflow by automating the installation of the correct Zig version. The maintainer has made progress by adding a run.sh script, which addresses the issue for Unix-like systems. However, the corresponding run.bat file is still pending because the maintainer lacks the capability to test it on Windows environments.

## Related Questions
- What is the current status of the run.bat file implementation?
- How does the run.sh script automate the Zig version installation?
- Are there any plans to test and implement the run.bat file in the future?
- What are the potential benefits of having an automated Zig version installer?
- How can contributors benefit from this automation feature?
- Is there a specific reason for not implementing the batch file yet?

*Source: unknown | chunk_id: github_issue_104_discussion*
