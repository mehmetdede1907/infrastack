# workflow.py

from crewai.workflow import Workflow
from error_detection_agent import ErrorDetectionAgent

class SREWorkflow(Workflow):
    def __init__(self):
        super().__init__(name="SREWorkflow")
        # Initialize agents
        self.error_detection_agent = ErrorDetectionAgent()

        # Register agents
        self.register_agent(self.error_detection_agent)
        # You can register additional agents here

    def run(self):
        # Start the workflow by running the first agent
        self.error_detection_agent.run()

        # In a full implementation, you would have message handlers and other agents
        # For now, we're focusing on the Error Detection Agent

if __name__ == "__main__":
    workflow = SREWorkflow()
    workflow.run()
