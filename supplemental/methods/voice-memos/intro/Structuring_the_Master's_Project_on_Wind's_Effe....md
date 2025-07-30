---
date: '2025-07-29T20:00:34+00:00'
duration_seconds: 2.1
keywords:
- monarch butterflies
- master's project
- wind analysis
- light exposure
- hypothesis testing
- site fidelity
- statistical modeling
llm_service: openrouter
original_filename: 250729_1300.mp3
processed_date: '2025-07-29T23:46:00.350309'
word_count: 889
---
# Master's Project Analysis Plan

This memo outlines the refined research plan for my master's project, focusing on the effect of wind on monarch butterflies, after a discussion with Ashley Fisher.

## Core Research Plan: A Three-Step Wind Analysis

The primary focus is a clean, three-step analysis of how wind affects monarch abundance at roosting sites.

### 1. Test the Established Threshold Hypothesis
First, I will test Kingston Leong's specific hypothesis: that wind speeds exceeding 2 meters per second are disruptive, causing butterflies to be dislodged or to fly away. My data collection method cannot distinguish between these two outcomes, but the result is the same: the butterflies are no longer in the frame. This is a straightforward test to see if butterflies leave when exposed to wind speeds above that threshold.

*   **Prediction:** I suspect we will not find strong evidence to support this specific 2 m/s threshold.

### 2. Model the General Relationship Between Wind and Abundance
Regardless of the first test's outcome, the natural follow-up question is: does wind, in a more general sense, cause butterflies to leave their roosting sites? I will use a multi-level, generalized fixed-effect model to determine if there is a statistical relationship between wind speed and changes in monarch abundance. If we find no relationship, the analysis stops here. We would then conclude that either the study's limitations prevent us from detecting an effect, or that long-held understandings of monarch habitat requirements need to be challenged.

### 3. Develop a Predictive Hazard Model
If we do find a significant relationship in the general model, the third step will be to use a Wilcoxon hazard analysis, similar to what Ray used. This analysis would predict the probability of monarchs abandoning a roost as wind speeds increase. The goal is not to set a definitive new threshold, but to present our observations on what is "too much wind" and provide recommendations with error bars. For example, we could state: "At X wind speed, we predict a Y% probability of the roost vacating." This would be a very useful and interpretable outcome.

This three-part story is simple to explain, uses relatively simple models, and provides a robust analysis of the wind question.

## Confounding Variable: The Role of Light

Initially, I was struggling with how to form a hypothesis around light. However, I now realize light is not a separate hypothesis to be tested, but rather a critical confounding variable that must be controlled for in the wind analysis.

**Rationale for Controlling for Light:**
1.  **Physiology:** Monarchs are ectotherms and readily absorb heat from sunlight. They exhibit sunning behaviors to warm up to their flight threshold (around 15°C / 55°F).
2.  **Behavioral Moderation:** The lipid-use budget hypothesis suggests monarchs adopt behaviors to minimize energy expenditure, which is exponentially related to their body temperature. They need to stay warm enough to have the option of flight but avoid overheating.
3.  **Empirical Observation:** During data collection, we observed that prolonged exposure to direct light seemed to be a strong predictor of changes in monarch abundance.

Therefore, to accurately isolate the effect of wind, we must account for light exposure. In the introduction, I will explain that monarch thermal biology makes them highly responsive to direct light, and because we tracked this in our dataset, we are including it as a control variable. We can state that light was a strong predictor of abundance changes, which serves as an empirical description and a call for future studies, but it is not the hypothesis we are testing.

## Proposed Change: Dropping the Site Fidelity Hypothesis

I propose removing the hypothesis related to loss of site fidelity. Kingston Leong predicted that after experiencing disruptive wind, butterflies would leave the roost to seek shelter elsewhere in the grove or leave the grove entirely for the season.

The problem is that my data cannot answer this question. I can only count the number of butterflies present in the frame; I have no way of knowing if the butterflies that appear later are the same ones returning or new, naive butterflies arriving. Answering the site fidelity question is better suited for a future project, perhaps using the Monarch Cam system with full coverage of a small grove.

Including this hypothesis gets us into the weeds with data that cannot provide a convincing answer. The wind and light analyses outlined above are clean, achievable, and robust.

## Ancillary Ideas

### Data Visualization Concept
As a side note, a compelling way to visualize the change in monarch abundance would be to create a time-lapse video of the roost. We could superimpose the classification cells over the video, showing the count per frame in a corner as the numbers change from high to low. This would effectively demonstrate how the monarch counts were performed.

### Potential Short Note: Rocket Launches
I have a unique, opportunistic dataset on rocket launches. We could conduct a simple analysis to see if monarch butterflies respond to them. The method would be to compare the change in monarch abundance in the 30 minutes before and after a launch to changes during randomly selected 30-minute intervals from the study period. We could also test different time windows. If there is no response, that itself is a noteworthy finding. This could be published as a short note and would likely generate interest.