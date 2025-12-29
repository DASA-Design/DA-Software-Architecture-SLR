# 📚 Wong et al.'s SAS Systematic Review

## **Summary**

Wong et al. (2022) conducted a comprehensive systematic literature review (SLR) of 293 studies from 1990 to 2020, synthesizing the state of the art in self-adaptive systems (SAS) across research categories and application domains. The review addresses gaps left by previous narrowly focused reviews, mapping SAS evolution through five temporal stages: from foundational theory (1990-2002) to domain-specific applications in IoT, IaaS, and cyber-physical systems (2016-2020). Key findings reveal a shift from conceptual to practical, tool-supported research, with strong emphasis on web services and cloud systems. The study identifies dominance of simulations and quantitative evaluations, systematic underrepresentation of empirical methods (under 8%), and limited formalism in trade-off mechanisms and feedback loop strategies, which remain largely heuristic.

## **Relation to Numrich's Work**

Wong et al.'s panoramic view of SAS development reveals a critical absence: structured, physics-inspired modeling frameworks for characterizing system behavior. This gap aligns precisely with Numrich's application of Dimensional Analysis (DA) in computational performance. While Wong et al. document ad hoc trade-off mechanisms and informal feedback control strategies prevalent in SAS research, Numrich demonstrates how dimensionless modeling and similarity theory can systematically characterize performance behaviors through formal scaling laws. This contrast reinforces our SLR's central finding: **DA is a viable, underutilized method in software architecture**, offering principled alternatives to the informal modeling still dominant in SAS research. Integrating dimensional analysis into SAS could strengthen analytical rigor, facilitate cross-domain transferability of adaptation techniques, and improve design and evaluation of adaptive mechanisms, addressing the need for formal approaches highlighted by Wong et al. as the field matures and diversifies.

## SLR Evidence Notes

### **Title**

* *Self-adaptive systems: A systematic literature review across categories and domains*

### **Short Name**

* Wong SAS SLR

### **Publication Year**

* 2022

### **Academic Source**

* ACM Computing Surveys (CORE A*)

### **Authors**

* Wong, Wai Ting
* Oliveira, Tiago Boldt
* Cámara, Javier
* Garlan, David

### **Objectives**

* To synthesize the state of the art in self-adaptive systems (SAS) across research categories and application domains
* To map the evolution of SAS research from 1990 to 2020
* To address gaps left by previous, narrowly focused reviews
* To identify trends in research approaches, evaluation methods, and application domains

### **Research Questions**

* RQ1: What is the current state of the art in self-adaptive systems?
* RQ2: How has the state of the art evolved over time?
* RQ3: Which are the application domains of self-adaptive systems over time?

### **Methodology By**

* Kitchenham et al. SLR guidelines

### **PS Source**

* CORE ranking (A*/A/B) venues: SEAMS, SASO, TAAS, ICSE, ICAC, and related conferences/journals

### **Review Timeline**

* 1990-2020

### **Timeframe**

* 30 years

### **Review Corpora**

* 35,903 documents screened

### **Primary Studies**

* 293 included studies

### **Result Summary**

* **RQ1 - Research Categories (ICSE 2014 taxonomy):**

  - Analytical (36%): Focus on algorithms (46%), mathematical contributions (26%), frameworks (14%). 94% provide formalization.
  - Empirical (27%): Focus on runtime (74%), explicit monitoring (83%) and adaptation (87%). Parameter-based adaptation (87%), quantitative evaluation (57%) or case studies (39%).
  - Technological (17%): Closed-loop approaches (81%), tools, models, frameworks, languages, architectures, algorithms. Simulations (40%).
  - Methodological (12%): New approaches (70%), frameworks (15%), analysis techniques (8%), architectures (4%). Quantitative evaluation (41%) or case studies (38%).
  - Perspectives (8%): Reflections (35%), reviews (31%), surveys (20%). Future work (71%), challenges (33%), requirements (16%), taxonomies (14%).
* **RQ2 - Evolution Over Time:**

  - **Initial Stage (1990-2002):** Technological (67%), Analytical (33%). Domains: networking, software engineering, IoT.
  - **Foundational Years (2003-2005):** Perspective (42%), Technological (24%), Methodology (16%), Analytical (9%), Empirical (9%). Domains: reviews, web services, load balancing, bio-inspired, IoT.
  - **Ramping Up (2006-2010):** Methodology (31%), Technological (27%), Perspective (24%), Analytical (10%), Empirical (8%). Domains: web services, IoT, reviews, robotics, e-commerce.
  - **Last Decade - First Half (2011-2015):** Technological (40%), Methodology (32%), Empirical (10%), Analytical (9%), Perspective (9%). Domains: web services, robotics, networking, IoT, ISR.
  - **Last Decade - Second Half (2016-2020):** Technological (41%), Methodology (25%), Analytical (16%), Perspective (12%), Empirical (6%). Domains: IoT, IaaS, web services, cyber-physical, automotive.
* **RQ3 - Application Domains:**

  - Early focus: networking, software engineering, IoT
  - Mid-period: web services, IoT, robotics, e-commerce, load balancing
  - Recent years: IoT, IaaS (cloud infrastructure), web services, cyber-physical systems, automotive, ISR (Intelligence, Surveillance, Reconnaissance)
  - Emerging trends: strong growth in cloud-based services, bio-inspired approaches, security, cyber-physical systems
* **General Trends:**

  - Shift from theoretical/model-based foundations to holistic, practical solutions
  - Perspective papers challenge status quo and highlight practitioner needs
  - Empirical studies severely underrepresented (<8%)
  - Technological and methodological papers dominate recent years
  - Evaluation methods: primarily quantitative or case studies, with simulations common
  - Trade-off mechanisms remain largely heuristic with limited formalism
  - Feedback loop strategies lack systematic formal frameworks

### **Main Conclusion or Contribution**

* SAS research has matured from foundational theory to practical, domain-specific applications over 30 years
* The field shows systematic evolution through five distinct temporal stages, each characterized by dominant research approaches and application domains
* Technological and methodological contributions dominate, focusing on tools, frameworks, and practical solutions
* Critical gap: empirical studies remain severely underrepresented ( < 8%), limiting validation of proposed approaches
* Trade-off mechanisms and feedback control strategies are predominantly ad hoc and heuristic, lacking formal analytical frameworks
* Strong industry pull toward cloud-based systems (IoT, IaaS), cyber-physical systems, and automotive applications
* Need for formal analytical methods and increased empirical validation identified as key research priorities
* Cross-domain applicability remains challenging due to lack of unifying formal frameworks for adaptation mechanisms
