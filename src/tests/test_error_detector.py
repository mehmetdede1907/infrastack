from crewai import Agent, Task

error_detection_prompt = """
Analyze the following logs to identify potential timeout errors:
{logs}

Focus on:
1. Error messages related to timeouts
2. Patterns in timestamps of errors
3. Services experiencing the most errors

Provide a summary of the detected timeout errors, including relevant log entries and their timestamps.
"""

error_detector = Agent(
    role='Error Detector',
    goal='Identify timeout errors in logs',
    backstory='Specialist in detecting and isolating error patterns in log data',
    verbose=True
)

def detect_errors(logs):
    task = Task(
        description=error_detection_prompt.format(logs=logs),
        agent=error_detector,
        expected_output="A detailed summary of detected timeout errors, including relevant log entries and their timestamps."
    )
    return task.execute()