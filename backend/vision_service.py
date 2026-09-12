import requests
import json
import base64

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llava:latest"


def analyze_image(image_path):

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")


    prompt = """
You are a Senior Software Business Analyst.

Analyze this software UI screenshot.

Return ONLY valid JSON.

Use this exact schema:

{
  "screen_name": "",
  "ui_components": [],
  "actions": [],
  "observations": [],
  "assumptions": [],
  "open_questions": []
}
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_data],
        "stream": False,
        "format": "json"
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        response.raise_for_status()

        result = response.json()

        return json.loads(result["response"])

    except Exception as e:

        return {
            "error": str(e)
        }