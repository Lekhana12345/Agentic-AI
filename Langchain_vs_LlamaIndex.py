import google.generativeai as genai

genai.configure(api_key="AIzaSyC_AVyPlyLfVJSEcJziAryFTx8Qsuq75Zs")

from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini in LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-pro-preview",
    google_api_key="AIzaSyC_AVyPlyLfVJSEcJziAryFTx8Qsuq75Zs"
)

# Simple query
response = llm.invoke("Explain AI agents in simple terms")

print(response.content)