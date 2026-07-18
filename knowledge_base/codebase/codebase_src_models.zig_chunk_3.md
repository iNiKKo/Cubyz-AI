# [hard/codebase_src_models.zig] - Chunk 3

**Type:** implementation
**Keywords:** floodfill algorithm, collision grid, bit manipulation, model data processing, UV mapping
**Symbols:** loadModel, loadRawModelDataFromObj, allTrue, disableAll, canExpand, addVert
**Concepts:** model loading, collision detection, quad meshing, OBJ file parsing

## Summary
This chunk handles model loading and collision detection, including parsing OBJ data, rasterizing quads, and generating collision boxes.

## Explanation
The chunk defines functions for loading models from OBJ files, processing vertex, normal, and UV data, and converting them into a list of quad information. It also includes methods for detecting collisions by creating a collision grid, using floodfill to propagate collision states, and expanding collision boxes while ensuring all bits in the grid are true within specified bounds.

## Code Example
```zig
const allOnes = ~@as(CollisionGridInteger, 0);
var grid: [collisionGridSize][collisionGridSize]CollisionGridInteger = @splat(@splat(allOnes));

var floodfillQueue = main.utils.CircularBufferQueue(struct { x: usize, y: usize, val: CollisionGridInteger }).init(main.stackAllocator, 1024);
defer floodfillQueue.deinit();
```

## Related Questions
- How does the `loadModel` function process UV data?
- What is the purpose of the `allTrue` function in collision detection?
- How is the collision grid initialized in this chunk?
- What algorithm is used to expand collision boxes?
- How does the floodfill queue contribute to collision detection?
- What is the role of the `addVert` function in model processing?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_3*
