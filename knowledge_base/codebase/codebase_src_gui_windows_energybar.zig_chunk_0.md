# [easy/codebase_src_gui_windows_energybar.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, energy bar, texture loading, drawing images, window resizing
**Symbols:** window, energyTexture, halfEnergyTexture, noEnergyTexture, init, deinit, render
**Concepts:** GUI rendering, texture management, player energy display

## Summary
Defines the Energy Bar GUI window with specific dimensions and positioning, initializes textures for full, half, and no energy states from predefined file paths, and provides rendering logic that adjusts the window height based on player energy levels.

## Explanation
This chunk defines a GUI window named `window` for displaying the player's energy bar. The window has a scale of 0.5 and is positioned relative to the hotbar window at its lower edge. It has a content size of (160, 20) pixels and does not show a title bar or background. The window is also marked as an HUD element and is not closeable by default.

Textures for full energy (`energyTexture`), half energy (`halfEnergyTexture`), and no energy (`noEnergyTexture`) are initialized from files located at `assets/cubyz/ui/hud/energy.png`, `assets/cubyz/ui/hud/half_energy.png`, and `assets/cubyz/ui/hud/no_energy.png`, respectively. The `init` function loads these textures, while the `deinit` function releases them.

The `render` function checks if the player is in creative mode to skip rendering. It then iterates over the player's energy levels from 0 up to `main.game.Player.super.maxEnergy`. For each level of energy, it binds the appropriate texture based on whether the current energy level plus one or half a unit exceeds the player’s actual energy value and draws it at the correct position. If the rendered content exceeds the window size, it adjusts the window's height accordingly and updates GUI positions.

## Code Example
```zig
pub fn deinit() void {
	energyTexture.deinit();
	halfEnergyTexture.deinit();
	noEnergyTexture.deinit();
}
```

## Related Questions
- What is the purpose of the `window` variable?
- How are textures initialized in this chunk?
- What does the `render` function do if the player is in creative mode?
- How does the `render` function determine which texture to bind?
- What happens when the rendered content exceeds the window size?

*Source: unknown | chunk_id: codebase_src_gui_windows_energybar.zig_chunk_0*
