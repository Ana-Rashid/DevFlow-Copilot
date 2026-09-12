import streamlit as st
import requests
import tempfile
import json


API_TEXT_URL = "http://127.0.0.1:8000/generate"
API_IMAGE_URL = "http://127.0.0.1:8000/analyze-image"
API_MULTIMODAL_URL = "http://127.0.0.1:8000/multimodal"
API_ENGINEERING_URL = "http://127.0.0.1:8000/engineering"
API_EVALUATE_URL = "http://127.0.0.1:8000/evaluate"


st.set_page_config(
    page_title="DevFlow Copilot",
    page_icon="🤖",
    layout="wide"
)


# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("🤖 DevFlow Copilot")

    st.info(
        """
        MoinSystems AI Internal Tool

        Generate:
        - Requirements
        - User Stories
        - Engineering Plans
        - QA Cases
        - Evaluations
        """
    )

    st.success(
        "MVP Status: Complete ✅"
    )



st.title(
    "🤖 MoinSystems AI DevFlow Copilot"
)


tabs = st.tabs(
    [
        "Requirements",
        "Screenshot AI",
        "Multimodal",
        "Engineering",
        "Evaluation"
    ]
)



# =====================================
# TAB 1 REQUIREMENT GENERATOR
# =====================================

with tabs[0]:

    st.header(
        "Requirement Generator"
    )


    requirement = st.text_area(
        "Client Requirement",
        height=250
    )


    if st.button(
        "Generate Specification"
    ):

        response = requests.post(
            API_TEXT_URL,
            json={
                "text": requirement
            }
        )

        st.success(
            "Generated Successfully"
        )

        st.json(
            response.json()
        )



# =====================================
# TAB 2 IMAGE
# =====================================

with tabs[1]:

    st.header(
        "UI Screenshot Analyzer"
    )


    image = st.file_uploader(
        "Upload Screenshot",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )


    if image:

        st.image(
            image,
            use_container_width=True
        )


        if st.button(
            "Analyze Screenshot"
        ):


            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".png"
            ) as file:

                file.write(
                    image.read()
                )

                path = file.name



            response = requests.post(
                API_IMAGE_URL,
                json={
                    "image_path": path
                }
            )


            st.json(
                response.json()
            )



# =====================================
# TAB 3 MULTIMODAL
# =====================================

with tabs[2]:

    st.header(
        "Requirement + Screenshot Analysis"
    )


    text = st.text_area(
        "Requirement",
        height=200
    )


    screenshot = st.file_uploader(
        "Screenshot",
        type=[
            "png",
            "jpg",
            "jpeg"
        ],
        key="multi"
    )


    if screenshot:

        st.image(
            screenshot,
            use_container_width=True
        )


    if st.button(
        "Run Multimodal Analysis"
    ):


        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        ) as file:

            file.write(
                screenshot.read()
            )

            path=file.name



        image_result=requests.post(
            API_IMAGE_URL,
            json={
                "image_path":path
            }
        ).json()


        final=requests.post(
            API_MULTIMODAL_URL,
            json={
                "requirement_text":text,
                "image_analysis":
                image_result.get("analysis")
            }
        )


        st.json(
            final.json()
        )



# =====================================
# TAB 4 ENGINEERING
# =====================================

with tabs[3]:

    st.header(
        "Engineering Artifact Generator"
    )


    req = st.text_area(
        "Project Requirement",
        height=220
    )


    if st.button(
        "Generate Engineering Output"
    ):


        response=requests.post(
            API_ENGINEERING_URL,
            json={
                "text":req
            }
        )


        result=response.json()


        if result.get("status")=="success":


            data=result["result"]


            st.success(
                "Engineering Artifacts Created"
            )


            st.subheader(
                "Project Summary"
            )

            st.write(
                data.get(
                    "project_summary"
                )
            )


            for key,value in data.items():

                if key!="project_summary":

                    st.subheader(
                        key.replace("_"," ").title()
                    )

                    st.json(value)



            # EXPORT

            st.divider()

            st.subheader(
                "Export Report"
            )


            json_data=json.dumps(
                data,
                indent=4
            )


            st.download_button(
                "Download JSON",
                json_data,
                "DevFlow_Report.json",
                "application/json"
            )


            markdown=f"""

# DevFlow Copilot Report


## Project Summary

{data.get("project_summary")}


## User Stories

{data.get("user_stories")}


## Requirements

{data.get("functional_requirements")}


## Database

{data.get("database_tables")}


## APIs

{data.get("api_endpoints")}


## QA

{data.get("qa_test_cases")}


## Risks

{data.get("risks")}


## Client Update

{data.get("client_update")}

"""


            st.download_button(
                "Download Markdown",
                markdown,
                "DevFlow_Report.md",
                "text/markdown"
            )



# =====================================
# TAB 5 EVALUATION
# =====================================

with tabs[4]:

    st.header(
        "AI Evaluation Dashboard"
    )


    evaluation_text=st.text_area(
        "Requirement For Evaluation",
        height=200
    )


    if st.button(
        "Evaluate"
    ):


        response=requests.post(
            API_EVALUATE_URL,
            json={
                "text":evaluation_text
            }
        )


        result=response.json()


        report=result.get(
            "evaluation_report",
            {}
        )


        col1,col2=st.columns(2)


        with col1:

            st.metric(
                "Quality Score",
                f'{report.get("quality_score",0)}/100'
            )


        with col2:

            st.metric(
                "Confidence",
                report.get(
                    "confidence",
                    "Unknown"
                )
            )


        st.subheader(
            "Result"
        )

        st.success(
            report.get(
                "evaluation"
            )
        )


        st.subheader(
            "Missing Sections"
        )

        missing=report.get(
            "missing_sections",
            []
        )


        if missing:

            st.json(
                missing
            )

        else:

            st.success(
                "No missing sections detected"
            )



        st.subheader(
            "Issues"
        )


        issues=report.get(
            "issues",
            []
        )


        if issues:

            st.json(
                issues
            )

        else:

            st.success(
                "No issues detected"
            )