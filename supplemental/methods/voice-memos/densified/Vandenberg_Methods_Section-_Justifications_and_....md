# Vandenberg Methods Section: Justifications and Details

This document outlines the rationale and justifications for key methodological decisions in the Vandenberg study, based on a brain dump addressing specific questions.

## Camera and Wavelength Selection

### Why Near-Infrared (NIR)?

The choice of NIR was inspired by a mention in a previous monarch butterfly study suggesting its potential for counting butterflies with machine learning. 

- **Literature Precedent**: There was existing literature, however minimal, demonstrating the viability of this approach.
- **No Alternatives Considered**: Due to the promising lead from the literature, other wavelengths were not actively considered.
- **Compatibility with Trail Cameras**: NIR modification is particularly well-suited for consumer-grade trail cameras.

### Why Trail Cameras?

Trail cameras were ideal for this study for several reasons:

- **Affordability**: Cost is low, at less than $150 per unit.
- **Durability**: They are designed for long-term deployment in harsh environmental conditions.
- **Built-in Features**: They include native time-lapse functionality.
- **Ease of Modification**: Trail cameras are designed for night photography and contain a mechanism that dynamically switches an IR cut filter. This allowed for a non-destructive modification to make the cameras capture only NIR light.

## Field Validation and Procedures

### How were camera modifications validated?

Validation was performed visually in the field.

- **Process**: A modified camera was taken to a site with monarch clusters. Test photos were taken.
- **Success Criterion**: The modification was considered successful if monarch clusters were readily and clearly distinguishable from the background scenery to a human observer. This was deemed sufficient since the plan always involved human labelers.

### What were the backup procedures for equipment failure?

No formal backup protocols were in place for equipment failure during critical monitoring periods.

## Sampling Design

### Justification for the 10-Minute Sampling Interval

The initial 10-minute interval was a field decision based on balancing multiple factors.

- **Butterfly Movement Patterns**: Preliminary observations showed that significant changes in butterfly abundance occurred on the scale of hours, not minutes.
- **Balancing Trade-offs**: The 10-minute interval was chosen as a sweet spot between ensuring sufficient temporal resolution and conserving battery life for long deployments. A 10-minute interval allowed for approximately six weeks of continuous operation.
- **Later Adjustments**: The interval was later relaxed to 30 minutes. Analysis of the time-series data showed that a 30-minute interval captured the same essential data structure and story as the 10-minute interval, while a 1-hour interval was too coarse. This change reduced the image processing and labeling workload by two-thirds without sacrificing critical data integrity.

> **Note**: There are detailed memos from Francis that further flesh out the sampling interval justification. These should be consulted for a more thorough explanation.

## Data Labeling and Grid System

### Grid System Development and Optimal Cell Size

The grid cell size was determined dynamically for each camera deployment rather than by a fixed formula.

- **Process**: The grid size (number of rows/columns) was set manually for each deployment. A formula was used to ensure grid cells remained square.
- **Optimization Goal**: The grid was adjusted so that at peak abundance, most occupied cells contained butterfly counts in the "tens to 99" range. This was considered the sweet spot for minimizing ambiguity in classification, especially between the "dozens" and "hundreds" categories, where errors have the largest impact on total abundance estimates.
- **Consequences of Poor Sizing**:
    - **Too Large**: A single grid cell covering the entire cluster would fail to capture spatial or temporal variation, only registering a change when the entire cluster was gone.
    - **Too Small**: Would create excessive noise from minor butterfly movements and dramatically increase the labeling burden.

### Why Use Order of Magnitude Categories?

This choice was a deliberate strategy to balance effort and accuracy.

- **Reduced Cognitive Load**: The primary reason was to reduce the cognitive burden and time required for human labelers to process tens of thousands of images.
- **Quantitative Rules**: The system provides a proxy for categorical data (e.g., small, medium, large) but anchors it to quantitative rules, making it less subjective than pure estimation.
- **Enables Statistical Analysis**: By taking the lower bound of each category, the data can be converted into a conservative, continuous estimate of abundance, which is suitable for statistical analysis.

### How was the grid system validated for capturing spatial variation?

The validation is handled within the study's analytical framework.

- **Unit of Observation**: The view of each camera is the fundamental unit being measured. Variation between these views is expected.
- **Statistical Approach**: To account for this, the `deployment ID` will be used as a random effect in the statistical model, which controls for the inherent differences in what each camera is observing.

## Observer Reliability and Training

### How was inter-observer reliability handled?

Formal inter-observer reliability tests were not conducted.

- **Mitigation Strategy**: To ensure consistency, a single observer was assigned to label all images from a single deployment. This maintains a consistent (if potentially biased) measurement across that entire unit of observation.

### What were common classification errors and how were they addressed?

Errors were identified and corrected through an iterative review process.

- **Common Errors**:
    - **Under-classification**: Early on, labelers sometimes underestimated the order of magnitude category.
    - **Over-classification (More Common)**: The most frequent error was classifying empty grid cells as occupied. This was often caused by labelers mistaking gaps in the tree canopy for butterflies.
    - **Missed Butterflies**: It was very rare for labelers to miss butterflies that were present.

- **Training and Feedback Loop**:
    1. A new labeler processed an initial batch of ~200 images.
    2. This work was reviewed, and detailed, specific feedback was provided, including screenshots and notes on individual images (e.g., "This is a gap in the canopy, not butterflies").
    3. The labeler corrected the initial batch.
    4. This iterative cycle of work, review, and feedback continued with subsequent batches until the labeler's accuracy and consistency improved to an acceptable level.