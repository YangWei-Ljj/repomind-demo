from app.services.auth import validate_token


def test_expired_token():
    assert validate_token("expired") is False


def test_valid_token():
    assert validate_token("demo-token") is True
