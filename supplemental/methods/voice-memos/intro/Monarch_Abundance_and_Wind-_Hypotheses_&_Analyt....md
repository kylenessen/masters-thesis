---
date: '2025-06-20T13:06:28'
duration_seconds: 1.9
keywords:
- Monarch Butterflies
- Wind Speed
- Abundance
- Hypothesis Testing
- Statistical Modeling
- Habitat Suitability
- Data Analysis
llm_service: openrouter
original_filename: DJI_01_20250620_130628.m4a
processed_date: '2025-06-20T13:41:48.387292'
word_count: 500
---
# Monarch Abundance and Wind: Hypotheses & Analytics Plan

This document outlines the informal hypotheses and proposed analytical approaches following a meeting with Francis. The project aims to test several hypotheses regarding the effect of wind on monarch butterfly abundance.

## 1. Loose Wind Hypothesis

*   **Hypothesis:** Higher wind speeds are negatively correlated with changes in monarch abundance. Increased wind results in higher rates of monarchs leaving a site, leading to more negative abundance calculations.
*   **Proposed Analysis:**
    *   **Predicted Variable:** Change in monarch abundance.
    *   **Predictor Variables:** Wind speed, wind gust.
    *   **Model Structure:** Incorporate autocorrelation (e.g., AR1) to account for temporal dependencies.
    *   **Random Effects:** `view`, `labeler`.

## 2. Strict Wind Hypothesis (Kingston Leong's Threshold)

*   **Hypothesis:** Monarch butterflies will abandon a site when wind speed explicitly exceeds the Kingston Leong threshold of 5 mph (2.2 m/s).
*   **Proposed Analysis:**
    *   **Predicted Variable:** Change in monarch abundance.
    *   **Predictor Variable:** A new continuous variable: `minutes_above_threshold` (total minutes wind speed was > 2.2 m/s).
    *   **Random Effects:** `view`, `labeler`.
*   **Open Question:** The time frame for calculating the 'change in abundance' needs to be determined. Options range from 30 minutes to a full day. This may require exploration to find the most effective interval.

## 3. Habitat Suitability Hypothesis

*   **Hypothesis:** After a site experiences winds exceeding the 5 mph threshold, monarchs will not return to it.
*   **Proposed Analysis & Challenges:** This hypothesis is complex to test. The goal is to assess the long-term impact of high-wind events on site re-occupancy.
    1.  **Define Analysis Period:** For each camera view, identify the first day that both a) monarch clusters are present and b) the wind threshold is exceeded. This day marks the start of the analysis period for that view.
    2.  **Define Response Variable:** Use the morning (first light) monarch abundance count. This avoids confounding the count with wind effects that might occur later on the same day.
    3.  **Define Predictor Variables:** Model morning abundance against a set of predictors to test the hypothesis:
        *   `days_since_last_threshold_exceeded`: The primary predictor. If the hypothesis is true, abundance should be near zero for any value > 0.
        *   `cumulative_threshold_days_with_monarchs`: Cumulative count of days where the threshold was exceeded while monarchs were present.
        *   `cumulative_threshold_days_total`: Cumulative count of all days the threshold was exceeded, regardless of monarch presence.
*   **Challenges & Considerations:**
    *   **Defining a 'Threshold Day':** A clear rule is needed to classify a day as having 'exceeded the threshold' (e.g., a single gust vs. a sustained period). The results from the 'Strict Wind Hypothesis' analysis may inform this definition.
    *   **Data Limitations:** The analysis must account for incomplete data coverage of the overwintering season and the inability to distinguish between new and returning individuals.
    *   **Expected Outcome:** The anticipated result is noise, which would suggest this hypothesis is not supported by the data.

## 4. Future Topics

*   **Light:** An additional factor to consider is the effect of light. The methodology for incorporating this into the models needs to be developed.