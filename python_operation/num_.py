"""
types of numbers:
int/float
Decimal--source_code:decimal.py
/Fraction
"""


def result(tax, price):
    return price * tax


if __name__ == '__main__':
    tax = 12.5 / 100
    price = 100.50
    _ = result(tax, price)
    print(_)
    print(round(_, 2))
