from crewai import Crew, Task
from agents.error_detector import error_detector
from agents.context_analyzer import context_analyzer
from agents.sre_engineer import sre_engineer
from tools.json_search_tool import json_search_tool
from tools.rag_tool import rag_tool

def run_sre_workflow():
    detect_errors_task = Task(
        description='Search logs for timeout errors and summarize findings',
        agent=error_detector
    )

    analyze_context_task = Task(
        description='Analyze metrics and traces related to detected errors',
        agent=context_analyzer
    )

    propose_solutions_task = Task(
        description='Analyze findings, identify root causes, and propose solutions',
        agent=sre_engineer
    )

    sre_crew = Crew(
        agents=[error_detector, context_analyzer, sre_engineer],
        tasks=[detect_errors_task, analyze_context_task, propose_solutions_task],
        tools=[json_search_tool, rag_tool],
        verbose=2
    )

    result = sre_crew.kickoff()
    return result