from pydantic import BaseModel
from typing import List


class Feature(BaseModel):
    name: str
    description: str


class UserStory(BaseModel):
    role: str
    goal: str
    benefit: str


class ProjectSpecification(BaseModel):
    project_summary: str
    features: List[Feature]
    user_stories: List[UserStory]
    assumptions: List[str]
    open_questions: List[str]