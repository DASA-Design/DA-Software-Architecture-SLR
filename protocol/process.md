# PROTOCOL

Comprehensive documentation of the systematic literature review (SLR) methodology, process artifacts, and quality controls for the study on Dimensional Analysis (DA) in Software Architecture. This document describes the protocol components, process stages, decision points, and supporting documentation that guide the review from planning through execution to final reporting.

[Back to top](#protocol-profile)

---

## Overview

The [protocol/](./) folder contains all methodological documentation, process artifacts, and visual models that define and guide the SLR execution. The protocol follows established guidelines from Kitchenham & Charters (2007) and Petersen et al. (2008) for systematic reviews in software engineering.

The protocol is organized into three main components:

1. **[Process Documentation](md/):** Methodological specifications, criteria, and schema definitions.
2. **[Visual Models](img/):** BPMN 2.0 workflow diagrams illustrating the three-stage review process and tasks.

**Review Scope:**

- **Goal:** Identify current state, applications, tools, contributions, limitations, and gaps related to DA in software architecture/development.
- **Time Windows:** 2010–2020 (initial phase) and 2010–2024 (update phase).
- **Academic Sources:** ACM Digital Library, ASME Digital Collection, IEEE Xplore, ScienceDirect, SpringerLink.
- **Research Questions:** 3 core questions (RQ-01, RQ-02, RQ-03) addressing applications, engineering practices, and tooling.

[Back to top](#protocol-profile)

---

## Directory Structure

### 1. Process Documentation ([`md/`](md/))

Contains structured markdown files defining all protocol components, from research questions to data extraction schemas.

#### 1.1 Core Protocol Components

| File                                                                             | Object ID | Purpose                 | Content Summary                                                                    |
| -------------------------------------------------------------------------------- | --------- | ----------------------- | ---------------------------------------------------------------------------------- |
| **[`research_questions.md`](md/research_questions.md)**                     | O-01      | Define review scope     | 3 research questions (RQ-01, RQ-02, RQ-03) with rationale aligned to PICO strategy |
| **[`pico_strategy.md`](md/pico_strategy.md)**                               | O-02      | Frame search strategy   | Population, Intervention, Comparison, Outcomes framework for systematic searching  |
| **[`academic_sources.md`](md/academic_sources.md)**                         | O-02      | Specify data sources    | 3 data sources (DS-01: Scientific Archives, DS-02: Zotero, DS-03: Voyant Tools)    |
| **[`search_string.md`](md/search_string.md)**                               | O-03      | Document search queries | Search strings customized for each academic database with filters and time periods |
| **[`inclusion_exclusion_criteria.md`](md/inclusion_exclusion_criteria.md)** | O-04      | Define selection rules  | 5 inclusion criteria (IC-01 to IC-05) and 6 exclusion criteria (EC-01 to EC-06)    |

**Research Questions:** Three core questions address DA applications (RQ-01), engineering practices (RQ-02), and tooling infrastructure (RQ-03), each aligned with the PICO intervention scope for the 2010-2024 study population. See [research_questions.md](md/research_questions.md) for complete question text and rationale.

**PICO Strategy:** Frames the search targeting DA studies in software architecture (Population), intervention applications aligned with research questions, internal temporal comparison (2020 vs. 2024), and outcomes identifying current state and trends. See [pico_strategy.md](md/pico_strategy.md) for framework details.

**Academic Sources:** Five major databases (ACM, ASME, IEEE Xplore, ScienceDirect, SpringerLink) spanning computing, engineering, and multidisciplinary research, plus reference management (Zotero) and text analytics (Voyant). See [academic_sources.md](md/academic_sources.md) for data source descriptions.

**Search Strings:** Database-specific Boolean queries combining DA core concepts ("dimensional analysis", "pi theorem") with software domain terms, filtered by publication period (2010-2020/2024) and relevance ranking. See [search_string.md](md/search_string.md) for complete queries per source.

**Inclusion Criteria:** Five criteria (IC-01 to IC-05) ensure documents are temporally relevant (2010-2024), accessible, scholarly (articles/proceedings), and keyword-aligned in title and abstract with DA and software architecture themes.

**Exclusion Criteria:** Six criteria (EC-01 to EC-06) reject documents lacking essential metadata (title, authors, DOI, abstract), books/chapters, or non-English/Spanish publications. See [inclusion_exclusion_criteria.md](md/inclusion_exclusion_criteria.md) for complete IC/EC specifications.

#### 1.2 Process Architecture

| File                                                       | Purpose                 | Content Summary                                                                  |
| ---------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------- |
| **[`process_summary.md`](md/process_summary.md)**     | Document workflow tasks | 19 process tasks (T-001 to T-019) across Plan-Execute-Report stages              |
| **[`process_objects.md`](md/process_objects.md)**     | Catalog data objects    | 12 data objects (O-01 to O-12) from research questions to final report           |
| **[`process_decisions.md`](md/process_decisions.md)** | Define quality gates    | 3 decision checkpoints (C-01, C-02, C-03) for protocol, selection, and reporting |

**Process Tasks:** 19 sequential tasks (T-001 to T-019) organized across Plan (protocol definition and validation), Execute (search, screening, data extraction), and Report (synthesis, mapping, quality control) stages. See [process_summary.md](md/process_summary.md) for task descriptions.

**Data Objects:** Process generates and transforms 12 artifacts (O-01 to O-12) from research questions through approved protocol, found documents, primary studies, extracted data, classification schemes, systematic maps, to final survey report. See [process_objects.md](md/process_objects.md) for object catalog.

**Decision Checkpoints:** Three quality gates (C-01, C-02, C-03) validate protocol quality, document selection, and report standards at stage transitions, enabling iterative refinement when criteria aren't met. See [process_decisions.md](md/process_decisions.md) for decision point specifications.

#### 1.3 Data Extraction and Classification

| File                                                             | Object ID | Purpose                      | Content Summary                                                          |
| ---------------------------------------------------------------- | --------- | ---------------------------- | ------------------------------------------------------------------------ |
| **[`data_metadata_fields.md`](md/data_metadata_fields.md)** | O-08      | Define extraction schema     | 10 data fields (SD-01 to SD-10) and 6 metadata fields (SMD-01 to SMD-06) |
| **[`map_categories.md`](md/map_categories.md)**             | O-09      | Define classification scheme | 4 mapping categories (CAT-01 to CAT-04) for systematic classification    |

**Data Extraction Schema:** Standardized extraction captures 10 Significant Data fields (SD-01 to SD-10) covering bibliographic information, methodology, tools, results, limitations, and future directions, plus 6 Significant Metadata fields (SMD-01 to SMD-06) for source tracking and classification. See [data_metadata_fields.md](md/data_metadata_fields.md) for complete schema.

**Classification Mapping:** Four-category scheme (CAT-01 to CAT-04) classifies studies by Subjects (topics/concepts), Methods (research techniques), Tools (software/instruments), and Outcomes (findings/conclusions). See [map_categories.md](md/map_categories.md) for category definitions.

[Back to top](#protocol-profile)

---

### 2. Visual Models ([`img/`](img/))

BPMN 2.0 workflow diagrams illustrating the three-stage review process with tasks, objects, decision gates, and data flows.

#### 2.1 PNG Format ([`img/png/`](img/png/))

Raster images for presentations, reports, and web documentation:

| File                                                                  | Description         | Content                                                                                       |
| --------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| **[`01 - SLR Method.png`](img/png/01%20-%20SLR%20Method.png)**   | High-level overview | Three-stage SLR process (Plan → Execute → Report) with quality checkpoints C-01, C-02, C-03 |
| **[`02 - SLR Process.png`](img/png/02%20-%20SLR%20Process.png)** | Detailed workflow   | Complete BPMN diagram with 19 tasks, 12 objects, 3 decision gates, and 3 data sources         |

**Figure 1: SLR Method Overview**

![SLR Method Overview](img/png/01%20-%20SLR%20Method.png)

*The three-stage systematic literature review methodology showing Plan (protocol definition), Execute (search and screening), and Report (synthesis and mapping) phases with quality control checkpoints between stages.*

**Figure 2: SLR Process Tasks**

![SLR Process Tasks](img/png/02%20-%20SLR%20Process.png)

*Detailed BPMN 2.0 workflow diagram illustrating all 19 process tasks, data objects (O-01 to O-12), decision gates (C-01 to C-03), and data sources (DS-01: Academic Archives, DS-02: Zotero, DS-03: Voyant Tools). Shows complete information flow from research question definition through final report delivery.*

#### 2.2 SVG Format ([`img/svg/`](img/svg/))

Scalable vector graphics for publication-quality documentation and editing:

| File                                                                  | Description                  | Purpose                                    |
| --------------------------------------------------------------------- | ---------------------------- | ------------------------------------------ |
| **[`01 - SLR Method.svg`](img/svg/01%20-%20SLR%20Method.svg)**   | High-level overview (vector) | Editable, scalable version for publication |
| **[`02 - SLR Process.svg`](img/svg/02%20-%20SLR%20Process.svg)** | Detailed workflow (vector)   | Editable, scalable version for publication |

**Purpose:** BPMN diagrams provide standardized visual representation of the SLR methodology, ensuring transparency, reproducibility, and clarity in communicating the research process. They serve as:

- Training materials for research team members
- Documentation for methodological rigor in publications
- Reference guides during protocol execution
- Quality assurance tools for process validation

[Back to top](#protocol-profile)

---

## Process Flow Summary

The SLR methodology flows through three interconnected stages with iterative quality controls:

```
STAGE 1: PLAN (Protocol Definition)
├─> T-001: Define Research Questions (O-01) ─────────────┐
├─> T-002: Specify Search Strategy (O-02)                │
├─> T-003: Create Search Strings (O-03)                  │
├─> T-004: Define Inclusion/Exclusion Criteria (O-04)    │
├─> T-005: Review Protocol Quality                       │
├─> C-01: Protocol Quality Check ◄───────────────────────┘
│        ├─ YES → Continue to Execute
│        └─ NO → T-006: Update Protocol (iterate)
│
STAGE 2: EXECUTE (Search and Screening)
├─> T-007: Execute Search Strings in DS-01 ──────────────┐
├─> T-008: Collect Documents and Metadata (O-06)         │
├─> T-009: Apply IC/EC Criteria (O-07)                   │
├─> T-010: Extract Data/Metadata to DS-02                │
├─> C-02: Selection Criteria Check ◄─────────────────────┘
│        ├─ YES → Continue to Report
│        └─ NO → T-011: Update Search Strategy (iterate)
│
STAGE 3: REPORT (Synthesis and Mapping)
├─> T-012: Synthesize Document Data (O-08)
├─> T-013: Perform Snowballing References
├─> T-014: Create Classification Mapping (O-09)
├─> T-015: Classify Documents via DS-03 (O-10)
├─> T-016: Summarize Findings (O-11)
├─> T-017: Review Report Quality
├─> C-03: Report Quality Check
│        ├─ YES → T-019: Deliver Report (O-12)
│        └─ NO → T-018: Update Report (iterate)
│
FINAL OUTPUT: O-12 (Survey Report)
```

**Key Decision Gates:**

- **C-01 (Protocol Quality):** Validates completeness of research questions, search strategy, criteria, and overall protocol design
- **C-02 (Selection Quality):** Ensures documents meet IC/EC criteria and represent relevant primary studies
- **C-03 (Report Quality):** Confirms synthesis quality, mapping completeness, and reporting standards

**Data Source Integration:**

- **DS-01 (Academic Archives):** Source of candidate documents via search execution
- **DS-02 (Zotero):** Reference management for primary studies curation and metadata organization
- **DS-03 (Voyant Tools):** Text analytics for classification, topic modeling, and thematic validation

[Back to top](#protocol-profile)

---

## Quality & Reproducibility

### Methodological Rigor

**Adherence to Guidelines:**

- ✅ Follows Kitchenham & Charters (2007) SLR guidelines for software engineering
- ✅ Incorporates Petersen et al. (2008) systematic mapping principles
- ✅ Implements Wohlin et al. (2012) quality assessment framework
- ✅ Uses PICO strategy for structured search formulation

**Transparency:**

- ✅ All protocol components documented in structured markdown files
- ✅ Search strings explicitly recorded for each database
- ✅ Inclusion/exclusion criteria clearly defined with unique IDs
- ✅ Process tasks, objects, and decisions formally specified
- ✅ BPMN 2.0 diagrams provide visual workflow documentation

**Reproducibility:**

- ✅ Complete protocol available in version-controlled repository
- ✅ Search strings replicable across academic databases
- ✅ Data extraction schema standardized with 16 fields (10 SD + 6 SMD)
- ✅ Classification scheme defined with 4 systematic categories
- ✅ Quality checkpoints ensure consistent application of criteria

### Quality Control Mechanisms

**Protocol Quality (C-01):**

- Research questions aligned with PICO strategy
- Search strings validated against pilot searches
- IC/EC criteria tested for clarity and applicability
- Expert review of protocol completeness

**Selection Quality (C-02):**

- Dual screening for IC/EC application (title/abstract → full text)
- Inter-rater reliability checks for subjective criteria
- Quality features scoring (YES: 1.0, PARTIAL: 0.5, NO: 0.0)
- Acceptance threshold: average score ≥ 0.75

**Report Quality (C-03):**

- Voyant Tools analysis for thematic consistency validation
- Mapping coverage across all 4 categories (CAT-01 to CAT-04)
- Snowballing completeness verification
- Synthesis alignment with research questions
- Peer review of findings and conclusions

### Data Management

**Version Control:**

- Protocol components tracked in Git repository
- Changes documented through commit history
- Iterative refinements traceable through version diffs

**Storage and Organization:**

- Structured folder hierarchy (protocol/md/, protocol/img/)
- Consistent file naming conventions
- Cross-references via markdown links
- Preservation of both PNG (web) and SVG (publication) formats

**Metadata Preservation:**

- Original search results preserved in [data/bibliography/](../data/bibliography/)
- Primary studies curated in [data/zotero/](../data/zotero/)
- Analysis outputs archived in [data/voyant/](../data/voyant/)

### Validation Checkpoints

| Stage             | Validation Activity           | Acceptance Criteria                                                   |
| ----------------- | ----------------------------- | --------------------------------------------------------------------- |
| **Plan**    | Protocol peer review          | All components (RQ, PICO, search strings, IC/EC) complete and aligned |
| **Execute** | IC/EC application consistency | Inter-rater agreement ≥ 80% on sample of 20% of documents            |
| **Execute** | Quality features scoring      | Primary studies achieve average QF score ≥ 0.75                      |
| **Report**  | Thematic consistency check    | Voyant analysis confirms keyword alignment with research questions    |
| **Report**  | Mapping completeness          | All primary studies classified across CAT-01 to CAT-04                |
| **Report**  | Synthesis validation          | Findings directly traceable to primary study evidence                 |

[Back to top](#protocol-profile)

---

## Protocol Execution Summary

**Current Status:**

- **Protocol Phase:** Completed and approved (O-05)
- **Search Execution:** Completed for 2010-2020 and 2010-2024 time windows
- **Primary Studies:** 6 studies curated in Zotero (O-07)
- **Analysis Phase:** Voyant Tools analysis completed
- **Reporting Phase:** In progress

**Key Milestones:**

1. ✅ Research questions defined (RQ-01, RQ-02, RQ-03)
2. ✅ PICO strategy formulated and validated
3. ✅ Search strings customized for 5 academic databases
4. ✅ IC/EC criteria established (5 IC + 6 EC)
5. ✅ Protocol quality checkpoint passed (C-01)
6. ✅ Search execution completed across all sources
7. ✅ Screening and selection completed (C-02 passed)
8. ✅ Primary studies exported to Zotero (6 documents)
9. ✅ Data extraction schema applied (SD-01 to SD-10, SMD-01 to SMD-06)
10. ✅ Classification mapping scheme defined (CAT-01 to CAT-04)
11. 🔄 Synthesis and mapping in progress
12. ⏳ Final report quality checkpoint pending (C-03)

**Document References:**

- Full bibliography: [data/bibliography/](../data/bibliography/)
- Primary studies: [data/zotero/primary-studies.csv](../data/zotero/primary-studies.csv)
- Analysis outputs: [data/voyant/](../data/voyant/)
- Analytical insights: [analysis/insights.md](../analysis/insigths.md)

[Back to top](#protocol-profile)

---

## References

**SLR Methodology Guidelines:**

1. Kitchenham, B., & Charters, S. (2007). *Guidelines for performing systematic literature reviews in software engineering.* EBSE Technical Report EBSE-2007-01.
2. Petersen, K., Feldt, R., Mujtaba, S., & Mattsson, M. (2008). *Systematic mapping studies in software engineering.* In Proceedings of the 12th International Conference on Evaluation and Assessment in Software Engineering (EASE).
3. Budgen, D., Turner, M., Brereton, P., & Kitchenham, B. (2008). *Using mapping studies in software engineering.* In Proceedings of PPIG 2008.
4. Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering.* Springer Science & Business Media.

**PICO Strategy:**

5. Petticrew, M., & Roberts, H. (2008). *Systematic reviews in the social sciences: A practical guide.* John Wiley & Sons.

**BPMN Notation:**

6. Object Management Group (OMG). (2011). *Business Process Model and Notation (BPMN) Version 2.0.* OMG Document Number: formal/2011-01-03.

[Back to top](#protocol-profile)

---

*Last Updated: December 29, 2025*
