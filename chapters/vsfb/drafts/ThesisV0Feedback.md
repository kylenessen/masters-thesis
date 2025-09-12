# [Remains mostly unchanged]{.comment-start id="1" author="Kyle Nessen" date="2025-09-08T22:17:00Z"}Introduction[]{.comment-end id="1"}

## Introduction Outline

The distribution and survival of invertebrate species are governed by a
complex interplay of biotic and abiotic factors. For many insects,
abiotic conditions such as temperature, humidity, and wind can be
primary drivers of behavior, physiology, and habitat selection. Wind, in
particular, can influence everything from dispersal and migration to
foraging efficiency and predation risk.

The monarch butterfly (*Danaus plexippus*) presents an excellent system
for studying these dynamics. Its diverse life history, which includes
distinct breeding and overwintering phases, exposes it to a unique suite
of environmental challenges. As a charismatic and threatened species,
understanding the factors that limit monarch populations is not only of
scientific interest but also critical for effective conservation.

The overwintering stage, when monarchs form dense aggregations in
coastal California and central Mexico, is a period of immense
physiological stress where abiotic factors are paramount. During this
time, the \"microclimate hypothesis\" suggests that monarchs select
groves that provide a specific suite of conditions necessary for
survival: protection from freezing temperatures, access to moisture,
dappled sunlight for thermal regulation, and shelter from wind.

Among the abiotic factors shaping monarch overwintering habitat, wind
has emerged as potentially critical yet remains poorly understood.
Leong's influential work (2016) proposed that wind acts as a primary
determinant of habitat suitability, specifically asserting that winds
exceeding 2 m/s physically disrupt monarch clusters. According to this
\"disruptive wind hypothesis,\" such winds dislodge butterflies from
their roosts or trigger escape responses, forcing monarchs to expend
critical energy reserves needed for winter survival while increasing
predation exposure. This 2 m/s threshold has become dogma in monarch
conservation, directly informing management guidelines adopted by
organizations including the Xerces Society.

Yet despite its widespread influence on conservation practice, Leong's
hypothesis rests on indirect evidence. The original conclusions derived
from comparing wind measurements between occupied and unoccupied roost
trees. An observational approach that cannot establish causation or
demonstrate actual butterfly responses to wind exposure. No study has
directly observed whether monarchs actually abandon roosts when winds
exceed 2 m/s, whether such abandonment represents temporary displacement
or permanent desertion, or whether the presumed energy costs actually
occur. This empirical gap is remarkable given that habitat management
decisions affecting millions of conservation dollars assume these wind
effects are real.

Testing the disruptive wind hypothesis requires isolating wind's effects
from confounding environmental drivers. As ectotherms, monarchs depend
on solar radiation for flight, with sunlight exposure triggering
departures for foraging, water-seeking, or mate-searching. The warming
effect of solar radiation itself depends on ambient temperature---direct
sunlight enables flight at lower intensities on warm days than cold
ones. Without accounting for this temperature-sunlight interaction, any
observed correlation between wind and monarch departures could be
spurious. Furthermore, wind itself is multidimensional: its potential
disruption may depend not only on average speed but also on consistency
(sustained winds versus calm periods) and turbulence (gustiness). A
meaningful test must therefore examine how different wind
characteristics influence monarch behavior while controlling for thermal
conditions.

This study provides the first direct, empirical test of whether wind
disrupts overwintering monarch butterflies. Using continuous time-series
observations of butterfly behavior within an occupied roost, paired with
simultaneous monitoring of wind conditions and thermal variables, we can
finally determine whether the foundational assumption underlying current
management practices is valid.

We tested whether wind disrupts overwintering monarch butterflies
through a series of hierarchical hypotheses, each building upon the
previous findings.

[Removed H4 and H5, as this analysis doesn\'t address it. I can recover
if necessary. I have an idea for how to test for site abandonment we can
discuss.]{.comment-start id="3" author="Kyle Nessen"
date="2025-09-08T22:18:00Z"}[OK]{.comment-start id="1597852636"
author="Francis X. Villablanca" date="2025-09-09T09:03:42"}First, we
hypothesized that wind acts as a disruptive force to overwintering
monarch butterflies. If true, we predict that monarch abundance at
roosts will decrease when exposed to [It seems the next hypothesis is
based on a \"disruptive wind\" effect of a specific nature. So, the
nature of the disruptive wind here is not clear. Put another way, how
are these two hyp different?\
Maybe it is not so important to actually distinguish between the first
and the second hypothesis. Because they are intrinsically quite
different. I am thinking this first Hyp leads to the set of AIC tests to
determine if wind is even a factor\... Can we make that clear in the
hypothesis and prediction? Something like. Hypothesis: wind, as well as
multiple environmental factors, might predict butterfly abundance at
overwintering clusters. Prediction: an information theoretic approach
should identify wind and environmental factors as attributes that
contribute significantly to the observed abundance of over wintering
monarch butterflies in clusters.]{.comment-start id="1428008541"
author="Francis X. Villablanca" date="2025-09-09T09:05:59"}disruptive
[]{.comment-end id="1428008541"}winds.

Second, we hypothesized that wind becomes disruptive above a specific
threshold of 2 m/s. If this threshold represents a meaningful biological
boundary, we predict that monarch abundance will decline at roosts
experiencing winds exceeding 2 m/s.

Third, we hypothesized that wind's disruptive effects scale with
intensity. If disruption increases with wind speed, we predict
proportionally greater decreases in monarch abundance as wind speeds
rise above the threshold.[[]{.comment-end id="1597852636"}]{.comment-end
id="3"}

## [Mostly unchanged]{.comment-start id="5" author="Kyle Nessen" date="2025-09-08T22:18:00Z"}Materials and Methods[]{.comment-end id="5"}

### Study Site

Site selection followed a systematic filtering process driven by project
requirements and practical constraints. The study was supported by a
federal grant that mandated research be conducted on federal lands. We
selected Vandenberg Space Force Base (VSFB, 34.7398°N, 120.5725°W) in
Santa Barbara County, California, based on several key advantages: mild
winters with infrequent frost events, extensive historical plantings of
blue gum eucalyptus (*Eucalyptus globulus*) that have created suitable
overwintering habitat throughout the installation, and restricted access
that provided security for long-term equipment deployment. The base
contains thirty documented monarch overwintering groves, with several
sites consistently ranking within the top 10% of population counts
statewide over the past decade (Xerces Society 2025a).

Working with the base's monarch conservation coordinator, we initially
screened twelve locations from the thirty sites based on their
documented capacity to support monarch aggregations and provide
year-round access. This collaboration leveraged local expertise from
managing Western Monarch Thanksgiving Count activities for multiple
years (Xerces Society 2025a). During the study period, ten of these
sites were actively monitored. However, due to low monarch populations
during the 2023-2024 season and no observed overwintering behavior in
the 2024-2025 season, only two sites (Spring Canyon and UDMH) produced
measurable butterfly clusters suitable for our analysis.

Spring Canyon (34.6315°N, 120.6182°W) represents the most productive and
historically reliable overwintering site on VSFB. Located in South Base
within 300 meters of Space Launch Complex 4, this approximately
2.0-hectare site consists entirely of mature blue gum eucalyptus trees
reaching heights of approximately 40 meters. An unnamed perennial creek
runs through the center of the grove, creating a riparian corridor that
supports heterogeneous canopy structure with variable tree spacing and
diverse understory vegetation. Surf Road, an infrequently used paved
access road, bisects both the perennial creek and forest canopy.

The UDMH site (34.6719°N, 120.5950°W), also located in South Base,
comprises a 5.1-hectare eucalyptus grove planted in windrows adjacent to
a waste treatment facility. The uniformly spaced trees maintain a
largely clear understory with scattered low shrubs. Although only
recently documented as an overwintering location in 2022, UDMH
immediately emerged as a significant site, supporting over 6,000
monarchs during its initial count and ranking among the base's highest
population sites.

### Monitoring Strategy

Equipment deployment strategies differed between monitoring seasons to
accommodate research objectives and field experience. During the
2023-2024 season, we employed two strategies: targeted deployments at
sites with confirmed monarch presence, and anticipatory deployments at
locations where monarchs were expected based on historical data but not
currently observed. Targeted deployments concentrated at Spring Canyon
and UDMH where active aggregations were documented throughout the
season. Anticipatory deployments occurred at four overwintering sites:
additional locations within Spring Canyon and UDMH, plus SLC-6 and
Tangair. No monarchs were recorded at anticipatory deployment sites;
consequently, these data are excluded from analysis.

Building on insights from the initial season, for the 2024-2025 season
we modified our approach to establish monitoring stations at ten sites
before monarch arrival, based on historical occurrence records compiled
by the base conservation coordinator. This expanded spatial coverage
aimed to capture greater environmental variation across potential
overwintering sites. However, the 2024-2025 season coincided with
historically low monarch abundance throughout California (Xerces Society
2025b), resulting in no observed clustering behavior at any monitored
location on base. Consequently, our final dataset comprises two sites
(Spring Canyon and UDMH) from the 2023-2024 season only.

### Field Equipment

To observe changes in monarch abundance in response to strong wind
events, we deployed remote monitoring equipment near butterfly clusters
at overwintering sites. Field observations utilized 15-meter telescoping
fiberglass poles (Max-Gain Systems, Inc., Marietta, GA) anchored at
three points using ground anchors with guy lines securing both the top
and base to create stable, freestanding structures.

Poles were positioned 4-17 meters from cluster locations. This range,
determined through field testing, balanced image resolution requirements
for our grid-based counting method against disturbance minimization.
Closer positioning compromised field of view, while greater distances
degraded butterfly visibility below classification thresholds. Pole
placement considered ground stability for the 15-meter structures,
infrastructure clearance requirements, and clear viewing angles. When
deploying near active clusters, we approached from directions that
minimized disturbance; no butterfly dispersal was observed during
equipment deployment.

We monitored monarch abundance using modified trail cameras (GardePro E7
and E8, Shenzhen, China) configured for near-infrared imaging to enhance
contrast between clustering butterflies and surrounding vegetation.
Trail cameras were selected for their durability in extended field
deployment, native time-lapse functionality, and modification potential.
Near-infrared wavelength selection followed previous literature
demonstrating effectiveness for butterfly population estimation (Hristov
et al. 2019).

Hardware modifications exploited the camera's internal filter-switching
mechanism by engaging nighttime mode to access the clear glass filter
position, then disconnecting power to prevent reversion to the infrared
cut filter. Near-infrared pass filters (\>850 nm) were mounted
externally to restrict incoming light to NIR wavelengths. This
configuration produced images where clustering butterflies appeared as
dark masses against bright eucalyptus foliage reflectance in the
near-infrared spectrum. Field validation confirmed sufficient contrast
for visual distinction of monarch clusters from background vegetation,
supporting our human-labeler analytical approach.

Cameras were mounted atop poles using lightweight tie-down straps and
positioned horizontally toward butterfly clusters at roosting height.
The wireless live view feature enabled real-time preview and precise
camera aiming during deployment. Cameras operated in time-lapse mode
with motion detection disabled.

Sampling interval selection balanced temporal resolution, battery life,
and data processing feasibility through empirical optimization and
rigorous statistical validation. Initial deployments used 10-minute
intervals to capture significant changes in butterfly abundance, which
preliminary observations indicated occurred on hourly rather than minute
scales, while maintaining approximately 6-week continuous operation.
Post-deployment statistical analysis using mixed-effects models and
information-theoretic approaches systematically compared multiple
sampling intervals across deployments. We conducted sequential subsample
analyses starting with full temporal resolution and progressively
testing reduced frequencies. Information-theoretic model comparison
using Akaike Information Criterion (AIC) demonstrated that 30-minute
intervals provided optimal balance, losing less than 5% of information
compared to full temporal resolution (measured by root mean square
error) while reducing image classification workload by 67%. Variance
comparison analysis and visual assessment of fitted trend lines
confirmed that this interval preserved essential time-series patterns
including diurnal activity cycles, weather-response dynamics, and
multi-day population trends. Battery life constraints and field
deployment logistics further supported this interval choice, enabling
extended autonomous operation essential for capturing complete
behavioral sequences during variable weather conditions.

To quantify the wind conditions hypothesized to influence butterfly
behavior, wind monitoring equipment consisted of Rain Wise WindLog Wind
Data Loggers (Rain Wise Inc., Trenton, Maine) installed at pole apices
to measure wind at heights approximating butterfly roosting locations.
These instruments recorded average wind speed and maximum wind gust at
one-minute intervals, the highest frequency supported by the sensors.
This recording interval enabled calculation of wind speed variance
within each photographic sampling period, capturing gustiness lost with
longer averaging periods.

To systematically organize our heterogeneous monitoring efforts, we
defined discrete monitoring periods as deployment units. Each deployment
represented a unique combination of monitoring location, camera
configuration (including camera ID, mounting height, and viewing angle),
associated wind measurements, and temporal coverage period. Since
equipment was frequently reused across locations and time periods, this
deployment-based structure provided standardized sampling units that
accounted for variation in environmental conditions and equipment
configurations while treating each deployment as independent for
statistical analyses. This approach produced time-series images from
each deployment for estimating monarch cluster abundance through
systematic grid-based counting methods, enabling analysis of abundance
patterns in relation to wind speed and other environmental variables.

### Image Analysis

#### Grid-based Counting Method

To quantify changes in monarch butterfly abundance from collected
imagery, we developed a systematic grid-based counting protocol
balancing accuracy with the practical constraints of analyzing tens of
thousands of images. This approach addressed the challenge of estimating
abundance in large aggregations where individual counts would be
prohibitively time-consuming and emulated field researcher methods,
including those used in the annual Thanksgiving Count (Xerces Society
2017). We subdivided each image using a grid overlay system where human
labelers assigned order-of-magnitude estimates per cell. Grid dimensions
remained fixed throughout each deployment to ensure consistency. Custom
software developed using the Electron framework in JavaScript
facilitated this labeling effort.

Grid cell size varied by deployment based on camera-to-cluster distance.
Cell dimensions were optimized to ensure most occupied cells contained
butterflies in the 10--99 count range, balancing classification
efficiency with spatial resolution. This standardization minimized cells
alternating between widely different order-of-magnitude categories
across the time series.

#### Counting Protocol

Human labelers estimated butterfly abundance within each grid cell using
four order-of-magnitude categories: 0 (no butterflies), 1--9 (single
digits), 10--99 (dozens), and 100--999 (hundreds). Labelers trained
using a comprehensive online guide with example images and detailed
classification criteria
(<https://kylenessen.github.io/monarch_trailcam_classifier/>). The
protocol prioritized efficiency while maintaining consistency across
observers.

Because abundance estimates derived exclusively from two-dimensional
photographic images, our classification protocol quantified only
butterflies visible in the image plane without estimating
three-dimensional cluster structure or depth. This approach
intentionally excluded hidden individuals behind visible butterflies in
overlapping aggregations, providing a conservative but consistent
measure reflecting observable surface area rather than total volume. For
cells containing partial butterflies at grid boundaries, labelers
included these in counts unless double-counting would cause an adjacent
cell to move to a higher category. When butterfly counts fluctuated
between categories across the time series, we consistently applied the
lower estimate to maintain conservative abundance estimates.

In addition to estimating monarch abundance, labelers recorded whether
cells received direct sunlight. Direct sunlight classification presented
challenges because oversaturated conditions eliminated the contrast
enabling butterfly detection in shaded areas. Labelers classified cells
as receiving direct sunlight when branches or butterflies exhibited
additional illumination clearly from direct rather than indirect light,
even when individual butterflies became difficult to distinguish due to
pixel oversaturation. This classification required careful attention to
subtle shape recognition and contextual awareness about butterfly
locations established from previous images in the time series. This
measurement was recorded only for occupied cells and stored separately.

Labelers received ongoing feedback throughout the classification
process. All classifications underwent review for common errors
including mislabeled cells, incorrect category assignments, and
inconsistent counting criteria application. Direct communication of
corrections to labelers ensured consistent protocol application.

#### Abundance Calculation

We calculated an abundance index for each frame by summing the products
of cell counts and their assigned category values across all grid cells,
employing conservative estimates using minimum values within each
order-of-magnitude category:

$$\text{Abundance index} = \sum_{i}^{}\rho_{i} \times C_{i}$$

where $\rho_{i}$ represents the number of cells in category $i$, and
$C_{i}$ represents the conservative estimate for that category. We used
minimum category values ($C_{1} = 1$ for category 1--9, $C_{2} = 10$ for
category 10--99, and $C_{3} = 100$ for category 100--999) rather than
midpoint or maximum values to ensure temporal analyses reflected genuine
population shifts rather than estimation uncertainty.

### [Beginning of new content]{.comment-start id="14" author="Kyle Nessen" date="2025-09-08T22:19:00Z"}Temperature Data Extraction[]{.comment-end id="14"}

Temperature represents a critical environmental variable influencing
monarch activity patterns and potentially confounding wind effects.
Ambient temperature data were extracted from trail camera images using
optical character recognition (OCR). Each camera displayed temperature
readings on the image overlay, but these values were not accessible
through EXIF metadata, necessitating visual extraction methods. We
developed an automated Python script utilizing OCR technology to extract
temperature values from approximately 56,000 images across all
deployments. The extraction process employed multiple preprocessing
strategies and pattern matching algorithms to accommodate variations in
image quality and display characteristics.

Following initial automated extraction, we manually reviewed and
corrected edge cases where OCR failed or produced anomalous values. All
temperature data underwent systematic quality control through
visualization of deployment-specific time series, enabling
identification and correction of erroneous values. This process ensured
complete temperature coverage for all analyzed images, providing the
ambient temperature covariate required for our statistical models.

### Statistical Analysis

#### Data Preparation

Statistical analysis employed a lag-based framework to capture the
temporal dynamics of butterfly responses to environmental changes,
comparing butterfly counts between consecutive 30-minute intervals.
Observation pairs were constructed by matching counts at time $t$ with
counts at time $t - 30$ minutes, applying a ±5 minute tolerance window
to accommodate minor temporal variations in image capture. The response
variable (change in butterfly abundance between time points) underwent
cube root transformation to achieve approximate normality while
preserving directional information:
$y = \text{sign}(\Delta) \times |\Delta|^{1/3}$, where $\Delta$
represents the difference in butterfly counts. While exploratory data
analysis revealed generally well-behaved distributions, we observed
bimodality in the raw butterfly abundance data driven primarily by a
single anomalous event at deployment SC8. At this deployment, a large
butterfly aggregation abruptly declined to near zero without
corresponding changes in the measured environmental variables (wind
speed, temperature, or solar exposure). This singular event was unlike
any other observation in the dataset. We retained this deployment in the
final analysis for two reasons: first, to maximize sample size and avoid
arbitrary data exclusion, and second, sensitivity analysis showed that
the cube root transformation of abundance differences adequately
addressed the distributional concerns, with model selection and
parameter estimates remaining consistent whether SC8 was included or
excluded. The transformation approach made the anomaly's inclusion or
exclusion immaterial to the final results. Observation pairs where both
time points recorded zero butterflies were excluded as uninformative,
reducing the dataset from approximately 2,500 potential pairs to 1,894
analyzable observations across 115 unique deployment-day combinations.

#### Variable Selection

Predictor variables were selected to test specific hypotheses while
avoiding multicollinearity. Maximum wind gust speed during each
30-minute interval served as the primary wind metric, with alternative
wind measurements (average sustained speed, modal gust, gust standard
deviation) excluded due to high correlation ($r > 0.75$). Environmental
predictors included average temperature between observation pairs,
number of butterflies in direct sunlight at the previous time point, and
minutes elapsed since the first observation of each day to capture
diurnal patterns. Total butterfly count at the previous time point was
included as a control variable, enabling distinction between
proportional and absolute changes in abundance. When included, this
variable tests effects on proportional change; when excluded, models
test effects on absolute change.

#### Model Framework

Analysis employed generalized additive mixed models (GAMMs) implemented
through the mgcv package in R. Model selection followed an
information-theoretic approach, comparing 48 candidate models using
Akaike Information Criterion (AIC). The candidate set comprised two
fundamental frameworks: models including the lag abundance term (24
models) and models excluding it (24 models), with each framework
containing null models, single predictor models, additive combinations,
two- and three-way interactions, and models incorporating smooth terms
for non-linear relationships. Random effects structure accounted for
variation at three hierarchical levels: deployment location, observer,
and deployment-day. Temporal autocorrelation within days was addressed
using a first-order autoregressive (AR1) correlation structure grouped
by deployment-day. All models were fitted using restricted maximum
likelihood (REML) estimation.

To test specifically for threshold effects at the proposed 2 m/s
disruptive wind speed, we conducted a sensitivity analysis using an
alternative wind metric. We repeated the entire model selection process,
replacing maximum wind gust speed with a threshold-based predictor: the
count of minutes within each 30-minute observation period where wind
gusts equaled or exceeded 2 m/s. This variable ranged from 0 to 30
minutes and was tested using the same 48 model structures, allowing
direct comparison of continuous versus threshold-based wind effects.

#### Model Validation

Model assumptions were verified through standard residual diagnostics
including examination of residual distributions, fitted versus residual
plots, and quantile-quantile plots. Convergence was confirmed for all
candidate models in both the primary and sensitivity analyses. Model
performance and predictor significance were evaluated through AIC
comparison, with models differing by less than 2 AIC units considered
equivalent.

#### Statistical Power Analysis

To evaluate whether our study had adequate statistical power to detect
wind effects if present, we conducted a simulation-based power analysis.
This approach assessed our ability to detect various effect sizes given
our sample size of 1,894 paired observations. We simulated 200 datasets
from the best-fitting model (which excluded wind effects) and
artificially introduced wind effects of known magnitude ranging from
0.05 to 0.20 standard deviations of the response variable. For each
effect size, we refitted models including wind terms to determine the
proportion of simulations where the artificial effect was detected as
statistically significant ($\alpha = 0.05$). This simulation approach
accounts for the complexity of our GAMM framework and hierarchical data
structure, providing robust estimates of statistical power for detecting
wind effects across a range of biologically plausible magnitudes.

## Results

### [The results section should start with some descriptive statistics. Basically, just let us be able to discern that there was variation within the relevant attributes. It should also include Information about cluster sizes, and the overall population size for overwintering monarchs.]{.comment-start id="1181496883" author="Francis X. Villablanca" date="2025-09-09T09:47:57"}Summary of Data[]{.comment-end id="1181496883"} and Model Selection

Environmental factors, but not wind, drove monarch abundance changes in
1,894 paired observations from 115 monitoring periods at two
overwintering sites during the 2023-2024 season. Testing of 48 candidate
models identified M23 as the best-fit model.

Model M23 included smooth terms for previous butterfly count,
temperature, butterflies in direct sun, and time since sunrise,
achieving an AIC value of 8081.848 (Table [1.1](#tab:model_selection)).
This model accounted for 88% of the model weight (AIC weight = 0.88),
with the next-best model (M22) showing substantially less support (ΔAIC
= 4.796). Wind variables appeared in only one of the top five models
(M24), which included maximum wind speed but performed substantially
worse than M23 (ΔAIC = 6.2, AIC weight = 0.04), with the wind effect
showing weak evidence of an association (p = 0.218).

  --------------------------------------------------------------------------------
  Model   Terms                                  AIC        ΔAIC    Weight  Wind p
  ------- -------------------------------------- -------- ------ --------- -------
  M23     Previous butterfly count, Temperature, 8081.8      0.0     0.880      NA

          Butterflies in direct sun, Time since                            
          sunrise                                                          

  M22     Previous butterfly count, Temperature  8086.6      4.8     0.080      NA
          (linear),                                                        

          Butterflies in direct sun, Time since                            
          sunrise                                                          

  M24     Previous butterfly count, Maximum wind 8088.0      6.2     0.040   0.218
          speed,                                                           

          Temperature, Butterflies in direct                               
          sun, Time since sunrise                                          

  M47     Temperature, Butterflies in direct     8101.3     19.4   \<0.001      NA
          sun,                                                             

          Time since sunrise                                               

  M17     Previous butterfly count, Temperature, 8105.9     24.0   \<0.001      NA

          Butterflies in direct sun                                        
  --------------------------------------------------------------------------------

  : []{#tab:model_selection .anchor}Model selection results showing the
  top five candidate models ranked by AIC. Model terms are shown with
  their respective AIC values, ΔAIC relative to the best model, and AIC
  weights [across the five top performing models]{.insertion
  author="Francis X. Villablanca" date="2025-09-09T19:18:42.192Z"}.
  [Given that no models are regarded as]{.insertion
  author="Francis X. Villablanca" date="2025-09-09T19:18:59.874Z"}
  [equivalent to the best fit model (M23), the actual weight of M23 is
  1.0.]{.insertion author="Francis X. Villablanca"
  date="2025-09-09T19:19:28.317Z"} Wind p-values are shown where
  applicable; NA indicates the model did not include wind variables.

### Analysis of the Best-Fit Model

The best-fit model (M23) explained 5.7% of variance in monarch abundance
changes (adjusted R² = 0.057). The model formula was:

$$\text{Change in abundance} \sim s(\text{Previous butterfly count}) + s(\text{Temperature}) + s(\text{Butterflies in direct sun}) + s(\text{Time since sunrise})$$

where $s()$ denotes smooth terms. All four smooth terms showed
significant effects on monarch abundance changes.

  -----------------------------------------------------------------------
  Term                              EDF   Ref. df    F-value      p-value
  ----------------------------- ------- --------- ---------- ------------
  Previous butterfly count         2.62      2.62      12.02     8.26e-07

  Temperature                      3.93      3.93       3.23        0.028

  Butterflies in direct sun        1.53      1.53      19.36     1.22e-05

  Time since sunrise               4.90      4.90       8.90      \<2e-16
  -----------------------------------------------------------------------

  : Summary of smooth terms in the best-fit model (M23). EDF represents
  effective degrees of freedom, indicating the complexity of each smooth
  relationship.

All four predictors in the best-fit model showed significant effects on
monarch abundance changes (Figure [1.1](#fig:partial_effects)). The
previous butterfly count exhibited a significant non-linear negative
relationship (EDF = 2.62, F = 12.02, p \< 0.001), with increasingly
negative changes as the previous count increased, indicating
proportionally greater departures from larger aggregations. Butterflies
in direct sun showed a strong negative effect on roost abundance (EDF =
1.53, F = 19.36, p \< 0.001), with greater numbers in direct sun
associated with larger decreases in total abundance.

Time since sunrise revealed a pronounced diurnal pattern (EDF = 4.90, F
= 8.90, p \< 0.001), capturing cyclical changes in monarch activity
throughout the [elaborate on the pattern - meaning describe the decrease
and the increase.]{.comment-start id="510059722"
author="Francis X. Villablanca"
date="2025-09-09T09:31:33"}day[]{.comment-end id="510059722"}.
Temperature exhibited a complex non-linear relationship (EDF = 3.93, F =
3.23, p = 0.028), with [further describe the pattern\... increase,
followed by decrease\...]{.comment-start id="1379661831"
author="Francis X. Villablanca" date="2025-09-09T09:32:36"}effects
peaking[]{.comment-end id="1379661831"} at approximately 20°C.

[]{#fig:partial_effects
.anchor}![](figures/media/image1.png){width="5.833333333333333in"
height="4.861111111111111in"}

Partial effects of the four significant predictors on monarch abundance
change in a 2x2 layout. [The partial effect on monarch abundance as
estimated from the s]{.insertion author="Francis X. Villablanca"
date="2025-09-09T19:22:59.563Z"}[ingle attribute being compared to
abundance while assuming all other attribute values are held
constant.]{.insertion author="Francis X. Villablanca"
date="2025-09-09T19:23:27.682Z"} Top row: butterflies in direct sun
(left) and previous butterfly count (right). Bottom row: time since
sunrise in minutes (left) and [Can you add a symbol or a line to the
figure indicating the flight temp threshold? Or add it to the
legend?]{.comment-start id="498657290" author="Francis X. Villablanca"
date="2025-09-09T09:24:59"}temperature []{.comment-end id="498657290"}in
°C (right). Solid lines show the estimated smooth functions with 95%
confidence intervals (shaded regions). All effects are shown on the same
scale for comparison.

### Evaluation of the Disruptive Wind Hypothesis

[I think this comment goes at the end of this section rather than at the
beginning. Meaning that you should show the actual result for these two
hypotheses, and then conclude with this statement.]{.comment-start
id="51997291" author="Francis X. Villablanca"
date="2025-09-09T09:36:39"}Our analysis provided no support for the
three hierarchical wind hypotheses:[]{.comment-end id="51997291"}

First, wind did not act as a disruptive force to overwintering monarchs.
Among our 48 candidate models, wind appeared in only one of the top five
models (M24), where it showed little evidence of an [It might be cool to
provide the partial effects plot for wind from this model. It should be
somewhat uninterpretable.]{.comment-start id="212183262"
author="Francis X. Villablanca" date="2025-09-09T09:34:32"}effect
[]{.comment-end id="212183262"}(p = 0.218) and resulted in substantially
poorer model performance compared to the best model (ΔAIC = 6.2).

Second, we found no evidence for disruption above the proposed 2 m/s
threshold. A sensitivity analysis using a specific threshold predictor
('minutes with wind speed \> 2 m/s') confirmed this lack of a threshold
effect, as [This is the crux of the argument. Can you provide a table
similar to the one that you provided above that compares the top models
and shows that the 2 m/s predictor had poor performance in the
models?]{.comment-start id="406950664" author="Francis X. Villablanca"
date="2025-09-09T09:38:27"}models with this variable performed poorly
and did not rank among the top candidates[]{.comment-end
id="406950664"}. Visually, the relationship between wind and monarch
abundance change remained flat across the 2 m/s boundary
(Figure [1.2](#fig:wind_scatter)). With mean maximum wind speeds of
2.2 m/s (SD = 1.4 m/s), conditions that should have revealed threshold
effects if present, no disruption occurred at or above this boundary.

Third, wind's effects did not scale with intensity. The relationship
remained flat across all observed wind speeds (0--12 m/s), with
confidence intervals consistently encompassing zero
(Figure [1.2](#fig:wind_scatter)).

[]{#fig:wind_scatter
.anchor}![](figures/media/image2.png){width="4.666666666666667in"
height="3.499998906386702in"}

Relationship between maximum wind speed (m/s) and monarch abundance
change. The red dashed line shows the proposed 2 m/s disruptive wind
threshold, while the flat trend line indicates no effect of wind on
butterfly departures. Points represent 30-minute observation periods.

### Statistical Power to Detect Wind Effects

Post-hoc power analysis confirmed our study had adequate statistical
power to detect biologically meaningful wind effects
(Table [1.3](#tab:power_analysis)). With 1,894 paired observations, we
achieved 87.5% power to detect moderate effect sizes (0.15 standard
deviations) and 98.5% power to detect larger effects (0.20 standard
deviations). Power for small effects (0.10 standard deviations) was 56%,
while very small effects (0.05 standard deviations) yielded only 16.5%
power. These results indicate that our failure to detect wind effects is
unlikely due to insufficient statistical power for effect sizes of
biological relevance.

  -----------------------------------------------------------------------
             Effect Size (SD units)      Power (Proportion) Power (%)
  ------- ------------------------- ----------------------- -------------
  0.05                         0.05                   0.165 16.5%

  0.1                          0.10                   0.560 56%

  0.15                         0.15                   0.875 87.5%

  0.2                          0.20                   0.985 98.5%
  -----------------------------------------------------------------------

  : []{#tab:power_analysis .anchor}Estimated power to detect wind
  effects of varying magnitudes. Effect sizes are expressed in standard
  deviations of the response variable (cube root transformed change in
  butterfly abundance).

### Model Diagnostics

Model residuals showed distinct linear banding patterns consistent with
the discrete counting method used to estimate butterfly abundance, while
the Q-Q plot indicated approximately normal residual distribution with
minor tail deviations (Figure [1.3](#fig:diagnostics)).

[]{#fig:diagnostics
.anchor}![](figures/media/image3.png){width="5.833333333333333in"
height="2.9166666666666665in"}

Model diagnostics for M23. Left: Residuals versus fitted values showing
banding that reflects the discrete counting method, with smoothed
relationship shown in blue. Right: Normal Q-Q plot of model residuals
showing reasonable normality with minor tail deviations.

## Discussion

### Wind Does Not Disrupt Overwintering Monarch Butterflies

Our study provides the first direct empirical test of the disruptive
wind hypothesis and finds no support for wind as a primary factor
influencing monarch butterfly clustering behavior. Despite the
widespread adoption of the 2 m/s wind threshold in conservation practice
(Society 2016), our data reveal no relationship between wind speed and
butterfly departures across the full range of observed conditions (0--12
m/s). While our models explain only 5.7% of variance in butterfly
movements, reflecting our focus on testing wind effects rather than
comprehensively explaining movement patterns, they had sufficient
statistical power to detect environmental signals. This finding
challenges assumptions underlying three decades of management guidance.

The absence of wind effects in our data is particularly striking given
that [observed]{.insertion author="Francis X. Villablanca"
date="2025-09-09T19:49:07.504Z"} mean maximum wind speeds (2.2 m/s, SD =
1.4) frequently exceeded the proposed threshold. If the disruptive wind
hypothesis were valid, we should have observed a clear signal:
transitions from aggregated butterflies to zero butterflies, as strictly
predicted by the [disruptive wind]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:49:38.69Z"}
hypothesis. Instead, we observed no change, small changes, or even
positive changes in butterfly abundance at wind speeds six times the
proposed [disruption]{.insertion author="Francis X. Villablanca"
date="2025-09-09T19:49:54.894Z"} threshold.

Importantly, our [analysis had adequate statistical power to detect
biologically meaningful wind effects. P]{.deletion
author="Francis X. Villablanca"
date="2025-09-09T19:51:40.787Z"}[p]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:51:40.821Z"}ower
analysis demonstrated 87.5% power to detect moderate effect sizes (0.15
standard deviations) and 98.5% power for larger effects (0.20 standard
deviations)[. Among our 48 candidate models,]{.deletion
author="Francis X. Villablanca" date="2025-09-09T19:52:05.637Z"}[,
while]{.insertion author="Francis X. Villablanca"
date="2025-09-09T19:52:08.323Z"} wind appeared in only one of the top
five models (M24)[.]{.insertion author="Francis X. Villablanca"
date="2025-09-09T19:52:27.683Z"}[,]{.deletion
author="Francis X. Villablanca" date="2025-09-09T19:52:25.775Z"}
[where]{.deletion author="Francis X. Villablanca"
date="2025-09-09T19:52:30.223Z"} [In that model]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:52:35.033Z"}
[it]{.deletion author="Francis X. Villablanca"
date="2025-09-09T19:52:38.913Z"} [wind]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:52:40.533Z"} showed
little evidence of an effect (p = 0.218) and resulted in substantially
poorer model performance compared to the best model (ΔAIC = 6.2,
capturing only 4% of model weight). This weak wind signal, combined with
our high statistical power, allows us to rule out all but very small
wind effects. Given that the disruptive wind hypothesis [I think this is
too strong of a statement. It needs to be tone down. I don\'t think the
hypothesis needs to be complete abandonment. Instead, I think the
hypothesis clearly predicts a reduction in abundance. That reduction in
abundance is exactly what we tested. So, I think the remainder of this
statement is perfectly valid as is, so long as the strength of the
statement is tone down to be \"significant reduction in
abundance.\"]{.comment-start id="1974545001"
author="Francis X. Villablanca" date="2025-09-09T09:54:43"}predicts
complete cluster abandonment []{.comment-end id="1974545001"}above
threshold speeds, a large effect by any measure, our failure to detect
such patterns provides strong evidence against the hypothesis rather
than merely absence of evidence.

The methodological validity of our approach is confirmed by the strong
signals detected for other environmental variables. Had our counting
method or analytical framework been flawed, we would not have captured
the pronounced effects of direct sunlight (F = 19.36, p \< 0.001) or the
complex diurnal patterns (F = 8.90, p \< 0.001) that emerged from the
same dataset.

### Alternative Drivers of Monarch Movement

While our study was designed specifically to test the wind hypothesis,
our results suggest that thermoregulation, light exposure, and diurnal
rhythms play more important roles than wind in driving short-term
movements at overwintering sites.

#### Direct Sunlight as the Strongest Predictor

Direct sunlight exposure emerged as the strongest environmental
predictor of [Do you mean this? Or do you mean reduction in abundance
even to the point of cluster abandonment?]{.comment-start
id="1340558452" author="Francis X. Villablanca"
date="2025-09-09T09:57:10"}cluster abandonment[]{.comment-end
id="1340558452"} in our study (F = 19.36, p \< 0.001). Butterflies
exposed to direct sunlight at the beginning of an observation interval
showed the largest decreases in abundance, suggesting that solar
radiation rapidly [warms]{.deletion author="Francis X. Villablanca"
date="2025-09-09T19:57:25.844Z"} [increases]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:57:28.85Z"}
butterfly body temperatures well above ambient conditions. This finding
aligns with Masters, Malcolm, and Brower (1988)'s work showing that
monarchs in direct sunlight can elevate their body temperature above
ambient conditions within minutes (Masters[, Malcolm, and
Brower]{.deletion author="Francis X. Villablanca"
date="2025-09-09T19:57:46.269Z"} [et al.]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:57:47.737Z"} 1988).
This rapid warming capability [could r]{.insertion
author="Francis X. Villablanca"
date="2025-09-09T19:57:59.93Z"}[eadily]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:58:01.439Z"}
explain[s]{.deletion author="Francis X. Villablanca"
date="2025-09-09T19:58:04.517Z"} why direct sunlight exposure is such a
strong predictor of [reductions in abundance and]{.insertion
author="Francis X. Villablanca" date="2025-09-09T19:58:17.877Z"} cluster
abandonment[I think this paragraph is fine as arguing for a pattern
driven by an attribute (sun exposure). But I certainly do not think that
you should add a putative or possible mechanism to the very end of the
very last sentence in the paragraph.\
The mechanism(s) behind this pattern need to be carefully considered an
articulated.]{.comment-start id="1216175895"
author="Francis X. Villablanca" date="2025-09-09T09:59:57"}, butterflies
must quickly respond to avoid overheating.[]{.comment-end
id="1216175895"}

The relationship between sunlight and departure represents a key
component of the thermoregulatory equation. [Isn\'t this the positive
impact of direct solar exposure that I have been
articulating?]{.comment-start id="1470941527"
author="Francis X. Villablanca" date="2025-09-09T10:01:06"}While
monarchs have evolved efficient solar heat absorption capabilities that
enable activity during cool conditions[]{.comment-end id="1470941527"},
[And then isn\'t this the negative impact of direct solar exposure that
you have been articulating?\
I love the trade-off statement at the end of the paragraph. It resonates
with me. But I think that the trade-off is obvious to me because we have
been thinking about it. It is not so obvious from the positive and
negative statements in the paragraph. In a sense, the trade-off nature
needs to be better explained, so that the concluding statement in this
paragraph is then simply a summary of those explanations. As it stands,
the positive and negative is obvious-ish, but the trade-off is
not.]{.comment-start id="1608569543" author="Francis X. Villablanca"
date="2025-09-09T10:05:06"}this same efficiency forces them to abandon
energetically favorable clustering positions when exposed to direct
solar radiation[]{.comment-end id="1608569543"}. This trade-off between
the benefits of clustering and the thermal constraints imposed by solar
exposure may fundamentally shape daily movement patterns at
overwintering sites.

#### Temperature Effects and Their Interpretation

Ambient temperature showed a subtle but significant relationship with
monarch abundance changes (EDF = 3.93, F = 3.23, p = 0.028). The data
suggest minimal change below 15°C (the known flight threshold), a slight
positive association around 20--21°C, and sharp declines above 25°C
consistent with thermoregulatory constraints. Given that thermal [I am
sorry to say we did not show preference. Instead we showed that the
temperature available correlated with latitude, and therefore the
temperature utilized correlated with latitude.]{.comment-start
id="427711220" author="Francis X. Villablanca"
date="2025-09-09T10:09:09"}preferences []{.comment-end
id="427711220"}vary between [sites]{.deletion
author="Francis X. Villablanca" date="2025-09-09T20:05:47.657Z"}
[overwintering groves in a latitudinal f]{.insertion
author="Francis X. Villablanca"
date="2025-09-09T20:05:59.923Z"}[ashion]{.insertion
author="Francis X. Villablanca" date="2025-09-09T20:06:02.22Z"} (Saniee
and Villablanca 2022), [Which \"patterns\" is not clear as written. Be
more specific.]{.comment-start id="509042118"
author="Francis X. Villablanca" date="2025-09-09T10:09:52"}these
patterns[]{.comment-end id="509042118"} require validation across the
overwintering range before we can generalize about monarch thermal [Be
sure this is the word that you mean. Testing for preference requires a
particular type of data. It has to not just be utilization of what is
available, but has to be a disproportionate utilization of part of what
is available and a disproportionate non-utilization of another part of
what is available.]{.comment-start id="1896033690"
author="Francis X. Villablanca"
date="2025-09-09T10:11:56"}preferences[]{.comment-end
id="1896033690"}[You might be better served by rewriting this paragraph
to stipulate that the temperature available at a specific grove would be
expected to be variable across the landscape (as a function of
latitude). This means that the effect that you see at Spring Canyon only
captures a portion of the continuum of temperature ranges that might be
evident across the entire overwintering range. Probably the best point
would be to say that you have only sampled a part of the
continuum...]{.comment-start id="986205021"
author="Francis X. Villablanca"
date="2025-09-09T10:14:20"}.[]{.comment-end id="986205021"}

#### Diurnal Activity Patterns

Time since sunrise revealed distinct diurnal patterns (EDF = 4.90, F =
8.90, p \< 0.001), with butterflies departing clusters in the morning
and reforming aggregations in the afternoon. This pattern persists even
after controlling for temperature and sunlight, aligning with anecdotal
observations from overwintering sites throughout California.

### Study Limitations

Several limitations warrant consideration. Our data derive from a single
season (2023--2024) at two sites, [This statement is not totally clear
as written. Try to explain what the issue was, and what a possible
negative affect would have been on this study.]{.comment-start
id="1430942253" author="Francis X. Villablanca"
date="2025-09-09T10:18:19"}with historically low monarch abundance
preventing temporal replication[]{.comment-end id="1430942253"}.
Additionally, our counting methodology introduced discretization
artifacts that contributed to large confidence intervals for
environmental predictors. While we detected strong signals like direct
sunlight effects, more subtle relationships require careful
interpretation[Remember, that Kingston could still be right. It is
possible that his inference is valid for monarchs in very large
aggregation clusters. You should say that that we identify this as a
possibility, because it appeared that most of the butterflies in your
study were able to connect. directly with the substrate. Butterflies in
aggregations orders of magnitude larger than what you observed, would be
connected to one another, rather than to the substrate. If one infers
that a direct connection to substrate changes the relationship to wind,
then, we only addressed a limited version of the hypothesis. One where
butterflies are directly connected to the substrate. It may be
reasonable to suggest exploring whether the dynamic for larger clusters
is comparable.]{.comment-start id="1044341027"
author="Francis X. Villablanca"
date="2025-09-09T10:24:24"}.[]{.comment-end id="1044341027"}

### Management Implications

Our findings suggest that management strategies prioritizing wind
protection warrant reconsideration. The absence of wind effects despite
frequent threshold exceedances indicates that usable habitat within
existing groves may be larger than currently recognized. Areas
previously dismissed due to perceived wind exposure may provide suitable
conditions [if]{.deletion author="Francis X. Villablanca"
date="2025-09-09T20:24:58.497Z"} [because]{.insertion
author="Francis X. Villablanca" date="2025-09-09T20:24:59.544Z"}
[]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:25:00.351Z"}they offer appropriate light and thermal
regimes.

While past management efforts aimed at wind protection may have been
based on incomplete understanding, they likely produced beneficial
outcomes by increasing tree density. The fundamental recommendation to
plant and maintain trees remains sound. Management should prioritize
maintaining existing mature trees while establishing future roosting
habitat at densities that support healthy, long-lived growth. [In
addition,]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:25:59.796Z"} [as suggested by Saniee and Villablanca
(2022),]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:26:40.402Z"} [it may become relevant to explore ways
in which to manage for thermal attributes, specifically]{.insertion
author="Francis X. Villablanca" date="2025-09-09T20:25:59.796Z"}
[sunlight.]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:26:12.28Z"}

### Future Research Directions

Our findings open several important avenues for future research. First,
explicit testing of light patterns as predictors of clustering locations
could establish whether canopy structure guides habitat selection. The
strong effect of direct sunlight (F = 19.36, p \< 0.001) combined with
the predictability of canopy-created light patterns suggests this may be
a primary factor in roost site selection[This would be a great place to
add something about Light Models. It would be good to come full circle
and identify how light models were used early on, and then morphed
slightly (ha ha ha understatement) to wind models.]{.comment-start
id="1408631966" author="Francis X. Villablanca"
date="2025-09-09T10:29:31"}.[]{.comment-end id="1408631966"}

Second, investigation of social dynamics and positive
[behavioral]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:29:45.951Z"} feedback mechanisms could address
unexplained variation in our models. Monarchs may exhibit emergent
clustering behaviors where initial settlement increases the probability
of others joining, creating self-reinforcing patterns independent of
environmental conditions.

Research should also examine whether our findings extend across the
broader overwintering range. Testing these patterns at sites with
different tree species, latitudes, and [in particular]{.insertion
author="Francis X. Villablanca" date="2025-09-09T20:30:25.555Z"}
population densities would strengthen conclusions about the generality
of wind effects, or their absence.

### Conclusions

Wind did not disrupt monarch clusters even at speeds far exceeding
[established]{.deletion author="Francis X. Villablanca"
date="2025-09-09T20:31:26.097Z"} [presumptive]{.insertion
author="Francis X. Villablanca" date="2025-09-09T20:31:30.18Z"}
thresholds. Instead, butterflies responded primarily to thermal
conditions, [including]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:31:44.597Z"} light exposure [and ambient
temperature]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:31:58.561Z"}, and [to]{.insertion
author="Francis X. Villablanca" date="2025-09-09T20:32:03.476Z"} diurnal
rhythms. These findings challenge current assumptions about
overwintering habitat requirements and suggest that management
priorities should be reevaluated. While our study represents one season
at two sites, the absence of wind effects despite adequate statistical
power raises important questions [about]{.deletion
author="Francis X. Villablanca" date="2025-09-09T20:32:21.49Z"}
[regarding]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:32:23.925Z"} [three]{.deletion
author="Francis X. Villablanca" date="2025-09-09T20:32:27.046Z"} decades
of conservation guid[elines]{.insertion author="Francis X. Villablanca"
date="2025-09-09T20:32:37.618Z"}[ance]{.deletion
author="Francis X. Villablanca" date="2025-09-09T20:32:31.809Z"}. As
monarch populations face continued threats, evidence-based management
becomes increasingly critical for conserving the overwintering sites
essential for this iconic species.

## References

Hristov, Nickolay I., Dionysios Nikolaidis, Tatjana Y. Hubel, and Louise
C. Allen. 2019. "Estimating Overwintering Monarch Butterfly Populations
Using Terrestrial LiDAR Scanning." *Frontiers in Ecology and Evolution*
7. <https://www.frontiersin.org/articles/10.3389/fevo.2019.00266>.

Masters, Alan R., Stephen B. Malcolm, and Lincoln P. Brower. 1988.
"Monarch Butterfly (Danaus Plexippus) Thermoregulatory Behavior and
Adaptations for Overwintering in Mexico." *Ecology* 69 (2): 458--67.
<https://doi.org/10.2307/1940444>.

Saniee, Kiana, and Francis Villablanca. 2022. "Hierarchy and Scale
Influence the Western Monarch Butterfly Overwintering Microclimate."
*Frontiers in Conservation Science* 3.
<https://www.frontiersin.org/articles/10.3389/fcosc.2022.844299>.

Society, Xerces. 2016. "State of the Monarch Overwintering Sites in
California."
<https://www.xerces.org/sites/default/files/2018-05/16-015_01_XercesSoc_State-of-Monarch-Overwintering-Sites-in-California_web.pdf>.

Xerces Society. 2017. "Step-by-Step Western Monarch Thanksgiving Count
Monitoring Guide."

---------. 2025a. "Western Monarch Thanksgiving Count and New Year's
Count Data, 1997-2025."
[WesternMonarchCount.com](https://WesternMonarchCount.com).

---------. 2025b. "Western Monarch Butterfly Population Declines to Near
Record Low." March 6, 2025.
<https://www.xerces.org/press/western-monarch-butterfly-population-declines-to-near-record-low>.
