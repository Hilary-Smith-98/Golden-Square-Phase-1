from lib.counter import *

def test_counter_add_3():
    Counter1 = Counter()
    Counter1.add(3)
    result = Counter1.report()
    assert result == "Counted to 3 so far."

def test_counter_no_add():
    Counter1 = Counter()
    result = Counter1.report()
    assert result == "Counted to 0 so far."

def test_counter_negative():
    Counter1 = Counter()
    Counter1.add(-1)
    result = Counter1.report()
    assert result == 'Counted to -1 so far.'