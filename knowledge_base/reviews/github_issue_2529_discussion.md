# [issues/issue_2529.md] - Issue #2529 discussion

**Type:** review
**Keywords:** workbench synchronization, client-centric design, server-shared inventory, crafting command, Inventory.Type removal, callback generalization, tool derivation, unsynced callbacks, source type, deposit handling
**Symbols:** CraftTool, Inventories, Inventory, Tool, ClientType, workbench, InventoryId, canPutIntoWorkbench, shouldDepositToUserOnClose, onLastCloseCallback
**Concepts:** client-server architecture, synchronization, callback generalization, inventory management

## Summary
The workbench synchronization is being reworked to be more client-centric, reducing server-shared inventory slots and adding a new crafting command. The discussion includes considerations for removing shared `Inventory.Type` and generalizing callbacks like `canPutIntoWorkbench` and `shouldDepositToUserOnClose`. A bug related to unsynced callbacks is identified, leading to a proposed solution involving a new `source` type.

## Explanation
The issue aims to improve the workbench synchronization by making it more client-centric. The server-shared inventory will be reduced to 25 slots, with the output slot handled client-side. A new crafting command is introduced to handle synchronization, similar to changes made in #2506 for inventory crafting. The discussion revolves around removing the shared `Inventory.Type` and generalizing callbacks such as `canPutIntoWorkbench` and `shouldDepositToUserOnClose`. Maintainers suggest deriving the tool from the crafting grid instead of including it explicitly. A user notes that complete removal of the shared type might not be feasible due to special handling required for the crafting grid. Generalization is proposed, with callbacks potentially becoming independent properties or using existing mechanisms like `onLastCloseCallback`. A bug related to unsynced callbacks is identified, prompting a solution involving a new `source` type pointing to the user's inventory to handle deposits on last close.

## Related Questions
- What is the purpose of the new `CraftTool` struct?
- How does the removal of shared `Inventory.Type` impact inventory management?
- Why was the tool removed from the `CraftTool` struct?
- What are the potential benefits of generalizing callbacks like `canPutIntoWorkbench`?
- How does the proposed solution address the bug with unsynced callbacks?
- What is the role of the `onLastCloseCallback` in this context?

*Source: unknown | chunk_id: github_issue_2529_discussion*
