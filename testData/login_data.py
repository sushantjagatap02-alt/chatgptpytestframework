# Test data for login tests
VALID_CREDENTIALS = {
    "email": "test@test.com",
    "password": "Password123"
}

INVALID_EMAILS = [
    {"email": "", "password": "Password123", "description": "Empty email"},
    {"email": "invalid", "password": "Password123", "description": "Invalid format"},
    {"email": "notexist@test.com", "password": "Password123", "description": "Non-existent email"},
]

INVALID_PASSWORDS = [
    {"email": "test@test.com", "password": "", "description": "Empty password"},
    {"email": "test@test.com", "password": "WrongPassword", "description": "Wrong password"},
]

BOTH_EMPTY = [
    {"email": "", "password": "", "description": "Both fields empty"},
]
