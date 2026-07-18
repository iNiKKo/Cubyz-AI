# [medium/codebase_src_vec.zig] - Chunk 3

**Type:** implementation
**Keywords:** complex numbers, vector operations, bounding boxes, mathematical functions, merge operation
**Symbols:** Complex, Complex.val, Complex.valSquare, Complex.conjugate, Complex.negate, Complex.add, Complex.addScalar, Complex.sub, Complex.subScalar, Complex.mul, Complex.mulScalar, Complex.div, Complex.divScalar, Complex.fromSqrt, Complex.exp, Boxi, Boxi.min, Boxi.max, Boxi.merge
**Concepts:** complex number operations, 3D bounding box

## Summary
Defines complex number operations and a box structure with merging functionality.

## Explanation
The chunk defines a `Complex` struct for handling complex numbers, including methods such as squaring the value (`valSquare`), computing the conjugate (`conjugate`), negation (`negate`), addition of two complex numbers (`add`), subtraction of two complex numbers (`sub`), multiplication of two complex numbers (`mul`), division of two complex numbers (`div`), creating from square root (`fromSqrt`), and exponentiation (`exp`). Additionally, it includes methods for adding a scalar to a complex number (`addScalar`), subtracting a scalar from a complex number (`subScalar`), multiplying a complex number by a scalar (`mulScalar`), and dividing a complex number by a scalar (`divScalar`). The `addScalar`, `subScalar`, `mulScalar`, and `divScalar` methods operate on the real part of the complex number with a scalar value. For example, `addScalar(a: Complex, b: f64)` adds the scalar `b` to the real part of `a.val`. Similarly, `exp(a: Complex)` computes the exponential of a complex number using Euler's formula and returns another complex number. The struct also defines a `Boxi` struct representing an axis-aligned bounding box in 3D space with integer coordinates, including a method to merge two boxes (`merge`).

## Code Example
```zig
pub fn negate(a: Complex) Complex {
	return .{.val = -a.val};
}
```

## Related Questions
- How do you compute the square of a complex number?
- What is the method to merge two Boxi instances?
- How does the `Complex` struct handle division by another complex number?
- Can you explain how the `exp` function works for complex numbers?
- What is the purpose of the `conjugate` method in the Complex struct?
- How do you add a scalar to a complex number?

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_3*
