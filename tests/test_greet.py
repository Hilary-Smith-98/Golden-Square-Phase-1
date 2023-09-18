from lib.greet import *

def test_greet_name_returns_correct_greeting():
    result = greet('John')
    assert result == 'Hello, John!'