import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import math

excel_file = 'vd2.xlsx'
data = pd.read_excel(excel_file, index = False).values

def dataSort(data):
    lenght = len(data)
    for i in range(lenght-1):
        for j in range(i, lenght):
            if data[i][0] > data[j][0]:
                data[i][0], data[j][0] = data[j][0], data[i][0]
                data[i][1], data[j][1] = data[j][1], data[i][1]
    return data

def FindMonotonousInterval(data):
    indexs = []
    lenght = len(data)
    index_head = 0
    index_tail = 1    
    for i in range(lenght-2):
        delta_y1 = data[i][1] - data[i+1][1]
        delta_y2 = data[i+1][1] - data[i+2][1]
        if delta_y1 * delta_y2 > 0:
            index_tail += 1
        else:
            indexs.append([index_head, index_tail])
            index_head = index_tail
            index_tail += 1
    indexs.append([index_head, index_tail])
    return indexs

def InterpolationConditions(data):
    lenght = len(data)
    for i in range(lenght-1):
        for j in range(i+1,lenght):
            if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                return False
            if data[i][0] == data[j][0]:
                return False
    return True

def x_equidistant(data, index):
    i = index[0]
    while i < (index[1]-1):
        delta_x1 = data[i][0] - data[i+1][0]
        delta_x2 = data[i+1][0] - data[i+2][0]
        i += 1
        if abs(delta_x1 - delta_x2) >= 10e-5:
            print("x khong cach deu")
            return False
    print("x cach deu")
    return True
       
def ConsiderApprox(data, indexs, y):
    lenght = len(indexs) - 1
    Newton = []
    Lagrange = []
    while lenght >= 0:
        if data[indexs[lenght][0]][1] > data[indexs[lenght][1]][1]: 
            # Xét trên đơn điệu giảm
            if (data[indexs[lenght][0]][1]<y or y<data[indexs[lenght][1]][1]):
                indexs.remove(indexs[lenght])
            else:
                print("Mang: {} => Su dung phuong phap: ".format(indexs[lenght]), end='')
                thu = Lagrange_Newton(-data, indexs[lenght], y)
                x_equidistant(data, indexs[lenght])
                if thu == True :
                    Newton.append(indexs[lenght])
                else:
                    Lagrange.append(indexs[lenght])
        else:
            # xét trên đơn điệu tăng
            if data[indexs[lenght][0]][1]>y or y>data[indexs[lenght][1]][1]:
                indexs.remove(indexs[lenght])
            else:
                print("Mang: {} => Su dung phuong phap: ".format(indexs[lenght]), end='')
                thu = Lagrange_Newton(data, indexs[lenght], y)
                x_equidistant(data, indexs[lenght])
                if thu == True :
                    Newton.append(indexs[lenght])
                else:
                    Lagrange.append(indexs[lenght])
        lenght -= 1
    
    return Newton, Lagrange

# Đơn điệu tăng
def Lagrange_Newton(data, index, y):
    delta_y = []
    flat =  True
    if index[1] - index[0] == 1:
        print("Newton voi khoang 2 moc")
    else:
        if data[index[0]+1][1] > y and data[index[0]][1] < y:
            print("Newton Tien")
        elif data[index[1]-1][1] < y and data[index[1]][1] > y:
            print("Newton Lui")
        else:
            for i in range(index[1]-index[0]):
                d_y = abs(data[index[0]+i][1] - data[index[0]+i+1][1])
                d_x = abs(data[index[0]+i][0] - data[index[0]+i+1][0])
                delta = d_y/d_x
                delta_y.append(delta)

            ty_hieu_1 = delta_y[1]/delta_y[0]
            ty_hieu_2 = delta_y[-1]/delta_y[-2]
            
            if (ty_hieu_1 <= 1.5 and ty_hieu_1 >= 0.67) or (ty_hieu_2 <= 1.5 and ty_hieu_2 >= 0.67):
                print('Larange')
                flat = False
            else:
                print('Newton')
    return flat


if __name__ == "__main__":
    # sap xep lai bo du lieu tang dan theo x
    # kiem tra dieu kien noi suy
    # xet tung khoang (L or N)
    y = 2.5
    data_sort = dataSort(data)
    if InterpolationConditions(data_sort) == False:
        print("Khong noi suy duoc!, x,y phai doi mot khac nhau")
    else:
        indexs = FindMonotonousInterval(data_sort)
        Newton, Lagrange = ConsiderApprox(data, indexs, y)
        print("Newton: ", Newton)
        print("Lagrange: ", Lagrange)

        # ve do thi kiem chung
        x = []
        y = []
        for i in range(len(data)):
            x.append(data[i][0])
            y.append(data[i][1])

        plt.plot(x, y,'go-')
        plt.plot(x,[2.5]*len(data), '-')
        plt.title('vd2')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig('vd2.png')
        plt.show()
