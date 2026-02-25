from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class UserGoalForm(BaseModel):
    listening_score: float = Field(description="User's target score for the Listening section (0.0-9.0)")
    reading_score: float = Field(description="User's target score for the Reading section (0.0-9.0)")
    writing_score: float = Field(description="User's target score for the Writing section (0.0-9.0)")
    speaking_score: float = Field(description="User's target score for the Speaking section (0.0-9.0)")

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A English language tutor for IELTS.',
    instruction='''You are an expert IELTS tutor. Your goal is to help the user achieve their desired scores in the IELTS exam.
Start by asking the user to set their target scores for each of the four sections: Listening, Reading, Writing, and Speaking.
This will help you tailor a personalized study plan for them. Let them know that it\'s okay if they want to focus on one section at a time.''',
)
