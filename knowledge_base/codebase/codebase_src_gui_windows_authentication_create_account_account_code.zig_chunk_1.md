# [medium/codebase_src_gui_windows_authentication_create_account_account_code.zig] - Chunk 1

**Type:** implementation
**Keywords:** secureZero, glyphs, rootComponent, deinit, optional cleanup, memory safety, lifecycle hooks, component tree teardown, account code clearing
**Symbols:** onClose, deinit
**Concepts:** secure memory clearing, component deinitialization, dialog lifecycle management

## Summary
This chunk defines the cleanup lifecycle for the account code creation dialog, including secure memory clearing of the displayed code and deinitialization of nested components.

## Explanation
The onClose function is responsible for ensuring no trace of the account code remains in memory by calling std.crypto.secureZero on the glyph buffer of accountCodeLabel.text. It also checks if window.rootComponent exists and calls comp.deinit() to tear down the root component tree. The deinit function handles cleanup of an optional accountCode field, delegating its own deinit call if present. Both functions are declared as pub, indicating they are part of the public API surface for this dialog module.

## Code Example
```zig
	pub fn onClose() void {
	// Make sure there remains no trace of the account code in memory
	std.crypto.secureZero(@TypeOf(accountCodeLabel.text.glyphs[0]), accountCodeLabel.text.glyphs);
	// The account code is cleared in the next() function, otherwise it's kept in case the user goes back in the dialog

	if (window.rootComponent) |*comp| {
		comp.deinit();
	}
}
```

## Related Questions
- What memory safety guarantees does std.crypto.secureZero provide for glyph buffers?
- How is the account code cleared differently between onClose and next functions?
- Under what conditions does deinit call accountCode.?.deinit()?
- What happens if window.rootComponent is null when onClose runs?
- Is there any defer cleanup logic in these lifecycle functions?
- Which types are used for the glyph buffer in accountCodeLabel.text?
- How does this chunk interact with the dialog state machine?
- Are there any error handling paths in onClose or deinit?
- What is the expected order of calls between onClose and deinit?
- Does secureZero require specific alignment or size constraints?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_create_account_account_code.zig_chunk_1*
