# 🤖 MoinSystems AI DevFlow Copilot

AI-powered software engineering assistant that converts client requirements and UI screenshots into complete development artifacts using local Generative AI models.

---

## 📌 Overview

MoinSystems AI DevFlow Copilot is a GenAI-based software development assistant designed for software houses.

The system helps software teams transform:

- Client requirements
- Meeting notes
- UI screenshots

into structured software engineering outputs.

It reduces manual documentation effort and improves communication between clients, developers, and QA teams.

---

## ✨ Features

### 1. Requirement Generator

Converts client requirements into structured software documentation.

Generated outputs include:

- Project summary
- Features
- User stories
- Assumptions
- Open questions


---

### 2. Screenshot Analyzer

Uses AI vision capabilities to analyze UI screenshots.

It identifies:

- UI components
- Layout structure
- Possible features
- Design elements


---

### 3. Multimodal Requirement Analysis

Combines:

- Text requirements
- UI screenshots

to generate a better understanding of the software project.


---

### 4. Engineering Artifact Generator

Generates development-ready software engineering documents:

- User stories
- Acceptance criteria
- Functional requirements
- Non-functional requirements
- Database tables
- API endpoints
- Implementation plans
- Developer tasks
- QA test cases
- Project risks
- Client updates


---

### 5. AI Evaluation Dashboard

Evaluates generated engineering artifacts.

Checks:

- Missing sections
- Requirement completeness
- API availability
- QA coverage
- Overall quality score
- Confidence level


Example:

```
Quality Score: 100/100

Confidence: High

Result: Passed
```

---

# 🏗️ System Architecture

```
Client Requirement
        |
        ↓
Requirement Generator
        |
        ↓
Engineering Artifact Generator
        |
        ↓
AI Evaluation Layer
        |
        ↓
Developer Ready Documentation
```

---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- Ollama


## AI Models

- Llama 3.1 (Text Generation)
- LLaVA (Vision Analysis)


## Frontend

- Streamlit


## Development Tools

- VS Code
- GitHub
- Local AI Models

---

# 📂 Project Structure

```
DevFlow-Copilot/

│
├── backend/
│   │
│   ├── app.py
│   ├── ollama_service.py
│   ├── engineering_service.py
│   ├── evaluation_service.py
│   ├── vision_service.py
│   ├── multimodal_service.py
│   ├── validator.py
│   └── outputs/
│
│
├── frontend/
│   │
│   └── streamlit_app.py
│
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Ana-Rashid/DevFlow-Copilot.git
```

Move into project:

```bash
cd DevFlow-Copilot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Setup Ollama

Install Ollama and download models:

```bash
ollama pull llama3.1
```

For image analysis:

```bash
ollama pull llava
```

Check models:

```bash
ollama list
```

---

# ▶️ Running the Application

## Start Backend

Open terminal:

```bash
cd backend
```

Run:

```bash
uvicorn app:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## Start Frontend

Open another terminal:

```bash
cd frontend
```

Run:

```bash
streamlit run streamlit_app.py
```

Frontend:

```
http://localhost:8501
```

---

# 🧪 Example Requirement

```
Build a hospital management system where doctors manage appointments,
patients register and view medical history, and admins manage users.
```

Generated outputs:

- User stories
- APIs
- Database design
- Development tasks
- QA test cases
- Risks

---

# 🎯 Project Goals

- Reduce software documentation time
- Improve requirement understanding
- Assist developers with AI-generated plans
- Reduce AI hallucination through evaluation
- Provide a local and cost-free GenAI workflow

---

# 🔒 AI Approach

This project uses local AI models through Ollama.

Advantages:

- No paid API dependency
- Local processing
- Better privacy
- Open-source AI workflow

---

# 👩‍💻 Developer

**Ana Rashid**

BS Information Technology Student  
University of Management and Technology (UMT)

---

# 📌 Future Improvements

- Export reports as PDF
- Add authentication
- Add project management integration
- Improve AI evaluation metrics
- Add more vision-based features

---

# 📄 License

This project is developed as an AI product prototype for learning and software engineering experimentation.