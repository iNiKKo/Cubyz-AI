# [issues/issue_2949.md] - Issue #2949 discussion

**Type:** review
**Keywords:** Access is denied, rename operation, VSCode process, background processes, directory access, script logging, Zig compiler, Cubyz build, Windows build issue, file system error
**Symbols:** run_windows.bat, debug_windows.bat, compiler\zig-x86_64-windows-0.16.0, zig
**Concepts:** file system access, process management, build automation

## Summary
The issue arises from the `run_windows.bat` script failing to build Cubyz on Windows due to an 'Access is denied' error when renaming the Zig compiler directory. The maintainer suspects that a leftover process, possibly from VSCode, might be holding onto the directory.

## Explanation
The issue arises from the `run_windows.bat` script failing to build Cubyz on Windows due to an 'Access is denied' error when renaming the Zig compiler directory. The maintainer suspects that a leftover process, possibly from VSCode, might be holding onto the directory. Specifically, the script attempts to rename the directory using the command `ren compiler\zig-x86_64-windows-0.16.0 zig`. This operation fails with an 'Access is denied' error, which prevents the build process from proceeding. The maintainer hypothesizes that a background process might still be accessing the directory, causing the rename operation to fail. Enabling logging in the script did not reproduce the issue, suggesting it might be related to specific conditions or leftover processes. Additionally, the exact steps for downloading and extracting the Zig compiler are as follows: `powershell -Command $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -uri https://github.com/PixelGuys/Cubyz-zig-versions/releases/download/0.16.0/zig-x86_64-windows-0.16.0.zip -OutFile compiler\archive.zip` followed by `C:\Windows\System32\tar.exe -xf compiler\archive.zip --directory compiler`. The maintainer also notes that the exact version of the Zig compiler required is `zig-x86_64-windows-0.16.0`, and the script checks for this specific version.

## Related Questions
-  What is the purpose of the `ren` command in the script?
-  How can we identify and terminate any processes holding onto the Zig compiler directory?
-  Is there a way to modify the script to retry the rename operation if it fails due to access issues?
-  Can enabling logging provide more insights into why the 'Access is denied' error occurs?
-  What steps should be taken to ensure that no background processes are accessing the Zig compiler directory during the build process?
-  How can we improve the script's error handling to gracefully manage access denial errors?

*Source: unknown | chunk_id: github_issue_2949_discussion*
