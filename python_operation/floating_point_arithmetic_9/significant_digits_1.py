import math

print('0.1:{}'.format(1 / 10))
# give 12 significant digits
significant_digits = format(math.pi, '.12g')
print('significant_digits:{}'.format(significant_digits))
# give 2 digits after the point
float_digits = format(math.pi,'.2f')
print('float_digits:{}'.format(float_digits))
# repr()-- 17 significant digits
repr_num = repr(math.pi)
print('repr_num:{}'.format(repr_num))
