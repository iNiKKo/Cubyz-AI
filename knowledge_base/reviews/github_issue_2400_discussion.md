# [issues/issue_2400.md] - Issue #2400 discussion

**Type:** review
**Keywords:** asset reloading, in-game testing, settings changes, biome modifications, command implementation
**Symbols:** /reload, /server stop, /server restart
**Concepts:** Asset Management, In-Game Development Tools, Real-Time Settings Adjustment

## Summary
The issue discusses adding a /reload command to resend assets and the entire world to the client, which would be useful for testing modified assets without restarting Cubyz. The maintainer notes that this is also important for reloading settings changes and biome modifications while in-game.

## Explanation
The addition of the /reload command aims to enhance the development and testing process by allowing developers to quickly see changes made to assets without needing to restart the application. This feature is particularly beneficial for iterative development and debugging. The maintainer highlights that this command will also support reloading settings and biomes, which can be crucial for real-time adjustments during gameplay.

## Related Questions
- What is the current state of the /server restart command on headfull mode?
- How does the /reload command plan to handle cached assets?
- Are there any potential performance implications with frequent asset reloading?
- How will the /reload command interact with server operations?
- What are the security considerations for allowing in-game asset reloading?
- How can we ensure that the /reload command works consistently across different environments?

*Source: unknown | chunk_id: github_issue_2400_discussion*
