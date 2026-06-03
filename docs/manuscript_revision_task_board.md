# Manuscript revision task board

This board tracks the remaining work from the commented Word document.

Source Word document.

`/Users/kylenessen/Library/CloudStorage/OneDrive-CalPoly/Thesis/Manuscript/manuscript_20260409.docx`

Working LaTeX file.

`/Users/kylenessen/Documents/GitHub/masters-thesis/manuscript.tex`

Current working rule.

Treat the accepted text in the Word document as the current prose unless Kyle says otherwise. The Word document still has tracked changes enabled. It also has 61 comments, with 49 open or not marked resolved. The task IDs below cover those 49 comments.

Do not build the LaTeX document unless Kyle explicitly asks for a build or compile.

## Section Gates

Work should move through the sections in order. A later section should not begin until all tasks in the earlier section have been merged back to `main`.

Multiple sessions may work in parallel inside one section when their file edits are unlikely to overlap. Prefer one task per branch. Commit small and atomic changes.

Status values are `Open`, `In progress`, `Blocked`, and `Done`.

## Section 1. Baseline Word To LaTeX Sync

Complete this section before any analysis, figure, table, or final prose tasks. The goal is to make `manuscript.tex` match the current accepted Word prose as a baseline. Do not resolve scientific disagreements in this section unless the Word text already clearly resolves them.

### EDIT-001. Sync title, Simple Summary, abstract, and keywords

Status. Open.

Source comments. None directly. This task comes from the document comparison.

Likely files. `manuscript.tex`.

Context. The Word title differs from the LaTeX title. The Word Simple Summary is cleaner than the current LaTeX version. The Word abstract contains a current abstract and an `ALTERNATIVE ABSTRACT` block. The keywords differ slightly.

Done when. The LaTeX front matter matches the intended current Word text. If the agent cannot infer which abstract Kyle wants, ask Kyle before choosing. Do not leave the alternate abstract in the manuscript unless Kyle confirms it belongs there.

### EDIT-002. Sync the Introduction prose and citation intent

Status. Open.

Source comments. `1435262033`, `1861464571`.

Likely files. `manuscript.tex`, `bibliography/Thesis.bib`.

Context. The Word Introduction has newer wording around wind, butterfly thermoregulation, and the interaction of wind with temperature and insolation. Francis added references by Munro et al. 2019, Tsai et al. 2020, and Krishna et al. 2021. Jay also noted that the Introduction may need a more balanced setup if grove management plans already considered factors beyond wind.

Done when. The Introduction in LaTeX reflects the accepted Word prose, the new references are represented correctly in BibTeX if they are used, and any claim that wind dominated management is phrased carefully enough to allow prior work on canopy and light.

### EDIT-003. Sync Materials and Methods prose

Status. Open.

Source comments. `1824005225`, `473839288`, `1468403588`, `1806968990`, `1182007124`, `380024150`, `982577787`.

Likely files. `manuscript.tex`.

Context. The methods text in Word includes current phrasing for model framework, variable selection, threshold model setup, and model validation. Some comments require later statistical confirmation, but the accepted baseline prose should still be synced first.

Done when. The LaTeX Methods section matches the accepted Word text where the wording is clearly current. Any unresolved statistical questions should be marked in the task board or left for Section 2.

### EDIT-004. Sync Results prose as the baseline

Status. Open.

Source comments. `850189325`, `2050568483`, `249936144`, `774033147`, `1837771308`, `931591290`, `184831444`, `1470233068`, `542381207`.

Likely files. `manuscript.tex`.

Context. The Word Results text has newer wording around the simple regression bridge, model interpretation, Next Day Window results, and discussion-like interpretation. Some comments ask that interpretation move later. For Section 1, sync the current accepted text without doing the later restructure.

Done when. The Results section in LaTeX reflects the accepted Word prose. Interpretation that may need relocation is still traceable for Section 4.

### EDIT-005. Sync Discussion and Conclusions as the baseline

Status. Open.

Source comments. `556409408`, `1822051757`, `916610491`, `209493019`, `195942775`, `279432750`, `622324121`, `542124272`.

Likely files. `manuscript.tex`, `bibliography/Thesis.bib`.

Context. The Word Discussion includes newer thermoregulation framing, a new `Discerning Between Possible Hypotheses` heading, updated limitation language, and conservation language that may still need smoothing.

Done when. The LaTeX Discussion and Conclusions match the accepted Word baseline. Do not over-polish the conservation implications yet. That belongs in Section 4.

## Section 2. Statistical And Analysis Decisions

Begin only after Section 1 is merged. These tasks may require data, scripts, or Kyle decisions. If the agent cannot verify the statistical claim from local files, ask Kyle what source data or script should be used.

### EDIT-006. Audit and explain the 52 model candidate set

Status. Open.

Source comments. `473839288`, `1468403588`.

Likely files. `manuscript.tex`, analysis scripts or model output files if present.

Context. Jay was confused by the candidate model count. Francis asked Kyle to confirm. The Methods section says there are two frameworks, each with 24 models, plus additional models with interactions and smooth terms.

Done when. The candidate set count is verified against the analysis source. The manuscript explains the model set in a way that is clear to a reader. If the count or structure is wrong, correct the manuscript and note what changed.

### EDIT-007. Add or assess `K` and log likelihood in model selection tables

Status. Open.

Source comments. `2018412757`, `380024150`, `982577787`, `306246836`.

Likely files. `manuscript.tex`, analysis outputs.

Context. Jay recommended checking log likelihood when models differ by less than 2 AIC units and differ by one parameter. Francis agreed that Kyle should add a clause or sentence. Jay also suggested adding number of parameters and log likelihood to the relevant model tables.

Done when. The relevant model tables and text either include `K` and log likelihood, or the task records why those columns were not added. If close models need an interpretive note, add it in the Methods or Results where appropriate.

### EDIT-008. Decide how threshold models should be compared

Status. Open.

Source comments. `1806968990`, `1182007124`, `486357702`, `1861267912`.

Likely files. `manuscript.tex`, analysis outputs.

Context. Jay asked whether threshold models should compete directly with continuous models and whether additional thresholds such as 4 or 8 m/s should be tried. Francis noted that comparable data and model structure should make AIC comparisons reasonable, but this may still require analysis judgment.

Done when. The manuscript clearly states what comparison was made and why. If no reanalysis is done, the text should not imply more than the existing comparison supports.

### EDIT-009. Decide whether best-fit model p-values belong in an information theoretic analysis

Status. Open.

Source comments. `67036694`, `2097415894`.

Likely files. `manuscript.tex`, analysis outputs.

Context. Jay cautioned against mixing p-values with an information theoretic approach and suggested model-averaged parameter estimates and confidence intervals. Francis responded that the models are mainly being used to assess whether wind alone is a useful predictor, rather than to estimate all parameter values.

Done when. Kyle and the agent choose a consistent reporting framework. The manuscript should either justify the current best-fit reporting or revise toward model-averaged estimates. Do not make a silent statistical paradigm change.

### EDIT-010. Clarify the role of the simple linear regression bridge

Status. Open.

Source comments. `298285836`, `249936144`.

Likely files. `manuscript.tex`.

Context. Jay questioned the simple regression section because it may duplicate or conflict with the model selection framework. Francis explained that the simple analysis is intended as a bridge for readers and managers who think of the hypothesis in simple wind-only terms.

Done when. The Methods and Results make clear that the regression is a heuristic bridge, not the primary inference engine. It should not undermine the multi-model framework.

## Section 3. Figures And Tables

Begin only after Section 2 is merged unless the task is purely a caption or cross-reference audit. Regenerated figures should use the existing project style and source scripts where available.

### EDIT-011. Audit figure numbering, labels, and in-text citations

Status. Open.

Source comments. `1332224640`, `1657910628`.

Likely files. `manuscript.tex`.

Context. Peter noted that figures did not show `Figure` labels in Word and that Figure 1 needed to be cited in text. LaTeX already uses figure environments, captions, and labels, so part of this may be a Word conversion artifact.

Done when. Every figure is referenced in the text before or near its placement. The LaTeX source uses proper `figure`, `caption`, and `label` commands. Note if the Word issue is only a conversion artifact.

### EDIT-012. Decide whether Figures 2 and 3 should become a two-panel figure

Status. Open.

Source comments. `1300236268`, `918939383`.

Likely files. `manuscript.tex`, `figures/`, figure scripts if present.

Context. Peter suggested combining the 30-minute and Next Day Window wind scatterplots because they share axes and analytical framing. Francis agreed that this is a good suggestion.

Done when. The figures are either combined into a two-panel figure with an updated caption and labels, or the task records why separate figures were kept.

### EDIT-013. Add visible red 2 m/s threshold lines where captions claim they exist

Status. Open.

Source comments. `2021869295`, `1233138264`, `50837945`.

Likely files. `figures/`, figure scripts, `manuscript.tex`.

Context. Peter and Jay could not see the red dashed line in the wind by sun interaction figure. Francis asked whether the red line belongs in Results or the last paragraph of the next section. Visual inspection of the current figure confirms that the line is not visible.

Done when. Any figure caption that mentions a red dashed 2 m/s threshold line has a visible line in the figure, or the caption no longer claims a line is present. If adding the line changes interpretation, update the surrounding text.

### EDIT-014. Improve model table captions and table contents

Status. Open.

Source comments. `583917242`, `153769611`, `693642028`, `1906731719`, `184231791`, `306246836`.

Likely files. `manuscript.tex`.

Context. Jay asked for stand-alone table captions and definition of column headings such as `edf` and `Ref.df`. He also noted that a model description listed variables not visible in the table. Francis agreed with improving a table and noted one power-analysis prose/table decision.

Done when. Captions define key abbreviations and make each table understandable without hunting through the text. Tables show the variables claimed in nearby prose or the prose is corrected. Any decision to delete redundant prose around the power table is applied consistently.

### EDIT-015. Consider adding a wind-speed histogram for occupied clusters

Status. Open.

Source comments. `461713005`, `1261848065`.

Likely files. `figures/`, figure scripts, `manuscript.tex`.

Context. Jay suggested that one persuasive argument is the number of clusters observed above 2 m/s and that a histogram of measured wind speed at clusters would be useful.

Done when. The manuscript either includes a histogram or explains why existing figures already make the point. If a histogram is added, include source script updates and a caption.

### EDIT-016. Clarify temperature partial effect interpretation

Status. Open.

Source comments. `1125610476`, `110014176`.

Likely files. `manuscript.tex`.

Context. Jay asked for a short interpretation of the temperature panel because the pattern appears to rise beyond the flight threshold range and then drop. Francis agreed that this is a useful suggestion.

Done when. The Results or Discussion include a cautious interpretation of the temperature partial effect without overclaiming.

## Section 4. Prose Integration And Scientific Framing

Begin only after Sections 1 through 3 are merged. These tasks should harmonize interpretation after the tables and figures have settled.

### EDIT-017. Move interpretation out of Results where needed

Status. Open.

Source comments. `850189325`, `774033147`, `931591290`, `1837771308`, `184831444`.

Likely files. `manuscript.tex`.

Context. Peter flagged several Results statements as interpretive and suggested moving them to Discussion. Francis noted that some of this may already be present elsewhere.

Done when. Results paragraphs report findings without over-interpreting them. Discussion captures the interpretive material once, without duplication.

### EDIT-018. Integrate thermoregulation references and framing

Status. Open.

Source comments. `1435262033`, `916610491`, `209493019`.

Likely files. `manuscript.tex`, `bibliography/Thesis.bib`.

Context. Francis supplied Munro et al. 2019, Tsai et al. 2020, and Krishna et al. 2021 as examples for butterfly wing reflectance, heating, and optical properties. These references support the thermoregulation framing in the Introduction and Discussion.

Done when. The references are in BibTeX, cited in the manuscript where they support the argument, and formatted using `\cite{}`.

### EDIT-019. Make conservation language non-prescriptive

Status. Open.

Source comments. `556409408`.

Likely files. `manuscript.tex`.

Context. Peter flagged conservation implication language as too prescriptive. The manuscript should avoid telling managers exactly what they must do unless the evidence directly supports it.

Done when. Conservation recommendations are framed as evidence-informed implications, research directions, or management considerations rather than prescriptions.

### EDIT-020. Balance management history around wind, light, and canopy management

Status. Open.

Source comments. `1861464571`, `622324121`.

Likely files. `manuscript.tex`.

Context. Jay noted that the paper may imply wind protection fully dominated grove management, while examples in the Discussion show that canopy opening and light management have also been part of practice.

Done when. The Introduction and Discussion acknowledge prior canopy and light work while still preserving the paper's core claim that the 2 m/s wind disruption threshold lacked direct empirical testing.

### EDIT-021. Clarify or remove vague claims about limited suitable sites

Status. Open.

Source comments. `542124272`.

Likely files. `manuscript.tex`.

Context. Jay asked for a specific report or decision if the manuscript claims that the 2 m/s threshold led people to conclude that suitable sites were limited.

Done when. The claim is supported with a specific citation or softened to avoid overstatement.

### EDIT-022. Tighten limitations around wind dislodgement, density, wetness, and freezing

Status. Open.

Source comments. `279432750`, `195942775`.

Likely files. `manuscript.tex`, `bibliography/Thesis.bib` if citation cleanup is needed.

Context. Jay said a limitations paragraph may be too vague for Bureau approval. Francis later changed the paragraph. The accepted text should be checked for clarity, citation support, and restraint.

Done when. The limitation is specific, supported, and does not speculate beyond the evidence.

### EDIT-023. Review low variance explained language

Status. Open.

Source comments. `1470233068`, `542381207`.

Likely files. `manuscript.tex`.

Context. Jay and Peter reacted to the low adjusted `R^2` values. This may not require a change, but the manuscript should make clear what the low variance means for the argument.

Done when. The text acknowledges low variance explained without weakening the wind hypothesis test. If no change is needed, mark the task done with a note.

## Section 5. Final Harmonization

Begin only after Sections 1 through 4 are merged.

### EDIT-024. Final comment coverage audit

Status. Open.

Source comments. All open or unflagged comment IDs listed in this board.

Likely files. `docs/manuscript_revision_task_board.md`, `manuscript.tex`.

Context. The board was built from 49 open or unflagged comments. Some comments are advisory, some are already addressed in Word, and some require Kyle decisions.

Done when. Every source comment ID is marked done, blocked, or intentionally not changed with a short reason.

### EDIT-025. Final LaTeX and style audit

Status. Open.

Source comments. None directly.

Likely files. `manuscript.tex`, `bibliography/Thesis.bib`.

Context. Before submission work continues, the manuscript needs a final pass for citation style, cross-references, figure captions, table captions, no em dash characters, and no unresolved Word artifacts.

Done when. The source has no obvious Word conversion artifacts, all citations use `\cite{}`, all labels resolve in source, and no em dash characters are present. Build only if Kyle explicitly asks.

## Comment ID Coverage

The following open or unflagged comment IDs were assigned to tasks.

`1332224640`, `1657910628`, `850189325`, `2050568483`, `1300236268`, `2021869295`, `774033147`, `542381207`, `931591290`, `556409408`, `2018412757`, `473839288`, `1806968990`, `380024150`, `298285836`, `583917242`, `1470233068`, `1125610476`, `1233138264`, `486357702`, `153769611`, `1824005225`, `1906731719`, `306246836`, `67036694`, `461713005`, `1261848065`, `279432750`, `1861464571`, `622324121`, `542124272`, `918939383`, `1837771308`, `184831444`, `1468403588`, `1182007124`, `982577787`, `249936144`, `110014176`, `1861267912`, `693642028`, `184231791`, `2097415894`, `50837945`, `1435262033`, `916610491`, `195942775`, `209493019`, `1822051757`.
