from crewai import Agent
from langchain.prompts import PromptTemplate

sre_analysis_prompt = PromptTemplate(
    input_variables=["error_analysis", "context_analysis", "rag_result"],
    template="""
    Given the following analyses and additional context:
    
    Error Analysis: {error_analysis}
    Context Analysis: {context_analysis}
    Additional Context: {rag_result}
    
    Your task is to:
    1. Identify the root causes of the detected timeout errors
    2. Propose detailed solutions to resolve the timeout issues
    3. Suggest preventive measures to avoid similar issues in the future
    4. Prioritize the proposed solutions based on their potential impact and ease of implementation
    
    Provide a comprehensive report with your findings, reasoning, and recommendations.
    """
)

sre_engineer = Agent(
    role='SRE Engineer',
    goal='Analyze findings and propose solutions for timeout errors',
    backstory='Senior SRE with expertise in problem-solving and system optimization',
    verbose=True,
    llm_config={
        "temperature": 0.7,
        "max_tokens": 2000,
        "prompt_template": sre_analysis_prompt
    }
)