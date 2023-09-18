from lib.gratitudes import Gratitudes

def test_gratitudes_format():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

def test_gratitudes_add_2():
    gratitudes = Gratitudes()
    gratitudes.add('Family')
    gratitudes.add('Education')
    assert gratitudes.format() == "Be grateful for: Family, Education"

