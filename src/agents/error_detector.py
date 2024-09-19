from crewai import Agent
from langchain.prompts import PromptTemplate

error_detection_prompt = PromptTemplate(
    input_variables=["logs"],
    template="""
    Analyze the following log data to identify potential timeout errors:
    {logs}
    
    Focus on:
    1. Error messages related to timeouts
    2. Patterns in timestamps of errors
    3. Services experiencing the most errors
    
    Provide a summary of the detected timeout errors, including relevant log entries and their timestamps.
    """
)

error_detector = Agent(
    role='Error Detector',
    goal='Identify timeout errors in logs',
    backstory='Specialist in detecting and isolating error patterns in log data',
    verbose=True,
    llm_config={
        "temperature": 0.7,
        "max_tokens": 1000,
        "prompt_template": error_detection_prompt
    }
)