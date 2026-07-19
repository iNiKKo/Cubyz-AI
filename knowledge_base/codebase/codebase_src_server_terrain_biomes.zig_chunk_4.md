# [hard/codebase_src_server_terrain_biomes.zig] - Chunk 4

**Type:** world_generation
**Keywords:** union, recursive initialization, noise-based selection, global state management, reset function
**Symbols:** TreeNode, TreeNode.leaf, TreeNode.leaf.totalChance, TreeNode.leaf.aliasTable, TreeNode.branch, TreeNode.branch.lowerBorder, TreeNode.branch.upperBorder, TreeNode.branch.children, TreeNode.init, TreeNode.getBiome, finishedLoading, biomes, caveBiomes, biomesById, biomesByIndex, byTypeBiomes, SubBiomeData, SubBiomeData.biome, SubBiomeData.parentEdgeDistance, UnfinishedSubBiomeData, UnfinishedSubBiomeData.biomeId, UnfinishedSubBiomeData.chance, UnfinishedSubBiomeData.parentEdgeDistance, UnfinishedSubBiomeData.getItem, unfinishedSubBiomes, UnfinishedTransitionBiomeData, UnfinishedTransitionBiomeData.biomeId, UnfinishedTransitionBiomeData.chance, UnfinishedTransitionBiomeData.propertyMask, UnfinishedTransitionBiomeData.width, TransitionBiome, TransitionBiome.biome, TransitionBiome.chance, TransitionBiome.propertyMask, TransitionBiome.width, unfinishedTransitionBiomes, reset
**Concepts:** biome generation, decision tree, noise sampling

## Summary
The chunk defines a `TreeNode` union for biome generation, including initialization and retrieval methods. It also manages global lists and maps of biomes.

## Explanation
The `TreeNode` union represents either a leaf or branch node in a decision tree used to select biomes based on noise values. The `init` method constructs the tree recursively by partitioning biome slices into lower, middle, and upper categories based on properties. Specifically, it uses bit shifting and masking to categorize biomes into three groups: lower, middle, and upper. For example, if a biome's property is 1 after shifting and masking, it is added to the lower group; if it is 4, it is added to the upper group; otherwise, it is added to the middle group. The `getBiome` method traverses the tree to select a biome using noise sampling. Global variables manage lists and maps of biomes, including unfinished sub-biomes and transitions. The `reset` function initializes these global states by setting `finishedLoading` to false and initializing all global lists and maps to empty states.

The `TreeNode.branch` struct contains the following fields:
- `lowerBorder`: A floating-point value representing the lower border of the branch.
- `upperBorder`: A floating-point value representing the upper border of the branch.
- `children`: An array of three pointers to `TreeNode` structs representing the child nodes of the branch.

The `init` method calculates the total chance of all biomes in the current slice and initializes the `aliasTable` for leaf nodes. For branch nodes, it calculates the lower, middle, and upper chances based on the properties of the biomes and partitions the slice into three groups accordingly. The `getBiome` method uses noise sampling to determine which child node to traverse based on the value of the noise function.

## Code Example
```zig
pub fn reset() void {
	finishedLoading = false;
	biomes = .empty;
	caveBiomes = .empty;
	biomesById = .{};
	biomesByIndex = .empty;
	byTypeBiomes = undefined;
}
```

## Related Questions
- What is the purpose of the `TreeNode` union?
- How does the `init` method partition biome slices?
- What does the `getBiome` method do in the `TreeNode` struct?
- What global variables are used to manage biomes?
- How is the `reset` function structured?
- What types of data structures are used for sub-biomes and transitions?

*Source: unknown | chunk_id: codebase_src_server_terrain_biomes.zig_chunk_4*
