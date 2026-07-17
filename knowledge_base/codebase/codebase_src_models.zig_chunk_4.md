# [hard/codebase_src_models.zig] - Chunk 4

**Type:** serialization
**Keywords:** OBJ parsing, std.mem.splitScalar, coordinateSystem.convertVec, ListManaged, neighborFacingQuads, deinit, getRawFaces
**Symbols:** Model
**Concepts:** OBJ file parsing, vertex loading, normal loading, UV loading, face splitting, tri generation, quad generation, mesh data access

## Summary
This chunk implements Model loading from OBJ files and provides internal mesh data access.

## Explanation
The chunk defines a function (name not explicitly declared in this snippet) that parses an OBJ file line-by-line using std.mem.splitScalar. It skips empty lines, comments starting with '#', and the header 'v ' for vertex positions by converting them into coordinates via coordinateSystem.convertVec and appending to vertices; 'vn ' normals are parsed similarly and appended to normals; 'vt ' UVs are parsed and appended to uvs. For faces ('f '), it splits each token by '/' expecting exactly two slashes with no double-slashes, parses the three components (vertex index, UV index, normal index) as unsigned integers, decrements them for zero-based indexing, validates that at most four vertices per face, then appends a Tri or QuadInfo to tris or quadFaces accordingly. After parsing all faces, it builds a ListManaged(QuadInfo) called quadInfos by iterating over tris: extracting the normal from normals.items[face.normal], UVs A/B/C from uvs.items using indices face.uvs[0/2/1], and corners A/B/C from vertices.items using face.vertex[0/2/1]; it constructs a QuadInfo with those three unique corners plus cornerB duplicated, normal, cornerUV mapping uvA→uvB→uvC→uvB, textureSlot 0. Then it iterates quadFaces similarly, extracting UVs in order [1,0,2,3] and vertices [1,0,2,3], constructing a QuadInfo with all four distinct corners and corresponding UVs. The function returns quadInfos.toOwnedSlice(). A deinit method frees six neighborFacingQuads arrays and internalQuads via main.globalAllocator. A getRawFaces public function iterates model.internalQuads and appends each quad's owned data to the passed quadList, then iterates over 6 neighbor indices (model.neighborFacingQuads[neighbor]), retrieves each quadIndex.quadInfo().*, copies that struct into a mutable quad variable, adds the face normal to every corner via @as(Vec3f, corner.*) + @as(Vec3f, quad.normal), and appends the modified quad.

## Code Example
```zig
fn deinit(self: *const Model) void {
	for (0..6) |i| {
		main.globalAllocator.free(self.neighborFacingQuads[i]);
	}
	main.globalAllocator.free(self.internalQuads);
	main.globalAllocator.free(self.collision);
}
```

## Related Questions
- What does the Model deinit method free and why are there six neighbor arrays?
- How are vertex indices normalized from OBJ 1-based to zero-based values in this chunk?
- In what order does the quadInfos construction iterate tris versus quadFaces?
- Why is cornerB duplicated when constructing a QuadInfo from a tri face?
- What validation occurs for face tokens before parsing their components?
- How does getRawFaces modify neighbor-facing quads before appending them?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_4*
