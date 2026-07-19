# [hard/codebase_src_graphics.zig] - Chunk 15

**Type:** implementation
**Keywords:** framebuffer, texture, OpenGL, rendering, resource management
**Symbols:** FrameBuffer, FrameBuffer.frameBuffer, FrameBuffer.texture, FrameBuffer.hasDepthTexture, FrameBuffer.depthTexture, FrameBuffer.init, FrameBuffer.deinit, FrameBuffer.updateSize, FrameBuffer.clear, FrameBuffer.validate, FrameBuffer.bindTexture, FrameBuffer.bindDepthTexture, FrameBuffer.bind, FrameBuffer.unbind
**Concepts:** OpenGL framebuffer management, texture handling, rendering setup

## Summary
The FrameBuffer struct manages OpenGL framebuffers and textures for rendering.

## Explanation
The FrameBuffer struct manages OpenGL framebuffers and textures for rendering. It encapsulates the creation, management, and destruction of these resources using OpenGL functions. The struct maintains state for the framebuffer ID (`frameBuffer`), texture ID (`texture`), depth texture presence (`hasDepthTexture`), and depth texture ID (`depthTexture`).

### Initialization (`init`)
The `init` method initializes a framebuffer with optional depth texture support. It sets up the framebuffer, binds it, and configures textures based on the provided parameters (`hasDepthTexture`, `textureFilter`, `textureWrap`). If depth texture is enabled, it generates and configures a depth texture.

### Deinitialization (`deinit`)
The `deinit` method deletes the framebuffer and associated textures (both color and depth) to free up resources.

### Update Size (`updateSize`)
The `updateSize` method resizes the framebuffer and its textures. It ensures that the width and height are at least 1, binds the framebuffer, and updates the texture dimensions using `glTexImage2D`. If a depth texture is present, it also updates the depth texture.

### Clear (`clear`)
The `clear` method sets up the clear color and clears both the color and depth buffers. It uses OpenGL functions like `glClearColor`, `glClearDepth`, and `glClear` to achieve this.

### Validate (`validate`)
The `validate` method checks if the framebuffer is complete by calling `glCheckFramebufferStatus`. If the status is not `GL_FRAMEBUFFER_COMPLETE`, it logs an error message.

### Bind Texture (`bindTexture`)
The `bindTexture` method binds the color texture to a specified OpenGL target using `glActiveTexture` and `glBindTexture`.

### Bind Depth Texture (`bindDepthTexture`)
The `bindDepthTexture` method binds the depth texture to a specified OpenGL target, ensuring that depth texture support is enabled.

### Bind Framebuffer (`bind`)
The `bind` method binds the framebuffer using `glBindFramebuffer`.

### Unbind Framebuffer (`unbind`)
The `unbind` method unbinds the current framebuffer by binding the default framebuffer (ID 0) using `glBindFramebuffer`.

## Code Example
```zig
pub fn clear(_: FrameBuffer, clearColor: Vec4f) void {
	c.glDepthFunc(c.GL_LESS);
	c.glDepthMask(c.GL_TRUE);
	c.glDisable(c.GL_SCISSOR_TEST);
	c.glClearColor(clearColor[0], clearColor[1], clearColor[2], clearColor[3]);
	c.glClear(c.GL_COLOR_BUFFER_BIT | c.GL_DEPTH_BUFFER_BIT);
}
```

## Related Questions
- How does the FrameBuffer struct initialize its OpenGL resources?
- What methods are provided to update the size of a framebuffer and its textures?
- How is depth texture handling managed within the FrameBuffer struct?
- What steps are taken to validate that a framebuffer is complete?
- How do you bind and unbind a framebuffer using the FrameBuffer struct?
- What OpenGL functions are used in the clear method of FrameBuffer?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_15*
