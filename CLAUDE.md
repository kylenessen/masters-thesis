# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the technical report deliverable for Subaward CalPol23-4132, "Wind Model Validation for Monarch Butterfly Overwintering Groves," under USDA Forest Service Award 21-DG-11132762-274 via the Xerces Society. The report repackages thesis research as a standalone technical report using the LaTeX `article` class.

## Build Commands

**When to Build:**

- Only build LaTeX documents when explicitly requested by the user
- Do NOT build automatically after making edits

**Build the report:**

```bash
latexmk -pdf render_report.tex
```

**Clean build files:**

```bash
latexmk -c
```

**Force rebuild:**

```bash
latexmk -pdf -f render_report.tex
```

**Important Notes:**

- Uses BibLaTeX with APA style and Biber backend
- Use `\parencite{}` for citations (not `\autocite{}`, `\citep{}`, or `\citet{}`)
- Unicode math symbols must be replaced with LaTeX commands (`$\geq$`, `$\Delta$`)
- Content files use `\section{}` internally; these are demoted to `\subsection{}` by `outline_report.tex`
- Do not include `\usepackage{}` commands in chapter or appendix content files
- Never use em dashes

## Project Structure

- `render_report.tex` - Main report build file
- `report/` - Report-specific files:
  - `preamble_report.tex` - Package configuration and formatting
  - `titlepage.tex` - Report title page
  - `transmittal_letter.tex` - Cover letter to Xerces
  - `executive_summary.tex` - Management-focused summary
  - `outline_report.tex` - Content outline with section demotion
- `chapters/vsfb/` - Body content (introduction, methods, results, discussion)
- `appendices/` - Candidate model tables
- `figures/` - All graphics and images
- `supplemental/` - Generated tables and figures referenced by content
- `bibliography/Thesis.bib` - Reference database

## Section Demotion

The content files were written for a thesis using `\chapter{}` wrappers. The report uses `article` class (no chapters). To handle this:

- `outline_report.tex` uses `\let` to demote `\section` to `\subsection` before including content files, then restores them
- A `\chapter` shim in the preamble maps `\chapter{}` to `\section{}` for appendix files
- The same demotion is applied around appendix includes in `render_report.tex`

This approach avoids modifying any shared content files.

## Bibliography Management

Uses BibLaTeX with Biber backend and APA citation style. The bibliography database is `bibliography/Thesis.bib`.
