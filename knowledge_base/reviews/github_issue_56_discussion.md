# [issues/issue_56.md] - Issue #56 discussion

**Type:** review
**Keywords:** NoClassDefFoundError, ClassNotFoundException, Java version check, Cubyz launcher, library dependencies
**Symbols:** java -version, Cubyz.jar, pixelguys/json/Json, cubyz.utils.Logger, cubyz.client.GameLauncher
**Concepts:** classpath management, dependency handling, Java version compatibility

## Summary
User reports an issue where running Cubyz.jar results in a NoClassDefFoundError despite having Java 18 installed. Maintainer suggests using the official launcher to handle dependencies.

## Explanation
User reports an issue where running `Cubyz.jar` results in a NoClassDefFoundError despite having Java 18 installed. The initial problem was that the system was using Java 8 instead of the required Java 11 or higher, even though Java 18 had been installed. After removing all old Java 8 installations and verifying that `java -version` now shows Java 18, running Cubyz.jar resulted in a NoClassDefFoundError for the 'pixelguys/json/Json' class. The maintainer explains that directly using `java -jar` to run Cubyz.jar is insufficient as it does not handle required libraries and assets. Instead, they recommend using the official launcher, which manages all dependencies and stores them in the user's home directory under `.cubyz`. This approach ensures that all necessary components are correctly loaded and prevents class loading issues. To verify that all old Java versions have been removed from your system, you can use `java -version` to check the currently set default version. If it still shows an older version like Java 8, you may need to adjust environment variables or modify the registry settings on Windows.

## Related Questions
- How does the Cubyz launcher manage Java version compatibility?
- What specific libraries and assets are required by Cubyz.jar?
- Why is using `java -jar` insufficient for running Cubyz.jar?
- What steps should I take to resolve the NoClassDefFoundError when running Cubyz.jar?

*Source: unknown | chunk_id: github_issue_56_discussion*
