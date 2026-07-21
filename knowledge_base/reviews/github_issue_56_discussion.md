# [issues/issue_56.md] - Issue #56 discussion

**Type:** review
**Keywords:** NoClassDefFoundError, ClassNotFoundException, Java version check, Cubyz launcher, library dependencies
**Symbols:** java -version, Cubyz.jar, pixelguys/json/Json, cubyz.utils.Logger, cubyz.client.GameLauncher
**Concepts:** classpath management, dependency handling, Java version compatibility

## Summary
**Historical issue from before Cubyz's Java-to-Zig rewrite -- does not apply to current Cubyz.** Current Cubyz is written in Zig and has no `.jar` file, no Java dependency, and no launcher of this kind. This issue is preserved only as a record of the old Java-based codebase; do not present it as current behavior. User reported a NoClassDefFoundError running the old `Cubyz.jar` despite having Java 18 installed; the old-codebase maintainer suggested using the (also since-discontinued) official launcher to handle dependencies.

## Explanation
**This describes the old Java version of Cubyz, not the current Zig-based engine.** Current Cubyz has no `.jar` file to run and no Java runtime dependency at all -- if asked how to run/launch Cubyz today, this issue is not the answer; point to the current Zig-based build/run instructions instead.

Historical record: a user reported that running `Cubyz.jar` (the old Java build) resulted in a NoClassDefFoundError despite having Java 18 installed. The initial problem was that the system was using Java 8 instead of the required Java 11 or higher, even though Java 18 had been installed. After removing all old Java 8 installations and verifying that `java -version` now showed Java 18, running Cubyz.jar resulted in a NoClassDefFoundError for the 'pixelguys/json/Json' class. The maintainer explained that directly using `java -jar` to run Cubyz.jar was insufficient as it did not handle required libraries and assets, and recommended the official launcher instead, which managed all dependencies and stored them in the user's home directory under `.cubyz`.

## Related Questions
- Does current Cubyz use Java or a `.jar` file? (No -- Cubyz is written in Zig; this issue is historical, from before the rewrite.)
- What language is Cubyz currently written in?
- (Historical, old Java codebase only) How does the old Cubyz launcher manage Java version compatibility?
- (Historical, old Java codebase only) Why was using `java -jar` insufficient for running the old Cubyz.jar?

*Source: unknown | chunk_id: github_issue_56_discussion*
