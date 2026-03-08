






from agents.planner_agent import create_plan
from agents.research_agent import research_topic
from agents.writer_agent import write_report
from tools.save_tool import save_report

topic = input("Enter research topic: ")

print("\n  ⚡︎ Planner Agent creating research plan...\n")
plan = create_plan(topic)

print("Research Plan:\n")
print(plan)

print("\n 🔎︎ Research Agent is collecting information...\n")
research_data = research_topic(topic)

print("\n 𖣯 Writer is Agent generating report...\n")
final_report = write_report(topic, research_data)

print("\n ✮✮✮✮✰ Final Report:\n")
print(final_report)

file_path = save_report(topic, final_report)

print(f"\nReport saved at: {file_path}")