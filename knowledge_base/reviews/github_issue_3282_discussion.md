# [issues/issue_3282.md] - Issue #3282 discussion

**Type:** review
**Keywords:** skin, texture, Modelrenderer, assets.zig, EntityModel, GUI, protocol, server, file explorer, preview, inverse mapping, brush shapes, memory optimization
**Symbols:** Skin Component, Modelrenderer, assets.zig, EntityModel
**Concepts:** Texture Management, GUI Design, Network Protocol, File I/O, Graphics Rendering

## Summary
The issue outlines tasks for implementing skin functionality in Cubyz, including displaying, selecting, and editing skins. It also discusses design considerations such as preloading textures and separating default textures from skins.

## Explanation
This issue document serves as a to-do list for developing skin features in Cubyz, including displaying, selecting, and editing skins. The tasks include adding a Skin Component, modifying the Modelrenderer to use skin textures, optimizing GPU memory by avoiding duplicate texture storage, implementing a GUI file explorer with preview, sending selected skins via protocol to the server, storing player skins locally, and ensuring server options to disallow custom skin selection. Additionally, it discusses creating an inverse mapping texture for editing skins and allowing different brush shapes.

The maintainer comments suggest preloading textures in assets.zig for better flexibility and separating Texture components from EntityModel to allow more reuse of textures. This separation would mean that if a Texture component is not available, a default universal texture (e.g., a uniform purple 'missing texture') could be used instead.

Specifically, the tasks include:
- Adding a Skin Component
- Modifying Modelrenderer to use skin components' textures if detected
- Avoiding duplicate texture storage to save GPU memory
- Implementing a GUI file explorer with a preview window for clients' .cubyz/skins/ folder
- Sending selected skins via skin protocol to the server and storing only the path on disk
- Storing player skins in the save1/skin/ folder
- Allowing server/world options to disallow custom skin selection, which also disables the skin selection button with a tooltip
- Ensuring textures are of the same dimension as the default texture of that model
- Resetting the skin component if a different model is selected
- Allowing transparent regions on the texture only if the default texture also has a transparent spot there

The design considerations include:
- Preloading all available textures in assets.zig or alike for better flexibility
- Separating Texture components from EntityModel to allow more reuse of textures, with a default universal texture (e.g., uniform purple 'missing texture') used if not available

## Related Questions
- How does the Skin Component interact with Modelrenderer?
- What is the purpose of preloading textures in assets.zig?
- How are duplicate textures avoided in GPU memory?
- What is the process for sending selected skins via protocol to the server?
- How is the GUI file explorer implemented, and what features does it have?
- What considerations are made for server options to disallow custom skin selection?

*Source: unknown | chunk_id: github_issue_3282_discussion*
