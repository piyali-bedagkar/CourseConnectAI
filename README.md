# CourseConnect AI

A dynamic, AI-powered academic planning platform transforming static university course catalogs into interactive tools. Built with NLP, Knowledge Graphs, and Large Language Models.

---

🚀 Overview

CourseConnect AI provides interactive course exploration through:

- **Interactive Knowledge Graph**: Explore connections between courses, professors, and topics visually.
- **AI Chatbot**: Natural language interface for instant academic planning assistance.

---

🎯 Features

- **Automated Data Parsing** from institutional PDFs.
- **Entity Extraction** using Transformers (BERT-based NER).
- **Knowledge Graph Visualization** using PyVis and NetworkX.
- **Real-time Chatbot Interaction** powered by OpenRouter LLM (LLaMA 3).

---

🛠️ Technologies Used

| Category           | Tools/Frameworks                     |
|--------------------|--------------------------------------|
| Web Framework      | Streamlit                            |
| NLP & AI           | Transformers, BERT-base-NER, LLaMA 3 |
| Graph Visualization| PyVis, NetworkX                      |
| PDF Parsing        | PyPDF2                               |
| Front-end          | HTML, CSS                            |
| Cloud AI API       | OpenRouter                           |

---

📁 Project Structure

UMD_CourseConnect_Chatbot/
│
├── Project_Code/
│ ├── data/
│ ├── lib/
│ ├── pages/
│ ├── utils/
│ │ ├── ui_utils.py
│ │ ├── pdf_parser.py
│ │ ├── graph_utils.py
│ │ └── nlp.py
│ ├── home.py
│ ├── chatbot.py
│ ├── knowledgegraph.py
│ ├── about.py
│ ├── requirements.txt
│ └── structured_courses_from_pdf.txt
│
├── Presentation_503_Data_Analyst_1.pdf
├── Presentation_and_ProductDemo.mp4
└── Report_503_Data_Analyst_1.pdf
