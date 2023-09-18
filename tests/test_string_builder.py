from lib.string_builder import *

def test_string_builder_add_nothing():
    Nothing = StringBuilder()
    assert Nothing.output() == ""

def test_string_builder_hello():
    Greeting = StringBuilder()
    Greeting.add("Hello")
    assert Greeting.output() == 'Hello'

def test_string_builder_length_single():
    Greeting = StringBuilder()
    Greeting.add("Hello")
    assert Greeting.size() == 5

def test_string_builder_hello_you():
    Greeting = StringBuilder()
    Greeting.add("Hello")
    Greeting.add(", you!")
    output_result = Greeting.output()
    assert output_result == 'Hello, you!'

def test_string_builder_length_multiple():
    Greeting = StringBuilder()
    Greeting.add("Hello")
    Greeting.add(", you!")
    assert Greeting.size() == 11
