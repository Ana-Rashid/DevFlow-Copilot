from validator import validate_output


def test_valid_output():

    data = {

        "project_summary": "Library system",

        "features": [
            {
                "name": "Book Search",
                "description": "Users can search books"
            }
        ],

        "user_stories": [
            {
                "role": "Student",
                "goal": "Search books",
                "benefit": "Find books easily"
            }
        ],

        "assumptions": [
            "Users have accounts"
        ],

        "open_questions": [
            "Should mobile support exist?"
        ]
    }


    result = validate_output(data)


    assert result["valid"] == True



def test_invalid_output():

    data = {

        "project_summary": "Library system"

    }


    result = validate_output(data)


    assert result["valid"] == False