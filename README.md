# 📄 Intelligent Resume Analyzer

An AI-powered resume screening and analysis tool that automatically extracts information from resumes, generates summaries, matches candidates against job requirements, and produces comprehensive hiring reports.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![AI](https://img.shields.io/badge/AI-Transformers-orange.svg)

## ✨ Features

- 🔍 **Smart Resume Parsing** - Extract text from PDF and TXT resume files
- 🤖 **AI-Powered Summarization** - Generate intelligent summaries using transformer models
- 📊 **Skill Matching** - Match candidate skills against required and preferred job skills
- 📈 **Match Scoring** - Calculate overall match percentage with hiring recommendations
- 📋 **Multi-Format Reports** - Export reports in TXT, PDF, DOCX, Excel, and HTML formats
- 🎯 **Hiring Recommendations** - Get automated recommendations (Reject/Weak Fit/Good Fit/Strong Fit)
- 📉 **Dashboard Generation** - Create HTML dashboards for visual analysis
- 🔄 **Batch Processing** - Process multiple resumes at once

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| AI Summarization | HuggingFace Transformers |
| Embeddings | SentenceTransformers (all-MiniLM-L6-v2) |
| PDF Processing | PyPDF2 / pdfplumber |
| Report Generation | FPDF, python-docx, openpyxl |
| Data Processing | Pandas |

## 📁 Project Structure

```
Intelligent Resume Analyzer/
├── main.py                          # Main entry point
├── requirements.txt                 # Python dependencies
├── .env                             # Environment variables
├── README.md                        # Project documentation
│
├── data/
│   ├── resumes/                     # Input: Resume files (PDF, TXT)
│   └── outputs/
│       ├── reports/                 # Generated TXT reports
│       ├── *.pdf                    # PDF exports
│       ├── *.docx                   # Word exports
│       ├── match_scores.xlsx        # Excel summary
│       ├── match_scores.json        # JSON scores data
│       └── dashboard.html           # HTML dashboard
│
├── src/
│   ├── ai_integration/
│   │   └── ai_client.py             # AI summarization client
│   └── ai_layer/
│       └── embeddings.py            # Semantic embeddings
│
└── myenv/                           # Virtual environment
```

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/intelligent-resume-analyzer.git
cd intelligent-resume-analyzer
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv myenv

# Activate - Windows
myenv\Scripts\activate

# Activate - macOS/Linux
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (Optional)

Create a `.env` file in the root directory:

```env
# Optional: For faster HuggingFace model downloads
HF_TOKEN=your_huggingface_token_here

# Optional: If using Gemini API
GEMINI_API_KEY=your_google_gemini_api_key_here
```

## 📦 Requirements

```txt
transformers
sentence-transformers
torch
PyPDF2
pdfplumber
python-docx
fpdf
openpyxl
pandas
python-dotenv
```

Install all dependencies:
```bash
pip install transformers sentence-transformers torch PyPDF2 pdfplumber python-docx fpdf openpyxl pandas python-dotenv
```

## 🎯 Usage

### 1. Add Resumes

Place your resume files (PDF or TXT) in the `data/resumes/` directory:

```
data/resumes/
├── candidate1.pdf
├── candidate2.pdf
└── candidate3.txt
```

### 2. Run the Analyzer

```bash
python main.py
```

### 3. View Results

After processing, find your reports in `data/outputs/`:

| Output File | Description |
|-------------|-------------|
| `reports/*.txt` | Detailed text reports for each candidate |
| `*.pdf` | PDF formatted reports |
| `*.docx` | Word document reports |
| `match_scores.xlsx` | Excel summary of all candidates |
| `match_scores.json` | JSON data for integration |
| `dashboard.html` | Interactive HTML dashboard |

## 📊 Sample Output

```
================ CANDIDATE REPORT ================

Name: John Doe
Email: john.doe@example.com

Experience: 2 years
Education: B.Tech

---------------- SKILLS ----------------

Candidate Skills:
Python, SQL, Machine Learning, AI, React

Matched Required Skills:
SQL, Python

Missing Required Skills:
Git, REST API

Missing Preferred Skills:
Docker, AWS

---------------- MATCH RESULT ----------------

Overall Match Score: 58.69 %

Hiring Recommendation: Weak Fit

=================================================
```

## ⚙️ Configuration

### Customizing Job Requirements

Modify the required and preferred skills in your configuration:

```python
required_skills = ["Python", "SQL", "Git", "REST API"]
preferred_skills = ["React", "Docker", "AWS"]
```

### Match Score Thresholds

| Score Range | Recommendation |
|-------------|----------------|
| 0% - 40% | ❌ Reject |
| 40% - 60% | ⚠️ Weak Fit |
| 60% - 80% | ✅ Good Fit |
| 80% - 100% | 🌟 Strong Fit |

### Embedding Model Options

Change the embedding model in `src/ai_layer/embeddings.py`:

```python
# Fast and efficient (default)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Higher accuracy, slower
model = SentenceTransformer("all-mpnet-base-v2")

# Multilingual support
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `embeddings.position_ids UNEXPECTED` | Safe to ignore - model architecture difference |
| `pad_token_id` warning | Normal behavior for text generation |
| `max_new_tokens` warning | Safe to ignore - setting takes precedence |
| Slow first run | Models are downloading - subsequent runs will be faster |
| Memory issues | Use smaller batch sizes or lighter models |

### Suppress Warnings (Optional)

```bash
# Run with reduced verbosity
TRANSFORMERS_VERBOSITY=error python main.py
```

## 🔒 Privacy & Security

- ✅ All processing is done locally
- ✅ No resume data is sent to external servers (when using local models)
- ✅ API keys are stored in `.env` (add to `.gitignore`)

## 📝 .gitignore Recommendations

```gitignore
# Virtual environment
myenv/
venv/
.env

# Data files
data/resumes/*
data/outputs/*
!data/resumes/.gitkeep
!data/outputs/.gitkeep

# Python cache
__pycache__/
*.pyc
.pytest_cache/

# IDE
.vscode/
.idea/
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** your feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Ideas for Contribution

- [ ] Add support for more file formats (DOCX input)
- [ ] Implement candidate ranking system
- [ ] Add job description parsing
- [ ] Create web interface
- [ ] Add multi-language support
- [ ] Implement resume comparison feature

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Likhith V C

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

## 👤 Author

**Likhith V C**

- 📧 Email: likhithvc21@gmail.com
- 🐙 GitHub: [@likhithvc](https://github.com/likhithvc)
- 💼 LinkedIn: [Likhith V C](https://linkedin.com/in/likhithvc)

## 🙏 Acknowledgments

- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [SentenceTransformers](https://www.sbert.net/)
- [Google Gemini AI](https://ai.google.dev/)

---

<p align="center">
  ⭐ Star this repository if you find it helpful!
</p>

