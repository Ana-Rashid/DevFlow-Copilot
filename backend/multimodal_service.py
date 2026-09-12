import json
from ollama_service import generate_requirement_analysis


def combine_analysis(
    requirement_text,
    image_analysis
):

    combined_input = f"""

You are a Senior Software Analyst.

Analyze the following software requirement
and UI screenshot analysis.

Requirement:

{requirement_text}


Screenshot Analysis:

{json.dumps(image_analysis, indent=2)}


Create a final software specification.

Return ONLY valid JSON.

Use this structure:

{{
    "project_summary": "",

    "features": [],

    "user_stories": [],

    "ui_components": [],

    "observations": [],

    "assumptions": [],

    "open_questions": []
}}

Rules:

- Observations must contain only things visible from screenshot.
- Assumptions must contain uncertain information.
- Do not invent missing UI elements.
- Add questions where information is missing.

"""


    result = generate_requirement_analysis(
        combined_input
    )


    return result