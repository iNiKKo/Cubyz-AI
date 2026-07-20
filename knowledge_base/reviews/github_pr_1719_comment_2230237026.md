# [src/settings.zig] - PR #1719 review diff

**Type:** review
**Keywords:** double free, deinit, zonObject, join, error handling, memory leak
**Symbols:** save, zonObject, keyboard, main.files.cubyzDir().readToZon, settingsFile, oldZonObject
**Concepts:** thread safety, memory management

## Summary
The change introduces a potential double-free issue by deinitializing both `oldZonObject` and `zonObject`.

## Explanation
The change introduces a potential double-free issue by deinitializing both `oldZonObject` and `zonObject`. Specifically, if `oldZonObject` is an object, calling `deinit(main.stackAllocator)` on it after joining with `zonObject` will lead to a double free. The code checks if `oldZonObject` is an object before joining; if not, it deinits `oldZonObject` and then assigns `zonObject` to it. This architectural oversight needs to be addressed to prevent memory corruption and ensure thread safety.

The error handling in the `readToZon` function call logs an error message if the file cannot be read, except when the error is `FileNotFound`. The purpose of `zonObject.join(zonObject)` is to merge the new settings with the old ones, preserving any unknown settings. Proper memory management is crucial to avoid issues like double frees and ensure thread safety.

The exact code changes are as follows:
```zig
- const oldZonObject: ZonElement = main.files.cubyzDir().readToZon(main.stackAllocator, settingsFile) catch |err| blk: {
+ var oldZonObject: ZonElement = main.files.cubyzDir().readToZon(main.stackAllocator, settingsFile) catch |err| blk: {
  if(err != error.FileNotFound) {
    std.log.err("Could not read settings file: {s}", .{@errorName(err)});
  }
  break :blk .null;
};
defer oldZonObject.deinit(main.stackAllocator);

- oldZonObject.join(zonObject);
+ if(oldZonObject == .object) {
+  oldZonObject.join(zonObject);
+} else {
+  oldZonObject.deinit(main.stackAllocator);
+  oldZonObject = zonObject;
```

The potential consequences of not properly managing memory in this function include memory corruption, undefined behavior, and crashes. To ensure that both objects are not deinitialized twice, the code should be modified to avoid calling `deinit` on `oldZonObject` if it has already been joined with `zonObject`. Additionally, similar issues might occur in other parts of the codebase where similar memory management patterns are used.

## Related Questions
- What is the purpose of `zonObject.join(zonObject)` in this code?
- How does the error handling work in the `readToZon` function call?
- Why is there a need to check if `oldZonObject` is an object before joining?
- What are the potential consequences of not properly managing memory in this function?
- How can we ensure that both objects are not deinitialized twice?
- Is there any other part of the codebase where similar issues might occur?

*Source: unknown | chunk_id: github_pr_1719_comment_2230237026*
