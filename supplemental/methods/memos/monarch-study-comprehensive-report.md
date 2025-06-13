# Comprehensive Report: Monarch Butterfly Camera Trap Study - Image Sampling Analysis

## Document Overview

This report synthesizes two technical documents from Kyle Nessen examining optimal sampling intervals for a monarch butterfly camera trap study. The primary question addressed is whether reducing the frequency of image classification (by skipping images) can maintain data quality while reducing labor costs.

### Document 1: "Check Image Skip Analysis" (2025-06-12)
- **Purpose**: Initial exploratory analysis to determine if skipping images during classification would preserve the overall patterns in monarch count data
- **Key Finding**: Visual inspection suggests that reducing sampling frequency from 5-minute to 60-minute intervals appears to maintain the general trend patterns

### Document 2: "Sampling Interval Analysis" (2025-03-21)
- **Purpose**: Rigorous statistical analysis using mixed-effects models to determine optimal sampling interval
- **Key Finding**: 30-minute intervals provide the best balance, losing less than 5% of information compared to full resolution

## Study Background and Motivation

### Camera Trap Deployment Details
- **Study System**: Trail cameras monitoring monarch butterfly aggregations
- **Original Sampling Frequencies**:
  - SC1 and SC2 deployments: 5-minute intervals
  - SC4 and subsequent deployments: 10-minute intervals
- **Classification Method**: Manual labeling of butterfly counts in categories (0, 1-10, 11-50, 51-100, 101-500, 501-1000, >1000)
- **Challenge**: Labor-intensive image classification process, particularly problematic for early deployments with 5-minute intervals

### Deployment Characteristics
1. **SC1 & SC2**: 
   - Cameras positioned close to butterfly clusters
   - Smaller field of view
   - More precise count estimates
   - 5-minute sampling interval

2. **SC4**: 
   - Camera positioned further from butterflies
   - Wider landscape view
   - More variance in counts due to "hundreds" category usage
   - 10-minute sampling interval

## Data Collection and Preparation Methods

### Image Classification Protocol
- **Daytime Images**: Full manual classification into count categories
- **Nighttime Images**: 
  - Difficult to observe butterflies due to camera flash
  - Labelers instructed to copy last valid daytime count
  - These periods identified and removed from analysis

### Data Processing Pipeline

#### 1. Data Standardization
- SC1 and SC2 data (5-minute intervals) reduced to 10-minute intervals by retaining every other row
- All deployments aligned to common 10-minute baseline
- Timestamps parsed and data sorted by deployment and time

#### 2. Observation Period Definition
- Created unique identifiers combining deployment ID and date
- Allows grouping by complete observation periods (e.g., "SC1_2023-11-19")

#### 3. Nighttime Data Removal
- Specific night periods identified for each deployment where counts were duplicated
- These observations removed to avoid bias in statistical models

#### 4. Subsampling Creation
- Datasets created at 10, 20, 30, 60, 90, and 120-minute intervals
- Method: Retain every nth row within each deployment group

#### 5. Response Variable Transformation
- Calculated change in butterfly counts between consecutive time points
- Zero changes replaced with 0.1 to allow log transformation
- Applied signed log transformation: log(|change|) × sign(change)
- Transformation necessary due to poor initial model performance

#### 6. Wind Data Integration
- Wind data aligned with butterfly observations by deployment and timestamp
- Calculated metrics per interval:
  - Average wind speed (mph)
  - Average wind gust (mph)
  - Maximum wind gust (mph)
  - Number of wind observations

## Statistical Modeling Approach

### Model Structure
- **Response Variable**: log-transformed monarch count change (monarch_change)
- **Fixed Effects**: 
  - avg_wind_speed_mph (scaled)
  - avg_wind_gust_mph (scaled)
  - max_wind_gust_mph (scaled)
- **Random Effect**: deployment_id (to account for site-specific variation)
- **Temporal Correlation**: First-order autoregressive structure (corAR1) within deployments
- **Implementation**: Linear mixed-effects model using nlme::lme() in R

### Model Comparison Methods

#### 1. Information-Theoretic Approach (AIC)
- Applied same model structure to each subsampled dataset
- Compared AIC scores across sampling intervals
- **Results**:
  - 10 min: AIC = 1343.45 (n=298)
  - 30 min: AIC = 468.60 (n=99)
  - 60 min: AIC = 234.91 (n=50)
  - 120 min: AIC = 116.14 (n=25)
- **Limitation**: AIC sensitive to sample size, making direct comparison problematic

#### 2. Root Mean Square Error (RMSE) Comparison
- Calculated relative RMSE compared to full dataset baseline
- More appropriate for comparing information loss across different sample sizes
- **Key Results**:
  - 20 min: ~3% information loss
  - 30 min: <5% information loss
  - 60 min: ~11% information loss
  - 90 min: ~16% information loss
  - 120 min: ~25% information loss

## Key Findings

### Optimal Sampling Interval: 30 Minutes
- Represents best balance between data quality and labor reduction
- Less than 5% information loss compared to full resolution
- Reduces image classification workload by 3× compared to 10-minute intervals
- RMSE increases rapidly beyond 30-minute intervals

### Model Performance (30-minute interval model)
- **Model Diagnostics**: Some issues present but approaching defensible performance
- **Wind Effects**: No significant relationship between wind variables and monarch count changes (all p-values > 0.35)
- **Random Effects**: Minimal deployment-level variation (StdDev = 9.47e-05)
- **Temporal Autocorrelation**: Parameter estimate = 0, suggesting no significant temporal correlation at 30-minute scale

### Visual Pattern Preservation
- Time series plots show that 30-minute intervals maintain:
  - Overall declining trends over observation periods
  - Peak activity periods
  - Day/night transitions
  - General magnitude of counts

## Specific Observations by Deployment

### SC1 (November 17-20, 2023)
- Initial counts: 100-150 monarchs
- Clear declining trend over 3-day period
- Final counts: near zero
- Pattern well-preserved at 30-minute intervals

### SC2 (November 17-19, 2023)
- More stable counts initially (around 100)
- Sharp decline on final day
- Higher baseline counts than SC1
- 30-minute sampling captures major transition points

### SC4 (December 3-4, 2023)
- Much higher counts (400-600 range)
- More variance due to "hundreds" category usage
- Stable period followed by sharp decline
- Pattern remains clear even at 60-minute intervals

## Methodological Considerations

### Strengths
1. **Multiple Analysis Approaches**: Both visual and statistical validation
2. **Conservative Transformation**: Log transformation handles zero-inflated count changes
3. **Hierarchical Modeling**: Accounts for deployment-specific effects
4. **Temporal Structure**: AR(1) correlation addresses time-series dependencies

### Limitations
1. **Limited Dataset**: Only 3 deployments fully analyzed
2. **Categorized Counts**: Loss of precision from count categories vs. exact numbers
3. **Nighttime Exclusion**: Potential loss of movement information
4. **Model Convergence**: Some diagnostic issues in final models

### Future Considerations
1. **Sunlight Exposure**: Author notes this may be more important than wind
2. **Camera Positioning**: Field of view affects count variance
3. **Seasonal Patterns**: Current analysis limited to fall aggregation period

## Recommendations for Methods Section

Based on this analysis, the methods section should emphasize:

1. **Sampling Design Justification**: 30-minute intervals selected based on empirical analysis showing <5% information loss while reducing classification effort by 67%

2. **Data Quality Control**: Systematic removal of nighttime periods where counts were artificially duplicated

3. **Statistical Rigor**: Mixed-effects modeling approach accounting for site-specific variation and temporal autocorrelation

4. **Transformation Rationale**: Log-transformation of count changes to handle zero-inflation and improve model performance

5. **Multi-scale Validation**: Both visual inspection and quantitative metrics (RMSE) used to validate sampling interval selection

## Appendix: Technical Details

### Data Structure
- **Temporal Coverage**: 
  - SC1: November 17-20, 2023
  - SC2: November 17-19, 2023
  - SC4: December 3-4, 2023

- **Sample Sizes by Interval** (for all deployments combined):
  - 10 min: 298 observations
  - 30 min: 99 observations
  - 60 min: 50 observations
  - 120 min: 25 observations

### Model Output (30-minute interval)
```
Fixed effects:
- Intercept: -0.443 (SE=0.248, p=0.078)
- avg_wind_speed: -0.559 (SE=2.050, p=0.786)
- avg_wind_gust: 0.334 (SE=2.145, p=0.877)
- max_wind_gust: 0.403 (SE=0.429, p=0.351)

Random effects:
- Deployment SD: 9.47e-05
- Residual SD: 2.47
```

This comprehensive analysis provides strong empirical support for using 30-minute sampling intervals in the monarch butterfly camera trap study, balancing scientific rigor with practical feasibility.