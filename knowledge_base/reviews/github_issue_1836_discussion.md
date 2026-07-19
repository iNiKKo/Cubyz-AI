# [issues/issue_1836.md] - Issue #1836 discussion

**Type:** review
**Keywords:** environment variable, config file, custom storage, average player, version download
**Concepts:** user customization, file storage, configuration management

## Summary
The discussion revolves around allowing users to specify custom storage locations for Cubyz saves and other global data. The maintainers initially considered using an environment variable but ultimately decided to use a configuration file placed next to the executable.

## Explanation
The maintainers explored various solutions for allowing users to specify custom storage locations for Cubyz saves and other global data. Initially, they considered using an environment variable as it seemed like the best solution. However, they found that setting up an environment variable could be complex for average players. Additionally, they discussed the possibility of using a third-party launcher to manage storage settings, although this was not ultimately chosen. Ultimately, they decided to place a configuration file next to the executable. This approach avoids the complexity of setting environment variables and does not require reconfiguration with each new version download.

## Related Questions
- What are the potential drawbacks of using an environment variable for specifying storage locations?
- Why did the maintainers decide against using a configuration file in favor of an environment variable initially?
- How does placing a config file next to the executable address the issue of reconfiguration with each new version?
- What are the advantages and disadvantages of using a third-party launcher to manage storage settings?
- How might setting up an environment variable be more complex for average players compared to using a configuration file?
- Can you explain the reasoning behind choosing a configuration file over other potential solutions?

*Source: unknown | chunk_id: github_issue_1836_discussion*
