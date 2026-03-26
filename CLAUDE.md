# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a journal manuscript for submission to MDPI *Insects*, based on a completed Master's thesis studying monarch butterfly ecology and wind patterns at overwintering sites in California. The research focuses on Vandenberg Space Force Base as the primary study site. The thesis version is archived in the `thesis-library-submission` branch and `thesis-archive/` directory.

## Build Commands

**When to Build:**

- Only build LaTeX documents when explicitly requested by the user
- Do NOT build automatically after making edits
- If the user says "build this" or "compile", then you should build

**Primary build:**

```bash
latexmk -pdf manuscript.tex
```

**Clean build files:**

```bash
latexmk -c
```

**Force rebuild:**

```bash
latexmk -pdf -f manuscript.tex
```

**Important Notes:**

- Uses the MDPI template with ACS numbered citation style
- Use `\cite{}` for citations (numbered references [1], [2], etc.)
- Do NOT use `\citep{}`, `\parencite{}`, or author-date citations
- Unicode math symbols must be replaced with LaTeX commands (`$\geq$`, `$\Delta$`)
- Do not modify `Definitions/mdpi.cls` -- this is the MDPI template class file
- Never use em dashes -- use en dashes (`--`) instead

## Project Structure

- `manuscript.tex` - Primary manuscript document for Insects submission
- `Definitions/` - MDPI template class file, style files, and logos (DO NOT EDIT)
- `bibliography/` - References (`Thesis.bib`) and citation files
- `figures/` - All graphics and images (organized by section)
- `supplemental/` - Advisor feedback, meeting notes, voice memos
- `docs/` - Journal submission guidelines and reference PDFs
- `thesis-archive/` - Archived Cal Poly thesis files (for reference only)
- `qgis/` - GIS project files for spatial analysis

## Key Study Site

**Vandenberg Space Force Base** - Camera-based behavioral study site focusing on monarch butterfly behavior and wind pattern interactions

## Bibliography Management

Uses BibTeX with MDPI's `mdpi.bst` style file. Bibliography is in `bibliography/Thesis.bib`. The MDPI template handles bibliography formatting via natbib.

## Manuscript Content

The manuscript tests the "Disruptive Wind Hypothesis" -- that wind speeds above 2 m/s disrupt overwintering monarch butterfly clusters. Key findings:

- No evidence of wind disruption at any speed (0--12.4 m/s)
- Wind effects only appear in interaction with direct sunlight
- Thermoregulation proposed as alternative explanation
- 30-minute and sunset-window temporal analyses

## Template Guidelines

**`Definitions/mdpi.cls` (DO NOT EDIT):**
- MDPI's official class file
- Never modify this file

**`manuscript.tex` (Primary working file):**
- All manuscript content lives here (single file per MDPI convention)
- Front matter, body sections, back matter, and appendices
- Document class: `\documentclass[insects,article,submit,pdftex,moreauthors]{Definitions/mdpi}`

## Supplemental Materials Workflow

**Supplemental Content Structure:**

- `/supplemental/methods/` - Voice memos, advisor materials, feedback
- `/supplemental/notes/` - Meeting notes, manuscript drafts (Word docs for advisor interface)

**GitHub Issue Workflow:**

- Issues track outstanding manuscript edits from advisor (Francis) comments
- Issues reference specific sections of `manuscript.tex`
- Labels: `content`, `formatting`, `bibliography`, `discussion-needed`

**Integration Approach:**

- Edit `manuscript.tex` directly
- Never use em dashes
- Check `supplemental/` for context when working on content issues

## Authors

- **Kyle Nessen** - Graduate student, primary researcher
- **Francis X. Villablanca** - Advisor, corresponding author (fvillabl@calpoly.edu)
