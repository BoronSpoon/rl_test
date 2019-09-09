import timeit
import numpy as np
s1 = """
a = []
b = []
c = []
d = None
a = {0:b, 1:c}
i = 0
d = a[i]
"""

s2 = """
a = []
b = []
c = []
d = None
a = {0:b, 1:c}
i = 0
if i == 0:
    d = b
else:
    d = c
"""

print(timeit.timeit(stmt=s1, number=10000))
print(timeit.timeit(stmt=s2, number=10000))