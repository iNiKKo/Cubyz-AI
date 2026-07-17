# [hard/codebase_src_server_terrain_biomes.zig] - Chunk 4

**Type:** world_generation
**Keywords:** TreeNode, init, getBiome, alias table, noise sampling, recursion, global state management
**Symbols:** TreeNode, TreeNode.leaf, TreeNode.leaf.totalChance, TreeNode.leaf.aliasTable, TreeNode.branch, TreeNode.branch.lowerBorder, TreeNode.branch.upperBorder, TreeNode.branch.children, TreeNode.init, TreeNode.getBiome, finishedLoading, biomes, caveBiomes, biomesById, biomesByIndex, byTypeBiomes, SubBiomeData, SubBiomeData.biome, SubBiomeData.parentEdgeDistance, UnfinishedSubBiomeData, UnfinishedSubBiomeData.biomeId, UnfinishedSubBiomeData.chance, UnfinishedSubBiomeData.parentEdgeDistance, UnfinishedSubBiomeData.getItem, unfinishedSubBiomes, UnfinishedTransitionBiomeData, UnfinishedTransitionBiomeData.biomeId, UnfinishedTransitionBiomeData.chance, UnfinishedTransitionBiomeData.propertyMask, UnfinishedTransitionBiomeData.width, TransitionBiome, TransitionBiome.biome, TransitionBiome.chance, TransitionBiome.propertyMask, TransitionBiome.width, unfinishedTransitionBiomes, reset
**Concepts:** biome generation, alias table, noise-based sampling, recursive tree construction

## Summary
The chunk defines a `TreeNode` union for biome generation, including initialization and sampling methods. It also manages global lists and maps of biomes.

## Explanation
The `TreeNode` union represents either a leaf node containing an alias table for biomes or a branch node with children nodes. The `init` method constructs the tree recursively based on biome properties and chance values. The `getBiome` method samples a biome using noise-based decision-making. Global variables manage lists and maps of biomes, including unfinished sub-biomes and transition biomes. The `reset` function clears these global states.

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
- How does the `init` method construct the tree?
- What does the `getBiome` method do?
- What are the global variables used for managing biomes?
- How does the `reset` function clear the global states?
- What is the role of the alias table in biome sampling?

*Source: unknown | chunk_id: codebase_src_server_terrain_biomes.zig_chunk_4*
