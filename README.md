# Wind Does Not Disrupt Overwintering Monarch Butterfly Clusters

Manuscript for submission to [*Insects*](https://www.mdpi.com/journal/insects) (MDPI).

**Authors:** Kyle Nessen and Francis X. Villablanca
**Affiliation:** Biological Sciences Department, California Polytechnic State University, San Luis Obispo

## Summary

This study provides the first direct empirical test of whether wind disrupts overwintering western monarch butterfly (*Danaus plexippus*) clusters -- a hypothesis that has guided conservation practice for over three decades. Using time-lapse photography and wind sensors deployed at Vandenberg Space Force Base during the 2023--2024 season, we found no evidence that wind speeds above 2 m/s disrupt clusters. Instead, wind effects depend on sunlight exposure, pointing toward thermoregulation as a primary driver of clustering behavior.

## Building

Requires a full TeX Live / MacTeX installation.

```bash
latexmk -pdf manuscript.tex
```

## Repository Structure

- `manuscript.tex` -- Main manuscript (MDPI template, ACS citation style)
- `Definitions/` -- MDPI template class and style files
- `bibliography/` -- BibTeX references
- `figures/` -- Manuscript figures
- `supplemental/` -- Advisor feedback, meeting notes, drafts
- `thesis-archive/` -- Archived Cal Poly thesis files

The original thesis is preserved in the `thesis-library-submission` branch.
