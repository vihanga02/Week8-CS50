
from test import calculate

def testteest():
    assert calculate(2003, 5, 17) == "Ten million, three hundred and seventeen thousand, six hundred minutes"
    assert calculate(2000, 2, 1) == "Twelve million, forty-seven thousand and forty minutes"
    assert calculate(1991, 1, 1) == "Sixteen million, eight hundred and twenty-four thousand, nine hundred and sixty minutes"
    assert calculate(29, 1, 2983) == "Invalid Date"