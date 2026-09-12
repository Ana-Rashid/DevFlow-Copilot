from schema import ProjectSpecification


def validate_output(data):
    """
    Validate AI generated JSON against our specification schema.
    """

    try:
        validated = ProjectSpecification(**data)

        return {
            "valid": True,
            "data": validated.model_dump()
        }

    except Exception as e:

        return {
            "valid": False,
            "error": str(e)
        }