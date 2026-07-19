# [issues/issue_2102.md] - Issue #2102 discussion

**Type:** review
**Keywords:** block entity, server crash, client kick, invalid request, network protocols, inventory management, GUI operations
**Symbols:** main.network.Protocols.blockEntityUpdate.sendClientDataUpdateToServer, main.game.world.?.conn, pos, inventorySize, main.items.Inventory.init, main.globalAllocator, inventory, main.gui.windowlist.chest.setInventory, main.gui.openWindow, main.Window.setMouseGrabbed
**Concepts:** client-server communication, error handling, user input validation

## Summary
The server no longer crashes but instead kicks the client when requesting block entity data for a non-block entity.

## Explanation
The server no longer crashes but instead kicks the client when requesting block entity data for a non-block entity. The original issue caused the server to crash when a client requested block entity data for a block that was not a block entity. The change now prevents this by kicking the client with an error message 'Got error while executing user command: Invalid. Disconnecting.' and disconnecting it, which is considered preferable as it stops invalid requests from affecting other clients or the server stability.

To replicate this issue, you can use a modified client that runs the following function:
```
main.network.Protocols.blockEntityUpdate.sendClientDataUpdateToServer(main.game.world.?.conn, pos);

const inventorySize = 20;
const inventory = main.items.Inventory.init(main.globalAllocator, inventorySize, .normal, .{.blockInventory = pos}, .{});

main.gui.windowlist.chest.setInventory(inventory);
main.gui.openWindow("chest");
main.Window.setMouseGrabbed(false);
```

The inventory is initialized using `main.items.Inventory.init` with a size of 20, type `.normal`, and block inventory position set to `pos`. The inventory is then set for a chest window using `main.gui.windowlist.chest.setInventory(inventory)`, and the window is opened with `main.gui.openWindow("chest")`. The mouse grab is disabled with `main.Window.setMouseGrabbed(false)`.

This change ensures that invalid requests are handled gracefully without impacting server stability or other clients. However, there is no mention of logging or monitoring for such invalid requests in the current implementation.

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
