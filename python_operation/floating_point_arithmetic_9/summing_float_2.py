"""since 0.1 is not exactly 1/10,

summing three values of 0.1 may not yield exactly 0.3, either:
"""
import math

bool_num = .1 + .1 + .1 == .3
print('result:{}'.format(bool_num))
bool_false = round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1)
print('bool_false:{}'.format(bool_false))
"""with inexact values become comparable to one another"""
bool_true = round(.1 + .1 + .1, 10) == round(.3, 10)
print('bool_true:{}'.format(bool_true))

# The float.as_integer_ratio() method expresses the value of a float as a fraction:
x = 3.14159
integer_ratio = x.as_integer_ratio()
print('integer_ratio:{}'.format(integer_ratio))
#  the ratio is exact
bool_true_integer = 3537115888337719 / 1125899906842624
print('bool_true_integer:{}'.format(bool_true_integer))

# giving the exact value stored by your computer:
hexadecimal_float_value  = x.hex()
print('hexadecimal_float_value:{}'.format(hexadecimal_float_value))
#  reconstruct the float value exactly
bool_true_original = x == float.fromhex(hexadecimal_float_value)
print('bool_true_original:{}'.format(bool_true_original))

"""math.fsum():
mitigate loss-of-precision during summation
"""
bool_false_sum = sum([0.1]*10) == 1.0
print('bool_false_sum:{}'.format(bool_false_sum))
bool_true_fsum = math.fsum([0.1]*10) == 1.0
print('bool_true_fsum:{}'.format(bool_true_fsum))

