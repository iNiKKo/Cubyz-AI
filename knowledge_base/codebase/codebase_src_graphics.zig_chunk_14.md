# [hard/codebase_src_graphics.zig] - Chunk 14

**Type:** implementation
**Keywords:** glGenFramebuffers, glBindFramebuffer, GL_DEPTH_ATTACHMENT, GL_COLOR_ATTACHMENT0, glTexImage2D, power-of-two sizing, @floatFromInt, gamma correction, texture wrap parameters, depth mask enable, framebuffer complete check, resource deallocation
**Symbols:** FrameBuffer, TextureArray, TextureArray.lodColorInterpolation, FrameBuffer.init, FrameBuffer.deinit, FrameBuffer.updateSize, FrameBuffer.clear, FrameBuffer.validate, FrameBuffer.bindTexture, FrameBuffer.bindDepthTexture, FrameBuffer.bind, FrameBuffer.unbind, TextureArray.init, TextureArray.deinit, TextureArray.bind
**Concepts:** framebuffer management, texture attachment, depth buffer handling, power-of-two texture sizing, gamma-corrected LOD interpolation, OpenGL API bindings, resource cleanup, validation checks

## Summary
This chunk defines the FrameBuffer struct with OpenGL initialization/deinitialization and size update logic, plus a TextureArray struct that manages texture IDs and includes a gamma-corrected LOD color interpolation algorithm.

## Explanation
The FrameBuffer struct declares fields frameBuffer (GLuint), depthTexture (optional GLuint), texture (GLuint), hasDepthTexture (bool). Its init method calls glGenFramebuffers, glBindFramebuffer, then conditionally generates the depth texture with glGenTextures and sets GL_TEXTURE_MIN/MAG_FILTER, GL_TEXTURE_WRAP_S/T parameters via glTexParameteri, attaching it as GL_DEPTH_ATTACHMENT. It also generates the color texture, sets identical filter/wrap params, attaches as GL_COLOR_ATTACHMENT0, and unbinds the framebuffer. The deinit method deletes both framebuffers and textures (depthTexture only if hasDepthTexture). updateSize computes max(1, width/height) to avoid zero dimensions, binds the framebuffer, updates depth texture via glTexImage2D with GL_DEPTH_COMPONENT32F format if present, then updates color texture with glTexImage2D using the provided internalFormat and GL_RGBA/GL_UNSIGNED_BYTE. clear sets depth func to LESS, enables depth mask, disables scissor test, calls glClearColor with Vec4f components, and clears both color and depth buffers. validate binds the framebuffer, defers unbinding, checks status via glCheckFramebufferStatus, logs an error if not GL_FRAMEBUFFER_COMPLETE, returns bool. bindTexture activates a texture target (GL_TEXTURE_2D_ARRAY or similar) then binds self.texture; bindDepthTexture asserts hasDepthTexture before activating and binding depthTexture. bind simply calls glBindFramebuffer with self.frameBuffer; unbind sets the bound framebuffer to 0. The TextureArray struct holds textureID (GLuint). Its init creates an undefined instance, generates a texture ID via glGenTextures, returns it. deinit deletes the texture. bind activates GL_TEXTURE_2D_ARRAY and binds self.textureID. lodColorInterpolation takes four Color values and an alphaCorrection flag; it converts each component to f32 via @floatFromInt, then computes weighted sums using gamma-corrected averaging (weights = a[i]*a[i] when alphaCorrection is true), accumulates rSum/gSum/bSum/aSum with those weights, normalizes by sqrt(sum)/2, and if alphaCorrection and aSum != 0 divides color sums by aSum. It returns a Color with truncated integer components. generate computes maxWidth/maxHeight over an images slice, rounds up to next power-of-two using bit tricks (maxWidth - 1 & maxWidth != 0 check then left shift), but the function body is cut off in this chunk.

## Related Questions
- How does FrameBuffer.init handle optional depth textures?
- What OpenGL calls are used to set texture filter and wrap parameters in FrameBuffer.init?
- Why is the width/height clamped with @max(..., 1) in updateSize?
- How does validate ensure a framebuffer is ready for rendering?
- Which assertion guards bindDepthTexture against missing depth texture?
- What is the purpose of the gamma-corrected average in lodColorInterpolation?
- How are power-of-two dimensions computed in TextureArray.generate?
- Does FrameBuffer.clear modify any OpenGL state beyond color/depth buffers?
- Can a user call both bindTexture and bindDepthTexture on the same FrameBuffer instance?
- What happens to depthTexture when deinit is called without hasDepthTexture set?
- How does TextureArray.init avoid leaking generated texture IDs?
- Is there any synchronization between FrameBuffer and TextureArray in this chunk?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_14*
