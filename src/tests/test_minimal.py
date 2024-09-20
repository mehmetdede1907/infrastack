
def test_minimal():
    agent = Agent(
        role='Tester',
        goal='Test the CrewAI setup',
        backstory='A simple agent for testing purposes',
        verbose=True
    )

    task = Task(
        description="Print 'Hello, World!' and confirm the CrewAI setup is working.",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=2
    )

    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    test_minimal()