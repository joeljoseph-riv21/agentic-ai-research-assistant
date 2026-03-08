from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def write_report(topic, research_content):

    prompt = f"""
You are a professional research report writer.

Topic:
{topic}

Research notes:
{research_content}

Create a clean structured research report.

Format:
1. Introduction
2. Key Concepts
3. Important Insights
4. Conclusion
"""

    response = llm.invoke(prompt)

    return response.content