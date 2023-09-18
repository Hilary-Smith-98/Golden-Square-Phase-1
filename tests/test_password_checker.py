from lib.password_checker import *
import pytest

def test_correct_password():
    pword_check = PasswordChecker()
    assert pword_check.check("12345678") == True

def test_incorrect_password():
    pword_check = PasswordChecker()
    with pytest.raises(Exception) as e:
        pword_check.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password - must be 8+ characters."
