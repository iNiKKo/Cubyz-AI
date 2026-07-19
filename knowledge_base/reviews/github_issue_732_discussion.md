# [issues/issue_732.md] - Issue #732 discussion

**Type:** review
**Keywords:** music system, keyword-based, mood levels, dynamic selection, biome tags, addon music, base mood, height-based anxiety
**Symbols:** Moody, biome weights, keywords, tags
**Concepts:** dynamic music selection, keyword system, mood levels, context-awareness

## Summary
The discussion revolves around enhancing the game's music system by introducing a more dynamic and context-aware approach using keywords and mood levels.

## Explanation
The discussion revolves around enhancing the game's music system by introducing a more dynamic and context-aware approach using keywords and mood levels. The initial proposal suggests replacing simple playlists with a keyword-based system where each song is associated with specific keywords, allowing for flexible and nuanced music selection based on various conditions such as time of day (day/night), player danger level, or biome type. Each music track can have a list of keywords like 'day', 'night', 'danger', 'building', etc., which are used to determine the likelihood of playing that song in different contexts. Biomes also get a list of keyword + weight pairs associated with them, and music is selected based on these weights and thresholds specific to each biome.

The maintainer introduces the concept of a 'Moody' sound selector that chooses songs based on mood levels and tags. The 'Moody' system uses various parameters such as player danger level, time of day, and biome type to select appropriate music tracks. For example, during the night, all songs with the 'day' keyword but not the 'night' keyword are automatically disabled unless explicitly allowed by biome settings.

Additional considerations include allowing addons to define their own music with specific tags (e.g., .any tag for base game compatibility), enabling biomes to have base mood levels, and addressing potential oddities in the height-based anxiety scale through biome tags and mood levels.

The system also allows for conditions such as player velocity or danger level to influence whether a song plays. For example, songs with the 'day' keyword are disabled at night unless explicitly allowed by biome settings.

The chance system for selecting songs in playlists involves setting the chance for a song to play to zero if it has already been played and resetting after each consecutive song or increasing based on the number of songs in the playlist. Additionally, there is an option to choose what song plays after another, called a 'sub-song', which can be used as a nuanced way to bridge different musical styles.

## Related Questions
- How does the chance system work for selecting songs in playlists?
- What specific keywords can be used to tag music tracks and biomes?
- Can you explain how base mood levels for biomes influence song selection?
- How do addons contribute to the music system with their own tags?
- What conditions beyond time of day can affect whether a song plays?

*Source: unknown | chunk_id: github_issue_732_discussion*
