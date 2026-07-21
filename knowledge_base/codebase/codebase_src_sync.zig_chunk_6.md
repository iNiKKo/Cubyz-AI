# [hard/codebase_src_sync.zig] - Chunk 6

**Type:** implementation
**Keywords:** inventory operations, item durability, crafting ingredients, health management, energy management
**Symbols:** executeBaseOperation, executeDurabilityUseOperation, removeProceduralItemCraftingIngredients, Context, Context.allocator, Context.cmd, Context.side, Context.user, Context.gamemode, Context.execute, Open, Open.inv
**Concepts:** inventory management, durability system, crafting ingredient removal, player health and energy

## Summary
Handles inventory operations and durability management in the game.

## Explanation
This chunk contains functions for executing various base operations on inventories, managing item durability, and removing crafting ingredients from a workbench. It includes methods for moving items, swapping stacks, deleting items, creating new items, transferring items between bags, using item durability, adding health or energy to players, and handling player death.

The `executeBaseOperation` function handles different types of base operations such as move, swap, delete, create, moveToBag, takeFromBag, useDurability, addHealth, and addEnergy. Each operation has specific logic for modifying the inventory or player attributes:
- **move**: Moves items from one slot to another.
  ```zig
  self.executeAddOperation(allocator, side, info.dest, info.amount, info.source.ref().item);
  self.executeRemoveOperation(allocator, side, info.source, info.amount);
  info.source.inv.update();
  info.dest.inv.update();
  ```
- **swap**: Swaps stacks between two slots.
  ```zig
  const oldDestStack = info.dest.ref().*;
  const oldSourceStack = info.source.ref().*;
  self.executeRemoveOperation(allocator, side, info.source, oldSourceStack.amount);
  self.executeRemoveOperation(allocator, side, info.dest, oldDestStack.amount);
  self.executeAddOperation(allocator, side, info.source, oldDestStack.amount, oldDestStack.item);
  self.executeAddOperation(allocator, side, info.dest, oldSourceStack.amount, oldSourceStack.item);
  info.source.inv.update();
  info.dest.inv.update();
  ```
- **delete**: Deletes a specified amount of an item from a slot.
  ```zig
  self.executeRemoveOperation(allocator, side, info.source, info.amount);
  info.source.inv.update();
  ```
- **create**: Creates new items in a slot.
  ```zig
  self.executeAddOperation(allocator, side, info.dest, info.amount, info.item);
  info.dest.inv.update();
  ```
- **moveToBag**: Transfers items from the inventory to a bag.
  ```zig
  const source = info.source.ref();
  const amount = @min(source.amount, info.amount);
  source.amount = info.dest.push(.{.item = source.item, .amount = amount});
  if (source.amount == 0) {
      source.item = .null;
  }
  info.amount = amount - source.amount;
  ```
- **takeFromBag**: Transfers items from a bag to the inventory.
  ```zig
  const dest = info.dest.ref();
  if (dest.item == .null) {
      dest.item = info.source.peek(0).item;
  }
  info.amount = @min(info.amount, dest.item.stackSize());
  var remainingAmount = info.amount;
  while (remainingAmount != 0) {
      var stack = info.source.peek(0);
      if (stack.item == .null) break;
      if (!std.meta.eql(stack.item, dest.item)) break;
      _ = info.source.pop();
      if (stack.amount > remainingAmount) {
          stack.amount -= remainingAmount;
          remainingAmount = 0;
          std.debug.assert(info.source.push(stack) == 0);
          break;
      }
      remainingAmount -= stack.amount;
  }
  info.amount -= remainingAmount;
  dest.amount += info.amount;
  ```
- **useDurability**: Decreases the durability of an item and removes it if its durability becomes zero. If the durability is zero, the item is removed from the inventory.
  ```zig
  self.executeDurabilityUseOperation(allocator, side, info.source, info.durability);
  info.source.inv.update();
  ```
- **addHealth**: Adds or subtracts health values to players. If the player's health drops below zero, they are killed, their health is reset to maximum, and a message is sent indicating that they have been killed.
  ```zig
  if (side == .server) {
      info.previous = info.target.?.player().health;
      info.target.?.player().health = std.math.clamp(info.target.?.player().health + info.health, 0, info.target.?.player().maxHealth);
      if (info.target.?.player().health <= 0) {
          info.target.?.player().health = info.target.?.player().maxHealth;
          info.cause.sendMessage(info.target.?.name);
          self.syncOperations.append(allocator, .{.kill = .{
              .target = info.target.?,
              .spawnPoint = info.target.?.getSpawnPos(),
          }});
      } else {
          self.syncOperations.append(allocator, .{.health = .{
              .target = info.target.?,
              .health = info.health,
          }});
      }
  } else {
      info.previous = main.game.Player.super.health;
      main.game.Player.super.health = std.math.clamp(main.game.Player.super.health + info.health, 0, main.game.Player.super.maxHealth);
  }
  ```
- **addEnergy**: Adds or subtracts energy values to players.
  ```zig
  if (side == .server) {
      info.previous = info.target.?.player().energy;
      info.target.?.player().energy = std.math.clamp(info.target.?.player().energy + info.energy, 0, info.target.?.player().maxEnergy);
      self.syncOperations.append(allocator, .{.energy = .{
          .target = info.target.?,
          .energy = info.energy,
      }});
  } else {
      info.previous = main.game.Player.super.energy;
      main.game.Player.super.energy = std.math.clamp(main.game.Player.super.energy + info.energy, 0, main.game.Player.super.maxEnergy);
  }
  ```

Crafting ingredients are removed from a workbench by iterating through the items in the inventory and deleting them using the `executeBaseOperation` function with the delete operation. The `executeDurabilityUseOperation` function decreases the durability of an item and removes it if its durability becomes zero. Player health and energy are managed by adding or subtracting values to the player's current health or energy, respectively.

## Code Example
```zig
pub fn execute(self: Context, _op: BaseOperation) void {
			return self.cmd.executeBaseOperation(self.allocator, _op, self.side);
		}
```

## Related Questions
- What is the purpose of the `executeBaseOperation` function?
- How does the chunk handle item durability usage?
- What operations are supported by the `Context.execute` method?
- How are crafting ingredients removed from a workbench?
- What happens when an item's durability reaches zero?
- How is player health and energy managed in this chunk?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_6*
