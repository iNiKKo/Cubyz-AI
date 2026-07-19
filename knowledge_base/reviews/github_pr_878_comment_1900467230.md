# [src/server/world.zig] - PR #878 review diff

**Type:** review
**Keywords:** base64, hashedName, playerData, readToZon, savePlayer, ZonElement, object, array, crash, put, gamemode, inventory
**Symbols:** ServerWorld, User, files.readToZon, std.fmt.bufPrint, std.base64.url_safe.Encoder.encode, player.loadFrom, main.items.Inventory.Sync.setGamemode, std.meta.stringToEnum, main.game.Gamemode, playerData.getChild, playerData.get, ZonElement.initObject
**Concepts:** File Handling, Error Handling, Security, Data Serialization, Architectural Review

## Summary
Refactored the `findPlayer` function to use hashed usernames for file paths and added a new `savePlayer` function. Updated error handling in `savePlayer` to ensure `playerZon` is an object.

## Explanation
The refactoring of the `findPlayer` function involved changing how player data files are accessed by using a base64 URL-safe encoded version of the username instead of the raw username. This change aims to prevent issues with special characters in filenames and improve security. The new `savePlayer` function is introduced to handle saving player data, ensuring that if the file does not exist or is not an object, a new one is created. The reviewer highlighted a critical architectural concern regarding the potential return type of `readToZon`, which might be an array instead of an object. This could lead to crashes when calling methods like `put`. The review emphasizes the need to check if `playerZon` is indeed an object and create a new one if it is not, thus preventing runtime errors.

The exact command/config syntax for how player data is loaded in the `findPlayer` function is as follows:
```zig
var dest: [1024]u8 = undefined;
const hashedName = std.base64.url_safe.Encoder.encode(&dest, user.name);

var buf: [32768]u8 = undefined;
const playerData = files.readToZon(main.stackAllocator, std.fmt.bufPrint(&buf, "saves/{s}/players/{s}.zig.zon", .{self.name, hashedName}) catch "") catch .null; // TODO: Utils.escapeFolderName(user.name)
defer playerData.deinit(main.stackAllocator);
const player = &user.player;
if(playerData == .null) {
    player.pos = @floatFromInt(self.spawn);
} else {
    player.loadFrom(playerData.getChild("entity"));

    main.items.Inventory.Sync.setGamemode(user, std.meta.stringToEnum(main.game.Gamemode, playerData.get([]const u8, "gamemode", "survival")).?);
}
```
The exact command/config syntax for how player data is saved in the `savePlayer` function is as follows:
```zig
var dest: [1024]u8 = undefined;
const hashedName = std.base64.url_safe.Encoder.encode(&dest, user.name);

var buf: [32768]u8 = undefined;
const path = try std.fmt.bufPrint(&buf, "saves/{s}/players/{s}.zig.zon", .{self.name, hashedName});

var playerZon: ZonElement = files.readToZon(main.stackAllocator, path) catch ZonElement.initObject(main.stackAllocator);
```
The error handling mechanism used in `savePlayer` to ensure `playerZon` is an object is as follows:
```zig
if (playerZon.type != .object) {
    playerZon = ZonElement.initObject(main.stackAllocator);
}
```
This ensures that if `readToZon` returns an array instead of an object, a new object is created to prevent runtime errors.

## Related Questions
- What is the purpose of hashing the username in the file path?
- How does the refactored `findPlayer` function handle player data loading?
- Why is there a check for `playerZon` being an object in the `savePlayer` function?
- What potential issues could arise if `readToZon` returns an array instead of an object?
- How does the new `savePlayer` function ensure data integrity during saving?
- What are the benefits of using base64 encoding for usernames in file paths?

*Source: unknown | chunk_id: github_pr_878_comment_1900467230*
