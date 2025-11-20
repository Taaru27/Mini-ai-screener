## Gemini Mini AI interview Screener

## Overview:

This project provides a FastAPI-based microservice that evaluates and ranks candidate answers using an LLM (Gemini API).

It includes two main endpoints:

/evaluate-answer → Generate score,summary of answer and improvement

/rank-candidates → Scores multiple texts and returns them sorted by score

## Useful for:

Screening candidate responses

Ranking interview answers

LLM-based evaluation pipelines

Automated quality scoring

🛠 1. Project Setup
✅ Step 1 — Clone the Repository
git clone https://github.com/Taaru27/Mini-ai-screener.git
cd mini-ai-screener

✅ Step 2 — Create a Virtual Environment
▶️ Windows
python -m venv venv
venv\Scripts\activate

▶️ Mac / Linux
python3 -m venv venv
source venv/bin/activate

✅ Step 3 — Install Dependencies
pip install -r requirements.txt


## Requirements should include:

fastapi
uvicorn
pydantic
google-generativeai
python-dotenv

✅ Step 4 — Add Your Gemini API Key

Create a file:

.env


Add:

GEMINI_API_KEY=your_key_here

🏗 2. Project Structure
├── llm_chain.py
├── main.py
├── .env
├── requirements.txt
└── README.md

🧠 3. API Endpoints
🔹 POST /evaluate-answer

Score a single response.

Request
{
  "text": "I have 2 years of experience in Oracle DB"
}

Response
{
  "score": 2,
  "summary": "Candidate mentions Oracle DB experience.",
  "improvement": "Add more details about projects."
}

🔹 POST /rank-candidates

Evaluate multiple responses and return them ranked from highest to lowest score.

Request
{
  "candidates": [
    "I have 2 years of exp in oracle db",
    "I worked on genai usecases",
    "I have knowledge on LLM"
  ]
}

Response
[
  {"answer": "...", "score": 3},
  {"answer": "...", "score": 2},
  {"answer": "...", "score": 1}
]

🚀 4. Running the Server

Run uvicorn:

uvicorn main:app --reload


API docs available at:

📌 Swagger UI

http://127.0.0.1:8000/docs


📌 Redoc

http://127.0.0.1:8000/redoc

🧪 5. Testing the APIs
▶️ Use Postman

Create a POST request

Paste the JSON body

Hit Send

## Why I Selected This Tech Stack

I selected this tech stack based on simplicity, reliability, and the ability to build an AI screener quickly, while still using production-ready tools used in real LLM applications.

🚀 FastAPI

FastAPI is the ideal choice for this backend because:

It is lightweight, modern, and extremely fast.

Comes with built-in Swagger UI (/docs), which makes API testing easy.

Has excellent support for async endpoints — crucial when calling LLMs in parallel.

Easy to structure into clean modules (routes, models, services).

🐍 Python

Python was chosen because:

Best ecosystem for AI, ML, and LLM development.

Works seamlessly with FastAPI and async programming.

Clean syntax → helps deliver fast in a 48-hour build challenge.

🔗 LangChain

LangChain is used to simplify LLM integration and prompt-chaining.

Why I used LangChain:

Provides clean pipelines (prompt → model → parser), reducing boilerplate code.

The JsonOutputParser ensures the LLM always returns strict, valid JSON.

Easy to maintain prompts using ChatPromptTemplate.

Supports async LLM calls with .ainvoke().

Makes the code more modular, readable, and expandable (e.g., adding retrieval later).

Using LangChain made the entire /evaluate-answer logic only a few lines while keeping structure clean:

prompt | model | parser


This is the exact use-case LangChain is built for.

🤖 Gemini API (Gemini Flash 2.5)

Gemini was selected because:

Free to use — perfect for assignments and demos.

Extremely fast, ideal for scoring and summarizing answers.

Produces consistent reasoning quality.

Works smoothly with LangChain’s ChatGoogleGenerativeAI wrapper.

⚡ Asyncio (Used in /rank-candidates)

Asyncio allows all candidate answers to be evaluated at the same time:

Much faster than processing each answer sequentially.

Scales better for lists of 10–50 candidates.

Makes the ranking endpoint feel production-ready.

🎯 Final Summary

This tech stack (FastAPI + Python + LangChain + Gemini + Asyncio) provides the perfect balance of speed, structure, simplicity, and LLM flexibility.
It allowed me to build a clean AI Interview Screener quickly, while using tools that are actually used in real-world production LLM systems.