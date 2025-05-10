import timeit

# Measure execution time of list comprehension with timeit
execution_time = timeit.timeit('[i**2 for i in range(1, 11)]', number=100000)
print("Execution Time (list comprehension):", execution_time, "seconds")

# Measure execution time of for-loop with append using timeit
execution_time_loop = timeit.timeit('''
a = []
for i in range(1, 15):
    a.append(i * 2)
''', number=100000)
print("Execution Time (for loop):", execution_time_loop, "seconds")
