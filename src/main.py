import sys
import os

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'agents'))
sys.path.insert(0, os.path.join(current_dir, 'tools'))

from crewai import Crew, Process
from agents.error_detector import detect_errors
from agents.context_analyzer import analyze_context
from agents.sre_engineer import propose_solutions
from tools.json_search_tool import json_search_tool
from tools.rag_tool import rag_tool

def run_sre_workflow():
    # Step 1: Detect errors
    log_data = json_search_tool.search_logs("timeout errors")
    error_summary = detect_errors(logs=log_data)
    print("Error Detection Results:")
    print(error_summary)

    # Step 2: Analyze context
    metric_data = json_search_tool.search_metrics("checkout-service payment-service")
    trace_data = json_search_tool.search_traces("trace-0002 trace-0003")
    context_analysis = analyze_context(error_summary=error_summary, metrics=metric_data, traces=trace_data)
    print("\nContext Analysis Results:")
    print(context_analysis)

    # Step 3: Propose solutions
    rag_context = rag_tool.query("SRE best practices for handling timeout errors")
    solutions = propose_solutions(error_analysis=error_summary, context_analysis=context_analysis, rag_context=rag_context)
    print("\nProposed Solutions:")
    print(solutions)

    return {
        "error_summary": error_summary,
        "context_analysis": context_analysis,
        "proposed_solutions": solutions
    }

if __name__ == "__main__":
    results = run_sre_workflow()
    
    print("\nFull SRE Workflow Results:")
    for key, value in results.items():
        print(f"\n{key.upper()}:")
        print(value)