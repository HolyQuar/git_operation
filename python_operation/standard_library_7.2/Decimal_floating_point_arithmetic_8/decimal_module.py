"""
Compared to the built-in float implementation of binary floating point, the class is especially helpful for:

--financial applications and other uses which require exact decimal representation,
--control over precision,
--control over rounding to meet legal or regulatory requirements,
--tracking of significant decimal places, or
--applications where the user expects the results to match calculations done by hand.
"""
# control over rounding/financial applications /control over precision
from decimal import *
decimal_data = round(Decimal('0.70')*Decimal('1.05'),2)
print('decimal_data:{}'.format(decimal_data))
float_point_round = round(.70*1.05,2)
print('float_point_round:{}'.format(float_point_round))

#  to perform modulo calculations and equality tests that are unsuitable for binary floating point:
zero_compute=Decimal('1.00')%Decimal('.10')
print('zero_compute:{}'.format(zero_compute))
print('zero_float:{}'.format(1.00%0.1))

# tracking of significant decimal places
bool_result = sum([Decimal('0.1')*10]) == Decimal('1.0')
print('bool_result:{}'.format(bool_result))

bool_false = sum([0.1]*10) == 1.0
print('bool_false:{}'.format(bool_false))

# The decimal module provides arithmetic with as much precision as needed
getcontext().prec = 12
result_data = Decimal(1)/Decimal(7)
print('result_data:{}'.format(result_data))