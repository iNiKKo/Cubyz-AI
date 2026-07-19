# [easy/codebase_src_server_terrain_chunkgen_OreGenerator.zig] - Chunk 0

**Type:** world_generation
**Keywords:** terrain generation, random number generation, voxel manipulation, chunk processing, ore distribution
**Symbols:** id, priority, generatorSeed, defaultState, ores, init, generate, considerCoordinates
**Concepts:** world generation, ore placement, randomized terrain features

## Summary
The OreGenerator module is responsible for generating ore veins within terrain chunks based on predefined ore types and world parameters.

## Explanation
The OreGenerator module is responsible for generating ore veins within terrain chunks based on predefined ore types and world parameters. It initializes with a list of available ores and generates ore veins in server chunks using a random seed to determine their placement and distribution. The priority level of the ore generator is set to **32768**, which influences how aggressively it processes each chunk in relation to other generators. The `init` function initializes the list of ores by setting `ores` to the items from `main.blocks.ores`. The `generate` function checks if the chunk's voxel size is 1 and then proceeds to generate ore veins by considering coordinates relative to nearby chunks (a total of 27 chunks centered around the target chunk) to create interconnected ore structures. The `considerCoordinates` function calculates the specific coordinates where ore should be placed within each chunk based on randomization and density parameters, ensuring that ore veins do not exceed their defined height range.

Each ore type has specific parameters such as `maxHeight`, `minHeight`, `size`, `density`, and `veins`. These parameters determine how the ore veins are generated. For example, `maxHeight` and `minHeight` define the vertical range in which the ore can be placed (e.g., `maxHeight <= z << main.chunk.chunkShift` or `ore.minHeight > z << main.chunk.chunkShift`). The `size` parameter controls the size of the ore veins, while the `density` parameter controls the concentration of the ore within those veins. The `veins` parameter determines how many veins of a particular type start in each chunk.

The random number generation process is crucial for determining the placement and distribution of ore veins. The `random.initSeed3D` function initializes a random seed based on the world seed and chunk coordinates, ensuring that the ore generation is consistent across different chunks while still being randomized. The `generatorSeed` is set to **0x88773787bc9e0105**, which is used as part of the seed initialization process.

The `considerCoordinates` function calculates the specific coordinates where ore should be placed within each chunk based on randomization and density parameters. It uses a radius calculated from the expected volume, which is derived from the size and density of the ore. The function ensures that ore veins do not exceed their defined height range by checking if the current z-coordinate falls within the `maxHeight` and `minHeight` constraints.

The OreGenerator also includes a TODO idea to add a RotationMode that allows overlaying the ore texture onto a regular block, potentially creating more ore-in-stone types for free.

## Code Example
```zig
pub fn init(parameters: ZonElement) void {
	_ = parameters;
	ores = main.blocks.ores.items;
}
```

## Related Questions
- What is the priority level of the ore generator?
- How does the OreGenerator initialize its list of ores?
- What determines the placement of ore veins in a chunk?
- How many nearby chunks are considered for generating ore veins?
- What is the role of the `considerCoordinates` function in ore generation?
- How does the OreGenerator ensure that ore veins do not exceed their defined height range?

*Source: unknown | chunk_id: codebase_src_server_terrain_chunkgen_OreGenerator.zig_chunk_0*
