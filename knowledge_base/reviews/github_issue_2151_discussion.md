# [issues/issue_2151.md] - Issue #2151 discussion

**Type:** review
**Keywords:** Zig, C++, Java, Vulkan, OpenGL, RAII, smart pointers, OOP, SSBOs, rewrite
**Symbols:** Zig, C++, Java, Vulkan, OpenGL
**Concepts:** language choice, safety, modern programming languages, performance considerations

## Summary
The discussion revolves around the choice of Zig as the programming language for a project, highlighting its simplicity, safety, and modern features compared to other languages like C++ and Java.

## Explanation
Quantum chose Zig due to its simplicity and safety compared to other languages like C++. They noted that C++ is complex and messy, while Java imposes a slow OOP pattern. Additionally, they mentioned moving away from OpenGL because of limitations such as SSBOs being limited to 2 GiB and modern OpenGL not working on macOS. Quantum spent almost a year getting comfortable with Zig before the rewrite and had a clear plan for it. Vulkan was cited as one reason but Quantum noted that its advantages over OpenGL are minimal.

## Related Questions
- What are the main reasons Quantum chose Zig over other languages?
- How does Zig compare to C++ in terms of complexity and safety?
- Why did Quantum decide to move away from OpenGL?
- What is Vulkan's advantage over OpenGL mentioned by Quantum?
- Why wasn't Rust mentioned as an alternative language?
- How does Quantum feel about the preparation for rewriting in Zig?

*Source: unknown | chunk_id: github_issue_2151_discussion*
