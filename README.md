# Supply Chain & Maintenance Readiness Copilot

## Business Problem
Field technicians lose hours cross-referencing equipment fault logs against dense PDF repair manuals and warehouse inventory spreadsheets. Delays happen when technicians diagnose an issue without knowing whether the replacement part is actually in stock.

## Solution Architecture
An end-to-end AI readiness copilot built with **FastAPI**, **SQL**, and **Retrieval-Augmented Generation (RAG)**:
1. **Structured SQL Layer:** Tracks warehouse parts inventory and active maintenance work orders.
2. **RAG Knowledge Base:** Indexes PDF equipment manuals to retrieve repair procedures with exact page citations.
3. **Automated Triage:** Parses technician fault reports, checks SQL inventory for required parts, and logs prioritized work orders.

## Tech Stack
- **Backend:** Python, FastAPI, Pydantic, SQLite / PostgreSQL
- **AI & Retrieval:** LLM API, Vector Database (ChromaDB/Qdrant), RAG Evaluation Suite
- **Deployment:** Docker, AWS

## Local Setup (Week 1)
1. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API server: `uvicorn app.main:app --reload`
4. Open interactive API docs at: `http://127.0.0.1:8000/docs`
