import statistics

# 输入一组数字
numbers = input("请输入一组数字，以空格分隔: ").split()
numbers = [int(num) for num in numbers]

# 求和
sum_of_numbers = sum(numbers)
print("求和结果:", sum_of_numbers)

# 计数
count_of_numbers = len(numbers)
print("计数结果:", count_of_numbers)

# 求平均数
average = sum_of_numbers / count_of_numbers
print("平均数:", average)

# 求中位数
median = statistics.median(numbers)
print("中位数:", median)

# 求众数
mode = statistics.mode(numbers)
print("众数:", mode)

# 求方差
variance = statistics.variance(numbers)
print("方差:", variance)
