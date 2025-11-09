def check_consent(user: dict) -> bool:
    return user.get("consent", False)

