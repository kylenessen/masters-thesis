## Detailed plan → GitHub‑issue–ready tasks

Each item includes **Title, Why, Edits, Acceptance criteria, Owner**. “Owner: You” means tasks you’ll perform (e.g., add/confirm a citation); “Owner: LLM” means text‑level edits a writing agent can implement directly.

---

### 1) Tighten the opening: foreground wind, trim over‑breadth

**Why:** Francis wants “explain, don’t just state,” but your first paragraph currently sprawls (temperature, water, marine/cave examples). It dilutes the wind case you are making.&#x20;
**Edits:**

* Keep a **compact 2–3 sentence setup** that abiotic drivers constrain ectotherms (temperature, solar radiation)—**because these become your confounders**—then pivot immediately to **wind** with 3–4 diverse examples (you already have strong ones).
* Remove marine/cave/water sections from the **opening**; those don’t buy you leverage on the wind argument.
  **Acceptance criteria:** Opening ≤ 10–12 sentences total across the first two paragraphs; wind is clearly the focal abiotic driver by the end of paragraph 2.
  **Owner:** LLM (surgical trim); You (sanity check that removed examples are not used later).

---

### 2) Replace the wind‑multidimensionality block with a single scope sentence (or hard‑cut)

**Why:** Avoid contradicting your one‑dimensional operationalization while acknowledging the concept (minimally) to satisfy Francis.&#x20;
**Edits:**

* **Preferred:** Insert the **one‑liner** from the section above at the end of your second wind paragraph; **delete** the later “wind is multidimensional; consistency and gustiness…” sentences near the confounders paragraph.
* **Option B (your preference):** Hard‑delete all multidimensionality language from the Introduction; keep the modeling choices in Methods/Results as written.
  **Acceptance criteria:** No more than **one** sentence about multidimensionality in the Introduction, or none if Option B; no references to “gustiness,” “turbulence,” or “variance” remain in the Intro.
  **Owner:** LLM.

---

### 3) Install a fuller **life‑history tour** (single robust paragraph)

**Why:** Your audience needs the complete annual cycle linked to abiotic constraints before you focus on overwintering. Francis asked for this explicitly.&#x20;
**Edits (paste‑ready paragraph):**
*Monarch butterflies (Danaus plexippus) cycle through breeding, migration, and overwintering phases that expose them to distinct abiotic constraints as ectotherms. During spring–summer breeding, multiple generations develop on milkweeds (Asclepias spp.), with temperature setting developmental and flight thresholds and precipitation shaping host and nectar availability. As day length shortens and temperatures fall, late‑summer individuals enter reproductive diapause, accumulate lipid reserves, and initiate oriented long‑distance migration. Overwintering then requires months‑long persistence on **fixed energy reserves**, during which temperature governs activity thresholds, direct sunlight can both enable flight and precipitate departures via rapid warming, and **wind** can alter stability, orientation, and energetic costs. These seasonal shifts—fast turnover and expansion during breeding, energy accumulation and transit during migration, and prolonged exposure with limited foraging during overwintering—make monarchs a powerful model for testing how abiotic drivers, and **wind in particular**, shape behavior and abundance at roosts.*
**Acceptance criteria:** A single paragraph (10–12 sentences) appears immediately **before** conservation stakes; its last sentence earns “monarchs are a great test case.”
**Owner:** LLM (insert the paragraph); You (add/retain supporting citations already in your bib, e.g., Masters et al. 1988 for thermoregulation if desired).

---

### 4) Delete the “plants create microclimates” paragraph outright

**Why:** It’s orthogonal to your argument and duplicates what will be handled by the historical microclimate hypothesis paragraph. You noted it’s a distraction.&#x20;
**Edits:** Remove the paragraph beginning “Many invertebrates exploit habitats where other organisms, particularly plants, modify local abiotic conditions…” and stitch surrounding paragraphs seamlessly.
**Acceptance criteria:** Paragraph is fully removed; transitions remain smooth; no orphaned cross‑references.
**Owner:** LLM.

---

### 5) Split and tighten the **microclimate vs. disruptive wind** sections

**Why:** Francis asked for two clean paragraphs: (1) *historical microclimate hypothesis → what held up vs. what didn’t*; (2) *disruptive wind hypothesis → correlational chain → untested*.&#x20;
**Edits (topic sentences and skeletons):**

* **Paragraph A (Microclimate – historical → qualified):**
  *Early management emphasized a single “microclimate” envelope (mild temperatures, high humidity, dappled light, wind protection), but subsequent work indicates **no single optimal microclimate**, with temperature responses varying by latitude and regional macroclimate outperforming local variables; **light** remains consistently important.*
  Then concisely cite Saniee & Villablanca (2022), Weiss (1991), Fisher (2018) as you did; conclude: *this qualifies the original framework and isolates wind as the least‑tested component.*
* **Paragraph B (Disruptive wind – inference → gap):**
  *Within that framework, a **2 m/s** “disruptive wind” threshold became influential, yet evidence has been **correlational** (occupied vs. unoccupied contrasts) without isolating confounders; despite uptake in guidance documents, the threshold remains **untested** as a causal driver of monarch abundance at clusters.*
  **Acceptance criteria:** Two adjacent paragraphs exist, each doing one job; no overlap or repetition; “untested” phrasing appears explicitly.
  **Owner:** LLM.

---

### 6) Support or soften the “widely used 2 m/s” claim

**Why:** Francis: *“Make this evident.”* You now cite **Leong 2016** and **Xerces 2016**—good. Avoid over‑claiming “adopted by federal and state agencies” unless you have agency documents.&#x20;
**Edits:**

* Keep: *“…has influenced conservation guidance (e.g., Leong 2016; Xerces 2016)….”*
* **Remove or soften**: “adopted by federal and state agencies” **unless** you can cite specific adoption memos/standards.
  **Acceptance criteria:** Every management uptake claim has a concrete citation; no uncited “federal/state adoption” language remains.
  **Owner:** You (decide whether to keep/soften); LLM (make the language match your choice).

---

### 7) Confounders paragraph: sharpen and **remove** multidimensionality language

**Why:** Francis asked you to **name confounders** and justify a **direct test**. You’ve done that; just remove the “gustiness/consistency” bit if you are cutting multidimensionality.&#x20;
**Edits (paste‑ready sentences):**
*Accordingly, a direct test must isolate wind from key confounders. As ectotherms, monarchs require sufficient body temperatures for flight, which are influenced by **ambient temperature** and **direct sunlight**; **time of day** shapes activity rhythms independent of wind. A meaningful test therefore evaluates wind’s association with **monarch abundance** while controlling for these drivers.*
**Acceptance criteria:** The confounders paragraph names temperature, direct sunlight, and time of day explicitly; no “gustiness/consistency/turbulence” language remains (unless you opted for the one‑liner in Task 2).
**Owner:** LLM.

---

### 8) Define the response variable once; use it consistently

**Why:** Francis: define “butterfly abundance at overwintering clusters” and then shorthand it. Some places still say “cluster abundance.”&#x20;
**Edits (paste‑ready sentence):**
*We define our response as **butterfly abundance at overwintering clusters** (hereafter, **“monarch abundance”**).*
Then **replace** all instances of “cluster abundance” with “monarch abundance.”
**Acceptance criteria:** Definition appears once near the start of your study description; “monarch abundance” is used consistently thereafter (Intro and Results).
**Owner:** LLM.

---

### 9) Parenthetical predictor list on first hypothesis mention

**Why:** Align Intro to Methods/Results; Francis asked for this.&#x20;
**Edits (replace your first hypothesis sentence):**
*First, we hypothesized that **monarch abundance** is predicted by wind and other environmental factors **(maximum wind gust; minutes with gust ≥ 2 m/s; temperature; direct sunlight; time since day start; previous abundance)**.*

> Use “time since day start” here (see Task 10).
> **Acceptance criteria:** Predictor list appears in parentheses on first hypothesis mention; wording matches your actual variables.
> **Owner:** LLM.

---

### 10) Fix the **“time since sunrise” vs. “time since first observation”** inconsistency

**Why:** Methods define the diurnal covariate as **minutes since the first observation of each day**, but Intro/Results text and a figure label say **time since sunrise**. That’s a contradiction.&#x20;
**Edits:**

* Replace all prose mentions of “time since sunrise” with **“time since day start (minutes since the first observation of each day)”** unless you actually computed sunrise (you didn’t).
* If any figure axis labels read “time since sunrise,” update to “time since day start.”
  **Acceptance criteria:** No references to “sunrise” remain unless supported by data; Methods, Intro, figure captions/labels are consistent.
  **Owner:** LLM (text); You (regenerate figures/captions if they currently say “sunrise”).

---

### 11) Calibrate conservation stakes language (avoid claiming a bottleneck)

**Why:** Francis asked to frame overwintering as an **identified priority**, not a proven bottleneck. Your current language flirts with stronger causality.&#x20;
**Edits:**

* Use “**identified conservation priority**” and “**proposed** bottleneck” (you already added “proposed” in one place—good).
* Keep USFWS 2024 listing text as you have it; that’s appropriate context.
  **Acceptance criteria:** No sentence asserts overwintering as *the* bottleneck; modal verbs (“may,” “could”) or “proposed/identified” framing is used.
  **Owner:** LLM.

---

### 12) Standardize wind metric language everywhere

**Why:** Consistency with Methods and model set.&#x20;
**Edits:**

* Use **“maximum wind gust”** (not generic “wind speed”) for the primary metric, and **“minutes with gust ≥ 2 m/s”** for the threshold variant.
* Ensure Results and figure captions match this wording.
  **Acceptance criteria:** No generic “wind speed” phrasing remains where you mean **max gust**; the threshold metric naming is consistent.
  **Owner:** LLM.

---

### 13) Keep the end‑of‑Intro hypothesis trio, but match terms precisely

**Why:** Francis liked your ending. Don’t change the structure—just the terms per Tasks 8–12.&#x20;
**Edits:** Minimal copy‑edit to align with “monarch abundance,” “maximum wind gust,” “minutes with gust ≥ 2 m/s,” and “time since day start.”
**Acceptance criteria:** The three hypotheses remain verbatim in intent; only terminology is synchronized.
**Owner:** LLM.

---

### 14) Remove site‑specific management claims unless cited (Ellwood, Pismo, etc.)

**Why:** Earlier versions referenced these; current draft mostly doesn’t, but if they reappear, they must be cited. Francis flagged “make it evident.”&#x20;
**Edits:** Either delete site‑specific management assertions or add specific restoration plan citations.
**Acceptance criteria:** No uncited site‑level management claims remain.
**Owner:** You (decide include/delete + provide citations); LLM (apply).

---

### 15) Insert the study‑setup sentence to mirror Methods

**Why:** Bridge from gap → approach with exact monitoring details (interval, co‑measured variables) so readers see the design answers the gap.&#x20;
**Edits (paste‑ready):**
*We monitored **every 30 minutes** at cluster locations and recorded **maximum wind gust, minutes with gust ≥ 2 m/s, ambient temperature,** and **direct sunlight**, enabling direct tests while controlling for confounders.*
**Acceptance criteria:** This sentence appears immediately before the hypothesis list and matches Methods vocabulary.
**Owner:** LLM.

---

### 16) Ensure Figures/Tables and text tell the same story (labels & terms)

**Why:** You already mention M23/M24 and show partial effects; labels must match variable names and phrasing fixed in Tasks 8–12.&#x20;
**Edits:**

* Confirm captions use **monarch abundance**, **maximum wind gust**, **minutes with gust ≥ 2 m/s**, **time since day start**.
* Where you currently say “flight threshold” in a figure narrative, ensure the threshold band matches the citation (Masters et al. 1988) and your numeric band in the caption.
  **Acceptance criteria:** No terminology mismatches between figures/tables and text.
  **Owner:** You (figure regeneration if needed); LLM (caption edits).

---

### 17) Keep the “evidence‑based management” paragraph but purge any leftover wind‑nuance claims

**Why:** Your management section is strong; just ensure no latent “gustiness/turbulence” language survived if you chose the cut.&#x20;
**Edits:** Search and remove those terms.
**Acceptance criteria:** Management section focuses on what your data show (sunlight, temperature, diurnal), not untested wind nuance.
**Owner:** LLM.

---

### 18) Bibliography check: coverage for three specific claims

**Why:** To avoid reviewer nitpicks.&#x20;
**Edits / Tasks for you:**

* Confirm that **Masters, Malcolm & Brower (1988)** is cited **at first mention** of flight threshold / sunlight warming.
* Confirm that **Leong 2016** and **Xerces 2016** are cited **exactly** where you claim management practice recognized the 2 m/s threshold.
* If you retain any phrase like “adopted by federal/state agencies,” **either** add specific agency documents **or** soften to “featured in guidance documents.”
  **Acceptance criteria:** These three claims are either fully supported by the citations above or softened accordingly.
  **Owner:** You.

---

## Small paste‑ready replacements (to speed editing)

* **Define the response variable (near start of study description):**
  *We define our response as **butterfly abundance at overwintering clusters** (hereafter, **“monarch abundance”**).*

* **Confounders + need for a direct test (no multidimensionality):**
  *Accordingly, a direct test must isolate wind from key confounders. As ectotherms, monarchs require sufficient body temperatures for flight, which are influenced by **ambient temperature** and **direct sunlight**; **time of day** shapes activity rhythms independent of wind. A meaningful test therefore evaluates wind’s association with **monarch abundance** while controlling for these drivers.*

* **First hypothesis sentence (with parenthetical predictors):**
  *First, we hypothesized that **monarch abundance** is predicted by wind and other environmental factors **(maximum wind gust; minutes with gust ≥ 2 m/s; temperature; direct sunlight; time since day start; previous abundance)**.*

* **Study setup bridge (just before hypotheses):**
  *We monitored **every 30 minutes** at cluster locations and recorded **maximum wind gust, minutes with gust ≥ 2 m/s, ambient temperature,** and **direct sunlight**, enabling direct tests while controlling for confounders.*

---

## Final notes on alignment & risk

* Cutting the wind‑multidimensionality *deep dive* is the right call for coherence. If you keep **one scope sentence**, you’ll likely satisfy Francis’s earlier note **without** reopening analysis demands you didn’t pursue.&#x20;
* The biggest objective inconsistency to fix is **“time since sunrise”** vs **“time since first observation.”** Reviewers spot that instantly.&#x20;
* Your new opening on wind is already strong; trimming nonessential abiotic examples will make it **feel even stronger** and keep the narrative tight.

If you want, I can apply the edits (Tasks 1–12, 15, 17) directly to the current draft text in one pass so it’s ready for you to review before creating the GitHub issues.
