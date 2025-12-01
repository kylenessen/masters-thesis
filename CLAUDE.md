# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Master's thesis LaTeX project studying monarch butterfly ecology and wind patterns at overwintering sites in California. The research focuses on Vandenberg Space Force Base as the primary study site.

## Build Commands

**When to Build:**

- Only build LaTeX documents when explicitly requested by the user
- Do NOT build automatically after making edits
- If the user says "build this" or "compile the thesis", then you should build

**Primary build:**

```bash
latexmk -pdf main.tex
```

**Individual chapter renders:**

```bash
latexmk -pdf render_pismo.tex  # Pismo site chapter
latexmk -pdf render_vsfb.tex   # VSFB site chapter
```

**Clean build files:**

```bash
latexmk -c
```

**Force rebuild:**

```bash
latexmk -pdf -f main.tex
```

**Important Notes:**

- The main thesis uses BibLaTeX with Chicago author-date style
- Use `\parencite{}` for citations (not `\autocite{}`, `\citep{}`, or `\citet{}`)
- Unicode math symbols (≥, Δ, etc.) must be replaced with LaTeX commands (`$\geq$`, `$\Delta$`)
- Chapter files should use `\section{}` not `\chapter{}`
- Do not include `\usepackage{}` commands in chapter files

## Project Structure

- `main.tex` - Primary thesis document
- `cpthesis.cls` - Cal Poly thesis template class file
- `variables.tex` - Study site parameters and coordinates
- `frontmatter/` - Abstract, acknowledgments, dedication, etc.
- `chapters/` - Main thesis content (introduction, methods, results, etc.)
- `appendices/` - Supplementary materials
- `figures/` - All graphics and images
- `bibliography/` - References and citation files
- `notes/` - Research notes and meeting transcripts
- `qgis/` - GIS project files for spatial analysis

## Key Study Site

**Vandenberg Space Force Base** - Camera-based behavioral study site focusing on monarch butterfly behavior and wind pattern interactions

## Bibliography Management

Uses BibLaTeX with Biber backend. Bibliography files are in `bibliography/` directory. The `latexmkrc` file is configured to handle nomenclature processing automatically.

## Research Data Context

The thesis involves:

- Wind monitoring using RainWise WindLog sensors (12 units at Pismo)
- Time-lapse photography at VSFB
- Multi-season data collection (2023-2024, 2024-2025)
- GIS spatial analysis using QGIS
- Statistical analysis components

## Template Requirements

This uses the official Cal Poly thesis template with specific formatting requirements. The `guidelines/` directory contains university standards. Key metadata is defined in `frontmatter/information.tex`.

## Template Editing Guidelines

**IMPORTANT: Exercise extreme caution when editing template core files.**

**`cpthesis.cls` (DO NOT EDIT):**
- This is the low-level formatting file based on revisions dating to the early 1990s
- If you need to change this file, you have most likely found a bug and should report it
- Changes can cause unexpected results and make the thesis non-compliant with Graduate Education style guidelines
- **Never modify this file**

**`main.tex` (EDIT WITH CAUTION):**
- This is the root file designed to minimize the need for editing
- Contains formatting and content settings for Graduate Education compliance
- Adding content structure (like appendices with `\appendix` and `\input{}` commands) is acceptable
- Changing formatting settings, package configurations, or template structure should be avoided
- Not all changes will cause problems, but care must be taken
- When in doubt, add content in separate files and include them rather than modifying core settings

## Supplemental Materials Workflow

**Supplemental Content Structure:**

- `/supplemental/methods/` - Voice memos, advisor materials, feedback for methods section
- Voice memos are processed into densified markdown files with descriptive names
- Example: `Vandenberg_Methods_Section-_Justifications_and_...md`

**GitHub Issue Workflow:**

- Issues reference specific LaTeX file locations (e.g., `chapters/vsfb.tex lines 45-60`)
- Include relevant supplemental file patterns to search for context
- Goal: Find relevant supplemental materials and integrate directly into authoritative LaTeX text
- Author reviews changes and merges via PR

**Integration Approach:**

- Search supplemental materials using filename patterns and content
- Edit the authoritative LaTeX files directly (not create new files)
- Focus on enhancing existing sections with additional context and detail
- Never use em dashes
