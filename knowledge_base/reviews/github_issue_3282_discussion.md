# [issues/issue_3282.md] - Issue #3282 discussion

**Type:** review
**Keywords:** skin, texture, Modelrenderer, assets.zig, EntityModel, GUI, protocol, server, file explorer, preview, inverse mapping, brush shapes, memory optimization
**Symbols:** Skin Component, Modelrenderer, assets.zig, EntityModel
**Concepts:** Texture Management, GUI Design, Network Protocol, File I/O, Graphics Rendering

## Summary
The issue outlines tasks for implementing skin functionality in Cubyz, including displaying, selecting, and editing skins. It also discusses design considerations such as preloading textures and separating default textures from skins.

## Explanation
This issue document serves as a to-do list for developing skin features in Cubyz. The tasks include adding a Skin Component, modifying the Modelrenderer to use skin textures, optimizing GPU memory by avoiding duplicate texture storage, implementing a GUI file explorer with preview, sending selected skins via protocol to the server, storing player skins locally, and ensuring server options to disallow custom skin selection. Additionally, it discusses creating an inverse mapping texture for editing skins and allowing different brush shapes. The maintainer comments suggest preloading textures in assets.zig and considering separating Texture components from EntityModel for more flexibility.

## Related Questions
- How does the Skin Component interact with Modelrenderer?
- What is the purpose of preloading textures in assets.zig?
- How are duplicate textures avoided in GPU memory?
- What is the process for sending selected skins via protocol to the server?
- How is the GUI file explorer implemented, and what features does it have?
- What considerations are made for server options to disallow custom skin selection?

*Source: unknown | chunk_id: github_issue_3282_discussion*
