# Data Source Limitations and Design Decisions
## Overview
This MCP tool aims to provide intelligent transportation guidance for the Tokyo metropolitan area. 
However, accessing reliable and open transit data in Japan presents several practical challenges.
This document outlines those challenges and explains the design decisions made as a result.

## ODPT API Access Constraints
The ODPT provides an official API for public transportation data in Tokyo and other parts of Japan. While it is labeled as an `open data` platform, access to the API requires:
- Manual account approval
- Submission of personal information (e.g., name, affiliation, contact details)
- Issuance of an access token after review

As a result, the API is not immediately accessible to independent developers or anonymous users.
This introduces friction in development workflows and limits reproducibility for open-source projects.

## Fragmented Data Ownership
Public transportation data in Tokyo is not managed by a single centralized authority.
Instead, it is distributed across a large number of independent railway and transit operators, each maintaining its own data infrastructure, formats, and access policies.

Major operators such as:
- East Japan Railway Company
- Tokyo Metro Co., Ltd.
- Toei Subway
- Odakyu Electric Railway
- Keio Corporation
- Tokyu Corporation
- Seibu Railway
- Tobu Railway
- etc.

These operators represent a mix of:
- Privately owned railway companies (which makes up the majority of urban rail in Japan)
- Public or municipal systems (such as Toei)

In total, the Tokyo metropolitan area includes **20+ railway operators** when accounting for major and minor lines. Each operators semi-independently, even though their services are highly interconnected from a passenger perspective.

This creates a uniquely complex transportation ecosystem. For example,**Shinjuku Station**-- the busiest railway station in the world-- serves multiple operators simultaneously, yet no single entity owns or fully centralizes all associated transit data.

As a result:
- Data formats are not standardized across operators
- Access methods vary significantly
- Comprehensive datasets are difficult to obtain without aggregation
- Most of operators do not provide developer-accessible APIs or open data feeds, limiting programmatic access to their systems

This fragmentation is a core reason why building a unified transit data system for Tokyo requires combining multiple partial sources rather than relying on a single provider.