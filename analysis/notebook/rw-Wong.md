### 📄 **Summary of PS-002: *Self-adaptive systems: A systematic literature review across categories and domains***

Wong et al.~\cite{wong_self-adaptive_2022} conducted a broad SLR of 293 studies from 1990 to 2020, organizing the self-adaptive systems (SAS). The review maps SAS evolution across five stages—from foundational theory to domain-specific applications like IoT and IaaS—highlighting a shift from conceptual to practical and tool-supported research. Key findings reveal a strong focus on web services and cloud systems, a dominance of simulations and quantitative evaluations, and a lack of empirical methods (under 8\%). Although a variety of modeling strategies are used, trade-off mechanisms and feedback loop strategies remain mostly heuristic, with limited formalism.

Wong et al. (2022) conducted a comprehensive systematic literature review (SLR) to synthesize the state of the art in self-adaptive systems (SAS), addressing gaps left by previous, more narrowly focused reviews. Their aim was to map the evolution, research categories, and application domains of SAS from 1990 to 2020.

### 🔗 **Relation to Numrich’s Work**

While Wong et al. provide a descriptive landscape of SAS development, they uncover an absence of structured, physics-inspired modeling frameworks—precisely the niche addressed by Numrich’s application of Dimensional Analysis (DA) in computing. Numrich’s work introduces dimensionless modeling and similarity theory to systematically characterize performance behaviors in computational systems—tools that could enhance the current SAS trade-off and feedback control strategies, which are still largely ad hoc. This contrast reinforces our SLR’s central finding:  **DA is a viable, underutilized method in software architecture** , offering a principled alternative to the informal modeling still prevalent in SAS research.

Integrating Numrich’s dimensional analysis into SAS research can strengthen the analytical rigor, facilitate cross-domain transferability, and improve the design and evaluation of adaptive mechanisms. Wong et al.’s SLR highlights the need for such formal approaches, especially as the field matures and diversifies.

Wong et al. (2022) provide a panoramic view of SAS research, revealing its evolution, dominant categories, and application domains. Their findings underscore the need for more empirical studies and formal analytical methods—areas where dimensional analysis, as advocated by Numrich, can play a pivotal role in advancing the field.

### Notes summary

#### Objective:

Wong et al. (2022) conducted a comprehensive systematic literature review (SLR) to synthesize the state of the art in self-adaptive systems (SAS), addressing gaps left by previous, more narrowly focused reviews. Their aim was to map the evolution, research categories, and application domains of SAS from 1990 to 2020.

#### Research Questions:

What is the current state of the art in self-adaptive systems?
How has the state of the art evolved over time?
Which are the application domains of self-adaptive systems over time?

#### Methodology:

The review followed established SLR guidelines (Kitchenham et al.).
Sources were filtered by CORE ranking (A*/A/B) within major venues (SEAMS, SASO, TAAS, ICSE, etc.).
Timeframe: 1990–2020.
Corpus: 30 primary studies, 35,903 documents screened, 293 included.

#### Key Findings

##### Research Categories

* Papers were classified into Analytical (36\%), Empirical (27\%), Technological (17\%), Methodological (12\%), and Perspectives (8\%) categories (ICSE 2014 taxonomy).
* Technological: Majority (81\%) use closed-loop approaches; focus on tools, models, frameworks, languages, architectures, algorithms. 40\% rely on simulations.
* Methodological: 70\% introduce new approaches; frameworks (15\%), analysis techniques (8\%), architectures (4\%). Evaluation is mostly quantitative (41\%) or case studies (38\%).
* Perspective: Reflections (35\%), reviews (31\%), surveys (20\%). Many outline future work (71\%), challenges (33\%), requirements (16\%), or provide taxonomies (14\%).
* Analytical: Focus on algorithms (46\%), mathematical contributions (26\%), frameworks (14\%). 94\% provide formalization.
* Empirical: Most focus on runtime (74\%), explicit monitoring (83\%) and adaptation (87\%). Adaptation is parameter-based (87\%), with quantitative (57\%) or case study (39\%) evaluation.

##### Evolution Over Time

* Five periods identified:
  * Initial Stage (1990–2002): Technological (67\%), Analytical (33\%); domains: networking, software engineering, IoT.
  * Foundational Years (2003–2005): Perspective (42\%), Technological (24\%), Methodology (16\%), Analytical (9\%), Empirical (9\%); domains: reviews, web services, load balancing, bio-inspired, IoT.
  * Ramping Up (2006–2010): Methodology (31\%), Technological (27\%), Perspective (24\%), Analytical (10\%), Empirical (8\%); domains: web services, IoT, reviews, robotics, e-commerce.
  * Last Decade – First Half (2011–2015): Technological (40\%), Methodology (32\%), Empirical (10\%), Analytical (9\%), Perspective (9\%); domains: web services, robotics, networking, IoT, ISR.
  * Last Decade – Second Half (2016–2020): Technological (41\%), Methodology (25\%), Analytical (16\%), Perspective (12\%), Empirical (6\%); domains: IoT, IaaS, web services, cyber-physical, automotive.

##### Application Domains

* Early focus: networking, software engineering, IoT.
* Later years: web services, IoT, robotics, networking, IaaS, cyber-physical systems, automotive, ISR.
* Recent trend: strong growth in cloud-based services (IoT, IaaS), bio-inspired approaches, security, and cyber-physical systems.

##### General Trends

* SAS research has shifted from theoretical/model-based foundations to holistic, practical solutions.
* Perspective papers challenge the status quo and highlight practitioner needs.
* Empirical studies remain underrepresented (<8\%), with technological and methodological papers dominating.
* Evaluation methods are mostly quantitative or case studies, with simulations common in technological work.

#### Relation to Numrich’s Work on Dimensional Analysis

Numrich’s work on Dimensional Analysis provides a rigorous framework for understanding and formalizing the relationships between variables and parameters in complex systems. In the context of Wong et al.’s SLR:

* Analytical Category: Many SAS papers (especially in the Analytical category) rely on mathematical formalization and algorithmic approaches, which can benefit from dimensional analysis to ensure consistency and scalability of adaptation mechanisms.
* Parameter Adaptation: The empirical findings show a strong focus on parameter adaptation (87\% in empirical studies). Dimensional analysis can help in identifying relevant parameters, their units, and scaling laws, improving the robustness of adaptation strategies.
* Cross-Domain Applicability: As SAS research expands into diverse domains (IoT, robotics, cyber-physical systems), dimensional analysis offers a unifying methodology to compare and transfer adaptation techniques across domains, ensuring that solutions are not domain-specific but generalizable.
* Evaluation and Simulation: Quantitative evaluation and simulation are prevalent. Dimensional analysis can enhance the design of experiments and interpretation of results, ensuring that findings are not artifacts of scale or unit inconsistencies.

##### Conclusion:

Integrating Numrich’s dimensional analysis into SAS research can strengthen the analytical rigor, facilitate cross-domain transferability, and improve the design and evaluation of adaptive mechanisms. Wong et al.’s SLR highlights the need for such formal approaches, especially as the field matures and diversifies.

##### Main Contribution:

Wong et al. (2022) provide a panoramic view of SAS research, revealing its evolution, dominant categories, and application domains. Their findings underscore the need for more empirical studies and formal analytical methods—areas where dimensional analysis, as advocated by Numrich, can play a pivotal role in advancing the field.
