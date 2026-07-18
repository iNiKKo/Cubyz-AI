# [src/graphics/Window.zig] - PR #717 review diff

**Type:** review
**Keywords:** game controller mappings, async download, timestamp check, unrecognized controllers, GLFW, std.Thread, HTTP request, file reading, error handling
**Symbols:** init, downloadControllerMappings, updateControllerMappings, controllerMappingsDownloading, downloadControllerMappingsThreadFunc
**Concepts:** asynchronous programming, file handling, HTTP requests, thread management

## Summary
Added functionality to download and update game controller mappings asynchronously, with checks for timestamp and unrecognized controllers.

## Explanation
The changes introduce a new feature to download game controller mappings from a remote URL if certain conditions are met. The `downloadControllerMappings` function checks the current timestamp and whether there are unrecognized controllers to determine if a download is necessary. If so, it spawns a new thread using `std.Thread.spawn` to perform the HTTP request and file writing operations asynchronously. The reviewer suggests using `main.files.read` instead of manually handling file opening and closing to reduce error-prone boilerplate code and improve safety.

## Related Questions
- What is the purpose of the `downloadControllerMappingsThreadFunc` function?
- How does the code determine if a controller mapping download is necessary?
- Why is it recommended to use `main.files.read` instead of manual file handling?
- What potential issues could arise from not closing files in this implementation?
- How does the code handle errors during the HTTP request and file writing process?
- What is the significance of the `controllerMappingsDownloaded` variable?

*Source: unknown | chunk_id: github_pr_717_comment_1761638915*
