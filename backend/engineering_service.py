from ollama_service import generate_requirement_analysis


def generate_engineering_artifacts(requirement):

    prompt = f"""
You are a Senior Software Architect.

Analyze this software project requirement:

{requirement}


Your task:
Generate a complete software engineering specification.


STRICT OUTPUT RULES:

- Return ONLY valid JSON.
- Do not add explanations.
- Do not add markdown.
- Do not write anything before or after JSON.
- Every field must contain meaningful data.
- Never return empty arrays.
- Do not include status fields.
- Do not include comments.


Generate at least:

- 3 user stories
- 5 acceptance criteria
- 5 functional requirements
- 3 non-functional requirements
- 4 database tables
- 5 API endpoints
- 5 implementation steps
- 5 developer tasks
- 5 QA test cases
- 3 risks


Use EXACT JSON structure:

{{
    "project_summary": "",

    "user_stories": [
        {{
            "role": "",
            "goal": "",
            "benefit": ""
        }}
    ],

    "acceptance_criteria": [],

    "functional_requirements": [],

    "non_functional_requirements": [],

    "database_tables": [
        {{
            "name": "",
            "description": ""
        }}
    ],

    "api_endpoints": [
        {{
            "method": "",
            "endpoint": "",
            "description": ""
        }}
    ],

    "implementation_plan": [],

    "developer_tasks": [],

    "qa_test_cases": [],

    "risks": [],

    "client_update": ""
}}


CONTENT RULES:


Project Summary:
- Describe the software system clearly.


User Stories:
- Use real user roles.
- Follow:
  As a [role], I want [goal], so that [benefit].


Acceptance Criteria:
- Must be measurable and testable.


Functional Requirements:
- Describe system capabilities.


Non Functional Requirements:
Include:
- Security
- Performance
- Usability
- Reliability


Database Tables:
- Use realistic table names.
- Add descriptions only.


API Endpoints:
- Include HTTP methods.
- Include realistic REST endpoints.


Implementation Plan:
- Give development phases.


Developer Tasks:
- Give actionable engineering tasks.


QA Test Cases:
- Give testing activities.


Risks:
- Give realistic software project risks.


Client Update:
- Write a short professional project progress update.
- Do NOT start with "Project is".
- Do NOT write a sentence outside JSON.


FINAL REMINDER:

Return ONLY JSON.
"""


    return generate_requirement_analysis(prompt)