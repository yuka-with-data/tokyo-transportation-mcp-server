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