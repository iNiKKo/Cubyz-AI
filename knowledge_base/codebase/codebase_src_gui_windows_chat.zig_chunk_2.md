# [medium/codebase_src_gui_windows_chat.zig] - Chunk 2

**Type:** api
**Keywords:** chat rendering, message queueing, command execution, network messaging, input validation
**Symbols:** render, addMessage, sendMessage
**Concepts:** GUI chat window, message queue, chat message sending, input handling

## Summary
Handles rendering and managing chat messages in the GUI.

## Explanation
This chunk contains functions for rendering the chat window, adding messages to a queue, sending messages, and handling input. The `render` function draws the chat window if it's not hidden. The `addMessage` function adds a message to the message queue. The `sendMessage` function checks the length of the input message, logs an error if it exceeds limits, flushes the message history, and sends the message either as a command or through the network protocol.

## Code Example
```zig
pub fn render() void {
	if (!hideInput) {
		const oldColor = main.graphics.draw.setColor(0x80000000);
		defer main.graphics.draw.restoreColor(oldColor);
		main.graphics.draw.rect(.{0, 0}, window.contentSize);
	}
}
```

## Related Questions
- How does the chat window render?
- What is the maximum length of a chat message?
- How are messages added to the queue?
- What happens if a message exceeds the character limit?
- How are commands sent through the chat?
- How is input cleared after sending a message?

*Source: unknown | chunk_id: codebase_src_gui_windows_chat.zig_chunk_2*
