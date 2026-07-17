# [src/models.zig] - Chunk 1660724247

**Type:** review
**Keywords:** loadModel, exportModel, undefined indices, segmentation fault, bounds checking, parsing, Vec3f, Quad, Triangle, stackAllocator, sanitize, malformed input, text format
**Symbols:** Model, exportModel, loadModel, Vec3f, Vec2f, Triangle, Quad, main.stackAllocator, main.files
**Concepts:** memory safety, bounds checking, parsing robustness, undefined behavior prevention, data serialization, text format parsing, index sanitization, array allocation, defer cleanup, stack allocator usage

## Summary
Added exportModel and loadModel functions to serialize/deserialize model data, but reviewers flagged unsafe parsing that can produce undefined indices leading to segmentation faults when handling malformed or incomplete vertex/UV/normal lines.

## Explanation
The new loadModel function parses a custom text format where each line starts with an identifier ('v ', 'vn ', 'vt ', 'f '). The parser assumes every coordinate field is present and splits on spaces; if a line contains fewer than the expected number of fields (e.g., only one '/' in a face definition), the split iterator yields fewer tokens, leaving some indices uninitialized. These undefined values are then used directly as array indices when appending to vertices, normals, uvs, or tris, which will cause out-of-bounds memory access and crash. Additionally, the parser does not validate that parsed integer indices lie within the bounds of the corresponding arrays; an attacker or corrupted file could supply indices larger than any allocated element. The exportModel side writes data assuming a fixed texture slot layout (4x4 grid) and normalizes coordinates by subtracting 0.5 and flipping axes, but it does not guard against malformed internal quad structures that might produce NaNs or infinities when written to the file, which would then be misread on load. The reviewer's concerns highlight three critical safety gaps: handling of incomplete lines (1//2 vs 1/2), missing fields leading to undefined indices, and lack of bounds checking for user-supplied data.

## Related Questions
- What happens if a face line contains only one '/' instead of two?
- How does the parser handle lines that end with '\r' on Windows?
- Are there any checks to ensure parsed indices are within array bounds before appending?
- Could exportModel produce NaNs if internal quad corners are uninitialized?
- What is the expected format for a valid 'v ' line in this model file?
- Does loadModel skip comment lines starting with '#' reliably on all platforms?
- How does the code handle empty lines or whitespace-only lines during parsing?
- Is there any validation that textureSlot values are within [0,15] before division by 4.0?
- What would be a minimal fix to prevent undefined indices from causing segfaults?
- Could a face definition with three vertices but missing normals cause issues later?

*Source: unknown | chunk_id: github_pr_539_comment_1660724247*
