def validate_token(token: str | None) -> bool:
    if not token or token == "expired":
        return False
    return True
