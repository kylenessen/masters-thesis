# VSFB Dynamic-Window Analysis: Methods and Results Brief

Purpose: Provide a precise, citable brief so another LLM can draft thesis-ready Methods and Results text that integrates the new dynamic-window daily GAMM analysis with the existing 30‑minute analysis. This brief maps files, variables, models, figures, and insertion points in the thesis.

---

## Overview

- Short-term (30‑minute) analysis in the thesis shows no effect of wind on immediate (t vs t−30 min) abundance changes and no evidence for a 2 m/s disruption threshold.
- New daily “dynamic-window” analysis tests whether day‑to‑day change in maximum cluster size depends on weather exposure aligned to the biology of roosting decisions. Both window definitions converge on the same best model: a smooth interaction between maximum wind gust and cumulative direct‑sun exposure.
- Conclusion across scales: no support for a simple disruptive wind threshold; instead, at the daily scale, wind’s association with roost change is conditional on sun exposure.

Key thesis anchors for integration:
- Methods addition anchor: `masters-thesis/chapters/vsfb/methods.tex:75` (subsection Statistical Analysis)
- Results addition anchor: `masters-thesis/chapters/vsfb/results.tex:15` (Summary of Data and Model Selection)

---

## Data and Preprocessing

Sources and structure
- Image classifications with per‑cell counts and `directSun` flags: `masters-analysis/data/deployments/*.json` (formats documented in `masters-analysis/data/deployments/json_structure.md:1`).
- Temperature (per image via OCR): `masters-analysis/data/temperature_data_2023.csv`.
- Wind (per-minute sustained and gust): SQLite databases in `masters-analysis/data/wind/*.s3db` (columns: `time`, `speed`, `gust`).
- Deployment metadata (joins and mapping to wind meters): `masters-analysis/data/deployments.csv`.

Pipeline (Python)
- Script: `masters-analysis/data_prep_dynamic_windows.py`.
  - Daily aggregates with “functional sunset”: `create_daily_aggregates_with_sunset` computes for each deployment–day: `max_butterflies`, `butterflies_95th_percentile`, `butterflies_top3_mean`, `time_of_max`, `last_observation_time`, `sum_butterflies_direct_sun`, `days_since_oct15`, `day_sequence` (`data_prep_dynamic_windows.py:260`).
  - Valid-day filtering: keep days with 15–25 daytime photos (`filter_valid_days`; `data_prep_dynamic_windows.py:580`).
  - Consecutive-day lag pairs: only t−1 to t pairs one day apart; skip pairs where both days are zero (`create_dynamic_lag_pairs`; `data_prep_dynamic_windows.py:640`).
  - Dynamic-window metrics (window spans defined below):
    - Temperature (24/7): `temp_min`, `temp_max`, `temp_mean`, `hours_above_15C`, `degree_hours_above_15C`, coverage versus expected 30‑min sampling (`calculate_dynamic_temperature_metrics`; `data_prep_dynamic_windows.py:359`).
    - Wind (24/7): `wind_avg_sustained`, `wind_max_gust`, `wind_gust_sum`, `wind_gust_sum_above_2ms`, `wind_minutes_above_2ms`, `wind_gust_sd`, `wind_mode_gust`, `wind_gust_hours`, coverage versus expected minutely sampling (`calculate_dynamic_wind_metrics`; `data_prep_dynamic_windows.py:422`).
    - Sun exposure (daylight only): `sum_butterflies_direct_sun` as the cumulative number of butterflies labeled `directSun` across frames in the window; daylight coverage approximated at ~2 obs/hour (`calculate_dynamic_sun_exposure`; `data_prep_dynamic_windows.py:529`).
  - Metrics completeness: geometric mean of coverage across temperature, wind, and daylight butterflies; analysis filters to `metrics_complete ≥ 0.95`.
  - Response construction per lag pair: differences for max/95th/top‑3 with signed square‑root and square transforms (`create_dynamic_lag_pairs`; `data_prep_dynamic_windows.py:769`).

Produced datasets
- 24‑hour window: `masters-analysis/data/monarch_daily_lag_analysis_24hr_window.csv`
- Sunset window: `masters-analysis/data/monarch_daily_lag_analysis_sunset_window.csv`

---

## Dynamic Windows and Rationale

Motivation
- Align exposure to the roost’s biological timing rather than fixed civil hours; directly tests weather from the observed daily peak through the next decision point.

Window definitions (implemented and compared in parallel)
- Sunset window (variable length): `time_of_max_count_t_1 → last_observation_time_t` (functional sunset). Mean duration ≈ 29.6 h; captures overnight through dusk when roosting decisions finalize.
- 24‑hour window (fixed length): `time_of_max_count_t_1 → +24 h`. Standardized exposure period.

References: `masters-analysis/analysis/dynamic_window_analysis/dynamic_window_gam_synthesis.qmd:21` and :39, :47.

---

## Modeling Framework (Daily GAMM)

Response selection
- Among nine transformations of max/95th/top‑3 differences, `butterfly_diff_sqrt` best approximated normality and is used as the response.
  - See: `dynamic_window_gam_synthesis.qmd:121`; `analysis/dynamic_window_analysis/24hr_window_gam_analysis.qmd:108`; `.../sunset_window_gam_analysis.qmd:106`.

Candidate predictors (19 total) and final selection
- Candidates enumerated in `dynamic_window_gam_synthesis.qmd:131` (baseline, temperature, wind, sun, window).
- Final modeling set (to reduce multicollinearity and df/n):
  - `temp_min`, `temp_max`, `temp_at_max_count_t_1`
  - `wind_max_gust`
  - `sum_butterflies_direct_sun`
  - `lag_duration_hours` (sunset-window analysis only)
  - Note: `wind_mode_gust` excluded due to only ~5 unique values, causing convergence issues (`dynamic_window_gam_synthesis.qmd:235`).

GAMM structure and estimation
- Fitted with `mgcv::gamm` (Gaussian, identity link), REML.
- Random intercepts for deployment: `random = list(deployment_id = ~1)`.
- Temporal autocorrelation: AR(1) within deployment by `observation_order_t`.
- Baseline control: `max_butterflies_t_1` as either smooth `s(., k=5)` or linear; form selected by information criteria.
- Model spaces: 76 models per window across null, single‑predictor, interaction‑only, additive, main+interaction, complex, and full (see `.../24hr_window_gam_analysis.qmd:407` and `.../sunset_window_gam_analysis.qmd:560`).
- Selection: AICc primary; ΔAICc < 2 competitive; df/n thresholds (≥0.2–0.3) flagged as overfitting risk; leave‑one‑deployment‑out CV on top candidates (see `.../sunset_window_gam_analysis.qmd:949`).

Sample sizes after completeness filter
- Sunset window: n = 96 pairs; mean duration ≈ 29.6 h.
- 24‑hour window: n = 94 pairs; fixed 24 h.

---

## Results: Model Selection and Effects

Convergent best model (both windows)
- Model: smooth interaction `ti(wind_max_gust, sum_butterflies_direct_sun)` with baseline controls.

Sunset window summary (n = 96)
- Formula: `butterfly_diff_sqrt ~ max_butterflies_t_1 + lag_duration_hours + ti(wind_max_gust, sum_butterflies_direct_sun)`.
- Interaction: edf ≈ 6.68; F ≈ 4.10; p ≈ 0.0008.
- Adjusted R² ≈ 0.397.
- Source: `dynamic_window_gam_synthesis.qmd:332` (summary block).

24‑hour window summary (n = 94)
- Formula: `butterfly_diff_sqrt ~ s(max_butterflies_t_1, k=5) + ti(wind_max_gust, sum_butterflies_direct_sun)`.
- Interaction: edf ≈ 3.54; F ≈ 3.59; p ≈ 0.020.
- Adjusted R² ≈ 0.232.
- Source: `dynamic_window_gam_synthesis.qmd:410` (summary block).

Interpretation of the interaction
- See comparison figure: `masters-analysis/analysis/dynamic_window_analysis/figures/window_comparison_interaction.png` (both windows plotted). Positive partial effects (red) indicate aggregation gains from day t−1 to t; negative (blue) indicate losses.
- Pattern: aggregation gains concentrate at **moderate sun exposure** combined with **moderate winds (~5–10 m/s)**. Effects flatten or become negative at very low or very high sun exposure; high winds with low sun do not show systematic gains.
- No evidence for a monotonic or threshold wind effect; rather, wind’s association with daily roost change is conditional on sun exposure.

Reconciliation with 30‑minute analysis
- Existing 30‑minute lag analysis in the thesis: wind variables are not predictive of immediate (t vs t−30 min) abundance change; no 2 m/s threshold effect (see `masters-thesis/chapters/vsfb/results.tex:78` and :91 guidance).
- Daily dynamic-window results refine this: still no threshold, but wind can matter **conditionally** when aggregated over biologically aligned windows spanning overnight through sunset.

---

## Figures and Tables to Add

Primary figure (recommended for main text)
- Title: “Wind × Sun Interaction Effects on Daily Roost Change Across Window Types”.
- File: `masters-analysis/analysis/dynamic_window_analysis/figures/window_comparison_interaction.png`.
- Caption guidance: “Partial effect surface from GAMMs of the square‑root transformed daily change in maximum cluster size. Positive values = aggregation gains; negative = losses. Gray areas denote regions without data support. Both window definitions select `ti(wind_max_gust, sum_butterflies_direct_sun)` as the best interaction.”

Optional supporting figures
- Window‑specific partials: `analysis/dynamic_window_analysis/figures/sunset_partial_effects.png`, `.../figures/24hr_partial_effects.png`.
- Clean binned interaction (no contours): `analysis/dynamic_window_analysis/figures/gratia_binned_smooth.png` and `..._horizontal.png` (generated by `analysis/dynamic_window_analysis/compare_window_results_final.R:1`).

Tables
- Model comparisons: `analysis/dynamic_window_analysis/model_comparison_comprehensive.csv` (sunset) and `.../model_comparison_24hr.csv` (24‑hour). Include AICc, ΔAICc, AICc weights, df, df/n, and overfitting risk notes.

---

## Suggested Thesis Text (LLM Cues)

Methods paragraph (Dynamic Window Analysis; insert after 30‑minute analysis)
> To test whether day‑to‑day roost changes depend on weather exposure aligned to roosting decisions, we constructed **dynamic weather windows** starting at the previous day’s maximum butterfly count and ending either at the next day’s last observation (functional sunset) or exactly 24 hours later. Within each window we computed 24/7 temperature and wind metrics and daylight‑only sun exposure defined as the cumulative number of butterflies labeled in direct sun across all images. We modeled the signed square‑root difference in daily maximum count using generalized additive mixed models with deployment random intercepts and AR(1) within‑deployment correlation. We compared 76 candidate models spanning null, additive, interaction‑only, and complex formulations, selecting by AICc with df/n overfitting checks and leave‑one‑deployment‑out cross‑validation. Analyses were restricted to observations with ≥95% metrics completeness.

Results paragraph (Dynamic Window Analysis; insert after 30‑minute results)
> Across both window definitions, the best‑supported model included a smooth interaction between maximum wind gust and cumulative direct‑sun exposure, with the same functional form selected in both analyses. The interaction surface indicates aggregation gains under **moderate sun exposure** and **moderate winds (~5–10 m/s)** and limited support for effects at very low or very high sun exposure. No model including a fixed 2 m/s disruption threshold was competitive. These daily‑scale results refine the 30‑minute analysis by showing that wind’s association with roost change is **conditional on sun exposure**, rather than monotonic or threshold‑based.

Key numbers to report
- Sunset window (n = 96): `ti(wind_max_gust, sum_butterflies_direct_sun)` edf ≈ 6.68; F ≈ 4.10; p ≈ 0.0008; adj. R² ≈ 0.397.
- 24‑hour window (n = 94): `ti(wind_max_gust, sum_butterflies_direct_sun)` edf ≈ 3.54; F ≈ 3.59; p ≈ 0.020; adj. R² ≈ 0.232.

Interpretation cue
- Emphasize the absence of a 2 m/s disruptive threshold at any scale tested; daily roost dynamics are best captured by a **wind × sun** interaction.

---

## Reproducibility

Data preparation
- Run `python masters-analysis/data_prep_dynamic_windows.py` to regenerate `monarch_daily_lag_analysis_24hr_window.csv` and `..._sunset_window.csv`.

Analysis
- Notebooks: `analysis/dynamic_window_analysis/sunset_window_gam_analysis.qmd`, `.../24hr_window_gam_analysis.qmd`, and synthesis `.../dynamic_window_gam_synthesis.qmd`.
- Figures: produced within the above QMDs and `analysis/dynamic_window_analysis/compare_window_results_final.R`.

---

## Caveats

- Sample sizes are modest (n ≈ 94–96 lag pairs); AICc, df/n checks, and LODOCV were used to mitigate overfitting.
- `sum_butterflies_direct_sun` is a cumulative count across frames; it integrates both exposure and instantaneous abundance, not minutes-in-sun per se.
- Gray regions in interaction plots indicate parameter space with little/no data; avoid interpreting outside supported regions.

---

## Open Decisions for Manuscript Assembly

1) Report both windows in the main text (recommended: lead with sunset; include 24‑hour as sensitivity) or move one to supplement while noting convergence.
2) Preferred interaction figure style: contour vs. clean binned surfaces (both are available).
3) File placement of new figures in the thesis repo (e.g., copy from `masters-analysis/analysis/dynamic_window_analysis/figures/` to `masters-thesis/figures/results/`).

