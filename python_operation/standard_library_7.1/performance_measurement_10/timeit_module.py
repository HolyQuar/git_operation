from timeit import Timer
# swapping arguments
traditional_times= Timer('t=a; a=b; b=t', 'a=1; b=output_formatting_1').timeit()
print('traditional_times:{}'.format(traditional_times))
tuple_time=Timer('a,b = b,a', 'a=1; b=output_formatting_1').timeit()
print('tuple_time:{}'.format(tuple_time))
