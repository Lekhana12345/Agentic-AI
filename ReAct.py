import google.generativeai as genai

genai.configure(api_key="AIzaSyC_AVyPlyLfVJSEcJziAryFTx8Qsuq75Zs")

model = genai.GenerativeModel("gemini-3.1-pro-preview")

def react_agent(query):
    prompt = f"""
You are a REACT (Reasoning + Acting) AI agent.

Follow this exact format:

Thought: think step by step
Action: what action to take
Observation: result of action
Final Answer: final response

Question: {query}
"""

    response = model.generate_content(prompt)
    return response.text


while True:
    q = input("Ask: ")
    print(react_agent(q))

# import google.generativeai as genai

# # 🔑 Add your API key
# genai.configure(api_key="AIzaSyAUUvO7uU6lFiZg18BbeCWJy5K2GBWqwCI")

# # 📦 Fetch models
# models = genai.list_models()

# print("Available Models:\n")

# for model in models:
#     # Only show generative models (useful ones)
#     if "generateContent" in model.supported_generation_methods:
#         print(f"Name: {model.name}")
#         print(f"Description: {model.description}")
#         print(f"Supported Methods: {model.supported_generation_methods}")
#         print("-" * 50)