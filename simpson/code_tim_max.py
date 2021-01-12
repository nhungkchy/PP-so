from sympy import *
import math
import numpy as np
def max_f(a, b, f):
    my_list = [limit(f, x, a), limit(f, x, b)]
    L = solve(f.diff(x), x)
    if L != []:
        for i in range (len(L)):
            if a <= L[i] <= b:
                my_list.append(limit(f, x, L[i]))
    return max(my_list)

file = open('demo_file.txt', 'w+')
x = Symbol('x')
f1 = 1/(x+1)
f2 = math.e ** (-x * x)
for i in range(2):
    f1 = f1.diff(x)
    f2 = f2.diff(x)

file.write(str(max_f(0, 1, f1)) + "\n")
file.write(str(max_f(0, 1, f2))+ "\n")

for i in range(2):
    f1 = f1.diff(x)
    f2 = f2.diff(x)

file.write(str(max_f(0, 1, f1))+ "\n")
file.write(str(max_f(0, 1, f2))+ "\n")



