# [easy/codebase_src_server_terrain_simple_structures_Stalagmite.zig] - Chunk 0

**Type:** implementation
**Keywords:** stalagmite, block placement, slope calculation, chunk generation, terrain generation
**Symbols:** Stalagmite, loadModel, generate
**Concepts:** structure generation, block placement, slope calculation

## Summary
Stalagmite structure generation logic

## Explanation
This Zig code defines the Stalagmite structure generation logic in Cubyz. The `loadModel` function initializes the structure from configuration parameters using default values if none are provided: 'block' defaults to 'cubyz:stalagmite', 'size' is set to 12, and 'sizeVariation' is set to 8. Additionally, 'baseSlope' defaults to 4.0 and 'topSlope' defaults to the value of 'baseSlope'. The `generate` function places the stalagmite within a chunk based on its position (x, y, z), size, slope, and random variations. It calculates the height of the stalagmite using parameters such as 'baseSlope', 'topSlope', and ensures that specific properties are satisfied for accurate placement: height(r = 0) = height, height'(r = 0) = -topSlope, height(r = baseRadius) = 0, height'(r = baseRadius) = -baseSlope. The code handles cases where the base radius is negative or zero and ensures correct block updates within the chunk by checking if a block's type is 0 or degradable before updating it.

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
- What are the default values for 'block', 'size', 'sizeVariation', 'baseSlope', and 'topSlope' in the `loadModel` function?
- How does the generate function place the stalagmite within a chunk based on its position, size, and slope?
- What specific properties must be satisfied for accurate height calculation of the stalagmite?
- What is the exact formula used to calculate 'baseRadius' when 'self.baseSlope' equals 'self.topSlope'?
- How does the code handle cases where the base radius is negative or zero during height and radius calculations?
- What are the conditions under which a block will be updated in the generation process within the chunk?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_Stalagmite.zig_chunk_0*
