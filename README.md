🧬 **Unravelling Klebsiella pneumoniae ST307 Through Genome Annotation and PPI Analysis**

A bioinformatics-driven study to explore potential therapeutic targets in *Klebsiella pneumoniae* ST307, an emerging multidrug-resistant (MDR) clone associated with hospital outbreaks worldwide.

---
## 🔍 **Project Workflow**

               +------------------------------+
               |   Download Genome Data       |
               |   (NCBI Assemblies ~1500)    |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               |    Quality Assessment        |
               |    (FastQC + QUAST)          |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               |    Select High-Quality       |
               |    Genomes (n = 886)         |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               |   Functional Annotation       |
               |   (Prokka, ~4.5L proteins)   |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               | Filter Non-Hypothetical,     |
               | Non-Redundant Proteins       |
               | (Final: 3,920 unique)        |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               | Protein-Protein Interaction  |
               | Network via STRING-db        |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               | Network Analysis in Cytoscape|
               | (CytoHubba Plugin)           |
               | Metrics: Degree, MCC, DMNC,  |
               | Bottleneck, Closeness        |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               |    Consensus Hub Genes       |
               |  Identified via Overlap      |
               |  (Multiple Centralities)     |
               +---------------+--------------+
                               |
                               v
               +------------------------------+
               |  Final Target Genes (n = 6)  |
               |                              |
               |                              |
               +------------------------------+

 **Selected Therapeutic Target Candidates**

```text
prsA metG pheT guaA arcB smpB
```

These genes are involved in key metabolic or stress-related pathways in the pathogen.

---

**Methods, Tools & Technical Skills**

- **Genome Quality Control**: FastQC, QUAST  
- **Annotation & Data Parsing**: Prokka, Python (Pandas), Bash scripting  
- **PPI Network Construction**: STRING database  
- **Network Analysis & Hub Gene Detection**: Cytoscape, cytoHubba  
- **File Handling & Visualization**: Excel/TSV, Matplotlib, Cytoscape



**Future Directions**

This work lays the foundation for downstream analyses such as druggability prediction, structure-based virtual screening, and molecular dynamics simulations of shortlisted target proteins. Future efforts will also involve comparative genomic analysis with other *Klebsiella* sequence types to identify clone-specific vulnerabilities and assess the evolutionary conservation of these hub genes. Ultimately, the goal is to transition from in silico discovery to wet-lab validation, guiding the development of novel therapeutics against MDR *K. pneumoniae* ST307.

---

## ✉️ **Contact**

For queries or collaborations:  
**[Your Name]** – [raghava.3324102gmail.com]  
GitHub: [github.com/Raghu-102433]

