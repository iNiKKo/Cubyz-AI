# [issues/issue_2538.md] - Issue #2538 discussion

**Type:** review
**Keywords:** TLS, certificate, man-in-the-middle, Let's Encrypt, custom CA, user experience, digest, bans, free software
**Concepts:** TLS, Certificate Authority, Man-in-the-Middle Attack, User Experience

## Summary
Discussion about requiring TLS certificates for server connections when joining through a domain name, with considerations for security, user experience, and certificate availability.

## Explanation
The discussion revolves around enhancing server security by requiring TLS certificates for connections made via domain names. The main concern is preventing man-in-the-middle attacks during the initial connection to a server. The maintainers suggest relying on existing Certificate Authorities (CAs) like Let's Encrypt, while also considering the possibility of creating a custom CA with controlled access and potential revenue generation. However, there are concerns about user experience, such as adding complexity with certificate digests for servers without proper certificates. The discussion also touches on the need to support custom authorities to bypass potential bans in existing infrastructure, aligning with principles of free software. Additionally, it is mentioned that obtaining a TLS certificate from Let's Encrypt is trivial and easy. There are also considerations about the interaction between SRV records and domain certificates, as well as the potential for government regulations affecting the decision to require TLS certificates for Cubyz servers.

## Related Questions
- What are the potential advantages and disadvantages of using a custom certificate authority for Cubyz servers?
- How does Let's Encrypt facilitate obtaining certificates for server owners?
- What security risks are associated with connecting to servers via direct IP addresses without certificate checks?
- How can certificate digests be used to verify server identity in cases where domain certificates are not available?
- What are the potential user experience impacts of requiring certificate digests for connections to servers without proper certificates?
- How might government regulations affect the decision to require TLS certificates for Cubyz servers?
- What are the implications of supporting custom authorities for bypassing bans in existing certificate infrastructure?
- How can the interface be designed to make setting up a server with TLS certificates as user-friendly as possible?
- What are the potential revenue sources if Cubyz implements its own certificate authority?
- How do SRV records interact with domain certificates, and what implications does this have for server setup?

*Source: unknown | chunk_id: github_issue_2538_discussion*
