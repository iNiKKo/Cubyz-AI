# [medium/docs_docs_development_multiplayer.md] - Chunk 2

**Type:** configuration
**Keywords:** server list, enabled flag, config.json, iNiKKo, servers.ashframe.net, iconUrl, discordServer, customClientDownloadUrl, Mercur, ImgBB
**Symbols:** iNiKKo, Cubyz Server List, servers.ashframe.net, enabled, serverName, serverIp, serverPort, description, iconUrl, discordServer, customClientDownloadUrl, Mercur, ImgBB
**Concepts:** Server List Integration, Configuration Flags, JSON Schema Fields, External Directory Submission, Icon URL Handling, Future-Proof Config Design

## Summary
The chunk details enabling/disabling server list integration via a boolean config flag and lists required JSON fields (serverName, serverIp, serverPort, description, iconUrl, discordServer, customClientDownloadUrl) with notes that the latter two are currently unused but reserved.

## Explanation
Cubyz Server List is an external directory maintained by iNiKKo where Mercur can automatically submit your server information. Integration is controlled by the 'enabled' boolean in config.json: true broadcasts server data to servers.ashframe.net, false disables it entirely. The required configuration fields are serverName (string), serverIp (hostname or IP address), serverPort (numeric game port), description (short string), iconUrl (direct URL to an image hosted on a service like ImgBB), discordServer (Discord invite link), and customClientDownloadUrl (custom client download link). The documentation explicitly states that discordServer and customClientDownloadUrl are not currently displayed on the website but are reserved for future use, implying they may be ignored by the current backend while still being accepted in config.

## Related Questions
- How do I disable Cubyz Server List integration in my config?
- What is the correct format for the serverIp field when submitting to the server list?
- Are discordServer and customClientDownloadUrl currently visible on the server list website?
- Where should I host the image URL referenced by iconUrl to ensure it works with Mercur?
- Which configuration key controls whether my server information is broadcasted externally?
- Can I use a relative path for iconUrl or does it require an absolute direct link?
- What happens if I set enabled to true but omit required fields like serverName?
- Is there any limit on the length of the description field for the server list submission?
- Does Mercur automatically detect and submit my server when enabled is true, or must I trigger it manually?
- Are discordServer and customClientDownloadUrl reserved for future use only, or will they be ignored now?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_2*
