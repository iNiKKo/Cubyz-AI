# [issues/issue_2400.md] - Issue #2400 discussion

**Type:** review
**Keywords:** asset reloading, in-game testing, settings changes, biome modifications, command implementation
**Symbols:** /reload, /server stop, /server restart
**Concepts:** Asset Management, In-Game Development Tools, Real-Time Settings Adjustment

## Summary
The issue discusses adding a /reload command to resend assets and the entire world to the client, which would be useful for testing modified assets without restarting Cubyz. The maintainer notes that this is also important for reloading settings changes and biome modifications while in-game.

## Explanation
The issue discusses adding a '/reload' command to resend assets and the entire world to the client, which would be useful for testing modified assets without restarting Cubyz. The maintainer notes that this is also important for reloading settings changes and biome modifications while in-game. Specifically, the /reload command will address issues such as cached asset loading on startup and provide a way to quickly test changes made during development or gameplay. This feature aims to enhance iterative development by allowing developers to see immediate effects of their changes without needing to restart the application.

The current state of the /server restart command on headfull mode is not specified in the issue report. The /reload command plans to handle cached assets by resending all assets to the client, effectively bypassing the cache. There may be potential performance implications with frequent asset reloading, such as increased network traffic and processing overhead. The /reload command will interact with server operations by potentially affecting the state of running servers, especially in headless mode where autokick might be involved. Security considerations for allowing in-game asset reloading include ensuring that only authorized users can execute the command to prevent unauthorized modifications. Ensuring consistency across different environments involves testing the command on various setups to ensure it behaves as expected.

## Related Questions
- What is the current state of the /server restart command on headfull mode?
- How does the /reload command plan to handle cached assets?
- Are there any potential performance implications with frequent asset reloading?
- How will the /reload command interact with server operations?
- What are the security considerations for allowing in-game asset reloading?
- How can we ensure that the /reload command works consistently across different environments?

*Source: unknown | chunk_id: github_issue_2400_discussion*
