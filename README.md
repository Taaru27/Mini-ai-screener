Gemini Mini AI interview Screener

Overview:

This project provides a FastAPI-based microservice that evaluates and ranks candidate answers using an LLM (Gemini API).

It includes two main endpoints:

/evaluate-answer → Generate score,summary of answer and improvement

/rank-candidates → Scores multiple texts and returns them sorted by score

Useful for:

Screening candidate responses

Ranking interview answers

LLM-based evaluation pipelines

Automated quality scoring

🛠 1. Project Setup
✅ Step 1 — Clone the Repository
git clone <your-repo-url>
cd <repo-folder>

✅ Step 2 — Create a Virtual Environment
▶️ Windows
python -m venv venv
venv\Scripts\activate

▶️ Mac / Linux
python3 -m venv venv
source venv/bin/activate

✅ Step 3 — Install Dependencies
pip install -r requirements.txt


Requirements should include:

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



