# [issues/issue_2419.md] - Issue #2419 discussion

**Type:** review
**Keywords:** joints, bones, skeleton, animation, inverse kinematics, model format, GLTF, .zon, JSON, OBJ
**Symbols:** .zon, JSON, OBJ, GLTF
**Concepts:** Animation, Inverse Kinematics, Model Format, Skeleton System

## Summary
Discussion on implementing a skeleton system for entity models in Cubyz, considering formats like .zon or JSON, and future plans to use GLTF.

## Explanation
Discussion on implementing a skeleton system for entity models in Cubyz, considering formats like .zon or JSON, and future plans to use GLTF. The proposal includes defining joints and bones either through a separate file format (.zon) or by extending existing formats like OBJ. A specific example of the .zon format is provided, which includes detailed information about how joints and bones are defined:

```
{
	.joints = {
		.name = "root",
		.position = {0.0, 1.0, 0.0},
	},
	.bones = {
		.from = "root",
		.to = "head",
		.controls = {
			.eyestalks = .all,
			.head = .all,
		},
	},
}
```

The structure of the .zon file format includes a `.joints` array where each joint has a `.name` and `.position`. The `.bones` array defines bones with `.from`, `.to`, and `.controls` properties, where `.controls` maps bone names to face groups like `.all`.

The discussion also mentions potential future adoption of the GLTF format, which supports binary representation and animations, suggesting that this issue might be addressed when transitioning to GLTF. The benefits of using GLTF over existing formats include its support for animations and binary representation.

Users have proposed various solutions, such as supporting .json models or using Blockbench for better model editing. There is also a mention of the need to define how much joints can move and which are fixed in future implementations.

## Related Questions
- What is the structure of the .zon file format for defining skeletons?
- How are joints and bones defined in the .zon file format?
- What specific benefits does the GLTF format offer over existing formats like OBJ?

*Source: unknown | chunk_id: github_issue_2419_discussion*
