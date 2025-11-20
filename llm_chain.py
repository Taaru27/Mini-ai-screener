import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert interviewer.\n"
     "Return STRICTLY in this JSON format:\n"
     "{\n"
     "  \"score\": 1-5,\n"
     "  \"summary\": \"one-line summary\",\n"
     "  \"improvement\": \"one suggestion\"\n"
     "}\n"
     
    ),
    ("user", "Candidate answer:\n{answer}")
])

chain = prompt | model | parser


async def evaluate_answer_llm(answer: str):
    return await chain.ainvoke({"answer": answer})
