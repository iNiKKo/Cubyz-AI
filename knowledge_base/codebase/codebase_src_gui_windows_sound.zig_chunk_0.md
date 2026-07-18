# [easy/codebase_src_gui_windows_sound.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, volume adjustment, decibel conversion, linear scale, window lifecycle
**Symbols:** window, musicCallback, deziBelToLinear, linearToDezibel, musicFormatter, padding, onOpen, onClose
**Concepts:** GUI window management, volume control, slider component, settings persistence

## Summary
This chunk defines a GUI window for sound settings, including components like sliders and formatters for music volume control.

## Explanation
The code initializes a `GuiWindow` with `contentSize = {128, 256}`. `deziBelToLinear`/`linearToDezibel` convert between a -60..0 dB slider range and a 0..1 linear volume, both treating anything below -59.95 dB as silent (`0` linear / `-60` dB). `musicFormatter` displays `"Music volume: Off"` when the linear percentage is exactly 0, otherwise just `"Music volume:"` (the source does not actually append the numeric percentage in that branch). `onOpen` sets up a single `ContinuousSlider` ranging from `-60` to `0` (dB), initialized from the current `settings.musicVolume` converted to dB; on change, `musicCallback` converts the new dB value back to linear, stores it in `settings.musicVolume`, and calls `settings.save()`. `onClose` deinitializes the window's root component.

## Code Example
```zig
fn musicCallback(newValue: f32) void {
	settings.musicVolume = deziBelToLinear(newValue);
	settings.save();
}
```

## Related Questions
- What is the purpose of the `musicCallback` function?
- How does the chunk convert between decibel and linear scales?
- What components are used to create the sound settings window?
- How is the music volume formatted for display in the GUI?
- What happens when the sound settings window is opened or closed?
- Where is the music volume saved and loaded from?

*Source: unknown | chunk_id: codebase_src_gui_windows_sound.zig_chunk_0*
