---
date: '2025-06-12T13:22:00-07:00'
duration_seconds: 0.8
keywords:
- Strong Wind Events
- Temporal Synchronization
- Methods Section
- Wind Speed Variance
- Kingston Threshold
- Data Collection Methodology
llm_service: openrouter
original_filename: DJI_36_20250612_130850.WAV
processed_date: '2025-06-12T14:49:08.037256'
word_count: 454
---
# Methods: Strong Wind Events & Temporal Synchronization

This document outlines the approach for addressing Issue #8: "Define strong wind events and temporal synchronization methodology."

## 1. Defining a "Strong Wind Event"

The current methods section has a critical gap: it monitors strong wind events without defining what constitutes "strong wind."

- **Proposed Definition**: The study will use the established **Kingston Threshold** of **5 mph (2.2 m/s)** as the *a priori* definition of a strong wind event. This is the canonical threshold considered by the broader Monarch research community prior to this study.
- **Additional Criteria**: The definition should also include duration requirements and other relevant criteria.
- **Post-Study Note**: While 5 mph is the working definition for the methods, preliminary findings suggest the actual biologically relevant threshold is likely higher. This will be discussed in later sections, but the methods should reflect the *a priori* hypothesis.

## 2. Temporal Synchronization Methodology

The methodology for temporally linking wind data and butterfly responses needs to be clearly explained.

### Data Collection Frequencies
- **Photographs**: Taken every 10 minutes to measure monarch abundance. (Note: This was later switched to 30-minute intervals to better capture meaningful changes in abundance).
- **Wind Measurements**: Average wind speed and gust were recorded every 1 minute.

### Rationale for Mismatched Frequencies
Collecting wind data at a higher frequency (1-minute) than photographic data (10-minute) was a deliberate methodological choice.

1.  **Enables a Novel Metric**: The high-frequency data allows for the calculation of **wind speed variance** (i.e., standard deviation or "gustiness") within each photo sampling period. This is a new, potentially biologically relevant metric that could not be captured with 10-minute average readings alone.
2.  **Data Integrity**: Recording at 1-minute intervals preserves the maximum amount of data. It can always be down-sampled to a 10-minute average, which is equivalent to a single 10-minute measurement. (Self-correction: May need a citation to validate this equivalence).
3.  **No Technical Trade-off**: Recording wind data at 1-minute intervals did not create a significant battery life trade-off and was the highest frequency the sensors could support.

### Linking Data
During analysis, wind metrics (average speed, gust, and variance) will be calculated for the corresponding 10-minute or 30-minute photo intervals to directly link environmental conditions to changes in monarch abundance.

## 3. Open Questions & Action Items

- **[To-Do] Define Temporal Lag**: The methodology for analyzing temporal lag between wind events and butterfly response is not yet developed and needs to be addressed.
- **[Action Item] Create GitHub Issue**: Create a GitHub issue to ensure **wind speed variance is included in the statistical analysis**. This is critical to justify its inclusion as a key part of the data collection rationale. Even if not statistically significant, it closes the methodological loop.