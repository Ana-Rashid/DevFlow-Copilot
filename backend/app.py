from fastapi import FastAPI
from pydantic import BaseModel

from ollama_service import generate_requirement_analysis
from vision_service import analyze_image
from multimodal_service import combine_analysis
from validator import validate_output
from engineering_service import generate_engineering_artifacts
from evaluation_service import evaluate_output

import json
import os
from datetime import datetime



app = FastAPI(

    title="DevFlow Copilot API",

    description="Local GenAI Requirement Generator",

    version="2.0"

)



OUTPUT_FOLDER = "outputs"


os.makedirs(

    OUTPUT_FOLDER,

    exist_ok=True

)



class RequirementRequest(BaseModel):

    text: str



class ImageRequest(BaseModel):

    image_path: str



class MultimodalRequest(BaseModel):

    requirement_text: str

    image_analysis: dict



@app.get("/")

def home():

    return {

        "message": "DevFlow Copilot API is running"

    }



@app.post("/generate")

def generate(request: RequirementRequest):


    ai_response = generate_requirement_analysis(

        request.text

    )


    if "error" in ai_response:

        return {

            "status": "failed",

            "error": ai_response["error"]

        }



    validation = validate_output(

        ai_response

    )


    timestamp = datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )


    file_name = f"generation_{timestamp}.json"


    file_path = os.path.join(

        OUTPUT_FOLDER,

        file_name

    )


    saved_data = {

        "model": "llama3.1:latest",

        "created_at": timestamp,

        "source_requirement": request.text,

        "validation_result": validation

    }



    with open(

        file_path,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            saved_data,

            file,

            indent=4

        )



    return {

        "status": "success",

        "saved_file": file_name,

        "validation": validation

    }



@app.post("/analyze-image")

def analyze(request: ImageRequest):


    result = analyze_image(

        request.image_path

    )


    return {

        "status": "success",

        "analysis": result

    }



@app.post("/multimodal")

def multimodal(request: MultimodalRequest):


    result = combine_analysis(

        request.requirement_text,

        request.image_analysis

    )


    return {

        "status": "success",

        "result": result

    }



@app.post("/engineering")

def engineering(request: RequirementRequest):


    result = generate_engineering_artifacts(

        request.text

    )


    if "error" in result:

        return {

            "status": "failed",

            "error": result["error"]

        }



    return {

        "status": "success",

        "result": result

    }



@app.post("/evaluate")

def evaluate(request: RequirementRequest):


    engineering_output = generate_engineering_artifacts(

        request.text

    )


    if "error" in engineering_output:

        return {

            "status": "failed",

            "error": engineering_output["error"]

        }



    evaluation_report = evaluate_output(

        engineering_output

    )


    return {

        "status": "success",

        "engineering_output": engineering_output,

        "evaluation_report": evaluation_report

    }