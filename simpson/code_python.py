from sympy import *
import math
import numpy as np
def F(x):         
    return 1/(x+1)

def max_f(a, b, f):
    my_list = [limit(f, x, a), limit(f, x, b)]
    L = solve(f.diff(x), x)
    if L != []:
        for i in range (len(L)):
            if a <= L[i] <= b:
                my_list.append(limit(f, x, L[i]))
    return max(my_list)
a = 0
b = 1
Max_2 = 0
Max_4 = 0
x = Symbol('x')
f = 1/(x+1)
for i in range(2):
    f = f.diff(x)
Max_2 = max_f(a, b, f)
for i in range(2):
    f = f.diff(x)
Max_4 = max_f(a, b, f)

#n là số khoảng chia, nếu choose khác HinhThang thì sẽ chạy công thức simpson, mọi người muốn nhập hàm khác thì chỉ cần thay hàm F(x)

def TTP(a, b, n, choose = "HinhThang"):
    ans = 0
    es = 0
    if choose == "HinhThang":
        h = (b - a)/n
        X = []
        Y = []
        for i in range (n+1):
            X.append(a+ i * h)
            #print(X)
            Y.append(F(a + i * h))
        for i in range(n+1):
            if i == 0 or i == n:
                ans += Y[i]
            else:
                ans += 2 * Y[i]
        return h / 2 * ans, Max_2/12 * (b-a) * math.pow(h, 2)
    else:
        h = (b - a) / n
        X = []
        Y = []
        for i in range (n+1):
            X.append(a+ i * h)
            Y.append(F(a + i * h))
        for i in range(n+1):
            if i == 0 or i == n:
                ans += Y[i]
            elif i % 2 == 1:
                ans += 4 * Y[i]
            else:
                ans += 2 * Y[i]
        return h / 3 * ans, Max_4 * (b-a) * math.pow(h, 4)

#ans là kết quả, es là sai số tính theo CT tổng quát trang 188 và 189
ans, es = TTP(0, 9999999999, 20, "Simpson")
print(ans)
print(es)


