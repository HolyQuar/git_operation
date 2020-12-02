"""
convert 0.1 to the closest fraction it can of the form J/2**N where J is an integer containing exactly 53 bits.
--1 / 10 ~= J / (2**N)
--J ~= 2**N / 10
"""
# J has exactly 53 bits (is >= 2**52 but < 2**53), the best value for N is 56
J_true_num = 2**52 <= 2**56 // 10 < 2**53
print('J_ture_num:{}'.format(J_true_num))
# The best possible value for J is then that quotient rounded:
q,r = divmod(2**56,10)
print('q:{},r:{}'.format(q,r))

# Since the remainder is more than half of 10, the best approximation is obtained by rounding up
q_num = q+1
print('q_num:{}'.format(q_num))
# 1/10: the best 754 double approximation it can get:
fraction_num = 0.1*2**55
print('fraction_num:{}'.format(fraction_num))
# the exact number stored in the computer is 53 bits.
# 17 significant digits
format_num = format(0.1,'.17f')
print('format_num:{}'.format(format_num))
