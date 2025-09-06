Of course. I've added a note on how to refer to your models in your writing. Here is the updated and finalized blueprint.

***

# # Blueprint for Thesis Results Section

## ## Writing Style Notes ✍️

* **Referring to Models**: In your main written paragraphs, use **descriptive phrases** rather than model code names for clarity. For example, instead of saying "`M22_temp_time` was the best model," write "The best-fit model was one that included smooth terms for temperature, sun exposure, and diurnal patterns."
* **Use Code Names as Labels**: Use your model code names (`M22_temp_time`, `M1_gust`, etc.) as **labels or identifiers** when you need to refer to a specific entry in a table (e.g., "see Table 1, `M22_temp_time`"). This keeps your writing clean and your tables unambiguous.

---

## ## Summary of Data and Model Selection

This section provides a high-level overview of the analysis, culminating in the selection of the best model.

* Start with a summary sentence stating the scope of the data used for the final analysis.
  * Include the final number of analyzable observation pairs: **1,894**.
  * Mention these were collected across **115 unique deployment-day combinations**.
* Introduce the modeling approach.
  * State that you used a **Generalized Additive Mixed Model (GAMM)** framework to test 47 candidate models.
  * Mention that model selection was performed using an **information-theoretic approach (Akaike Information Criterion, AIC)**.
* Present the primary model selection results.
  * Directly state that the best-fit model was **`M22_temp_time`**.
  * Provide its key AIC metrics:
    * **AIC Value**: 8081.848.
    * **Delta AIC**: 0.000.
    * **AIC Weight**: 0.88, indicating it carries 88% of the support among all candidate models.
  * Emphasize its superiority by comparing it to the next-best model (`M21_time_of_day`), which had a substantially higher **Delta AIC of 4.796**.
  * *Instruction: Insert a condensed version of the AIC comparison table here, showing the top 5-10 models and their AIC, Delta AIC, and AIC Weight values*.

---

## ## Analysis of the Best-Fit Model (`M22_temp_time`)

This section unpacks the winning model to show *what* factors drive monarch movement.

* State the model's structure and overall fit.
  * Provide the full formula for the best-fit model:
        `butterfly_difference_cbrt ~ s(total_butterflies_t_lag) + s(temperature_avg) + s(butterflies_direct_sun_t_lag) + s(time_within_day_t)`
  * Report the model's **adjusted R-squared value of 0.0568**.
* Detail the significant smooth terms.
  * *Instruction: Insert the summary table for the smooth terms from your model output (similar to the table on page 14 of the PDF)*.
  * For each predictor, describe the relationship found, citing the statistics and referencing its partial effect plot.
    * **Previous Butterfly Count (`s(total_butterflies_t_lag)`)**: A significant, non-linear negative relationship was found (edf = 2.621, F = 12.020, p = 8.26e-07). As the initial number of butterflies in the roost increased, the change in abundance became more negative. *(Reference your partial effect plot, e.g., Figure X)*.
    * **Average Temperature (`s(temperature_avg)`)**: A significant, non-linear relationship was observed (edf = 3.930, F = 3.230, p = 0.0283). The effect on monarch movement was positive, peaking at approximately 20°C before declining. *(Reference your partial effect plot, e.g., Figure Y)*.
    * **Butterflies in Direct Sun (`s(butterflies_direct_sun_t_lag)`)**: A significant negative relationship was found (edf = 1.534, F = 19.356, p = 1.22e-05). A greater number of butterflies in direct sun was associated with a larger decrease in total roost abundance. *(Reference your partial effect plot, e.g., Figure Z)*.
    * **Time Within Day (`s(time_within_day_t)`)**: A significant, non-linear diurnal pattern was detected (edf = 4.898, F = 8.901, p < 2e-16), showing cyclical changes in abundance throughout the day. *(Reference your partial effect plot, e.g., Figure A)*.

---

## ## Evaluation of the "Disruptive Wind Hypothesis"

This section directly addresses your primary hypotheses using the model results. It should explicitly state whether each hypothesis was supported or rejected.

* **Hypothesis 1: Wind acts as a disruptive force.**
  * This hypothesis was **not supported**. The AIC model selection process did not select any wind variable in the top-performing models, indicating wind was not a primary driver of monarch abundance change.
* **Hypothesis 3: Wind's disruptive effects scale with intensity.**
  * This hypothesis was **not supported**. The `max_gust` predictor, which measures wind intensity, was not selected in any top model.
* **Hypothesis 2: Wind becomes disruptive above a 2 m/s threshold.**
  * This hypothesis was **not supported**. A parallel sensitivity analysis using a specific threshold predictor (`minutes with wind speed > 2 m/s`) was conducted, and this variable also failed to appear in any top models.
  * Mention that the two wind metrics (`max_gust` and `minutes_above_threshold`) were highly correlated (r = 0.78).
* Provide visual evidence to corroborate these findings.
  * *Instruction: Insert the simple scatter plot of `max_gust` vs. `butterfly_difference_cbrt` (from `image_cdbb1a.png`). Describe its key features: the flat trend line and the confidence interval encompassing zero, which visually confirm the lack of a meaningful relationship.*

---

## ## Model Diagnostics

This final section reports on the model's adherence to statistical assumptions and acknowledges limitations apparent in the results.

* Report on the residuals.
  * *Instruction: Reference your **Residuals vs. Fitted Values plot** (from page 21 of the PDF)*.
  * Explicitly describe the **visible linear banding/patterning** in the residuals. State that this indicates unexplained structure that is an artifact of the discrete nature of the response variable, which arises from the binned counting method.
* Report on normality.
  * *Instruction: Reference your **Normal Q-Q Plot** (from page 22 of the PDF)*.
  * Describe the plot as showing that the residuals are **approximately normally distributed but with some deviations in the tails**, a finding consistent with the patterns observed in the residuals vs. fitted plot.
