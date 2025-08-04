# Introduction

## Hypotheses and Predictions

### Wind Dispersal Hypothesis (H1)

**Hypothesis:** Higher wind speeds are negatively correlated with
monarch butterfly abundance at overwintering sites, as increased wind
causes monarchs to leave their roosting locations.

**Prediction:** We predict a significant negative correlation between
wind speed measurements and changes in monarch abundance, where higher
wind speeds correspond to decreases in butterfly counts at monitoring
sites.

**Proposed Analysis:** We will test this hypothesis using a
mixed-effects linear model with temporal autocorrelation to account for
the hierarchical structure of our data and time-series dependencies. The
response variable will be the change in monarch abundance calculated
between consecutive observation periods, allowing for both positive
(recruitment/clustering) and negative (departure/dispersal) values.
Primary fixed effects will include mean wind speed (averaged across the
observation period), maximum wind speed, 95th percentile wind speed, and
wind speed variance, which together capture the overall wind exposure,
peak wind events, extreme conditions, and gustiness experienced during
each observation interval.

Beyond testing linear relationships, we recognize that H1 encompasses a
broad investigation of wind effects on monarch behavior. If initial
analyses suggest that wind is indeed a significant factor influencing
overwintering abundance, we propose additional approaches to
characterize the nature of these relationships. Specifically, we could
implement segmented regression to identify potential breakpoints in
wind-abundance relationships, allowing the data to reveal critical wind
speeds where monarch behavior changes. Alternatively, smoothing splines
or piecewise regression could capture non-linear responses to wind
exposure. These threshold discovery methods would help determine whether
wind effects on monarch abundance are gradual and continuous or exhibit
sharp transitions at specific wind speeds.

To account for non-independence in our data structure, we will include
random intercepts for camera view (to control for site-specific
variation) and labeler identity (to control for observer effects in
abundance estimation). Given the temporal nature of abundance
measurements, we will incorporate an AR(1) autocorrelation structure to
model the expected correlation between consecutive time points, which is
critical for obtaining unbiased parameter estimates in time-series
ecological data.

Model diagnostics will include examination of residual plots, normality
assessment, and validation of the autocorrelation structure. We
anticipate reporting standardized effect sizes for wind variables, 95%
confidence intervals for all parameters, and visualization of the
predicted relationship between wind speed and abundance change. If
threshold effects are detected, we will report the estimated
breakpoint(s) with confidence intervals. A significant negative
coefficient for wind speed variables would support our hypothesis that
increased wind conditions drive monarch dispersal from overwintering
sites.

The statistical model will be implemented in R using the `nlme` package
as follows:

    # Linear model
    model_h1_linear <- lme(abundance_change ~ mean_wind_speed + max_wind_speed + 
                           wind_speed_95th + wind_speed_variance,
                           random = ~ 1 | view/labeler,
                           correlation = corAR1(form = ~ time_index | view),
                           data = monarch_wind_data,
                           method = "REML")

    # Threshold discovery using segmented regression
    library(segmented)
    model_h1_segmented <- segmented(model_h1_linear, 
                                   seg.Z = ~ mean_wind_speed,
                                   npsi = 1)  # test for 1 breakpoint

### Critical Wind Threshold Hypothesis (H2)

**Hypothesis:** Monarch butterflies abandon overwintering sites when
wind speeds exceed Kingston Leong's critical threshold of  5 mph (2.2
m/s).

**Prediction:** We predict that exposure to wind speeds exceeding 2.2
m/s will be significantly associated with negative changes in monarch
abundance.

**Proposed Analysis:** We will test the Kingston Leong threshold
hypothesis using a simple mixed-effects model that directly examines the
relationship between threshold exceedance and abundance change. The
response variable will be change in monarch abundance between
consecutive observation periods. The primary fixed effect will be
`minutes_above_2.2ms`, representing the total duration (in minutes) that
wind speeds exceeded the Kingston threshold during each observation
interval.

This focused approach tests the specific claim that 2.2 m/s represents a
critical threshold for monarch site abandonment, independent of other
wind characteristics. We will include the same random effects structure
as H1 (random intercepts for camera view and labeler identity) and AR(1)
temporal autocorrelation to account for data dependencies.

A significant negative coefficient for `minutes_above_2.2ms` would
support the Kingston Leong threshold hypothesis, while a non-significant
result would suggest that this specific threshold may not be
biologically meaningful for monarch site abandonment behavior.

The statistical model will be implemented in R using the `nlme` package
as follows:

    model_h2 <- lme(abundance_change ~ minutes_above_2.2ms,
                    random = ~ 1 | view/labeler,
                    correlation = corAR1(form = ~ time_index | view),
                    data = monarch_wind_data,
                    method = "REML")

### Site Fidelity Loss Hypothesis (H3)

**Hypothesis:** Following exposure to wind speeds exceeding 5 mph while
monarchs are present, butterflies will not return to previously occupied
sites, indicating permanent abandonment after high-wind events.

**Prediction:** We predict that morning abundance counts will remain
near zero at sites following days when both monarchs were present and
wind speeds exceeded 5 mph, with the predictor variable "days since last
threshold exceeded" showing no recovery in abundance for values greater
than zero.

**Proposed Analysis:** We will test this hypothesis using a logistic
mixed-effects model that examines site occupancy patterns following wind
threshold events. This approach directly tests the conservation claim
that monarchs permanently abandon sites after experiencing unsuitable
wind conditions.

We define a wind threshold event as any day when wind speeds exceed
2.2 m/s for ≥30 consecutive minutes while monarchs are present
(abundance \> 0). This operational definition ensures we capture
sustained wind exposure during active site occupation, rather than brief
gusts or events occurring at unoccupied sites. The 30-minute minimum
duration represents our initial analytical approach based on
photographic sampling intervals, though we anticipate exploring
alternative durations as data patterns emerge.

The response variable will be binary site occupancy status (occupied =
abundance \> 0, unoccupied = abundance = 0) derived from morning
abundance counts to avoid confounding with same-day wind effects. We
propose initially focusing on the 14-day period following each threshold
event to capture both immediate and sustained abandonment patterns
predicted by conventional wisdom, with the understanding that this
analysis window may be adjusted based on preliminary results and data
availability.

The primary fixed effect will be `days_since_wind_event`, representing
the number of days elapsed since the threshold event occurred. According
to the site abandonment hypothesis, we expect a strong negative
relationship where the probability of site occupation remains near zero
for all post-event time points, with no recovery pattern over the 14-day
analysis window.

This conservative analytical approach uses complete abandonment (zero
abundance) as the response threshold, giving the conventional wisdom
hypothesis the strongest possible test. If monarchs truly abandon sites
after wind exposure, this effect should be easily detectable even with
limited sample sizes. We will include random intercepts for camera view
and labeler identity to control for site-specific and observer effects,
following the same random effects structure used in H1 and H2.

Model diagnostics will focus on examining residual patterns, assessing
model convergence, and validating the binary response assumption. We
will report odds ratios for the temporal predictor, 95% confidence
intervals, and visualization of predicted occupancy probability across
the post-event time series. A significant negative coefficient for
`days_since_wind_event` would support the site abandonment hypothesis,
while a non-significant result would challenge current conservation
guidance regarding wind exposure and habitat suitability.

The statistical model will be implemented in R using the `glmer`
function from the `lme4` package as follows:

    library(lme4)
    model_h3 <- glmer(site_occupied ~ days_since_wind_event + (1|view) + (1|labeler),
                      family = binomial,
                      data = post_event_data)

### Thermal Regulation Hypothesis (H4)

**Hypothesis:** Overwintering monarch butterflies modify their
clustering behavior in response to direct sunlight exposure, with this
effect moderated by ambient temperature, as monarchs are sensitive to
overheating risks.

**Prediction:** We predict a significant interaction between sunlight
exposure proportion and ambient temperature on changes in monarch
abundance, where the combination of high direct sunlight exposure and
elevated temperatures will produce the greatest negative changes in
butterfly counts, particularly during morning observation periods when
clusters are most likely to disband.

**Proposed Analysis:** We will test this hypothesis using a
mixed-effects linear model with an interaction term to examine the
combined effects of sunlight exposure and ambient temperature on monarch
clustering behavior. This approach directly tests the thermal regulation
hypothesis that monarchs modify their behavior to avoid overheating when
exposed to direct sunlight under elevated temperature conditions.
Analysis will exclude observation periods with zero monarch abundance,
focusing exclusively on periods when butterflies are present to exhibit
thermal regulation behavior.

To isolate thermal regulation effects from concurrent wind influences,
we will include wind variables as covariates in our thermal regulation
model. This expanded approach tests whether sunlight-temperature
interactions remain significant predictors of monarch behavior when
accounting for wind effects, addressing the possibility that thermal and
wind factors are correlated in our dataset. By controlling for wind
while testing thermal mechanisms, this analysis approaches the broader
question of relative factor importance that might be addressed through a
comprehensive global model, but maintains focus on thermal regulation as
the primary mechanism of interest.

The response variable will be change in monarch abundance calculated
between consecutive observation periods, allowing for both positive
(clustering) and negative (dispersal) values. Our primary fixed effects
will include: (1) sunlight exposure proportion, calculated as the
proportion of butterflies experiencing direct sunlight relative to total
butterflies present during each observation period; (2) ambient
temperature, derived from temperature readings extracted via OCR from
deployment photographs; and (3) their interaction term (sunlight
exposure $\times$ ambient temperature), which tests our core prediction
that thermal effects are most pronounced when both factors are elevated.

This sunlight exposure metric addresses the key challenge of scaling
exposure measurements to population size. By calculating the proportion
of butterflies in direct sunlight relative to the total butterfly
population present, we obtain a continuous variable between 0 and 1.
Periods with zero sunlight exposure represent times when no butterflies
were positioned in sunny locations, providing natural contrast
conditions for our analysis.

To control for baseline differences between morning and afternoon
observation periods, we will include time period (morning vs. afternoon)
as a fixed effect in our model. Additionally, we will include mean wind
speed as a covariate to control for concurrent wind effects that might
confound thermal responses. This approach accounts for natural temporal
variation in monarch behavior while isolating thermal regulation
mechanisms from wind-driven dispersal effects, allowing us to test
whether sunlight-temperature interactions represent independent
behavioral drivers beyond wind influences.

We will include the same random effects structure as H1-H3 (random
intercepts for camera view and labeler identity) to control for
site-specific variation and observer effects. Given the temporal nature
of our data, we will incorporate AR(1) autocorrelation to model expected
correlation between consecutive time points, ensuring unbiased parameter
estimates in our time-series analysis.

Model diagnostics will focus on examining residual patterns, validating
the autocorrelation structure, and assessing the distribution of
sunlight exposure values. We will report interaction effect coefficients
with 95% confidence intervals, standardized effect sizes for all
predictors, and visualization of the predicted relationship between
sunlight-temperature combinations and abundance change. Results will
include the estimated effect of time period to characterize baseline
differences between morning and afternoon observations.

A significant negative interaction coefficient would support our thermal
regulation hypothesis, indicating that monarch abundance decreases most
markedly when both sunlight exposure and ambient temperature are
elevated, even when controlling for wind effects. Conversely,
non-significant interaction effects would suggest that thermal
regulation responses are not independent of wind influences or that
thermal regulation is not dependent on the combined influence of
sunlight and temperature factors. This expanded analysis will help
determine whether thermal factors represent primary drivers of monarch
behavior or secondary effects correlated with wind conditions.

The statistical model will be implemented in R using the `nlme` package
as follows:

    # Thermal regulation model with wind control
    model_h4 <- lme(abundance_change ~ sunlight_exposure_prop * ambient_temp + 
                     period + mean_wind_speed,
                    random = ~ 1 | view/labeler,
                    correlation = corAR1(form = ~ time_index | view),
                    data = monarch_thermal_data,
                    method = "REML")
