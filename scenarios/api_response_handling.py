def build_response(success, data=None, error=None):
    """
    Build a structured API-like response.
    """
    if success:
        return {
            "status": "success",
            "data": data
        }

    return {
        "status": "error",
        "message": error or "Unknown error"
    }


def example_responses():
    print(build_response(True, {"id": 1}))
    print(build_response(False, error="Invalid request"))


if __name__ == "__main__":
    example_responses()
