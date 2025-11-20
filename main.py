from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import asyncio
from llm_chain import evaluate_answer_llm

app = FastAPI(title="Gemini Mini AI Screener")

class EvaluateRequest(BaseModel):
    text: str

class RankRequest(BaseModel):
    candidates: List[str]


@app.post("/evaluate-answer")
async def evaluate(req: EvaluateRequest):
    result = await evaluate_answer_llm(req.text)
    return result


@app.post("/rank-candidates")
async def rank(req: RankRequest):
    tasks = [evaluate_answer_llm(a) for a in req.candidates]
    results = await asyncio.gather(*tasks)

    combined = [
        {"answer": ans, **score}
        for ans, score in zip(req.candidates, results)
    ]

    combined.sort(key=lambda x: x["score"], reverse=True)
    return combined
