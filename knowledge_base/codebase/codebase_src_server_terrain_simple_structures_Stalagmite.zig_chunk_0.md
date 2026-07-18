# [easy/codebase_src_server_terrain_simple_structures_Stalagmite.zig] - Chunk 0

**Type:** implementation
**Keywords:** stalagmite, block placement, slope calculation, chunk generation, terrain generation
**Symbols:** Stalagmite, loadModel, generate
**Concepts:** structure generation, block placement, slope calculation

## Summary
Stalagmite structure generation logic

## Explanation
This chunk defines the Stalagmite structure in Cubyz. It includes a loadModel function to initialize the structure from configuration parameters and a generate function to place the structure within a chunk based on its position, size, and slope.

## Code Example
```zig
pub fn generate(self: *Stalagmite, _: GenerationMode, x: i32, y: i32, z: i32, chunk: *main.chunk.ServerChunk, _: CaveMapView, _: CaveBiomeMapView, seed: *u64, _: bool) void {
    const relX: f32 = @as(f32, @floatFromInt(x)) + main.random.nextFloat(seed)*0.6 - 0.3;
    const relY: f32 = @as(f32, @floatFromInt(y)) + main.random.nextFloat(seed)*0.6 - 0.3;
    const relZ: f32 = @as(f32, @floatFromInt(z)) + main.random.nextFloat(seed)*0.6 - 0.3;

    const height = self.size + random.nextFloat(seed)*self.sizeVariation;

    // We want to ensure the following properties:
    // height(r = 0) = height
    // height'(r = 0) = -topSlope
    // height(r = baseRadius) = 0
    // height'(r = baseRadius) = -baseSlope
    // With height(r) = a·r² + b·r + c → height'(r) = 2a·r + b
    // c = height, b = -topSlope
    // 0 = a·baseRadius² + b·baseRadius + c
    // -baseSlope = 2a·baseRadius + b
    // → a·baseRadius = (-baseSlope - b)/2
    // This permits both positive and negative values for baseRadius, so we need to account for that during substitution:
    // = (-baseSlope - b)/2·±baseRadius + b·baseRadius + c
    // → baseRadius = -c/(±(-baseSlope - b)/2 + b)
    const c = height;
    const b = -self.topSlope;
    var baseRadius: f32 = undefined;
    var a: f32 = undefined;
    if (self.baseSlope == self.topSlope) {
        baseRadius = height/self.topSlope;
        a = 0;
    } else {
        baseRadius = -c/((-self.baseSlope - b)/2 + b);
        if (baseRadius < 0) {
            baseRadius = -c/(-(-self.baseSlope - b)/2 + b);
        }
        a = (-self.baseSlope - b)/(2*baseRadius);
    }

    const xMin: i32 = @floor(relX - baseRadius);
    const xMax: i32 = @ceil(relX + baseRadius);
    const yMin: i32 = @floor(relY - baseRadius);
    const yMax: i32 = @ceil(relY + baseRadius);
    var x3: i32 = xMin;
    while (x3 <= xMax) : (x3 += 1) {
        var y3: i32 = yMin;
        while (y3 <= yMax) : (y3 += 1) {
            const distSquare = vec.lengthSquare(Vec2f{@as(f32, @floatFromInt(x3)) - relX, @as(f32, @floatFromInt(y3)) - relY});
            if (distSquare >= baseRadius*baseRadius) continue;
            const r = @sqrt(distSquare);
            const columnHeight = a*r*r + b*r + c;
            if (x3 >= 0 and x3 < chunk.super.width and y3 >= 0 and y3 < chunk.super.width) {
                const zMin: i32 = @round(relZ - columnHeight);
                const zMax: i32 = @round(relZ + columnHeight);
                var z3: i32 = zMin;
                while (z3 <= zMax) : (z3 += 1) {
                    if (z3 >= 0 and z3 < chunk.super.width) {
                        const block: main.blocks.Block = chunk.getBlock(x3, y3, z3);
                        if (block.typ == 0 or block.degradable()) {
                            chunk.updateBlockInGeneration(x3, y3, z3, self.block);
                        }
                    }
                }
            }
        }
    }
}
```

## Related Questions
- What is the purpose of the Stalagmite structure in Cubyz?
- How does the generate function place the stalagmite within a chunk?
- What are the key properties that must be satisfied for the height calculation of the stalagmite?
- What is the algorithm used to calculate the base radius of the stalagmite?
- How does the code handle cases where the base radius is negative?
- What is the purpose of the block placement logic within the generate function?
- What are the conditions under which a block will be updated in the generation process?
- How does the code ensure that the stalagmite structure is placed correctly within the chunk?
- What is the role of the random number generator in the Stalagmite structure generation?
- How does the code handle cases where the base radius is zero?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_Stalagmite.zig_chunk_0*
