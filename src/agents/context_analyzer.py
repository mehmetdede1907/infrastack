from crewai import Agent, Task, Crew

context_analysis_prompt = """
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

context_analyzer = Agent(
    role='Context Analyzer',
    goal='Analyze the context around detected timeout errors',
    backstory='Expert in correlating metrics and traces with error patterns',
    verbose=True
)

def analyze_context(error_summary, metrics, traces):
    task = Task(
        description=context_analysis_prompt.format(
            error_summary=error_summary,
            metrics=metrics,
            traces=traces
        ),
        agent=context_analyzer,
        expected_output="A detailed analysis of the context surrounding the timeout errors, including correlations between metrics, traces, and detected errors."
    )
    
    crew = Crew(
        agents=[context_analyzer],
        tasks=[task],
        verbose=2
    )
    
    result = crew.kickoff()
    return result