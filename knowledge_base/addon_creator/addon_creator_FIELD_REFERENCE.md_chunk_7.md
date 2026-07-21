# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 7

**Type:** documentation
**Keywords:** importExistingAddon, import addon, regex parse, app-io.js, zig.zon
**Symbols:** importExistingAddon, window.projectData

## Summary
Cubyz Addon Creator Studio: how importing an existing addon works (step 3 of the save/export/import pipeline, the reverse of export). This chunk covers IMPORT only -- for the export operation, see the sibling export chunk. Do not blend the two: import regex-*parses* text; export *writes* text -- they are opposite directions.

## Explanation
Importing an existing addon, via **`importExistingAddon()`** in `app-io.js`, does the exact reverse of exporting: it **regex-parses the `.zig.zon` text of each file back into the same internal field names**, repopulating `window.projectData` and the form fields. Unlike export (which walks in-memory objects and writes text out), import reads text in and parses it back into objects.

### Particle Properties
| UI Label | Field ID | Internal property | Exported field | Notes |
|---|---|---|---|---|
| (Particle ID) | `particleId` | `id` | filename | |
| Particle Texture | `particleTextureSearch` | `texture` | `.texture = "{ref}"` | auto-namespaced |
| (checkbox, has emission) | `particleHasEmission` | `hasEmission` | -- | doesn't write a field directly; controls whether a companion `{texture}_emission` texture file is also bundled into the export |
| Speed/Life/Density/Rotation Velocity/Drag min+max pairs | `particleSpeedMin/Max` etc | matching min/max properties | `.speed`/`.lifeTime`/`.density`/`.rotationVelocity`/`.dragCoefficient = {.min=..., .max=...}` | |
| (checkboxes) Random Rotate / Collides | `particleRandomRotate`/`particleCollides` | same | `.randomRotate`/`.collides` | direct boolean passthrough |
| Spawn Shape | `particleSpawnShape` | `shape` | `.shape = .{shape}` | `sphere` adds `.radius` (from `particleShapeRadius`); `cube` adds `.size` (from `particleShapeSize`) |
| Spawn Direction | `particleDirectionMode` | `mode` | `.mode = .{mode}` | `direction` mode adds `.direction = .{x, y, z}` from `particleDirX/Y/Z` |

## Related Questions
- How does the Cubyz Addon Creator import an existing addon?
- What function handles importing an existing addon in the Cubyz Addon Creator?
- How does importing an addon differ from exporting one in the Cubyz Addon Creator?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_7*
