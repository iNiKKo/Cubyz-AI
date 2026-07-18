# [issues/issue_533.md] - Issue #533 discussion

**Type:** review
**Keywords:** lag, multi-threading, stuttering, performance penalties, GLFW, timestamps, input extrapolation, render thread
**Symbols:** Cubyz, physics, networking, graphics rendering, glfwPollEvents
**Concepts:** thread safety, performance optimization, input handling, frame rate

## Summary
Discussion on improving gameplay responsiveness during lag by considering multi-threading for physics and networking, with concerns about potential stuttering and performance penalties.

## Explanation
The issue revolves around the sequential execution of Cubyz's physics, networking, and graphics rendering, which leads to lag affecting all aspects. The maintainer suggests that only using an extra thread is feasible due to limitations in the second option requiring precise timestamps for input events. The user highlights specific scenarios where low FPS causes gameplay issues, such as skipping over gaps or failing to register jump inputs. There's a suggestion to extrapolate current inputs over the last frame duration with more granular timesteps, but this would require changes in how GLFW event callbacks are processed.

## Related Questions
- What are the potential performance impacts of running physics and networking in separate threads?
- How can we ensure that input events are accurately timestamped for multi-threading?
- What is the current implementation of GLFW event processing in Cubyz?
- Can extrapolating inputs over frame durations improve responsiveness without introducing new issues?
- How does the render thread interact with other game systems during lag spikes?
- Are there any existing solutions or libraries that can help manage multi-threading for game development?

*Source: unknown | chunk_id: github_issue_533_discussion*
