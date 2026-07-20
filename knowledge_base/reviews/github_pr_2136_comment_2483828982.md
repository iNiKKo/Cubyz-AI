# [src/gui/windows/save_creation.zig] - PR #2136 review diff

**Type:** review
**Keywords:** world seed, random integer, time-based seed, seed generation code, architectural review, security concerns, predictable seeds
**Symbols:** getWorldSeed, testingModeCallback
**Concepts:** seed generation, randomness, security, predictability

## Summary
A new function `getWorldSeed` is introduced to generate a world seed using a random integer if the input string is empty. The reviewer suggests using existing code for seed generation instead, citing concerns about the current method's reliance on time, which limits the search space for reconstructing a seed.

## Explanation
A new function `getWorldSeed` is introduced to generate a world seed using a random integer if the input string is empty. The reviewer suggests using existing code for seed generation instead, citing concerns about the current method's reliance on time, which limits the search space for reconstructing a seed. The existing code is lacking because it depends directly on the time, making the search space to reconstruct a seed from a generated world much smaller. This could pose security risks or make world generation less random. The reviewer emphasizes the importance of using a more secure and unpredictable method for seed generation.

The new function `getWorldSeed` checks if the input string is empty. If it is, it generates a random integer using `std.crypto.random.int(u64)`. The reviewer suggests instead using the existing code that creates the seed for the world, as this existing code does not rely on time directly, making it more secure and unpredictable.

## Related Questions
- What is the purpose of the `getWorldSeed` function?
- Why does the reviewer suggest using existing seed generation code?
- How does the current method of seed generation rely on time?
- What are the potential security implications of predictable seeds?
- How can the seed generation be made more secure and unpredictable?
- What is the impact of using a random integer for seed generation when no input is provided?

*Source: unknown | chunk_id: github_pr_2136_comment_2483828982*
