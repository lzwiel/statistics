import statistics

# 输入一组数字
numbers = input("请输入一组数字，以空格分隔: ").split()
numbers = [int(num) for num in numbers]

# 求和
sum_of_numbers = sum(numbers)
print("Sum:", sum_of_numbers)

# 计数
count_of_numbers = len(numbers)
print("Count:", count_of_numbers)

# 求平均数
average_of_numbers = sum_of_numbers / count_of_numbers
print("Average:", average_of_numbers)

# 求众数
mode_of_numbers = statistics.mode(numbers)
print("Mode:", mode_of_numbers)

# 求中位数
median_of_numbers = statistics.median(numbers)
print("Median:", median_of_numbers)

# 找出最大数和最小数
max_number = max(numbers)
min_number = min(numbers)
print("Max:", max_number)
print("Min:", min_number)

# 重新按数字大小从大到小重新排序
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted:", sorted_numbers)
