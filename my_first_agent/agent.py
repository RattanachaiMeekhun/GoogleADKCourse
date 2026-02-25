from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A English language tutor for IELTS.',
    instruction='Guide the user in improving their English skills for the IELTS exam.'
)