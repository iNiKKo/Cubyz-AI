# [src/server/terrain/simple_structures/SbbGen.zig] - PR #1530 review diff

**Type:** review
**Keywords:** rotation, SbbGen, structureRef, loadModel, error handling, unknown rotation, structure ID, ZonElement, NeverFailingAllocator
**Symbols:** SbbGen, structureRef, placeMode, rotation, getHash, loadModel, NeverFailingAllocator, ZonElement, sbb.StructureBuildingBlock, Blueprint.PasteMode, sbb.Rotation
**Concepts:** error handling, data validation, parameter parsing

## Summary
Added rotation parameter handling to SbbGen and improved error messages for missing or invalid structure IDs.

## Explanation
The change introduces a new `rotation` field in the `SbbGen` struct to handle rotations of structure building blocks. The `loadModel` function now retrieves this rotation from parameters, converting it using `sbb.Rotation.fromZon`. If an unknown string is encountered during rotation parsing, an error message is logged with the specific structure ID and rotation value. This update enhances error handling by providing more informative messages when loading fails due to missing or invalid data.

## Related Questions
- What is the purpose of the `rotation` field in the `SbbGen` struct?
- How does the function handle errors when parsing the rotation parameter?
- What happens if an unknown string is provided for the rotation?
- Why was it necessary to improve error messages for missing or invalid structure IDs?
- Can you explain how the `loadModel` function retrieves and processes the rotation parameter?
- What changes were made to the error logging in the `loadModel` function?

*Source: unknown | chunk_id: github_pr_1530_comment_2159975173*
