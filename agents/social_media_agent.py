# agents/social_media_agent.py
from crewai import Agent
from utils.llm_pipeline import pipe
from langchain_community.llms import HuggingFacePipeline

llm = HuggingFacePipeline(pipeline=pipe)

social_media_agent = Agent(
    role="Social Media Content Creator",
    goal="Create short, engaging posts for Instagram and LinkedIn",
    backstory="Expert in creating attention-grabbing product posts",
    llm=llm,
    verbose=True
)
