import sys
import os

# Get the absolute path of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (src)
parent_dir = os.path.dirname(current_dir)

# Add the parent directory and its subdirectories to sys.path
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.join(parent_dir, 'agents'))
sys.path.insert(0, os.path.join(parent_dir, 'tools'))

from context_analyzer import analyze_context
from json_search_tool import json_search_tool

def test_context_analyzer():
    # Simulate error summary
    error_summary = "Timeout errors detected in checkout-service and payment-service"
    
    # Simulate metric and trace search
    metric_data = json_search_tool.search_metrics("checkout-service payment-service")
    trace_data = json_search_tool.search_traces("trace-0002 trace-0003")
    
    # Run context analysis
    result = analyze_context(error_summary=error_summary, metrics=metric_data, traces=trace_data)
    
    print("Context Analyzer Result:")
    print(result)
    
    # Add assertions to verify the result
    assert "CPU usage" in result, "CPU metrics not analyzed"
    assert "HTTP request duration" in result, "Request duration not analyzed"
    assert "trace-0002" in result and "trace-0003" in result, "Relevant traces not analyzed"

if __name__ == "__main__":
    test_context_analyzer()