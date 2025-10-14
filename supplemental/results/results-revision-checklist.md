# Results Section Revision Checklist

**Purpose**: Systematic revision guide based on feedback from Francis and Jenn on the results section. Work through these items one at a time to maintain focus and avoid context overload.

**Status Key**:

- [ ] Not started
- [x] Completed
- [~] In progress

---

## PHASE 1: CRITICAL CONCEPTUAL FIXES

These address the most fundamental issues with the results section structure and logic.

---

### Task 1.1: Address the Wind Variable Paradox

**Priority**: CRITICAL
**Status**: [x]

**Issue**: Jenn pointed out that the best AIC models (M23) don't include wind terms, yet wind is your primary hypothesis. This creates a tension between "what predicts roost abandonment?" (model selection question) vs. "does wind affect roost abandonment?" (hypothesis testing question).

**Context from Comments**:

- Jenn (comment #34-35): "Since your hypothesis is about wind, it's odd that these models don't have wind in them. I don't know how to reconcile a model with a better AIC score against a model that explicitly tests your hypothesis."
- Note: Jenn made these comments BEFORE seeing the bivariate scatter plots, which satisfied her concerns about the lack of simple wind relationship

**What to Do**:

1. Add a clear statement in the Model Selection section acknowledging this tension
2. Explain that the bivariate analysis (Figures 1-2) already demonstrated wind alone has no predictive power
3. Frame M50's inclusion of the wind×sun interaction as testing your conditional hypothesis: wind effects depend on solar exposure context
4. Consider language like: "Model M50 was selected over the simpler M23 despite similar AIC scores (ΔAIC = 3.8) because it explicitly tests our hypothesis that wind effects are conditional on solar exposure, which the bivariate analyses suggested was necessary"

**Location in Text**:

- Wind Disruption Analysis → Model Selection subsection
- Table with model comparison (M50 vs M23)

**References to Update**:

- The paragraph introducing M50 as the best-fit model
- Any discussion of why interaction terms matter

---

### Task 1.2: Add Explicit Section Labels and Repeated Reminders

**Priority**: CRITICAL
**Status**: [x]

**Issue**: Francis emphasized multiple times that readers will "get lost in the weeds" and that the document is vulnerable to being quoted out of context. Need to repeatedly remind readers which analysis section they're in.

**Context from Comments**:

- Francis (comment #30): "I suggest that within this section, you repeatedly remind the reader that they are in the wind disruption, 30 minute interval portion of the analysis. This is in part to actually provide the reader with a reminder. But it is also important to put it in to key places so that you cannot be quoted out of context."
- Francis (comment #72): "I think the answer is to keep reminding the reader as to what section they are in. Just keep using the name of the analysis."

**What to Do**:

1. At the start of subsections, add clear labels: "In the 30-minute wind disruption analysis..."
2. When referring back to findings, use full context: "The 30-minute responsive change analysis showed..."
3. When transitioning between analyses, explicitly name both: "Unlike the 30-minute analysis, the day-to-day site fidelity analysis..."
4. Add these reminders in key interpretive paragraphs, not just section headers

**Locations to Update**:

- Start of "Model Selection" subsection
- Start of "Analysis of Best Fit Model"
- Throughout the interpretation of M50 results
- In the partial effects discussion
- When discussing the tensor interaction
- In the threshold sensitivity analysis introduction
- When comparing 30-min vs day-to-day results

**Example Wording**:

- "In the 30-minute wind disruption analysis, model selection via AIC..."
- "The tensor interaction in the responsive change analysis revealed..."
- "Statistical significance in the 30-minute interval model does not..."

---

### Task 1.3: Add Substantial Transition Between Analyses

**Priority**: CRITICAL
**Status**: [x]

**Issue**: The jump from 30-minute analysis to Site Fidelity Analysis is too abrupt. Readers need to understand WHY you're conducting a second analysis and how it differs conceptually from the first.

**Context from Comments**:

- Francis (comment #72): "I think you need a really clear and substantial transition here. I found it pretty easy to get lost in the weeds in the section above... when you move to a totally different hypothesis test, the reader should be reminded of why the additional hypothesis is needed, and that you are moving to that additional hypothesis test here."
- Francis provided suggested language: "In the preceding section, we examine how monarchs respond to immediate environmental conditions. But here we acknowledge that monarchs may not be able to respond immediately to conditions. For example, if a weather variable were to have an impact when temperature was too low for flight, a monarch might respond but only at the next available opportunity."

**What to Do**:

1. Add a full transitional paragraph at the start of "Site Fidelity Analysis" section
2. Explain the limitation of the 30-minute analysis (assumes immediate response)
3. Explain why day-to-day analysis addresses this limitation (delayed response opportunity)
4. Clarify what "site fidelity" means and why changes in abundance indicate presence/absence of fidelity
5. Link site fidelity explicitly to habitat suitability

**Suggested Structure**:

```
The 30-minute wind disruption analysis examined how monarchs respond to immediate environmental conditions. However, this approach assumes butterflies can respond instantaneously to unfavorable conditions. If adverse conditions occur when temperatures are too low for flight, monarchs may be unable to respond until the next available flight opportunity.

To test whether cumulative weather exposure influenced day-to-day roost dynamics and site fidelity, we analyzed... [continue with existing text]

[Add sentence]: Changes in abundance from day to day indicate butterflies abandoning or remaining at roost sites, with site fidelity serving as a proxy for habitat suitability under varying environmental conditions.
```

**Location in Text**:

- At the very start of "Site Fidelity Analysis" section
- Before the paragraph beginning "To test whether cumulative weather exposure..."

---

### Task 1.4: Rename "Sensitivity Analysis" Sections

**Priority**: HIGH
**Status**: [x]

**Issue**: "Sensitivity analysis" has a specific statistical meaning (testing which variables contribute most to effects), which is not what you're doing. Francis suggests alternative names.

**Context from Comments**:

- Francis (comment #58): "Sensitivity Analysis has a specific meaning in statistics. It is a method by which the partial effect of variables is addressed in order to determine which one has the largest contribution to the effect. I would suggest calling this the **Threshold Wind Disruption Analysis**."
- Francis (comment #106): "please change to something like 'robustness of analysis'"

**What to Do**:

1. Rename the 30-minute threshold section to "Threshold Wind Disruption Analysis"
2. Rename the 24-hour section to "Robustness Analysis: 24-Hour Butterfly Change"
3. Update any cross-references to these sections throughout the document
4. Update the justification text in the threshold section to clarify you're testing whether wind acts as a binary threshold vs. continuous variable

**Locations to Update**:

- Section header for threshold analysis (currently "Sensitivity Analysis")
- Section header for 24-hour analysis (currently "Sensitivity Analysis: 24-Hour Butterfly Change")
- Any references to these sections in text
- Table captions referring to "threshold analysis" or "24hr analysis"

**Example Justification Language** (for threshold section):
"We conducted this threshold analysis to determine whether wind is best characterized as a continuous variable or a binary disruption threshold, regardless of whether it operates independently or conditionally on other factors."

---

## PHASE 2: CLARIFICATION AND DEFINITIONS

These address confusion about variables, terms, and concepts.

---

### Task 2.1: Clarify "Time Since Sunrise" Variable

**Priority**: HIGH
**Status**: [x]

**Issue**: Multiple reviewers confused about what this variable represents. Is it time of day? Duration of observations? Something else?

**Context from Comments**:

- Jenn (comment #39-40): "do you mean time of day? or is this recording some other action like count, post sunrise."

**What to Do**:

1. First mention of "time since sunrise" needs a parenthetical definition
2. Clarify whether this is: (a) elapsed time since sunrise that morning, (b) time of day coded as hours since sunrise, or (c) something else
3. Explain why this variable matters (captures diurnal patterns? thermal accumulation?)
4. If it's essentially "time of day," consider whether that's clearer terminology

**Locations to Update**:

- First mention in Model Selection section: "smooth terms for... time since sunrise"
- First mention in Analysis of Best Fit Model: "time since sunrise"
- Figure 1.1 caption (partial effects plot)
- Table 1.2 (basis dimension checks)

**Example Clarification**:
"time since sunrise (hours elapsed since sunrise that morning, capturing diurnal activity patterns)"

---

### Task 2.2: Explain "Butterflies in Direct Sun" Calculation

**Priority**: HIGH
**Status**: [ ]

**Issue**: Jenn confused about how the average is only 17 individuals across 600+ observations of direct sunlight.

**Context from Comments**:

- Jenn (comment #21): "I don't really understand how it's only 17 across 600 observations."

**What to Do**:

1. Clarify that this is CONDITIONAL on sunlight being present (not averaged across all 1,894 observations)
2. Explain whether this is: (a) number of butterflies in sun per observation when sun present, or (b) cumulative butterfly-observations in sun
3. Consider adding more detail to descriptive statistics for this variable
4. The later text mentions "most observations occurred at low butterfly counts in direct sun" - make this clearer upfront

**Location in Text**:

- Descriptive Statistics section, paragraph about solar exposure
- Consider revising: "Direct solar exposure occurred in 31.7% of observations (n = 601), with butterflies actively basking when present in sunlight. When direct sunlight was available, an average of 17.0 individual butterflies occupied sunlit positions (range: 1-295), though most observations recorded very few butterflies in direct sun."

---

### Task 2.3: Explain Why "Butterflies in Direct Sun" Not as Main Effect

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: Jenn questions why this variable only appears in interaction terms, not as a standalone predictor.

**Context from Comments**:

- Jenn (comment #42): "but not the direct sunlight variable alone?"
- Jenn (comment #41): "Why isn't wind speed in the model by itself? why only as an interaction term?"

**What to Do**:

1. Check model M23 (second-best model) - does it include butterflies in direct sun as a main effect?
2. If yes, note that AIC selected M50 (with interaction) over M23 (with main effect), suggesting interaction form is better
3. Add explanation that model selection process tested both main effects and interactions
4. Clarify that the interaction term implicitly includes the main effects (tensor smooths can capture both)

**Location in Text**:

- In the Model Selection discussion
- Possibly in a footnote or parenthetical when first introducing the interaction term

**Example Language**:
"Model selection tested both additive effects (M23: wind and sunlight as separate predictors) and interactive effects (M50: wind×sunlight interaction). The tensor smooth interaction in M50 can capture both main effects and their interaction, and was selected over the additive form despite similar AIC values (ΔAIC = 3.8)."

---

### Task 2.4: Improve "Partial Effects" Explanations in Captions

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: Not all readers will understand what "partial effects" means in a statistical context. Need clearer caption language.

**Context from Comments**:

- Francis (comment #45): "Not all readers will be able to interpret a partial effect. Consider a revision to the caption..."
- Francis (comment #97): "Same comment about partial effect"

**What to Do**:

1. Revise figure captions to explain partial effects in plain language
2. Consider: "Partial effects show the relationship between each predictor and butterfly abundance change while holding all other variables constant at their means"
3. Or simpler: "Effects of individual environmental factors on butterfly abundance, isolated from other variables"
4. Apply consistently to all partial effects figures

**Locations to Update**:

- Figure 1.1 caption (30-minute partial effects)
- Figure 1.6 caption (day-to-day partial effects)
- Consider adding a brief explanation in text the first time "partial effects" appears

**Suggested Revised Caption**:
"Partial effects of environmental predictors on monarch butterfly abundance changes from the best-fit GAMM model (M50). Partial effects isolate the relationship between each predictor and the response while holding other variables constant. Shaded regions represent 95% confidence intervals."

---

### Task 2.5: Add Figure Numbers to All Captions

**Priority**: LOW (per Kyle - export artifact)
**Status**: [ ]

**Issue**: Text references figures by number but some captions lack numbers.

**Context from Comments**:

- Francis (comment #46): "there is a reference to this figure with a figure number in the text. But the caption below the figure does not have a reference number associated with it"

**Note from Kyle**: This is an artifact of how the document was exported and shouldn't be a concern for the markdown files.

**What to Do**:

- Verify that figure numbers are present in the actual markdown source files
- If this is just an export issue, no action needed
- If numbers are actually missing in source, add them consistently

---

### Task 2.6: Make Variable Names More Descriptive in Tables

**Priority**: LOW
**Status**: [ ]

**Issue**: Even if variable names match your code, they can be more reader-friendly in tables.

**Context from Comments**:

- Jenn (comment #36): "even if these are your variable names, you can call them whatever you want here to make it clear what the variable is. Just FYI. Maybe no action"

**What to Do**:

1. Review all model selection tables
2. Consider making terms more descriptive:
   - "Previous butterfly count" → "Butterfly abundance at previous observation"
   - "Time since sunrise" → "Time elapsed since sunrise (hours)"
   - "Butterflies in direct sun" → "Number of butterflies in direct sunlight"
3. This is lower priority but improves readability

**Locations**:

- Table of top 5 models (30-minute analysis)
- Table of top 5 models (sunset analysis)
- Table of top 5 models (threshold analysis)
- Table of top 5 models (24-hour analysis)

---

## PHASE 3: STATISTICAL REFINEMENTS

These address technical statistical issues and rigor.

---

### Task 3.1: Add Regression Statistics to Bivariate Plots

**Priority**: HIGH
**Status**: [ ]

**Issue**: Francis suggests testing whether slopes differ significantly from zero. Jenn wanted regression lines removed from plots because they were non-significant but looked misleading.

**Context**:

- Francis (comment #26): "Instead of just an R squared, you could do a regression to see if the slope is significantly different from zero. A slope of zero is the null for a regression"
- Kyle's feedback: Jenn saw scatter plots and was satisfied; wanted regression line OFF because non-significant but visually trending. Francis hasn't seen this iteration. Both regressions had p > 0.05, sunset analysis "just barely so"

**What to Do**:

1. Keep plots without regression lines (respects Jenn's concern about visual misleadingness)
2. Add regression statistics to the text for statistical rigor
3. For 30-minute analysis: "Linear regression confirmed no significant relationship between wind speed and cluster size changes (β = [slope], SE = [SE], p = [p-value], n = 1,894)"
4. For sunset analysis: Report transparently even if close to significance (e.g., "β = [slope], SE = [SE], p = 0.06, n = 96")

**Locations to Update**:

- Text accompanying Figure 1 (30-minute bivariate)
- Text accompanying Figure 2 (sunset bivariate)

**Action Items**:

- [ ] Get actual regression statistics for both analyses
- [ ] Add statistics to text near current r-values
- [ ] Keep plots without regression lines

---

### Task 3.2: Standardize Test Statistics in Tables

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: Mixing F-statistics in some tables and t-statistics in others creates inconsistency.

**Context from Comments**:

- Francis (comment #90): "a little goofy that you have Ts here and Fs in the table"

**What to Do**:

1. Check Table 1.1 (M50 summary) - uses F-statistics for all smooth terms
2. Check Table 1.5 (M32 summary) - uses t-statistics for linear terms, F for smooth interaction
3. This is actually correct (linear terms get t-tests, smooth terms get F-tests), but consider adding a note to clarify
4. Alternative: Report both consistently as F-statistics if possible (t² = F for df=1)

**Locations**:

- Table 1.1 (30-minute analysis)
- Table 1.5 (day-to-day analysis)

**Suggested Addition to Caption**:
"Linear terms are tested using t-statistics; smooth terms use F-statistics."

---

### Task 3.3: Add Citations for Statistical Claims

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: Claims about what's "acceptable" for residuals need supporting references.

**Context from Comments**:

- Francis (comment #52): "This needs a reference. Otherwise, it just sounds like an opinion."
- Francis (comment #102): "please provide a reference"

**What to Do**:

1. Find references supporting that minor tail deviations in QQ plots are acceptable for ecological data
2. Find references about sample size and robustness of GAM diagnostics
3. Add citations to both diagnostic interpretation paragraphs

**Locations Needing Citations**:

- Model Diagnostics subsection (30-minute analysis): "acceptable given the large sample size and complexity of ecological data"
- Model Diagnostics subsection (sunset analysis): "acceptable given the sample size and complexity of ecological data"

**Suggested References to Find**:

- Wood 2017 (GAMs book) on diagnostic interpretation
- Zuur et al. on mixed effects models and diagnostics
- Papers discussing robustness of GAMMs to assumption violations

---

## PHASE 4: INTERPRETATION AND BIOLOGICAL CONTEXT

These address how results are interpreted and contextualized.

---

### Task 4.1: Interpret Interaction Plot with Closed System Assumption

**Priority**: HIGH
**Status**: [ ]

**Issue**: Francis wants explicit interpretation of what the red vs. blue regions mean for butterfly movement patterns.

**Context from Comments**:

- Francis (comment #99): "I think you need one sentence regarding interpretation. Important to know that this is somewhat of a closed system. It is possible some monarchs are leaving entirely, and possible that some monarchs are entering this cluster area. If you assume it is a closed system then they are moving from the blue part of the figure to the red part. Please make some kind of statement along those lines. Please don't leave the reader to come up with their own interpretation."

**What to Do**:

1. Add 1-2 sentences after describing the Figure 1.7 (sunset interaction plot) patterns
2. Acknowledge the system may not be fully closed (some emigration/immigration possible)
3. Explain that within the study area, blue regions (decreases) and red regions (increases) suggest movement between deployment locations
4. Link to site fidelity and habitat suitability concept

**Location in Text**:

- After describing the interaction plot patterns in Site Fidelity Analysis
- Before the cautionary statements about interpolation boundaries

**Suggested Language**:
"While some monarchs may leave or enter the study area entirely, observed patterns suggest redistribution of butterflies among deployment locations within the study sites. Under conditions associated with cluster size decreases (blue regions), butterflies are likely relocating to microsites with more favorable environmental conditions (red regions), demonstrating selective site fidelity based on local weather exposure."

---

### Task 4.2: Emphasize "Mostly Shaded Observations" Finding

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: The fact that most observations occurred with very few butterflies in direct sun is mentioned but not emphasized as an important biological finding.

**Context from Text**:

- Multiple mentions: "the overwhelming majority of observations occurred at very low butterfly counts in direct sun"
- This appears to be an important behavioral pattern worth highlighting

**What to Do**:

1. In the Descriptive Statistics section, make this more prominent
2. Add a sentence interpreting what this means biologically (preference for shaded positions?)
3. Reference this when discussing why interaction plots show most data at low sun exposure
4. Consider whether this deserves mention in Discussion section

**Locations to Update**:

- Descriptive Statistics section (when first introducing butterflies in direct sun)
- When interpreting Figure 1.2 (30-minute interaction plot)
- When interpreting Figure 1.7 (sunset interaction plot)

**Suggested Addition**:
"The distribution of observations reveals a strong behavioral pattern: monarchs predominantly occupied shaded positions during the monitoring period, with most observations recording fewer than 25 butterflies in direct sunlight. This suggests that direct solar exposure, while important for thermoregulation, represents a relatively infrequent microhabitat choice during winter conditions."

---

### Task 4.3: Clarify "Time Since Sunrise" Biological Meaning

**Priority**: MEDIUM
**Status**: [x]

**Issue**: After defining what the variable is (Task 2.1), need to explain why it matters biologically.

**What to Do**:

1. When interpreting the time since sunrise partial effect (Figure 1.1)
2. Explain what the diurnal pattern means: "morning departures and afternoon returns"
3. Link to thermal constraints, foraging behavior, or other biological mechanisms
4. This helps readers understand why it's in the model

**Location**:

- When describing Figure 1.1 partial effects
- In the interpretation of model results

**Current Text**:
"Time since sunrise captured a significant diurnal pattern (p < 0.001) with morning departures and afternoon returns."

**Suggested Enhancement**:
"Time since sunrise captured a significant diurnal pattern (p < 0.001) with morning departures and afternoon returns, consistent with monarchs leaving clusters during morning warming periods for foraging or repositioning, then returning to established roost sites as temperatures cool in late afternoon."

---

### Task 4.4: Add Interpretation of Adjusted R² Difference

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: The day-to-day analysis has much higher R² (0.397) than 30-minute analysis (0.064), but this isn't interpreted clearly.

**Context from Text**:

- "representing substantially greater explanatory power than the 30-minute responsive change analysis"
- Francis added suggested reference text: "(adjusted R2 of 0.061 to 0.064)"

**What to Do**:

1. Use Francis's suggested text to make the comparison explicit
2. Add interpretation of what this means biologically
3. Explain why cumulative effects over days might be more predictable than 30-minute changes

**Location**:

- In the Site Fidelity Analysis section, when reporting M32 model performance
- After the sentence about "substantially greater explanatory power"

**Suggested Addition**:
"...representing substantially greater explanatory power than the 30-minute responsive change analysis (adjusted R² = 0.064). This suggests that cumulative weather exposure over day-long periods is more strongly associated with roosting decisions than immediate short-term conditions, supporting the hypothesis that monarchs integrate environmental conditions over extended time periods when making site fidelity decisions."

---

## PHASE 5: DATA PRESENTATION AND FIGURES

These address how data is presented visually and in tables.

---

### Task 5.1: Add Caution About Interpolation Artifacts

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: Need to emphasize caution about strong partial effects at data distribution edges where observations are sparse.

**Context from Text**:

- Currently mentions "gray regions mask areas too distant from observed data points"
- Need to add stronger cautionary language about edge effects

**What to Do**:

1. Add caution statement when first introducing tensor interaction plots
2. Emphasize that strongest effects at distribution edges may be interpolation artifacts
3. Apply this consistently to all interaction plot interpretations

**Locations**:

- Figure 1.2 description (30-minute interaction)
- Figure 1.5 description (threshold interaction)
- Figure 1.7 description (sunset interaction)
- Figure 1.10 description (24-hour interaction)

**Suggested Addition** (example for Figure 1.2):
"Caution is warranted when interpreting the strongest partial effects at the edges of the data distribution, where observations are sparse and interpolation artifacts may occur. Gray regions mask areas too distant from observed data points for reliable interpretation."

---

### Task 5.2: Enhance Table Readability

**Priority**: LOW
**Status**: [ ]

**Issue**: Tables could be more reader-friendly with minor formatting improvements.

**What to Do**:

1. Consider adding thousand separators to large numbers (8074.03 → 8,074.03)
2. Ensure consistent decimal places across similar measures
3. Consider bolding the best-fit model row in selection tables
4. Add notes explaining abbreviations (edf, Ref.df) in table footnotes

**Locations**:

- All model selection tables
- All model summary tables
- Basis dimension check tables

---

### Task 5.3: Verify Gray Masking on All Interaction Plots

**Priority**: MEDIUM
**Status**: [ ]

**Issue**: Need to ensure gray regions consistently mask unreliable interpolation areas on all tensor interaction plots.

**What to Do**:

1. Check that gray masking appears on all four interaction plots
2. Verify masking is consistent with data distribution (black points)
3. Ensure caption language about gray regions is consistent across figures

**Locations**:

- Figure 1.2 (30-minute wind×sun interaction)
- Figure 1.5 (threshold interaction)
- Figure 1.7 (sunset wind×sun interaction)
- Figure 1.10 (24-hour interaction)

---

## PHASE 6: CROSS-CUTTING ISSUES

These span multiple sections.

---

### Task 6.1: Remove Em Dashes Throughout

**Priority**: LOW
**Status**: [ ]

**Issue**: CLAUDE.md specifies "Never use em dashes"

**What to Do**:

1. Search for all em dashes (—) in the results section
2. Replace with alternative punctuation:
   - Use commas for parenthetical phrases
   - Use colons for explanatory clauses
   - Use periods to break into separate sentences
   - Use semicolons for related independent clauses

**Note**: This is more of a final polish item

---

### Task 6.2: Consistent Terminology for Analyses

**Priority**: HIGH
**Status**: [ ]

**Issue**: Need consistent names for the two main analyses throughout the document.

**What to Do**:

1. Choose official names:
   - Option A: "30-minute wind disruption analysis" and "day-to-day site fidelity analysis"
   - Option B: "responsive change analysis" and "site fidelity analysis"
   - Option C: "short-term wind disruption analysis" and "cumulative weather exposure analysis"
2. Use these names consistently everywhere
3. Update all cross-references
4. Consider whether these names should appear in section headers

**Decision Needed**: Which naming convention do you prefer?

---

### Task 6.3: Verify All P-values and Statistics

**Priority**: HIGH
**Status**: [ ]

**Issue**: Need to ensure all reported statistics are accurate and consistently formatted.

**What to Do**:

1. Check p-value formatting (< 0.001 vs = 0.057 vs 0.001)
2. Verify all test statistics match source output
3. Ensure consistent significant figures across similar measures
4. Check that degrees of freedom are reported where appropriate

**This likely requires cross-checking with R output files**

---

## SUMMARY OF PRIORITIES

**Must Do Before Next Review**:

1. Task 1.1 - Address wind variable paradox
2. Task 1.2 - Add repeated section reminders
3. Task 1.3 - Add substantial transition between analyses
4. Task 1.4 - Rename sensitivity analyses
5. Task 3.1 - Add regression statistics to bivariate plots
6. Task 4.1 - Interpret interaction plot with closed system assumption

**Should Do for Clarity**:
7. Task 2.1 - Clarify "time since sunrise"
8. Task 2.2 - Explain "butterflies in direct sun"
9. Task 2.4 - Improve partial effects captions
10. Task 4.2 - Emphasize "mostly shaded" finding

**Nice to Have**:
11. Task 2.3 - Explain why no main effects for sun/wind
12. Task 3.2 - Standardize test statistics
13. Task 3.3 - Add citations for statistical claims
14. Task 5.1 - Add interpolation caution

**Final Polish**:
15. Task 6.1 - Remove em dashes
16. Task 6.2 - Consistent terminology throughout

---

## NOTES FOR NEXT SESSIONS

- Francis is unaware of the bivariate scatter plot discussions with Jenn
- Jenn was satisfied with scatter plots showing no relationship
- Regression lines were removed because non-significant but visually misleading
- Need actual regression statistics (both p > 0.05, sunset "just barely")
- Figure numbering issues are export artifacts, not source file issues
- Work through these one at a time to avoid context overload
