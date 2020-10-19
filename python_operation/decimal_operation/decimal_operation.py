from decimal import *
if __name__=='__main__':
    """
    A decimal number is immutable:
     special values such as Infinity, -Infinity, and NaN.-0,+0
    """
    getcontext().prec = 6
    result=Decimal(1) / Decimal(7)
    print(round(result,5))
    getcontext().prec = 28
    result1=Decimal(1) / Decimal(7)
    print(result1)
    print(getcontext())
    #construction
    #integer
    int_decimal=Decimal(10)
    int_decimal=Decimal(10)
    print(int_decimal)
    print(type(int_decimal))
    #str
    str_decimal=Decimal('3.14')
    print(str_decimal)
    #float--28bit
    float_decimal = Decimal(3.14)
    print(float_decimal)
    print(Decimal(str(2.0**0.5)))
    print(Decimal('NaN'))

    print(Decimal('-Infinity'))