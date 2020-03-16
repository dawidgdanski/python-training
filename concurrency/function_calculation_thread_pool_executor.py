# ch1/example2.py

from concurrent.futures import ThreadPoolExecutor, as_completed
from timeit import default_timer as timer


# sequential
def f(x):
    return x * x - x + 1


start = timer()
result = 3
for i in range(20):
    result = f(result)

print('Result is very large. Only printing the last 5 digits:', result % 100000)
print('Sequential approach took: %.2f seconds.' % (timer() - start))


# concurrent
def concurrent_f(x):
    global result
    result = f(result)


result = 3

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(concurrent_f, i) for i in range(20)]

    _ = as_completed(futures)

print('Result is very large. Only printing the last 5 digits:', result % 100000)
print('Concurrent approach took: %.2f seconds.' % (timer() - start))
