# ⬡ CodeScan — Ultimate Plagiarism Detector

**CodeScan** is a multi‑engine AI‑powered plagiarism detection system for source code. It answers the question "How similar are these two code files?" using **12+ structural, semantic, and compiler‑level detection engines**, providing a weighted similarity score and a clear verdict — all through an interactive Streamlit dashboard.

The goal is to reduce the time instructors and interviewers spend manually reviewing suspicious code, while keeping every verdict grounded in explainable, engine‑level evidence.

---

## Features

- Streamlit chat‑like interface for pasting or uploading code pairs
- Source‑backed verdicts with detailed engine‑by‑engine scores
- PDF/HTML forensic report generation
- Batch folder comparison with interactive heatmaps
- ChromaDB‑free, all‑in‑memory analysis (no external vector DB)
- Sentence‑transformer‑free; uses CodeBERT for semantic embeddings
- LangChain/OpenRouter not used — pure Python pipeline
- Dedicated analysis routes for:
    - AST & Control Flow Graph comparison
    - Winnowing (MOSS‑style) fingerprinting
    - Bytecode & Big‑O complexity matching
    - Tree Edit Distance (Zhang‑Shasha)
    - Type‑agnostic normalisation (defeats variable renaming)
    - CodeBERT semantic similarity
- Conservative verdict behaviour: no ambiguous scores; engines that fail are filtered out
- Evaluation possible through scan history and analytics dashboard

---

## Tech Stack

| Layer              | Technology                                               |
|--------------------|----------------------------------------------------------|
| Language           | Python 3.8+                                              |
| UI                 | Streamlit                                                |
| Embeddings         | CodeBERT (Hugging Face Transformers)                     |
| ML Classifier      | scikit‑learn Decision Tree                               |
| AST & Analysis     | `ast`, `zss` (optional), `dis`, `difflib`, `re`           |
| Visualisation      | Plotly, Pandas                                           |
| Storage            | SQLite (for scan history)                                |
| Package manager    | pip + virtualenv                                         |

---


## Project Structure

```text
CodeScan/
│
├── app.py                 # Main Streamlit application entry point and navigation
├── config.py              # Global configuration settings and constants
├── database.py            # SQLite database management and query handling
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
├── pages/
│   ├── analyze.py         # Single code-pair plagiarism analysis
│   ├── batch.py           # Batch comparison and similarity heatmap generation
│   ├── history.py         # Scan history and report management
│   ├── analytics.py       # Dashboard, metrics, and forensic statistics
│   ├── settings.py        # Engine configuration, sensitivity, and language options
│   └── about.py           # Application information and documentation
│
├── engines/
│   ├── codebert_engine.py # CodeBERT-based similarity detection engine
│   └── ...                # Additional plagiarism detection engine wrappers
│
└── assets/                # Optional static resources (images, styles, icons, etc.)
```

### Directory Overview

* **app.py** – Launches the Streamlit application and manages page routing.
* **pages/** – Contains all user-facing interface modules.
* **engines/** – Houses the plagiarism detection and similarity analysis engines.
* **database.py** – Stores scan results, reports, and historical records.
* **config.py** – Centralized application settings and feature flags.
* **assets/** – Stores static files used throughout the application.


---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/codescan.git
   cd codescan

2. **Create and activate a virtual environment**
  python -m venv venv
  source venv/bin/activate      # Linux/Mac
  venv\Scripts\activate         # Windows

3. **Install dependencies**
   pip install -r requirements.txt

4. **Run the Streamlit app**
   streamlit run app.py

---
   
# Main Pipeline Commands

The complete detection pipeline is fully integrated into the Streamlit application. No separate ingestion, preprocessing, or analysis scripts are required.

## Run the Application

Start the Streamlit interface using:

```bash
streamlit run app.py
```

## Analyze a Pair of Code Files

1. Open the **Analyze** page.
2. Paste the two code snippets to be compared.
3. Click **Analyze Code** to perform the forensic analysis.

## Perform Batch Comparison

1. Navigate to the **Batch Analysis** page.
2. Upload a folder containing source code files.
3. The system automatically compares all possible file pairs and generates similarity results.

## Generate Forensic Reports

Each analysis automatically produces a detailed forensic report, which can be downloaded in:

* HTML format
* Plain text format

## Machine Learning Model Retraining

The plagiarism classification model supports continuous learning and retrains automatically after every **10 high-confidence scans**. No manual retraining or external trigger is required.
## Current Status

All core plagiarism detection engines are fully functional and integrated into the analysis pipeline:

### Similarity Engines

* Sequence Similarity
* Jaccard Similarity
* N-Gram Similarity
* AST Node-Type Similarity
* Control Flow Graph (CFG) Similarity
* Winnowing Fingerprinting (MOSS-style)
* Bytecode Instruction Similarity
* Big-O Complexity Matching
* Type-Agnostic Normalization (AST + Regex Fallback)
* Tree Edit Distance (TED) *(optional)*
* CodeBERT Semantic Similarity *(lazy-loaded)*

### Machine Learning

* Adaptive ML classifier with automatic retraining
* Activates after sufficient high-confidence training samples are collected
* Continuously improves verdict accuracy over time

### Decision Engine

The system automatically filters unreliable or outlier engines, assigns higher weights to structural analysis methods, and computes a final similarity score.

A hybrid decision model combining:

* Rule-based thresholds
* Machine learning predictions

produces the final classification:

* **Original**
* **Suspicious**
* **Plagiarized**

### Analytics Dashboard

The analytics module provides:

* Scan history visualization
* Verdict distribution charts
* Similarity score trends
* Forensic statistics and performance metrics

---

## Known Limitations

### CodeBERT Requirements

* Requires an internet connection during the first execution.
* Downloads approximately **500 MB** of model data.
* Can be memory-intensive on low-resource systems.

### Tree Edit Distance (TED)

* Available only for syntactically valid Python code.
* Automatically disabled when syntax errors are detected.

### Multi-Language Support

* Non-Python languages receive partial support.
* Token-based engines remain active.
* AST, CFG, and TED analysis are currently Python-specific.

### Machine Learning Warm-Up

* The ML classifier requires approximately **10 high-confidence scans** before contributing to final verdicts.

### User Management

* No authentication or multi-user support.
* Designed primarily as a local single-user application.

### Large File Performance

* Extremely large files (>10,000 lines) may increase analysis time due to:

  * AST traversal overhead
  * Structural analysis complexity
  * CodeBERT input limitations

---

## Future Developments

Planned enhancements include:

### Multi-Language Structural Analysis

* Integrate Tree-sitter parsers for:

  * C
  * C++
  * Java
  * Additional programming languages

### Repository-Level Comparison

* Compare entire Git repositories.
* Detect cross-file and project-level plagiarism.

### Automatic Language Detection

* Implement zero-shot language identification.
* Automatically select the appropriate parsing engine.

### Cloud Deployment

* Public hosted version
* Persistent storage
* User accounts and authentication

### LLM-Assisted Explanations

* Generate human-readable explanations describing why two code samples are considered similar.

### API Integration

* REST API for headless operation.
* Integration with:

  * Learning Management Systems (LMS)
  * Automated grading platforms
  * Academic integrity tools

### Collaborative Review

* Multi-instructor review workflow
* Shared annotations on flagged code pairs
* Team-based forensic investigations

---

## License

This project was developed as part of an academic semester project for educational and research purposes.

---

## Contributors

| Name           | Role                               | GitHub  |
| -------------- | ---------------------------------- | ------- |
| Rahoul Kumar | Lead Developer & ML Pipeline       | @CodeWithRahoul |
| Muhammad Hamza  | UI/UX Design & Backend Integration | @MuhammadHamza2210 |
| Abdullah Arif    | Feature Engineering & Testing      | @Abdullah  |



