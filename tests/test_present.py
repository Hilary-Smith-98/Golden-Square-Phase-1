import pytest
from lib.present import *

# Test wrap
def test_present_wrap_gift():
    present = Present()
    present.wrap('Gift')
    assert present.contents == 'Gift'

# Test wrap error
def test_present_wrap_twice():
    present = Present()
    present.wrap('Gift')
    with pytest.raises(Exception) as e: 
        present.wrap('Gift_2')
    error_message = str(e.value) 
    assert error_message == "A contents has already been wrapped."

# Test unwrap
def test_present_unwrap_gift():
    present = Present()
    present.wrap('Gift')
    assert present.unwrap() == 'Gift'

# Test unwrap error
def test_present_unwrap_no_gift():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'