# [issues/issue_1074.md] - Issue #1074 discussion

**Type:** review
**Keywords:** mass, stability, sharpness, texture roughness, elasticity, stiffness, material properties, real-world simulation, property measurement, property relevance
**Symbols:** .density, .mass, .stability, .sharpness, .grip, .hardness, .textureRoughness, .elasticity, .stiffness
**Concepts:** material properties, real-world simulation, property measurement, property relevance

## Summary
Discussion on adding and changing parameters for materials in Cubyz, focusing on properties like mass, stability, sharpness, texture roughness, elasticity, and grip.

## Explanation
The discussion revolves around the addition of new material properties such as mass, stability, sharpness, texture roughness, elasticity, and grip, while also considering the removal or renaming of existing ones. The maintainers debate the relevance and clarity of these properties, particularly around concepts like sharpness, elasticity, and stiffness. There is a focus on distinguishing between elasticity and stiffness, with elasticity being defined more broadly as the ability to return to its original shape after deformation. The maintainers also discuss the measurement and usefulness of these properties in simulating real-world materials accurately.

Specifically, the maintainers propose the following parameters:
- .density
- .mass
- .stability
- .grip
- .hardness
- .elasticity
- .stiffness

The maintainers also discuss the measurement of these properties. For elasticity and stiffness, a scale from 0 to 10 is proposed, where:
- 0 = elastic
- 10 = stiff

The maintainers explain that high stability with low stiffness results in an elastic material, while low stability with low stiffness results in something like dough. High stability with high stiffness results in a very stiff material, and low stability with high stiffness results in a brittle material.

Additionally, the maintainers clarify that elasticity is defined as the ability of a body to resist a distorting influence and return to its original size and shape when that influence or force is removed, which aligns more closely with their understanding of it compared to just being about stretching or bending.

## Related Questions
- What is the difference between elasticity and stiffness in material properties?
- Why was sharpness considered for inclusion as a material property?
- How does the maintainers' understanding of elasticity align with its definition from Wikipedia?
- What are the implications of removing stiffness as a material property?
- How might the new set of parameters (.density, .elasticity, .stiffness, .grip, .hardness) affect the simulation of materials in Cubyz?
- What is the proposed measurement scale for elasticity and stiffness?

*Source: unknown | chunk_id: github_issue_1074_discussion*
