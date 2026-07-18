# [hard/codebase_src_physics.zig] - Chunk 5

**Type:** implementation
**Keywords:** spring model, friction coefficients, collision detection, velocity adjustment, player eye position
**Symbols:** calculateEyeMovement, calculateWallCollision
**Concepts:** eye movement physics, wall collision handling

## Summary
This chunk implements physics calculations for eye movement and wall collisions in the game.

## Explanation
The `calculateEyeMovement` function computes the new position and velocity of the player's eye based on spring and friction models, checking for block collisions and adjusting the eye's position accordingly. The `calculateWallCollision` function handles collision detection and response when the player hits walls, adjusting their motion and velocity while considering factors like crouching and stepping height.

## Code Example
```zig
pub fn calculateEyeMovement(comptime side: main.sync.Side, deltaTime: f64, pos: Vec3d, vel: Vec3d, eye: *Player.EyeData, stepAmount: f64) void {
	if (main.game.getBlockWithSide(side, @floor(pos[0]), @floor(pos[1]), @floor(pos[2])) != null) {
		var directionalFrictionCoefficients: Vec3f = @splat(0);
		var acc: Vec3d = @splat(0);
		// Apply springs to the eye position:
		var springConstants = Vec3d{0, 0, 0};
		{
			const forceMultipliers = Vec3d{
				400,
				400,
				400,
			};
			const frictionMultipliers = Vec3d{
				30,
				30,
				30,
			};
			const strength = (-eye.pos)/(eye.box.max - eye.box.min);
			const force = strength*forceMultipliers;
			const friction = frictionMultipliers;
			springConstants += forceMultipliers/(eye.box.max - eye.box.min);
			directionalFrictionCoefficients += @floatCast(friction);
			acc += force;
		}

		// This our model for movement of the eye position on a single frame:
		// dv/dt = a - k*x - λ·v
		// dx/dt = v
		// Where a is the acceleration, k is the spring constant and λ is the friction coefficient
		inline for (0..3) |i| blk: {
			if (eye.step[i]) {
				const oldPos = eye.pos[i];
				const newPos = oldPos + eye.vel[i]*deltaTime;
				if (newPos*std.math.sign(eye.vel[i]) <= -0.1) {
					eye.pos[i] = newPos;
					break :blk;
				} else {
					eye.step[i] = false;
				}
			}
			if (i == 2 and eye.coyote > 0) {
				break :blk;
			}
			const frictionCoefficient = directionalFrictionCoefficients[i];
			const v_0 = eye.vel[i];
			const k = springConstants[i];
			const a = acc[i];
			// here we need to solve the full equation:
			// The solution of this differential equation is given by
			// x(t) = a/k + c_1 e^(1/2 t (-c_3 - λ)) + c_2 e^(1/2 t (c_3 - λ))
			// With c_3 = sqrt(λ^2 - 4 k) which can be imaginary
			// v(t) is just the derivative, given by
			// v(t) = 1/2 (-c_3 - λ) c_1 e^(1/2 t (-c_3 - λ)) + (1/2 (c_3 - λ)) c_2 e^(1/2 t (c_3 - λ))
			// Now for simplicity we set x(0) = 0 and v(0) = v₀
			// a/k + c_1 + c_2 = 0 → c_1 = -a/k - c_2
			// (-c_3 - λ) c_1 + (c_3 - λ) c_2 = 2v₀
			// → (-c_3 - λ) (-a/k - c_2) + (c_3 - λ) c_2 = 2v₀
			// → (-c_3 - λ) (-a/k) - (-c_3 - λ)c_2 + (c_3 - λ) c_2 = 2v₀
			// → ((c_3 - λ) - (-c_3 - λ))c_2 = 2v₀ - (c_3 + λ) (a/k)
			// → (c_3 - λ + c_3 + λ)c_2 = 2v₀ - (c_3 + λ) (a/k)
			// → 2 c_3 c_2 = 2v₀ - (c_3 + λ) (a/k)
			// → c_2 = (2v₀ - (c_3 + λ) (a/k))/(2 c_3)
			// → c_2 = v₀/c_3 - (1 + λ/c_3)/2 (a/k)
			// In total we get:
			// c_3 = sqrt(λ^2 - 4 k)
			// c_2 = (2v₀ - (c_3 + λ) (a/k))/(2 c_3)
			// c_1 = -a/k - c_2
			const c_3 = vec.Complex.fromSqrt(frictionCoefficient*frictionCoefficient - 4*k);
			const c_2 = (((c_3.addScalar(frictionCoefficient).mulScalar(-a/k)).addScalar(2*v_0)).div(c_3.mulScalar(2)));
			const c_1 = c_2.addScalar(a/k).negate();
			// v(t) = 1/2 (-c_3 - λ) c_1 e^(1/2 t (-c_3 - λ)) + (1/2 (c_3 - λ)) c_2 e^(1/2 t (c_3 - λ))
			// x(t) = a/k + c_1 e^(1/2 t (-c_3 - λ)) + c_2 e^(1/2 t (c_3 - λ))
			const firstTerm = c_1.mul((c_3.negate().subScalar(frictionCoefficient)).mulScalar(deltaTime/2).exp());
			const secondTerm = c_2.mul((c_3.subScalar(frictionCoefficient)).mulScalar(deltaTime/2).exp());
			eye.vel[i] = firstTerm.mul(c_3.negate().subScalar(frictionCoefficient).mulScalar(0.5)).add(secondTerm.mul((c_3.subScalar(frictionCoefficient)).mulScalar(0.5))).val[0];
			eye.pos[i] += firstTerm.add(secondTerm).addScalar(a/k).val[0];
		}
	}

	if (stepAmount > 0) {
		if (eye.coyote <= 0) {
			eye.vel[2] = @max(1.5*vec.length(vel), eye.vel[2], 4);
			eye.step[2] = true;
			if (vel[2] > 0) {
				eye.vel[2] = vel[2];
				eye.step[2] = false;
			}
		} else {
			eye.coyote = 0;
		}
		eye.pos[2] -= stepAmount;
	}
}
```

## Related Questions
- What is the purpose of the `calculateEyeMovement` function?
- How does the function handle block collisions?
- What parameters are required for the `calculateWallCollision` function?
- How is the eye's velocity adjusted in the `calculateEyeMovement` function?
- What conditions trigger a step adjustment in the `calculateWallCollision` function?
- How is collision detection implemented in the `calculateWallCollision` function?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_5*
