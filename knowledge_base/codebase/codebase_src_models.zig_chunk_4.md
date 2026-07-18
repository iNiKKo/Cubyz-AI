# [hard/codebase_src_models.zig] - Chunk 4

**Type:** serialization
**Keywords:** error handling, memory management, string parsing, data structures, file I/O
**Symbols:** loadRawModelDataFromObj
**Concepts:** model loading, OBJ file format

## Summary
Parses raw OBJ model data into a list of QuadInfo structures.

## Explanation
The chunk defines functions to load and process OBJ model data. It includes parsing vertices, normals, UVs, and faces from the input data. Triangular faces are converted into quads by duplicating one vertex. The function handles errors during parsing and logs them using `std.log.err`. It uses Zig's standard library for string manipulation and memory management.

## Related Questions
- How does the function handle errors during parsing?
- What data structures are used to store parsed vertices, normals, and UVs?
- How are triangular faces converted into quads?
- What is the purpose of the `coordinateSystem` parameter in the function?
- How does the function manage memory for the lists it creates?
- What logging mechanism is used to report parsing errors?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_4*
