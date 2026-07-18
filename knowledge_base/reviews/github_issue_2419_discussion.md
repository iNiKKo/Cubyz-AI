# [issues/issue_2419.md] - Issue #2419 discussion

**Type:** review
**Keywords:** joints, bones, skeleton, animation, inverse kinematics, model format, GLTF, .zon, JSON, OBJ
**Symbols:** .zon, JSON, OBJ, GLTF
**Concepts:** Animation, Inverse Kinematics, Model Format, Skeleton System

## Summary
Discussion on implementing a skeleton system for entity models in Cubyz, considering formats like .zon or JSON, and future plans to use GLTF.

## Explanation
The discussion revolves around adding a skeleton system to support inverse kinematics and other animations in Cubyz. The proposal includes defining joints and bones either through a separate file format (.zon) or by extending existing formats like OBJ. A specific example of the .zon format is provided:

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

There's also mention of potential future adoption of the GLTF format, which supports binary representation and animations, suggesting that this issue might be addressed when transitioning to GLTF. The discussion highlights the benefits of using GLTF over existing formats due to its support for animations and binary representation.

## Related Questions
- What are the proposed formats for defining skeletons in Cubyz?
- How does the discussion suggest handling animations in the future?
- Why is there a mention of switching to GLTF format?
- What are the potential benefits of using GLTF over existing formats?
- How might the implementation of a skeleton system impact model compatibility?
- Are there any specific concerns raised about the proposed changes?

*Source: unknown | chunk_id: github_issue_2419_discussion*
