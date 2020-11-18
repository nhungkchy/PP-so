import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series


#y = [17,17.5,76,210.5,1970]
#x = [1,2,3,4,7]
# x = [1,1.2,1.4,1.6,2]
# y = [2.1435,2.297,2.639,3.031,4]

# x = [1,2,3,4,5]
# y = [2,4,8,16,32]

def choosePoint(x, y):
    newX = []
    newY = []
    point = float(input("Nhap diem noi suy: "))
    for i in range(len(x)):
        if point < x[i]:
            return i
    if i == 0 or i == None:
        print("Moc duoc chon khong nam trong khoang noi suy.")
    else:
        if len(x) < 6:
            print("Lay tat ca cac moc noi suy")
            newX = x
            newY = y
        

def multiPoly(A, B):
    prod = [0]*(len(A) + len(B) - 1)
    for i in range(0, len(A), 1):
        for j in range(0, len(B), 1):
            prod[i + j] += A[i] * B[j]
    return prod

def Lagrange(x, y, F, L):
    L = [[0] * len(x)] * len(x)
    poly = [[0, 0]]*len(x)  # mảng cho các đa thức đơn vị
    temp = [1]*len(x)
    tempPoly = [[]]*len(x)  # đa thức cơ sở ( 1 + 0*x)
    for i in range(len(x)):
        poly[i] = [-x[i], 1]
        # hàm tạo các đa thức nhỏ từ mảng x
    for i in range(len(x)):
        if i == 0:
            tempPoly[i] = poly[1]
        else:
            tempPoly[i] = poly[0]
        for j in range(len(x)):
            if (j != 0 and j != i and i != 0) or (i == 0 and (j > 1)):
                # if i != j:
                tempPoly[i] = multiPoly(tempPoly[i], poly[j])
                # tinh tu so L[i]
            if j != i:
                temp[i] *= (poly[i][0] - poly[j][0])
                # tính mẫu số L[i]
    for i in range(len(tempPoly)):
        L[i] = [tempPoly[i][j]/temp[i] for j in range(len(tempPoly[i]))]
        # tính các đa thức Lagrange cơ bản

    for i in range(len(x)):
        for j in range(len(x)):
            F[i] += L[j][i] * y[j]
            # tính đa thức Lagrange
    return L, F
    # return tempPoly, L

def printPoly(F):
    print("F = ", end='')
    for i in range(len(F)):
        if i != len(F)-1:
            print(f'{F[i]}*x^{i} + ', end='')
        else:
            print(f'{F[i]}*x^{i}  ', end='')

if __name__ == "__main__":
    data = pd.read_excel('VD.xlsx')
    x = []
    y = []
    for i in range(len(data)):
        y.append(data.iat[i, 0])  # đọc dữ liệu lưu cho x
        x.append(data.iat[i, 1])  # đọc dữ liệu lưu cho y
    size = len(x)
    print(x)
    print(y)
    F = [0]*len(x)  # mảng cho đa thức nội suy Lagrange
    L = [[0]*len(x)]*len(x)  # mảng cho các đa thức Lagrange cơ bản
    L, F = Lagrange(x, y, F, L)
    printPoly(F)
    k = 0.9
    result = 0
    for i in range(len(F)):
        result += F[i]*pow(k,i)
    print("\n kết quả")
    print(result)
