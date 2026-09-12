def evaluate_output(result):

    score = 100
    issues = []

    required_sections = [
        "project_summary",
        "user_stories",
        "acceptance_criteria",
        "functional_requirements",
        "non_functional_requirements",
        "database_tables",
        "api_endpoints",
        "implementation_plan",
        "developer_tasks",
        "qa_test_cases",
        "risks",
        "client_update"
    ]

    missing = []

    for section in required_sections:

        if section not in result:
            missing.append(section)
            score -= 8

        elif result[section] in [None, "", [], {}]:
            missing.append(section)
            score -= 8

    if len(result.get("user_stories", [])) == 0:
        issues.append("No user stories generated.")

    if len(result.get("qa_test_cases", [])) == 0:
        issues.append("QA test cases missing.")

    if len(result.get("api_endpoints", [])) == 0:
        issues.append("API endpoints missing.")

    if score >= 90:
        confidence = "High"

    elif score >= 70:
        confidence = "Medium"

    else:
        confidence = "Low"

    return {

        "quality_score": score,

        "confidence": confidence,

        "missing_sections": missing,

        "issues": issues,

        "evaluation": "Passed" if score >= 70 else "Needs Review"

    }