from decimal import Decimal
from fractions import Fraction
integer_num = Fraction.from_float(0.1)
print('integer_num_type:{}'.format(type(integer_num)))
print('integer_num:{}'.format(integer_num))
integer_ratio = (0.1).as_integer_ratio()
print('integer_ratio:{}'.format(integer_ratio))

decimal_num = Decimal.from_float(0.1)
print('decimal_num:{}'.format(decimal_num))
format_decimal_num = format(Decimal.from_float(0.1),'.17')
print('format_decimal_num type:{}'.format(type(format_decimal_num)))
print('format_decimal_num:{}'.format(format_decimal_num))
