# [src/server/world.zig] - PR #878 review diff

**Type:** review
**Keywords:** base64, hashedName, playerData, readToZon, savePlayer, ZonElement, object, array, crash, put, gamemode, inventory
**Symbols:** ServerWorld, User, files.readToZon, std.fmt.bufPrint, std.base64.url_safe.Encoder.encode, player.loadFrom, main.items.Inventory.Sync.setGamemode, std.meta.stringToEnum, main.game.Gamemode, playerData.getChild, playerData.get, ZonElement.initObject
**Concepts:** File Handling, Error Handling, Security, Data Serialization, Architectural Review

## Summary
Refactored the `findPlayer` function to use hashed usernames for file paths and added a new `savePlayer` function. Updated error handling in `savePlayer` to ensure `playerZon` is an object.

## Explanation
The refactoring of the `findPlayer` function involved changing how player data files are accessed by using a base64 URL-safe encoded version of the username instead of the raw username. This change aims to prevent issues with special characters in filenames and improve security. The new `savePlayer` function is introduced to handle saving player data, ensuring that if the file does not exist or is not an object, a new one is created. The reviewer highlighted a critical architectural concern regarding the potential return type of `readToZon`, which might be an array instead of an object. This could lead to crashes when calling methods like `put`. The review emphasizes the need to check if `playerZon` is indeed an object and create a new one if it is not, thus preventing runtime errors.

## Related Questions
- What is the purpose of hashing the username in the file path?
- How does the refactored `findPlayer` function handle player data loading?
- Why is there a check for `playerZon` being an object in the `savePlayer` function?
- What potential issues could arise if `readToZon` returns an array instead of an object?
- How does the new `savePlayer` function ensure data integrity during saving?
- What are the benefits of using base64 encoding for usernames in file paths?

*Source: unknown | chunk_id: github_pr_878_comment_1900467230*
