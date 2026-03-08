from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from tools.search_tool import search_web

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def research_topic(topic):

    results = search_web(topic)

    combined_text = ""

    for r in results:
        combined_text += r["content"] + "\n"

    prompt = f"""
    You are a research assistant.

    Topic: {topic}

    Using the information below, create a structured research summary.

    Information:
    {combined_text}

    Output format:
    - Overview
    - Key Points
    - Important Insights
    """

    response = llm.invoke(prompt)

    return response.content