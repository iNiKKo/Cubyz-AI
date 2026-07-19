# [issues/issue_2102.md] - Issue #2102 discussion

**Type:** review
**Keywords:** block entity, server crash, client kick, invalid request, network protocols, inventory management, GUI operations
**Symbols:** main.network.Protocols.blockEntityUpdate.sendClientDataUpdateToServer, main.game.world.?.conn, pos, inventorySize, main.items.Inventory.init, main.globalAllocator, inventory, main.gui.windowlist.chest.setInventory, main.gui.openWindow, main.Window.setMouseGrabbed
**Concepts:** client-server communication, error handling, user input validation

## Summary
The server no longer crashes but instead kicks the client when requesting block entity data for a non-block entity.

## Explanation
The original issue caused the server to crash when a client requested block entity data for a block that was not a block entity. The change now prevents this by kicking the client with an error message 'Got error while executing user command: Invalid. Disconnecting.' and disconnecting it, which is considered preferable as it stops invalid requests from affecting other clients or the server stability.

## Related Questions
- What is the purpose of `main.network.Protocols.blockEntityUpdate.sendClientDataUpdateToServer`?
- How does the server handle invalid block entity data requests now?
- Why was kicking the client considered preferable over crashing the server?
- What changes were made to prevent server crashes in this scenario?
- How is the inventory initialized and set for a chest window?
- What are the implications of disconnecting clients with invalid requests?
- Is there any logging or monitoring added for such invalid requests?
- How does this change affect other clients connected to the server?
- Are there any potential performance impacts from kicking clients?
- What is the role of `main.globalAllocator` in inventory initialization?

*Source: unknown | chunk_id: github_issue_2102_discussion*
