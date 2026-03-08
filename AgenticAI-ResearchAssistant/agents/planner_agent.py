from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def create_plan(topic):

    prompt = f"""
You are an AI research planner.

Topic: {topic}

Create a simple research plan that includes:
1. Key subtopics to research
2. Important questions to answer
3. Suggested structure for a research report

Keep the plan clear and short.
"""

    response = llm.invoke(prompt)

    return response.content