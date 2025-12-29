# 📚 Kredel's Work

## 📄 **Document Summaries**

**1. Kredel et al. (2013) – *A Simple Concept for the Performance Analysis of Cluster-Computing***

Proposes a dimensionless speed-up model for cluster performance using key hardware and application parameters, inspired by the roofline model, and validated on HPC applications like scalar product and Linpack.

**2. Kredel et al. (2015) – *A Hierarchical Model for the Analysis of Efficiency in Cluster-Computing***

Develops a hierarchical model using abstract efficiency metrics for multi-level clusters, focusing on transparency, simplicity, and combining theoretical performance with empirical validation.

---

## 🧠 **Authors' Perspective on Numrich’s Work**

Kredel et al. recognize Numrich’s contributions as intellectually stimulating and rooted in physical analogies (mechanics and dimensional analysis), especially in *Computer Performance Analysis and the Pi Theorem* and  *Computational Force* , but they critique these approaches for being overly abstract and detached from practical performance modeling.

They argue that:

* **Numrich's mechanical analogy** , particularly the  *principle of computational least action* , while elegant, struggles to integrate real-world aspects like parallel architecture, complex software, and communication costs.
* **His use of the Buckingham Pi-theorem** introduces theoretical dimensionless metrics, which they acknowledge as insightful for hardware/software co-design but not sufficiently practical for deriving "thumb rules" needed in cluster computing.
* Ultimately, they seek to simplify and ground performance modeling in fewer, empirically verifiable parameters, which they believe is more actionable in modern heterogeneous systems.
