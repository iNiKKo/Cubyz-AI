# [src/server/world.zig] - PR #878 review diff

**Type:** review
**Keywords:** base64, hashing, file handling, player data, gamemode, ZonElement, readToZon, savePlayer, object type check, directory traversal
**Symbols:** ServerWorld, User, files.readToZon, main.stackAllocator, std.fmt.bufPrint, hashedName, playerData, player.loadFrom, main.items.Inventory.Sync.setGamemode, std.meta.stringToEnum, main.game.Gamemode, savePlayer, path, playerZon
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The `findPlayer` function has been updated to hash the player's name for safer file handling and to load specific child elements from the player data. A new `savePlayer` function has been added to save player data, with a critical review noting potential issues if `readToZon` returns an array instead of an object.

## Explanation
The changes in the `findPlayer` function include hashing the player's name using base64 URL-safe encoding to prevent directory traversal attacks and ensure safer file paths. The function now specifically loads the 'entity' child from the player data and sets the gamemode based on the data retrieved. A new `savePlayer` function has been introduced to handle saving player data, including creating a new ZonElement if `readToZon` does not return an object. This is crucial for preventing crashes when calling put operations on non-object types.

## Related Questions
- What is the purpose of hashing the player's name in the `findPlayer` function?
- How does the new `savePlayer` function handle cases where `readToZon` returns an array instead of an object?
- Why is it important to check if `playerZon` is an object before performing put operations?
- What potential security risks are mitigated by hashing the player's name in file paths?
- How does the `savePlayer` function ensure that player data is saved correctly?
- What changes were made to the `findPlayer` function to improve its functionality and safety?

*Source: unknown | chunk_id: github_pr_878_comment_1900467230*
