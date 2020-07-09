import statistics
#from statistics import mean, median, mode, stdev
#from statistics import mean
#from statistics import median

nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
print("the minimum is: ")
num_min = min(nums)
print(num_min)
print("the max is: ")
num_max = max(nums)
print(num_max)
print("the sum: ")
print(sum(nums))

print("Mean is" + statistics.mean(nums))
print("Median is : "+ (statistics.median(nums)))
print("Variance is" + statistics.variance(nums))
print("Standard deviation is" + statistics.stdev(nums))