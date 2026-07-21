# [medium/docs_docs_development_multiplayer.md] - Chunk 5

**Type:** documentation
**Keywords:** updating server, manual update, world backup, saves folder, DDoS protection, VPS, Cloudflare, relay proxy, server security
**Symbols:** VPS, Cloudflare

## Summary
How to update a Cubyz server, back up world saves, and protect a server from DDoS/network exposure.

## Explanation
**Updating:** currently manual -- download the latest release, extract it, and manually copy over any custom configurations from the previous server directory.

**World backup:** also manual -- copy the specific world folder. On Windows: `C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME`. On Linux: `/home/USERNAME/.cubyz/saves/WORLD_NAME`.

**Server security:** port forwarding and sharing your public IP exposes your local network to the internet, risking DDoS attacks and unauthorized access. Mitigations: use a VPS to keep your home IP private and isolate the server from personal devices (costs a subscription fee); use a domain name behind a proxy like Cloudflare for DDoS mitigation and IP masking (requires a cheap custom domain, ~£10/year, so players connect via e.g. `ashframe.net`); or route traffic through a cheap VPS relay/proxy to hide your home IP, at the cost of some added latency.

**Third-Party Services & Add-ons:**

Add-ons are community-made extensions that modify or introduce new content to Cubyz, such as items, biomes, recipes and other.

#### 1. Downloading Add-ons
You can download add-ons directly from the official Discord server in the [#addons-mods](https://discord.com/invite/jM96g8pr25) channel, or browse the online community asset marketplace [here](https://addons.ashframe.net/).

#### 2. Installing Add-ons

**Step 1:** Navigate to your world save directory:
=== "Windows"

    ```
    C:\Users\USERNAME\Saved Games\Cubyz\saves\WORLD_NAME
    ```

=== "Linux"

    ```
    /home/USERNAME/.cubyz/saves/WORLD_NAME
    ```

**Step 2:** Extract the downloaded add-on archive.

**Step 3:** Place the extracted folder directly into the `assets` folder inside your specific world folder.

!!! note

    If you install add-ons on a dedicated server, they will automatically sync and download for connecting players.

### Discord Bot ([Mercur](https://github.com/AMerkuri))
Mercur provides bi-directional chat communication between your Discord server and your Cubyz server, and also can transmits server status data to the [Cubyz Server List](#cubyz-server-list-inikko).

**Installation:**
Install the required dependencies.

- **Debian / Ubuntu:*
```bash
sudo apt update
sudo apt install nodejs npm
```

- **Arch Linux:**
```bash
sudo pacman -S nodejs npm
```

**Setup:**
1. Create a folder for the bot (for example, `Mercur_Bot`).
2. Open a terminal inside that folder.
3. Run:
```bash
npx cubyz-discord-relay@latest
```
If no `config.json` file is found, the bot will automatically generate one and then exit.

**Configuration:**
1. Open the generated `config.json` file.
2. Update all required fields. See the [Cubyz Server List](#cubyz-server-list-inikko) section for information about the server list configuration.
3. After saving your changes, run the bot again:
```bash
npx cubyz-discord-relay@latest
```
!!! note

       If you are running **Cubyz 0.0.0**, use `@2.4.3` instead of `@latest`.

**Updating:**
To update the bot, simply run:
```bash
npx cubyz-discord-relay@latest
```
If a newer version includes changes to the configuration file:
1. Rename your current `config.json` (for example, to `old_config.json`).
2. Generate a new configuration file by running:
   ```bash
   npx cubyz-discord-relay@latest
   ```
3. Copy your settings from `old_config.json` into the newly generated `config.json`.
Your bot is now updated and ready to use.

### Cubyz Server List ([iNiKKo](https://github.com/iNiKKo))
Mercur can automatically submit your server information to the [Cubyz Server List](https://servers.ashframe.net/).

**Configuration:**
Enable or disable server list integration:
```json
enabled: true
```
- `true` – Broadcast your server information to the [Cubyz Server List](https://servers.ashframe.net/).
- `false` – Disable server list integration.
Configure the remaining fields in your `config.json`:
```json
serverName: "NAME_OF_YOUR_SERVER",
serverIp: "HOSTNAME_OR_IP_ADDRESS",
serverPort: YOUR_GAME_PORT,
description: "SHORT_SERVER_DESCRIPTION",
iconUrl: "DIRECT_URL_TO_IMAGE",
discordServer: "DISCORD_INVITE_LINK",
customClientDownloadUrl: "CUSTOM_CLIENT_DOWNLOAD_LINK"
```

**Server Icon:**
Upload your server icon to an image hosting service such as [ImgBB](https://imgbb.com/), then copy the **direct image URL** into the `iconUrl` field.
!!! note
    `discordServer` and `customClientDownloadUrl` are currently not displayed on the Cubyz Server List website, but they are reserved for future use.

## Related Questions
- How do I download and install add-ons in Cubyz?
- What is the process for setting up the Discord Bot (Mercur)?
- How do I configure the Cubyz Server List integration?
- What are the benefits of using a VPS for my Cubyz server?
- Can you explain how to update the Discord Bot (Mercur) if there's a new version?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_5*
