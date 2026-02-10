def validate_email(email):
    """
    Validate an email address using basic rules.
    """
    if not email:
        return False, "Email cannot be empty"

    if "@" not in email:
        return False, "Email must contain '@'"

    if "." not in email.split("@")[-1]:
        return False, "Email domain is invalid"

    return True, "Valid email"


def test_cases():
    examples = [
        "",
        "userexample.com",
        "user@domain",
        "user@domain.com"
    ]

    for email in examples:
        print(email, "->", validate_email(email))


if __name__ == "__main__":
    test_cases()
