# [src/vec.zig] - PR #3265 review comment

**Type:** review
**Keywords:** coordinate system, vector, conversion, rotation, accuracy, architectural review, enum, function, suggestion, center of rotation
**Symbols:** CoordinateSystem, convertCoordinateSystemVec0to1, Vec3f
**Concepts:** coordinate system conversion, vector transformation, architectural improvement

## Summary
Added a function to convert vectors between different coordinate systems and received a suggestion to include an explicit center of rotation for improved accuracy.

## Explanation
The change introduces a new enum `CoordinateSystem` defining various coordinate system types. A function `convertCoordinateSystemVec0to1` is added to convert a vector from one coordinate system to another based on the specified system type. The reviewer suggests modifying this function to include an explicit center of rotation, which would allow for more precise transformations by accounting for the position relative to the origin or any other reference point. This suggestion aims to enhance the functionality and accuracy of the coordinate conversion process.

## Related Questions
- What is the purpose of the `CoordinateSystem` enum in the code?
- How does the `convertCoordinateSystemVec0to1` function work?
- Why was it suggested to include an explicit center of rotation in the coordinate conversion function?
- What are the potential benefits of adding a center of rotation parameter?
- Can you explain the different cases in the switch statement for converting coordinate systems?
- How might the inclusion of a center of rotation affect the performance of vector transformations?

*Source: unknown | chunk_id: github_pr_3265_comment_3446861557*
