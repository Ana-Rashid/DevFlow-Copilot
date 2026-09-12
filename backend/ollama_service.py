import requests
import json
import re

from prompts import SYSTEM_PROMPT


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llama3.1:latest"


def clean_json(output):

    output = output.replace("```json", "")
    output = output.replace("```", "")

    match = re.search(
        r"\{.*\}",
        output,
        re.DOTALL
    )

    if match:
        output = match.group(0)

    return output.strip()



def generate_requirement_analysis(requirement_text):

    prompt = f"""
{SYSTEM_PROMPT}

Client Requirement:

{requirement_text}
"""


    payload = {

        "model": MODEL_NAME,

        "prompt": prompt,

        "stream": False,

        "format": "json",

        "options": {

            "temperature": 0.1,

            "num_ctx": 4096,

            "num_predict": 2500

        }

    }


    try:

        response = requests.post(

            OLLAMA_URL,

            json=payload,

            timeout=600

        )


        response.raise_for_status()


        result = response.json()


        output = result.get(

            "response",

            ""

        )


        cleaned_output = clean_json(output)


        return json.loads(cleaned_output)



    except Exception as e:

        return {

            "error": str(e)

        }