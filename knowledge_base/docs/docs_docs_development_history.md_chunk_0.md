# [easy/docs_docs_development_history.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz, Java, C++, Vulkan, Rewrite, Release, Development, History
**Symbols:** Cubyz, Zenith391, QuantumDeveloper
**Concepts:** Early History, Development Process, Rewrite Attempts, Release Information

## Summary
Cubyz was created by zenith391 and ZaUserA in August 2018, with the name 'Cubz'. It was later renamed to 'Cubyz' on March 17, 2019. The project was initially developed using Java, but a rewrite attempt was made in C++ and Vulkan, which was abandoned due to issues with the Java Garbage collector. Cubyz version 0.0.0 was released on October 5th, 2025.

## Explanation
Cubyz was created by zenith391 and ZaUserA in August 2018 under the name 'Cubz'. The project was later renamed to 'Cubyz' on March 17, 2019. Cubyz version 0.0.0 was released on October 5th, 2025.

Full why-Zig causal chain, in order: Cubyz was initially written in Java. The re-code away from
Java happened mainly because of the Java garbage collector -- when the upper memory limit was
hit, Java would try to free up memory, which would freeze the game for some time (QuantumDeveloper
has a video explaining this lag in detail). The first rewrite attempt was in C++ and Vulkan, but
that attempt was abandoned. After the C++/Vulkan attempt was abandoned, zenith391 showed
QuantumDeveloper a new language: Zig. QuantumDeveloper considered C++20 and Rust as alternatives,
but settled on Zig -- the feature that really impressed him about Zig specifically was its
cross-compilation support out-of-the-box, since he could build for Windows and test it with Wine
without worrying about Windows-related OS-specific issues. So: Java (original) -> C++/Vulkan
(abandoned rewrite attempt) -> Zig (final rewrite, chosen over C++20/Rust alternatives for its
cross-compilation support), and Zig is what Cubyz is written in today.

## Related Questions
- What was the initial name of Cubyz?
- When was Cubyz first renamed to 'Cubyz'?
- Who were the creators of Cubyz?
- What is the current status of Cubyz development?
- What are some of the features added by QuantumDeveloper during early development?
- Why was the rewrite attempt in C++ and Vulkan abandoned?
- When was Cubyz version 0.0.0 released?
- Who is QuantumDeveloper, and what other projects does he maintain besides Cubyz?
- What is the purpose of the Workbench in Cubyz?
- How many screenshots are included in the 'Early Development Builds' section?
- What is the name of the language that impressed QuantumDeveloper during the rewrite attempt?
- What is the feature that really impressed QuantumDeveloper about Zig?

*Source: unknown | chunk_id: docs_docs_development_history.md_chunk_0*
