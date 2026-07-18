# [medium/docs_docs_development_multiplayer.md] - Chunk 1

**Type:** documentation
**Keywords:** add-ons, installation, Mercur, Discord bot, Cubyz Server List, configuration, update
**Symbols:** add-ons, Mercur, Cubyz Server List
**Concepts:** Add-ons, Third-Party Services, Discord Bot Integration, Server List

## Summary
This section covers third-party services and add-ons in Cubyz, including downloading and installing add-ons, setting up a Discord bot named Mercur, and configuring the Cubyz Server List.

## Explanation
Add-ons are community-made extensions that modify or introduce new content to Cubyz, such as items, biomes, recipes, and other features. They can be downloaded from the official Discord server in the [#addons-mods](https://discord.com/invite/jM96g8pr25) channel or through an online marketplace [here](https://addons.ashframe.net/). To install add-ons, users need to navigate to their world save directory based on their operating system:

- **Windows:** `C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME`
- **Linux:** `/home/USERNAME/.cubyz/saves/WORLD_NAME`

After navigating to the correct directory, extract the downloaded add-on archive and place it directly into the `assets` folder inside your specific world folder.

The Mercur Discord bot facilitates communication between Discord and Cubyz servers and can submit server information to the [Cubyz Server List](https://servers.ashframe.net/). To install Mercur, follow these steps:

1. Install Node.js and npm on your system using the following commands for different Linux distributions:
   - **Debian / Ubuntu:**
     ```bash
     sudo apt update
     sudo apt install nodejs npm
     ```
   - **Arch Linux:**
     ```bash
     sudo pacman -S nodejs npm
     ```
2. Create a folder for the bot (for example, `Mercur_Bot`). Open a terminal inside that folder and run:
   ```bash
   npx cubyz-discord-relay@latest
   ```
3. If no `config.json` file is found, it will be automatically generated.
4. Configure the `config.json` file with necessary details such as server name, IP address, port, description, icon URL, and Discord invite link:
   ```json
   {
     "enabled": true,
     "serverName": "NAME_OF_YOUR_SERVER",
     "serverIp": "HOSTNAME_OR_IP_ADDRESS",
     "serverPort": YOUR_GAME_PORT,
     "description": "SHORT_SERVER_DESCRIPTION",
     "iconUrl": "DIRECT_URL_TO_IMAGE",
     "discordServer": "DISCORD_INVITE_LINK",
     "customClientDownloadUrl": "CUSTOM_CLIENT_DOWNLOAD_LINK"
   }
   ```
5. After saving your changes, run the bot again:
   ```bash
   npx cubyz-discord-relay@latest
   ```
6. To update Mercur, simply run:
   ```bash
   npx cubyz-discord-relay@latest
   ```
7. If a newer version includes changes to the configuration file, rename your current `config.json` (for example, to `old_config.json`) and generate a new one by running the update command again. Copy settings from `old_config.json` into the newly generated `config.json`. Your bot is now updated and ready to use.

The Cubyz Server List can be configured using the following fields in your `config.json`:
- **enabled:** Set to `true` or `false` to enable or disable server list integration.
- **serverName:** The name of your server.
- **serverIp:** Your server's hostname or IP address.
- **serverPort:** Your game port number.
- **description:** A short description of your server.
- **iconUrl:** Direct URL to the image hosting service for your server icon (e.g., [ImgBB](https://imgbb.com/)).
- **discordServer:** Discord invite link (currently not displayed but reserved for future use).
- **customClientDownloadUrl:** Custom client download link (currently not displayed but reserved for future use).

## Related Questions
- What are the specific steps to install add-ons on a Windows system?
- How do I configure Mercur's `config.json` file with all necessary details?
- Where can I find my server save directory on Linux?
- How do I update the Mercur Discord bot and handle configuration changes?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_1*
