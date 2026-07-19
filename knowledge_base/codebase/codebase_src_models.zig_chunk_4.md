# [hard/codebase_src_models.zig] - Chunk 4

**Type:** serialization
**Keywords:** error handling, memory management, string parsing, data structures, file I/O
**Symbols:** loadRawModelDataFromObj
**Concepts:** model loading, OBJ file format

## Summary
Parses raw OBJ model data into a list of QuadInfo structures.

## Explanation
The chunk defines functions to load and process OBJ model data. It includes parsing vertices, normals, UVs, and faces from the input data. Triangular faces are converted into quads by duplicating one vertex. The function handles errors during parsing and logs them using `std.log.err`. It uses Zig's standard library for string manipulation and memory management.

**Parsing Process:**
- **Vertices (`v`):** Each line starting with 'v' contains three floating-point numbers representing the x, y, and z coordinates of a vertex. These are converted into `Vec3f` using the provided coordinate system.
- **Normals (`vn`):** Each line starting with 'vn' contains three floating-point numbers representing the normal vector's x, y, and z components. These are also converted into `Vec3f`.
- **UVs (`vt`):** Each line starting with 'vt' contains two floating-point numbers representing the texture coordinates (u, v). These are stored as `Vec2f`.
- **Faces (`f`):** Each line starting with 'f' describes a face using vertex/uv/normal indices. The function checks for exactly three or four vertices per face and logs an error if more are found. Triangular faces are directly converted into `Triangle`, while quadrilateral faces are split into two triangles by duplicating one vertex.

**QuadInfo Structure:**
- **Normal (`Vec3f`):** The normal vector of the quad.
- **Corners (`[4]Vec3f`):** The four corner vertices of the quad.
- **CornerUV (`[4]Vec2f`):** The UV coordinates for each corner vertex.
- **TextureSlot (`usize`):** The texture slot index, initialized to 0.

**Triangle Structure:**
- **Vertex (`[3]usize`):** Indices of the three vertices forming the triangle.
- **UVs (`[3]usize`):** Indices of the UV coordinates for each vertex.
- **Normal (`usize`):** Index of the normal vector.

## Related Questions
- How does the function handle errors during parsing?
- What data structures are used to store parsed vertices, normals, and UVs?
- How are triangular faces converted into quads?
- What is the purpose of the `coordinateSystem` parameter in the function?
- How does the function manage memory for the lists it creates?
- What logging mechanism is used to report parsing errors?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_4*
