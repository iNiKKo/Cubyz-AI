# [issues/issue_55.md] - Issue #55 discussion

**Type:** review
**Keywords:** Android, PostmarketOS, Java, garbage collector, OpenGL, OpenGL ES, third-party development
**Concepts:** platform support, maintenance burden, language switch

## Summary
The maintainer has decided against adding Android support to Cubyz due to the game's current state and the complexity involved in maintaining multiple platforms.

## Explanation
The maintainer has decided against adding Android support to Cubyz due to several factors: the game is not yet fully developed with many features still missing, ongoing issues with Java (particularly garbage collector-induced lag spikes), which might lead to a language switch, and the complexity of maintaining compatibility across different platforms. The maintainer also highlights that supporting Android would require adapting new graphics features for both OpenGL and OpenGL ES, adding an extra maintenance burden. Despite these challenges, the open-source nature of Cubyz allows third-party developers to create an Android version independently. The maintainer mentions that Java is causing lag spikes due to garbage collector issues and that a language switch might be necessary in the future. They also express doubts about PostmarketOS running Cubyz without actually trying it. The maintainer has decided against supporting Android primarily because of the early development stage of Cubyz and the additional maintenance burden.

## Related Questions
- What are the current issues with Java in Cubyz?
- How does the maintainer plan to handle platform-specific graphics features?
- Why did the maintainer decide against supporting Android?
- Can third-party developers create an Android version of Cubyz?
- What is the current state of Cubyz development?
- How might a language switch affect existing platforms?
- What are the potential maintenance challenges of supporting multiple platforms?
- Is there any plan to revisit Android support in the future?
- Does PostmarketOS run Cubyz without trying it?
- How does PostmarketOS relate to running Cubyz on mobile devices?

*Source: unknown | chunk_id: github_issue_55_discussion*
