## 🔍 **RQ-03: What are the software tools associated with Dimensional Analysis?**

### ✅ **Summary:**

The primary software tools associated with Dimensional Analysis (DA) include symbolic computation libraries, numerical modeling environments, and benchmarking utilities. These tools are used to compute π-groups, simulate runtime models, analyse performance metrics, and automate dimensional reduction in software architecture and development contexts.

---

### 📚**Evidence List:**

| ID    | Document Title                                              | Software Tools Associated with DA                                                                                  |
| ----- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| PS-01 | *Implementation of Buckingham's Pi Theorem Using Python*  | Python libraries (SymPy, NumPy), Jupyter Notebooks for symbolic computation and automation of π-group generation. |
| PS-02 | *Self-Similarity of Parallel Machines*                    | Custom benchmarking tools using runtime data from SGI Altix XE1300 and IBM Blade Cluster.                          |
| PS-03 | *Computer Performance Analysis and the Pi Theorem*        | Dimensional matrix modeling; analytical scripts (likely symbolic or algebraic tools, though not explicitly named). |
| PS-04 | *Computational Forces in the SAGE Benchmark*              | Custom performance modeling using the SAGE benchmark (SAIC’s Adaptive Grid Eulerian hydrocode).                   |
| PS-05 | *Computational Forces in the Linpack Benchmark*           | Benchmarking suites like LINPACK, along with analytical reduction tools for force ratio modeling.                  |
| PS-06 | *Dimensional Analysis Applied to a Parallel QR Algorithm* | Mathematical modeling environments and symbolic algebra to derive dimensional matrices and compare algorithms.     |

### 🛠️**Common Tool Types:**

* **Symbolic computation frameworks** (e.g., SymPy in Python)
* **Benchmarking platforms** (e.g., LINPACK, SAGE)
* **Algebraic modeling tools** (for performance decomposition)
* **Execution environment instrumentation** (to collect runtime data for dimensional comparisons)

### 🧠 **Patterns:**

* **Symbolic Tools:** Python libraries like **SymPy** automate π-group computation, mainly in fluid mechanics (PS-01).
* **Benchmarks as Proxies:** Tools like **SAGE** and **LINPACK** provide structured data for DA modeling, though not DA-specific (PS-04, PS-05).
* **Custom Runtime Analysis:** Studies use tailored scripts to extract dimensionless parameters from system traces (PS-02, PS-03).
* **Lack of Specialized Tools:** No dedicated DA toolchains exist in software architecture; most rely on repurposed symbolic or benchmarking tools.
