# [medium/docs_docs_development_multiplayer.md] - Chunk 2

**Type:** configuration
**Keywords:** server list, enabled flag, config.json, iNiKKo, servers.ashframe.net, iconUrl, discordServer, customClientDownloadUrl, Mercur, ImgBB
**Symbols:** iNiKKo, Cubyz Server List, servers.ashframe.net, enabled, serverName, serverIp, serverPort, description, iconUrl, discordServer, customClientDownloadUrl, Mercur, ImgBB
**Concepts:** Server List Integration, Configuration Flags, JSON Schema Fields, External Directory Submission, Icon URL Handling, Future-Proof Config Design

## Summary
The chunk details enabling/disabling server list integration via a boolean config flag and lists required JSON fields (serverName, serverIp, serverPort, description, iconUrl, discordServer, customClientDownloadUrl) with notes that the latter two are currently unused but reserved.

## Explanation
To allow external players to connect to your Cubyz server, you need to configure port forwarding on your home router. This involves several steps:

1. **Find Your Router's IP Address (Default Gateway):**
   - On Windows, open Command Prompt or PowerShell and run `ipconfig` to find the Default Gateway.
   - On Linux, use terminal commands like `ip route | grep default` or `ip a` to locate the Gateway IP.

2. **Find Your Router's Login Details:**
   - The default username and password are usually printed on a sticker on your router.
   - If you forget your custom password, reset the router by pressing and holding the reset button for 10–30 seconds until the lights flash.

3. **Locate the Port Forwarding Section:**
   - This section can be found under menus like Advanced, Security, or LAN, with labels such as Port Forwarding, Port Mapping, NAT Forwarding, Virtual Server, or Port Triggering.

4. **Configure the Port Forward Rule:**
   - **Internal/Local IP Address:** Find this using the same terminal commands from Step 1 (labeled as IPv4 Address).
   - **Port:** Enter the port used by your server (default is `47649` or as shown in-game under the 'Invite Players' menu).
   - **Protocol:** Select UDP.

Save your changes, and your server will be ready for external connections!

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
