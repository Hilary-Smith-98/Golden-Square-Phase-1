from lib.report_length import *

def test_report_length_7():
    result = report_length('Hello! ')
    assert result == 'This string was 7 characters long.'

def test_report_length_0():
    result = report_length("")
    assert result == 'This string was 0 characters long.'