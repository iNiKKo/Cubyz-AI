# [medium/docs_docs_development_multiplayer.md] - Chunk 3

**Type:** documentation
**Keywords:** port forwarding, default gateway, router IP, ip route, ip a, ipconfig, router login, port forwarding section, UDP, internal IP
**Symbols:** ip route, ip a, ipconfig, UDP

## Summary
Full step-by-step guide to port forwarding a Cubyz server: finding your router's IP (default gateway), logging into the router, locating the port-forwarding section, and configuring the rule.

## Explanation
Port forwarding requires logging into your home router's admin panel using its local IP address and login details.

**1. Find your router's IP address (default gateway):** On Windows, open Command Prompt/PowerShell and run `ipconfig`, then look for "Default Gateway". On Linux, open a terminal and run `ip route | grep default` (alternatively `ip a`), then look for the "Gateway IP". Once found (typically something like `192.168.1.1` or `192.168.0.1`), paste it into a browser's address bar to open the router's login page.

**2. Find your router's login details:** default username/password are usually printed on a sticker on the back or bottom of the physical router. If those don't work and the custom password is forgotten, hold the router's pinhole reset button (with a paperclip) for 10-30 seconds until the lights flash, resetting it to factory defaults.

**3. Locate the port forwarding section:** name varies by router brand -- check the Advanced, Security, or LAN menus for labels like Port Forwarding, Port Mapping, NAT Forwarding, Virtual Server, or Port Triggering.

**4. Configure the port forward rule:** set the Internal/Local IP Address to the local IP of the hosting machine (find it the same way as step 1, labeled "IPv4 Address", usually starting with `192.168.x.x` or `10.0.x.x`); set Port to your server's port (default `47649`, or whatever is shown in-game under "Invite Players"); set Protocol to **UDP** specifically, not TCP, since Cubyz's server networking runs over UDP.

## Related Questions
- How do you find your machine's local gateway IP for Cubyz server port forwarding, on Linux?
- How do you find your machine's local gateway IP for Cubyz server port forwarding, on Windows?
- What command finds your default gateway IP on Linux?
- What should you do if you forgot your router's admin login and the default credentials don't work?
- What network protocol should you select when configuring a Cubyz port forward rule?
- What menus should you check to find the port forwarding section in a router's admin panel?
- What internal IP address should you use when configuring a Cubyz port forward rule?

*Source: unknown | chunk_id: docs_docs_development_multiplayer.md_chunk_3*
