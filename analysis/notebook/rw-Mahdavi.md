# 📚 Mahdavi-Hezavehi's SLR

## **Summary** :

Mahdavi-Hezavehi et al. (2017) present a systematic literature review that classifies and evaluates architectural methods for handling multiple Quality Attributes (QAs) in self-adaptive systems, identifying performance, reliability, cost, availability, and scalability as the most commonly addressed QAs, and emphasizing that most methods rely on single-loop feedback mechanisms, use utility functions and QA metrics for decision-making, and lack systematic frameworks for adaptation and trade-off management.

## **Relation to Numrich’s Work** :
Both this study and Numrich’s research aim to simplify the management of complex trade-offs and computational behaviors in software systems through modeling. However, while Mahdavi-Hezavehi et al. rely on utility functions, metrics, and ad hoc adaptation strategies, they overlook dimensional analysis as a viable and formal tool, something our SLR confirms has strong potential, as evidenced by Numrich’s application of dimensionless modeling to unify and clarify software performance dynamics. This absence underscores the gap that Numrich’s methods could fill in architectural approaches to self-adaptive systems.

## SLR Evidence Notes

### **Title**

* *A systematic literature review on methods that handle multiple quality attributes in architecture-based self-adaptive systems*

### **Short Name**

* M to H MQA

### **Publication Year**

* 2017

### **Academic Source**

* Science Direct

### **Authors**

* Mahdavi-Hezavehi, Sara
* Durelli, Vinicius H.S.
* Weyns, Danny
* Avgeriou, Paris

### **Objectives**

* To review the state-of-the-art of architecture-based methods for handling multiple QAs in self-adaptive systems and provide a descriptive analysis of the collected data from the literature.

### **Research Questions**

* RQ1: What are the characteristics of the existing architectural methods for handling multiple QAs in self-adaptive software systems?
* RQ2: Which sets of QAs are addressed by existing methods?
* RQ3: How many feedback loops are used in current methods and how are they arranged to handle multiple QAs?
* RQ4: What are the application domains of current methods dealing with multiple QAs?
* RQ5: What are the development paradigms of current methods dealing with multiple QAs?
* RQ6: What are the limitations and strengths of existing methods dealing with multiple QAs?
* RQ7: How do these methods handle multiple QAs?
* RQ8: What models are used to represent and analyse multiple QA characteristics?
* RQ9: How do these methods address multiple QA trade-offs?
* RQ10: How are the decision making and trade-off analysis of multiple QAs performed at runtime?
* RQ11: What runtime tactics/strategies are used to realize adaptation in systems dealing with multiple QAs?
* RQ12: Is the decision-making unit dealing with multiple QAs centralized or decentralized?
* RQ13: What tools/languages are used/developed to support QA trade-off in existing methods?
* RQ14: Does the method provide any evidence for validating the result of decision-making mechanism regarding satisfaction of QAs after adaptation (i.e., assurances)?

### **Methodology By**
* B. A. Kitchenham and S. Charters

### **PS Source**
* ACM Digital Library, IEEE Xplore, Science Direct, and SpringerLink

### **Review Timeline**
* 2000–2014

### **Timeframe**
* 14 years

### **Review Corpora**
* 7453 records

### **Primary Studies**
* 54 included studies

### **Result Summary**
* RQ1: Characteristics analyzed include the method, system controller, target system, and application/development domain.
* RQ2: Most addressed QAs: Performance (67\%), Cost (31\%), Reliability (28\%), Availability (19\%), Scalability (13\%).
* RQ3: Feedback loops: one (50\%), two (6\%), three (4\%), mainly for performance, cost, availability, etc.
* RQ4: Application domains: generic/unspecified (44\%), robotics (11\%), mobile apps (6\%), healthcare (4\%), transportation (4\%).
* RQ5: Development paradigms: web systems (13\%), SOA (11\%), cloud computing (6\%).
* RQ6: Strengths often discussed; top: rigorous evaluation (28\%). Weaknesses: knowledge gaps (4\%), oversimplification (9\%), space explosion (4\%).
* RQ7: Handling multiple QAs often relates to the system’s domain, goals vs side effects, model types, and prioritization.
* RQ8: Models: metrics (30\%), utility functions (22\%), Markov chains (7\%), with 30\% unidentified models and other approaches (22\%) like Petri nets and feature models.
* RQ9: Trade-offs mostly handled with utility functions (17\%), some structure-based steps and coordination (2\%).
* RQ10: Decision-making mechanisms include reference to tools/languages, control centralization, and runtime assurance evidence.
* RQ11: MAPE-K loops show proactive and reactive strategies; reactive easier but proactive preferred.
* RQ12: 35\% centralized, 19\% decentralized. QAs vary with control structure.
* RQ13: Tools: PRISM, XTEAM, Groove, Factory (trade-off support); IBM toolkit, OPERA (measurement); Languages: Stich, D-KLAPER.
* RQ14: Validation approaches: simulation (17\%), model checking (9\%), testing (17\%), runtime verification (6\%), formal proofs (2\%), etc.

### **Main Conclusion or Contribution**
* Performance, reliability, flexibility, maintainability, and availability are emphasized QAs.
* Need for better trade-off analysis and proactive mechanisms.
* Most methods use one feedback loop with ad hoc adaptation strategies and weak formal frameworks.
* QA data and utility functions help model trade-offs; testing is the most common assurance method.
