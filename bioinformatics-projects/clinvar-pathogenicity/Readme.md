# ClinVar Pathogenicity Analysis

### Project Overview  
This project analyzes genetic variant data from the **ClinVar** database to explore the distribution of clinical significance classifications — such as *Pathogenic*, *Benign*, *Likely Benign*, and *Uncertain Significance*.  
The goal is to better understand how variant classifications are represented and to prepare this dataset for downstream bioinformatics or machine-learning analyses.

---

### Objectives  
- Load and process the large **ClinVar Variant Summary** dataset efficiently.  
- Summarize the number of variants by clinical significance label.  
- Save results in a structured, reusable format for future analysis.  

---

### Dataset  
**Source:** NCBI ClinVar Variant Summary file (`variant_summary.txt`)  
- Format: Tab-separated text file (`.txt`)  
- Size: ~3.3 GB (contains millions of genetic variant records)  
- Key column used: `ClinicalSignificance`

---

### Project Structure  
```
bioinformatics-projects/
└── clinvar-pathogenicity/
├── data/
│ ├── raw/
│ └── processed/
├── src/
│ ├── analysis/
│ │ ├── pathogenicity_analysis.py
│ │ └── preview_data.py
│ └── utils/
├── reports/
│ └── pathogenicity_counts.csv
├── tests/
├── requirements.txt
└── Readme.md
```

---

### How to Run  
1. Place your **variant_summary.txt** file inside `data/raw/`.  
2. Open a terminal and run:
   ```bash
   python -m src.cli --csv data/raw/variant_summary.txt --counts

### Example Output

Below is a snippet of the generated `pathogenicity_counts.csv`, summarizing ClinVar classifications of pathogenicity:

| Clinical Significance                                  | Count     |
|--------------------------------------------------------|-----------:|
| Uncertain significance                                 | 3,922,803 |
| Likely benign                                          | 2,001,603 |
| Benign                                                 | 426,828   |
| Pathogenic                                             | 385,693   |
| Conflicting classifications of pathogenicity           | 300,251   |
| Likely pathogenic                                      | 217,122   |
| Pathogenic / Likely pathogenic                         | 68,016    |
| Not provided                                           | 15,241    |
| Drug response                                          | 3,804     |
| Other                                                  | 3,121     |
| No classification for the single variant               | 1,394     |

*(File generated at `reports/pathogenicity_counts.csv`)*  

---

## Tools & Libraries Used
- Python 3.10  
- Pathlib  
- VS Code  
- Git & GitHub


