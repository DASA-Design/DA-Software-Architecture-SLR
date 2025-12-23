# REVIEW PROCESS
This section documents the *Systematic Literature Review (SLR)* on *Dimensional Analysis (DA)* in software architecture and development. The process follows established SLR \& *Systematic Mapping Study (SMS)* guidance in software engineering and is structured as an iterative workflow with quality checkpoints.

[Back to top](#review-process)

---
## Purpose \& Scope
- **Goal:** identify the current state, applications, tools, contributions, limitations, and gaps related to DA in software architecture/development.
- **Time window:** searches were executed in two phases: an initial run targeting **2010–2020** and an update targeting **2010–2024**.
- **Primary sources:** five academic archives were used as the main search venues: **ACM**, **ASME**, **IEEE Xplore**, **ScienceDirect**, and **SpringerLink**.

[Back to top](#review-process)

---
## High-level workflow (Plan > Execute > Report)
The _SLR_ is organized into three stages (also represented as BPMN 2.0 diagrams in the [Image 1](#image-1-slr-method-overview) below and in the `protocol/img/svg/` folder). these stages are:

1. **Plan:** define and validate the review protocol,
2. **Execute:** search, screen, and curate the corpus of primary studies,
3. **Report:** synthesize, map, and quality-check results before final reporting,

### Image 1: SLR Method Overview

<svg viewBox="0 0 900 900" width="300" height="300">
    <!-- SVG content -->
    <image href="img/svg/01 - SLR Method.svg" alt="overall-diagram" />
    <div align="center"><em>Image 1. SLR Method Overview.</em></div>
</svg>

The detailed tasks are in [Image 2](#image-2-slr-process-tasks), and as seen, the decision gates applied between iterations ensure (a) protocol quality, (b) document eligibility, and (c) report quality.

### Image 2: SLR Process tasks

<svg viewBox="0 0 900 900" width="300" height="300">
    <!-- SVG content -->
    <image href="img/svg/02 - SLR Process.svg" alt="task-diagram" />
    <div align="center"><em>Image 2. SLR Process tasks.</em></div>
</svg>

[Back to top](#review-process)

---
## STAGE-1: Plan (protocol definition and quality control)

In the planning stage, the protocol is specified and iterated until it satisfies quality controls according to the process tasks in [Image 2](#image-2-slr-process-tasks).

### Protocol Artifacts

The protocol is defined through the following artifacts:

- **Research Questions (RQs)** (object **O-01**)
- **Data Sources & Strategy** (object **O-02**)
- **Search String(s)** tailored per source (object **O-03**)
- **Inclusion \& Exclusion Criteria (IC \& EC)** (object **O-04**)
- **Approved Protocol** after review (object **O-05**)

### PICO Strategy (search framing)

The search strategy is refined using PICO:

- **Population:** studies (2010–2020, updated to 2024) on DA in software architecture or development
- **Intervention:** application of DA aligned with the RQs
- **Comparison:** no external control group; the search is repeated (2020 and 2024) for internal comparison
- **Outcomes:** identify the state and trends of DA in software architecture/development

The full PICO strategy is documented in [PICO Strategy](../protocol/md/pico_strategy.md)
<!-- --8<-- "md/pico_strategy.md:pico-table -->

### Search Strings

Search queries are adapted to each data source and include relevance sorting and time filters. The repository records the final strings and parameters in:

- [protocol/md/search_string.md](../protocol/md/search_string.md)

### Inclusion \& Exclusion Criteria

Screening applies explicit IC/EC checks that constrain the corpus by:

- **Time relevance:** 2010–2020 (or 2010–2024 for update)
- **Availability:** full text accessible via the sources
- **Type:** article / conference paper / journal / proceedings
- **Keyword alignment:** title/abstract must align with DA + software architecture/development framing
- **Metadata sanity:** exclude items without title/authors/DOI/abstract
- **Language:** English or Spanish

Full criteria are documented in:

- [protocol/md/inclusion_exclusion_criteria.md](../protocol/md/inclusion_exclusion_criteria.md)

### Quality Checkpoint (protocol)

A protocol-quality decision gate (**C-01**) is used to decide whether the protocol is sufficient or must be updated.

[Back to top](#review-process)

---

## STAGE-2: Execute (search, screening, and corpus curation)

This stage operationalizes the protocol:

1. **Execute the search strings** in each academic archive (task **T-007**)
2. **Collect documents and metadata** into a candidate list (task **T-008**, object **O-06**)
3. **Apply IC/EC** to select relevant studies (task **T-009**, object **O-07**)
4. **Export to Zotero** and build a curated primary-studies knowledge base (data source **DS-02**)
5. **Extract required data and metadata** into a standardized form (task **T-010**)
6. **Iteratively refine** search strings/strategy if inconsistencies are found (task **T-011**, decision **C-02**)

### Data and Metadata Extraction Schema

Each retained study is analyzed using standardized fields:

- **Significant Data (SD):** title, abstract, keywords, authors, methodology, tools, results, limitations, future directions, references
- **Significant Metadata (SMD):** source, venue, date added, year, DOI, type

Schema is documented in:

- [protocol/md/data_metadata_fields.md](../protocol/md/data_metadata_fields.md)

### Current Corpus Snapshot (from Zotero export in this repo)

The current in-repo Zotero exports show:

- **Primary studies (CSV items):** 6 records in [data/zotero/primary-studies.csv](../data/zotero/primary-studies.csv)
- **Publication years observed:** minimum **2008**, maximum **2022** (note: this is a snapshot of what is currently exported in the repo, not necessarily the final set for the 2010–2024 update)
- **Zotero report export:** [data/zotero/report.pdf](../data/zotero/report.pdf) and [data/zotero/report.htm](../data/zotero/report.htm)

[Back to top](#review-process)

---
## STAGE-3: Report (synthesis, mapping, and final quality control)

In the reporting stage, the curated corpus is synthesized and mapped to answer the RQs and produce the final report.

### Synthesis and NLP-assisted Analysis

- Documents are loaded into the **Voyant** NLP tool (data source **DS-03**) for:

    - semantic consistency checks
    - vocabulary density and readability estimation
    - visualization (e.g., Cirrus, collocates graphs)
    - topic modeling via **Latent Dirichlet Allocation (LDA)**

### Systematic Mapping

Primary studies are categorized using a mapping schema with four top-level categories:

- **CAT-01 Subjects** (topics/focus areas)
- **CAT-02 Methods** (research approaches)
- **CAT-03 Tools** (software/technologies)
- **CAT-04 Outcomes** (results, limitations, future directions)

Schema is documented in:

- [protocol/md/map_categories.md](../protocol/md/map_categories.md)

### Snowballing

Forward/backward snowballing is applied to expand the primary studies set (task **T-013**) and to support comprehensive synthesis.

### Quality Assurance for Study Selection

After title/abstract screening, content is evaluated with **Quality Features (QF)** scored as:

- **YES:** 1.0
- **PARTIAL:** 0.5
- **NO:** 0.0

Documents with average score **≥ 0.75** are accepted as *Primary Studies*. Voyant is also used to check thematic consistency.

### Final Quality Checkpoint (report)

A report-quality decision gate (**C-03**) is used to decide whether to adjust NLP/mapping/insights or to finalize the report.

[Back to top](#review-process)

---
## REFERENCES
<!-- internal references -->


<!-- external references -->
1. Kitchenham, B., & Charters, S. (2007). Guidelines for performing systematic literature reviews in software engineering. EBSE Technical Report.
2. 
3. Petersen, K., Feldt, R., Mujtaba, S., & Matt
   sson, M. (2008). Systematic mapping studies in software engineering. In EASE.
4. Budgen, D., Turner, M., Brereton, P., & Kitchenham, B. (2008). Using mapping studies in software engineering. In EASE.
5. Wohlin, C., Runeson, P., Höst, M., Ostlund, Å., & Regnell, B. (2012). Experimentation in software engineering. Springer.

[Back to top](#review-process)

---