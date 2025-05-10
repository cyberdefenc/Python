#%timeit(for single line execution time) and %%timeit(for multiline execution time)

import time
import numpy as np

# Measure execution time of list comprehension
start = time.time()   #  stores the current time (start time).
[i**2 for i in range(1, 11)]
end = time.time()    #stores the current time after the operation finishes (end time).
print(end)
print("Execution Time (list comprehension):", end - start, "seconds")

# Measure execution time of for-loop with append
a = []
start = time.time()
for i in range(1, 15):
    a.append(i * 2)
end = time.time()
print("Execution Time (for loop):", end - start, "seconds") #  gives you the total execution time in seconds.
