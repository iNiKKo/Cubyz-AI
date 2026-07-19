# [easy/codebase_src_gui_windows_healthbar.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, texture initialization, drawing loop, dynamic content size, window repositioning
**Symbols:** window, heartTexture, halfHeartTexture, deadHeartTexture, init, deinit, render
**Concepts:** GUI component, health bar, texture rendering, player health display

## Summary
Defines a health bar GUI component for the Cubyz game, handling initialization of textures from specified files, rendering heart icons based on player health, and cleanup procedures.

## Explanation
The chunk defines a health bar GUI window that displays the player's health using heart icons. It initializes three textures: `heartTexture`, `halfHeartTexture`, and `deadHeartTexture` from file paths 'assets/cubyz/ui/hud/heart.png', 'assets/cubyz/ui/hud/half_heart.png', and 'assets/cubyz/ui/hud/dead_heart.png' respectively. The `render` function calculates how many whole and half hearts to display based on the player's current health and maximum health. Specifically, it multiplies the player's health by 2 and rounds up to determine the number of half-heart units. It then divides this by 2 to get the number of whole hearts and uses the modulus operator to determine if there is a remaining half heart. If the player's health exceeds their maximum health, the excess is ignored, and only the maximum possible hearts are displayed. The `render` function binds the appropriate texture (full heart, half heart, or dead heart) and draws each heart icon in a grid layout within the window. If the rendered content exceeds the initial window size, it updates the window's content size and triggers a repositioning of all GUI windows. The `init` function initializes these textures from file paths, while the `deinit` function cleans up by deinitializing them.

The health bar window is positioned relative to the hotbar window with its upper edge attached to the upper edge of the hotbar window and its lower edge also attached to the upper edge of the hotbar window. The window's content size is initially set to 160x20 pixels, but it can dynamically adjust based on the number of heart icons rendered. If the player is in creative mode, the health bar does not render any hearts.

## Code Example
```zig
pub fn deinit() void {
	heartTexture.deinit();
	halfHeartTexture.deinit();
	deadHeartTexture.deinit();
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the health bar determine which texture to use for each heart icon?
- What happens if the player's health exceeds their maximum health?
- How is the position and size of the health bar window determined?
- What textures are loaded during initialization, and from where?
- How does the chunk handle rendering when the player is in creative mode?

*Source: unknown | chunk_id: codebase_src_gui_windows_healthbar.zig_chunk_0*
