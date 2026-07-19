# [hard/codebase_src_items.zig] - Chunk 3

**Type:** implementation
**Keywords:** height map, material roughness, lighting intensity, image rendering, grid processing
**Symbols:** TextureGenerator, TextureGenerator.generateHeightMap, TextureGenerator.generate
**Concepts:** texture generation, material handling, lighting calculations

## Summary
The TextureGenerator struct generates textures for ProceduralItems based on material information and crafting grid data.

## Explanation
The TextureGenerator struct generates textures for ProceduralItems based on material information and crafting grid data. The generateHeightMap function creates a height map from the itemGrid by considering neighbor items and their materials to determine texture roughness. Specifically, it initializes a 17x17 height map array and iterates through each pixel, calculating its value based on neighboring items' material properties and random factors. If there are different neighbors at a junction, the height is adjusted inward to make embedded parts stick out more. Further neighbors with lower priority also influence the height calculation.

The generate function initializes the materialGrid based on the crafting grid and seed by setting each pixel's material according to its source or overlay value in the proceduralItem's type. It then uses the height map generated from this materialGrid to calculate lighting for each pixel, setting colors in the proceduralItem's image accordingly. The lighting calculation involves determining the nearest free space using the height map values, adjusting light based on a formula that typically ranges from -7 to 5 and normalizing it to near-normalized values between 0 and 1. This normalized value is then used to index into the material's color palette for setting pixel colors.

The height map calculation considers the texture roughness of materials, which affects the randomness in height generation. The lighting intensity is calculated based on the height differences and adjusted to ensure that all parts are illuminated appropriately.

## Code Example
```zig
fn generateHeightMap(itemGrid: *[16][16]?BaseItemIndex, seed: *u64) [17][17]f32 {
		var heightMap: [17][17]f32 = undefined;
		var x: u8 = 0;
		while (x < 17) : (x += 1) {
			var y: u8 = 0;
			while (y < 17) : (y += 1) {
				heightMap[x][y] = 0;
				// The heighmap basically consists of the amount of neighbors this pixel has.
				// Also check if there are different neighbors.
				const oneItem = itemGrid[if (x == 0) x else x - 1][if (y == 0) y else y - 1];
				var hasDifferentItems: bool = false;
				var dx: i32 = -1;
				while (dx <= 0) : (dx += 1) {
					if (x + dx < 0 or x + dx >= 16) continue;
					var dy: i32 = -1;
					while (dy <= 0) : (dy += 1) {
						if (y + dy < 0 or y + dy >= 16) continue;
						const otherItem = itemGrid[@intCast(x + dx)][@intCast(y + dy)];
						heightMap[x][y] = if (otherItem) |item| (if (item.material()) |material| 1 + (4*random.nextFloat(seed) - 2)*material.textureRoughness else 0) else 0;
						if (otherItem != oneItem) {
							hasDifferentItems = true;
						}
					}
				}

				// If there is multiple items at this junction, make it go inward to make embedded parts stick out more:
				if (hasDifferentItems) {
					heightMap[x][y] -= 1;
				}

				// Take into account further neighbors with lower priority:
				dx = -2;
				while (dx <= 1) : (dx += 1) {
					if (x + dx < 0 or x + dx >= 16) continue;
					var dy: i32 = -2;
					while (dy <= 1) : (dy += 1) {
						if (y + dy < 0 or y + dy >= 16) continue;
						const otherItem = itemGrid[@intCast(x + dx)][@intCast(y + dy)];
						const dVec = Vec2f{@as(f32, @floatFromInt(dx)) + 0.5, @as(f32, @floatFromInt(dy)) + 0.5};
						heightMap[x][y] += if (otherItem != null) 1.0/vec.dot(dVec, dVec) else 0;
					}
				}
			}
		}
		return heightMap;
	}
```

## Related Questions
- What is the purpose of the TextureGenerator struct?
- How does the generateHeightMap function work?
- What data does the generate function use to create textures?
- How are lighting calculations performed in the generate function?
- What is the role of the height map in texture generation?
- How is the materialGrid initialized in the generate function?

*Source: unknown | chunk_id: codebase_src_items.zig_chunk_3*
