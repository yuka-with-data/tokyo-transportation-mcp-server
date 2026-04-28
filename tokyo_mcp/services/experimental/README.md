## Experimental Adapters

This directory contains **experimental implementations** used during the early prototyping phase of the project.

### Purpose

These modules were created to quickly validate MCP tool behavior and end-to-end system flow by retrieving transit data from third-party web sources.

### Important Notes

* These components rely on **web scraping** and are **not intended for production use**
* They may be unstable, subject to breakage, or restricted by external service terms
* They are being **phased out** as the project migrates to structured and reliable data sources (e.g., ODPT, GTFS)

### Current Role

The code in this directory is kept for:

- reference during the migration process
- comparison with new data source implementations
- experimentation and prototyping
- testing and experimenting with the MCP architecture as a whol

It should be considered **temporary and replaceable**, not part of the long-term system architecture.
