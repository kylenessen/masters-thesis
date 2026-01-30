# Technical Report Build Plan

## Context

The Cal Poly subaward (CalPol23-4132) under the Xerces/USDA Forest Service grant (21-DG-11132762-274) requires a final technical report deliverable. The project title is "Wind Model Validation for Monarch Butterfly Overwintering Groves." The original SOW described CFD simulation work, but the project pivoted to empirical wind/camera observation work after the LiDAR drone platform crashed during training in year one and was unusable for over a year. Xerces is aware of and supportive of this change. The thesis has been defended and contains the research. We need to repackage it as a technical report.

### Contract Details
- **Federal Award**: 21-DG-11132762-274 (USDA Forest Service International Programs)
- **Subaward**: CalPol23-4132
- **PTE**: The Xerces Society, Inc.
- **PTE PI**: Emma Pelton
- **Sub PI**: Francis Villablanca
- **Subrecipient**: Cal Poly Corporation
- **Project Period**: 11/01/2023 - 12/31/2024
- **Amount**: $75,851.00

### Deliverable Requirement (from Attachment 4)
"The analysis report identified as the Deliverable in the Statement of Work must be submitted to Xerces no later than December 31, 2024."

### SOW Deliverable (from Attachment 5-1, page 15)
"A report detailing all findings that is publication quality. The report (and publication) will include an accuracy assessment detailing how the final model performed against real world measurements."

---

## Goal

Create `render_report.tex` as a separate build target that pulls in the same chapter content files but produces a document that looks and feels like a professional technical report, not a thesis. No changes to the thesis files themselves.

---

## Files to Create

### 1. `render_report.tex` (main build file)

Use the `article` document class (12pt). This replaces `main.tex` for the report build. Structure:

```
\documentclass[12pt, letterpaper]{article}

% Packages: same math/figure/table/bibliography packages from main.tex
% Key formatting differences:
%   - Single spacing (or 1.15) using setspace package
%   - 1-inch margins using geometry package
%   - Section numbering (1, 1.1, 1.2) not chapter numbering
%   - Running headers/footers using fancyhdr
%   - No chapter commands (article class doesn't have them)

% Input the report-specific preamble
\input{report/preamble_report}

\begin{document}
    \input{report/titlepage}
    \newpage
    \input{report/transmittal_letter}
    \newpage
    \tableofcontents
    \newpage
    \listoffigures
    \listoftables
    \newpage
    \input{report/executive_summary}
    \newpage
    \input{report/outline_report}

    % Bibliography
    \newpage
    \printbibliography[title={References}]

    % Appendices
    \newpage
    \appendix
    \input{appendices/30min_models}
    \input{appendices/threshold_models}
    \input{appendices/sunset_models}
    \input{appendices/24hr_models}
\end{document}
```

### 2. `report/` directory (new)

Create a `report/` directory for all report-specific files:

#### 2a. `report/preamble_report.tex`

Report-specific package configuration and formatting:
- `\usepackage[margin=1in]{geometry}`
- `\usepackage{setspace}` with `\setstretch{1.15}` (slightly more than single-spaced)
- `\usepackage{fancyhdr}` with running header: abbreviated title on left, page number on right
- `\usepackage{titlesec}` to style section headings
- Same packages from `main.tex` for math, figures, tables, bibliography, hyperref, cleveref
- Same `\graphicspath{{figures/}}` and `\addbibresource{bibliography/Thesis.bib}`
- Same caption setup from main.tex
- Import `frontmatter/preamble.tex` for any additional packages the content needs
- Override caption format to remove the italic/bold styling if desired for a cleaner report look

#### 2b. `report/titlepage.tex`

Professional technical report title page. Layout:

```
[Centered, top of page]

FINAL TECHNICAL REPORT

[vertical space]

Wind Model Validation for Monarch Butterfly Overwintering Groves

[vertical space]

Prepared for:
The Xerces Society, Inc.
Emma Pelton, Principal Investigator
Under USDA Forest Service Award 21-DG-11132762-274

[vertical space]

Prepared by:
California Polytechnic State University
San Luis Obispo, CA

Francis Villablanca, Ph.D., Principal Investigator
Kyle Nessen, M.S., Graduate Researcher

[vertical space]

Subaward No. CalPol23-4132

[vertical space]

[Report Date - use actual submission date]
```

No logos needed unless you want to add Cal Poly's. Keep it clean and institutional.

#### 2c. `report/transmittal_letter.tex`

A one-page cover/transmittal letter. Content outline:

**Paragraph 1 - Transmittal:**
This report constitutes the final technical deliverable under Subaward CalPol23-4132, "Wind Model Validation for Monarch Butterfly Overwintering Groves," funded through USDA Forest Service Award 21-DG-11132762-274 via The Xerces Society, Inc.

**Paragraph 2 - Scope Modification:**
The original statement of work proposed computational fluid dynamics (CFD) simulations using LiDAR-derived forest geometry to model wind patterns in overwintering groves. During the first year of the project, the drone-mounted LiDAR platform required for aerial data acquisition was damaged during training operations and remained out of service for an extended period, making the originally proposed methodology infeasible within the project timeline. In coordination with Xerces, the research approach was revised to pursue direct empirical investigation of wind effects on overwintering monarch butterfly clusters at Vandenberg Space Force Base.

**Paragraph 3 - What was accomplished:**
The revised study deployed time-lapse cameras and wind sensors at monarch cluster roost sites over the 2023-2024 overwintering season, producing 1,894 paired observations across 78 days. This approach enabled the first direct empirical test of the Disruptive Wind Hypothesis, a foundational assumption in monarch habitat management for over three decades. The findings have direct implications for habitat management practices at overwintering sites managed by the Department of Defense, U.S. Forest Service, California State Parks, and other land managers.

**Paragraph 4 - Close:**
The enclosed report presents the complete methodology, results, and analysis in publication-quality format as specified in the statement of work. Questions regarding this report may be directed to [PI contact info].

Format as a formal letter with institutional letterhead info (Cal Poly address, etc.) at top, addressed to Emma Pelton.

#### 2d. `report/executive_summary.tex`

A rewritten version of the abstract, framed for a technical/management audience:

- Start with a `\section*{Executive Summary}` or styled as an unnumbered section
- Open with the management context (why this matters for overwintering site management)
- State what was done (methods, briefly)
- State the key findings (no wind disruption effect, the 2 m/s threshold is not supported)
- Close with management implications/recommendations
- Keep to roughly one page

This is NOT the thesis abstract copy-pasted. Rewrite it to emphasize practical management implications over academic framing. The audience is Xerces staff and USDA Forest Service program managers, not a thesis committee.

#### 2e. `report/outline_report.tex`

This replaces `chapters/outline.tex` for the report. Instead of `\chapter{}` commands (which don't exist in `article` class), use `\section{}`:

```latex
\section{Introduction}
\label{sec:introduction}
\input{chapters/vsfb/introduction}

\section{Materials and Methods}
\input{chapters/vsfb/methods}

\section{Results}
\input{chapters/vsfb/results}

\section{Discussion}
\input{chapters/vsfb/discussion}
```

**Important**: The chapter content files already use `\section{}` internally. When wrapped in `\chapter{}` (thesis mode), those become subsections of the chapter. In `article` class with `\section{}` wrappers, the internal `\section{}` calls will collide.

**Solution**: Check what the chapter content files actually use. If they use `\section{}`, then `outline_report.tex` should NOT add another `\section{}` wrapper. Instead, just `\input` the files directly and let their internal `\section{}` commands be the top-level sections. OR, rename the wrapper to `\section{}` and change the internal commands in the content files... but that would modify thesis files.

**Better solution**: Use `report/outline_report.tex` to just `\input` the files directly without any wrapping section command, if the content files already have their own `\section{}` structure. Test this and adjust. If the content files use `\section{Site Description}`, `\section{Data Collection}`, etc., those will render as top-level sections in `article` class, which is exactly what we want for a report.

If we need a higher-level grouping (like "1. Introduction" containing "1.1 Site Description"), we could use `\part{}` or just restructure with `\section` / `\subsection` by having the outline file provide `\section{Introduction}` and then patching the content files' `\section` to `\subsection` via a `\let` command:

```latex
% Demote \section to \subsection for included content
\let\origsection\section
\let\section\subsection
\let\subsection\subsubsection

\origsection{Introduction}
\input{chapters/vsfb/introduction}

\origsection{Materials and Methods}
\input{chapters/vsfb/methods}

% etc.

% Restore
\let\section\origsection
```

This is the cleanest approach -- it doesn't modify any thesis content files.

---

## Build Command

```bash
latexmk -pdf render_report.tex
```

---

## Key Technical Considerations

1. **Section numbering collision**: The `\let` trick above (demoting `\section` to `\subsection` within included files) is the cleanest way to handle this without modifying thesis chapter files.

2. **Cross-references**: The thesis uses `\cref` / `\label` extensively. Since we're using `article` class, references to "Chapter X" will need to say "Section X" instead. `cleveref` handles this automatically based on document class -- `article` class will say "Section" not "Chapter" by default. Should work without changes.

3. **Figure/table numbering**: In `article` class, figures are numbered sequentially (Figure 1, 2, 3...) not by chapter (Figure 1.1, 1.2...). This is fine for a report. If chapter-style numbering is preferred, add `\counterwithin{figure}{section}` and `\counterwithin{table}{section}`.

4. **Bibliography**: Same .bib file, same biblatex config. Works as-is.

5. **Appendices**: The `\appendix` command in `article` class changes section numbering to A, B, C. The appendix files should work, but test whether their internal structure (which may assume `\chapter`) needs adjustment.

6. **The `frontmatter/preamble.tex` file**: This is `\input` in `main.tex` for additional packages. Read this file before building to see if it defines commands or loads packages that depend on the `cpthesis` class. If so, replicate the needed parts in `report/preamble_report.tex`.

7. **The `variables.tex` file**: Check if this is used by the chapter content. If so, `\input` it in the report preamble.

---

## Implementation Order

1. Create `report/` directory
2. Read `frontmatter/preamble.tex` and `variables.tex` to understand dependencies
3. Read the chapter content files (`chapters/vsfb/introduction.tex`, etc.) to confirm their internal sectioning structure
4. Read the appendix files to confirm their structure
5. Create `report/preamble_report.tex` with all necessary packages and formatting
6. Create `report/titlepage.tex`
7. Create `report/transmittal_letter.tex`
8. Create `report/executive_summary.tex`
9. Create `report/outline_report.tex` with the `\let` section-demotion approach
10. Create `render_report.tex` as the main build file
11. Build with `latexmk -pdf render_report.tex`
12. Debug and iterate on formatting
13. Verify all figures, tables, cross-references, and bibliography render correctly

---

## What NOT to Change

- No modifications to any files in `chapters/`, `appendices/`, `frontmatter/`, `bibliography/`, or `figures/`
- No modifications to `main.tex`, `cpthesis.cls`, or any thesis-specific files
- The thesis build (`latexmk -pdf main.tex`) must remain unaffected
