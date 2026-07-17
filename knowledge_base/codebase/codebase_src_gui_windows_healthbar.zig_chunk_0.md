# [easy/codebase_src_gui_windows_healthbar.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, Texture.initFromFile, isCreative, super.health, ceil, max, boundImage, updateWindowPositions, deadHeartTexture, hud, scale, contentSize, render loop, attachment points, placeholder hearts
**Symbols:** GuiWindow, GuiComponent, Texture, Vec2f, window, heartTexture, halfHeartTexture, deadHeartTexture, init, deinit, render
**Concepts:** GUI component, health bar rendering, texture atlas management, creative mode bypass, dynamic content sizing, ECS player state access

## Summary
This chunk defines the health bar GUI component, initializing heart textures and rendering player health as a grid of whole hearts, half-hearts, and dead-heart placeholders.

## Explanation
The chunk declares a public GuiWindow instance named window with scale 0.5, attached to hotbar.window at upper points (selfAttachmentPoint = .upper, otherAttachmentPoint = .upper) and (.upper, .lower), content size {160,20}, isHud true, no title bar, no background, not hidden when mouse grabbed, and not closeable. It declares three global Texture variables: heartTexture, halfHeartTexture, deadHeartTexture (all undefined initially). The init() function loads textures from assets/cubyz/ui/hud/heart.png, half_heart.png, dead_heart.png via Texture.initFromFile. deinit() calls .deinit on each texture. render() first returns early if main.game.Player.isCreative(). It computes displayHealth as max(0, main.game.Player.super.health), calculates halfHeartUnits = ceil(displayHealth*2), wholeHearts = floor(halfHeartUnits/2), halfHeart = halfHeartUnits%2, and totalHearts = ceil(main.game.Player.super.maxHealth). The rendering loop iterates i from 0 to totalHearts-1; when x reaches window.contentSize[0] it resets x=0 and increments y by 20. For each heart slot: if i < wholeHearts bind heartTexture, else if i < wholeHearts+halfHeart bind halfHeartTexture, else bind deadHeartTexture. Then draw.boundImage is called with position Vec2f{x, window.contentSize[1] - y - 20} and size {20,20}. After the loop, y is incremented by 20; if y != window.contentSize[1], the contentSize height is updated to y and gui.updateWindowPositions() is invoked.

## Code Example
```zig
pub fn deinit() void {
	heartTexture.deinit();
	halfHeartTexture.deinit();
	deadHeartTexture.deinit();
}
```

## Related Questions
- What happens to the health bar when the player is in creative mode?
- How are heart textures loaded and what file paths are used?
- Why does render() update window.contentSize[1] after drawing hearts?
- What determines whether a dead-heart placeholder is drawn for a given slot?
- Which GUI component is this window attached to and how are attachment points configured?
- Does the health bar ever draw more than totalHearts icons, or is it capped?
- How does the code compute wholeHearts versus halfHeart from displayHealth?
- What is the purpose of gui.updateWindowPositions() in render()?
- Are any textures reused across multiple slots or are they bound per slot?
- If a player has exactly 3 health points, how many dead-heart placeholders appear?
- How does the rendering loop handle wrapping when x reaches window.contentSize[0]?
- What is the exact size of each drawn heart icon in pixels?

*Source: unknown | chunk_id: codebase_src_gui_windows_healthbar.zig_chunk_0*
