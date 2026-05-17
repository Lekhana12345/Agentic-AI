import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Set environment variables using Python instead of 'export'
os.environ["GOOGLE_API_KEY"] = "AIzaSyC_AVyPlyLfVJSEcJziAryFTx8Qsuq75Zs"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_PROJECT"] = "lab_5_2_agent_deployment"

app = FastAPI(
    title="Agentic API with LangSmith",
    description="A fully observable LangChain agent",
    version="1.0.0"
)

# 2. Fix the Pydantic model for v2 compatibility
class QueryRequest(BaseModel):
    # Removed the deprecated 'example' argument
    query: str = Field(..., description="The query for the agent to answer")

class QueryResponse(BaseModel):
    answer: str
    status: str = "success"

# ... (Continue with your llm, prompt, and API endpoint definitions below)
# 2. Initialize the LangChain Components
# Because LANGCHAIN_TRACING_V2 is set, this is automatically monitored!

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-pro-preview",
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert technical tutor. Provide clear, concise answers."),
    ("user", "{input}")
])

# Create a simple chain: Prompt -> LLM -> String Output
agent_chain = prompt | llm | StrOutputParser()

# 3. Create the API Endpoint
@app.post("/api/v1/agent/invoke", response_model=QueryResponse)
async def invoke_agent(request: QueryRequest):
    try:
        # Use asynchronous invocation (ainvoke) to prevent blocking the API
        response_text = await agent_chain.ainvoke({"input": request.query})

        return QueryResponse(answer=response_text)

    except Exception as e:
        # If the LLM fails, the error will still be logged in LangSmith
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Agentic API"}