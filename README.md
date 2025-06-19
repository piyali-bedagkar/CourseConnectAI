# CourseConnect AI 
###▶️ [Watch Demo Video](https://drive.google.com/file/d/13AsalUA6Q_Wvq3weQIiJvv_aazSv-OjN/view?usp=sharing)


A dynamic, AI-powered academic planning platform transforming static university course catalogs into interactive tools. Built with NLP, Knowledge Graphs, and Large Language Models.

---

## 🚀 Overview

CourseConnect AI provides interactive course exploration through:

- **Interactive Knowledge Graph**: Explore connections between courses, professors, and topics visually.
- **AI Chatbot**: Natural language interface for instant academic planning assistance.

---

## 🎯 Business Context (EdTech Sector)

**Customers:**  
- Students  
- Academic advisors  
- University administrative staff  

**Business Opportunities:**  
- **Centralizing** academic planning data  
- **Reducing** reliance on manual advising  
- **Providing** analytical insights on student academic interests and course popularity  

---

## 🎯 Features

- **Automated Data Parsing** from institutional PDFs.
- **Entity Extraction** using Transformers (BERT-based NER).
- **Knowledge Graph Visualization** using PyVis and NetworkX.
- **Real-time Chatbot Interaction** powered by OpenRouter LLM (LLaMA 3).

---

## 🛠️ Technologies Used

| Category           | Tools/Frameworks                     |
|--------------------|--------------------------------------|
| Web Framework      | Streamlit                            |
| NLP & AI           | Transformers, BERT-base-NER, LLaMA 3 |
| Graph Visualization| PyVis, NetworkX                      |
| PDF Parsing        | PyPDF2                               |
| Front-end          | HTML, CSS                            |
| Cloud AI API       | OpenRouter                           |

---

## ⚙️ Technical Implementation

### 1️⃣ Data Collection and Parsing:
- Extracted unstructured course data from PDFs using **PyPDF2** (`pdf_parser.py`).
- Transformed course data into structured text (Course ID, title, professor, time, description).

### 2️⃣ NLP-Based Entity Extraction:
- Leveraged transformer model (**dslim/bert-base-NER**) to parse structured course text into entities:
  - Course Titles  
  - Professors  
  - Timings  
  - Keywords (`nlp.py`)

### 3️⃣ Knowledge Graph Construction:
- Utilized **NetworkX** and **PyVis** to visualize course relationships in an interactive graph.
- Integrated visualization into a **Streamlit** web application (`graph_utils.py`, `knowledgegraph.py`).

### 4️⃣ Chatbot (LLM Integration):
- Connected platform to **OpenRouter’s LLaMA 3 (8B)** API.
- Implemented prompt-driven queries for dynamic responses to student questions (`chatbot.py`).

### 5️⃣ User Interface (UI):
- Developed using **Streamlit**, enhanced with custom **HTML/CSS** for seamless UX.
- Features intuitive navigation, dedicated pages for Knowledge Graph & Chatbot (`home.py`, `ui_utils.py`).

---

## 📊 Data Flow:
PDF → Text → Structured Course Blocks → Entity Triples → Graph (JSON) → LLM Context
