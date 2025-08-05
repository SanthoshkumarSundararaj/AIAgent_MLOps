# agents/manager_agent.py
from crewai import Agent
from utils.llm_pipeline import pipe
from langchain_community.llms import HuggingFacePipeline
from agents.social_media_agent import social_media_agent
from agents.inventory_agent import inventory_agent

llm = HuggingFacePipeline(pipeline=pipe)

manager_agent = Agent(
    role="Manager",
    goal="Assign tasks to the correct worker agent based on type",
    backstory="Oversees all automation agents in the system",
    llm=llm,
    verbose=True
)

# Task routing
def assign_task(task_type, inputs):
    if task_type == "social_media":
        return social_media_agent.execute_task(inputs)
    elif task_type == "inventory":
        return inventory_agent.execute_task(inputs)
    else:
        return "No matching worker found"
