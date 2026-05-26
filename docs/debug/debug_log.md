# Debug Log — Fare Aggregation Issue (Test Case #5)

## Issue Summary
Fare calculation is inaccurate for multi-segment routes that include walking transfers between train legs.

## Observed Behavior
- Route output is structurally correct
- Total fare is undercounted when walking segments exist between rail segments
- Fare aggregation fails to include all applicable train segments

## Suspected Root Cause
- Fare is being inferred from route segments (`fareSection`)
- Walking segments break the mapping between segments and fare-bearing blocks
- DOM structure does not reliably represent logical fare boundaries

## Key Insight
- Yahoo Transit route summary already provides a precomputed total fare
- Segment-based aggregation introduces inconsistency when mixed transport types exist

## Current Hypothesis
Primary issue is reliance on segment-level parsing instead of using summary-level fare as the source of truth.

## Important Note (Temporary Implementation)
This parser is a **temporary data retrieval layer** used for experimentation and validation purposes only.

It is **not intended as a permanent or production-grade transit data solution**.
Please see the `doc/` for more info.

## Next Step
- Refactor parser to prioritize route summary fare extraction
- Use segment parsing only for route explanation, not fare computation