from crewai import Agent
from langchain.prompts import PromptTemplate

context_analysis_prompt = PromptTemplate(
    input_variables=["error_summary", "metrics", "traces"],
    template="""
    Given the following error summary and corresponding metrics and traces:
    
    Error Summary: {error_summary}
    Metrics: {metrics}
    Traces: {traces}
    
    Analyze the context around the detected timeout errors. Focus on:
    1. Performance metrics (CPU, memory, response times) around the time of errors
    2. Trace information for the affected requests
    3. Any correlations between metrics, traces, and the detected errors
    
    Provide a detailed analysis of the context surrounding the timeout errors.
    """
)

context_analyzer = Agent(
    role='Context Analyzer',
    goal='Analyze the context around detected timeout errors',
    backstory='Expert in correlating metrics and traces with error patterns',
    verbose=True,
    llm_config={
        "temperature": 0.7,
        "max_tokens": 1500,
        "prompt_template": context_analysis_prompt
    }
)