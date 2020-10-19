import statistics
"""The statistics module calculates basic statistical properties 
-(the mean, median, variance, etc.) of numeric data"""
data=[2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
sorted_data=sorted(data)
print('sorted_data:{}'.format(sorted_data))
# mean
mean_num = statistics.mean(data)
print('mean_num:{}'.format(mean_num))
# median
median_num = statistics.median(data)
print('median_data:{}'.format(median_num))
# variance
variance_num = statistics.variance(data)
print('variance_num:{}'.format(variance_num))

