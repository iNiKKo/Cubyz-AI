# [issues/issue_1661.md] - Issue #1661 discussion

**Type:** review
**Keywords:** durability per swing, off-by-ε errors, fractional damage, resource gathering, adventure style, game mechanics
**Concepts:** usability, realism, immersion, resource management

## Summary
Discussion on whether to keep durability per swing in Cubyz, with arguments for and against the mechanic.

## Explanation
The issue revolves around the usability and realism of the durability system in Cubyz, specifically whether to keep durability per swing or switch to a block-based durability system. Users argue that durability per swing is more intuitive and aligns better with game mechanics. Maintainers counter that it disrupts the adventure-style gameplay by focusing too much on resource management, potentially breaking immersion. They discuss the impact of off-by-ε errors on damage calculations, which can effectively halve tool durability in the worst case scenario. The maintainer suggests alternative approaches like fractional damage or adjusting durability values to mitigate these issues. For example, a wooden pickaxe has 474 durability and an iron pickaxe has 1560 durability under the current system. The maintainer concludes that durability per swing does not make sense as hitting harder should result in more tool wear per swing. They propose tying durability to specific blocks (e.g., diamond ore always taking 20 durability) to enhance gameplay realism.

## Related Questions
- What are the potential impacts of removing durability per swing on gameplay immersion?
- How could fractional damage calculations improve the accuracy of tool wear in Cubyz?
- What alternative methods can be used to address off-by-ε errors in damage calculations?
- How does adjusting durability values affect the balance between surface exploration and resource gathering?
- What are the benefits and drawbacks of allowing multiple players or tools to contribute to a block's destruction?
- How could durability being tied to specific blocks (e.g., diamond ore always taking 20 durability) enhance gameplay realism?

*Source: unknown | chunk_id: github_issue_1661_discussion*
