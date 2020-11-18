import pandas as pd 
import matplotlib.pyplot as plt

excel_file = 'data.xlsx'
data = pd.read_excel(excel_file, index = False).values
x =pd.read_excel(excel_file, index = False).values

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

def ConsiderApprox(data, indexs, y):
    lenght = len(indexs) - 1
    Newton_tien = []
    Newton_lui = []
    Lagrange = []
    while lenght >= 0:
        if data[indexs[lenght][0]][1] > data[indexs[lenght][1]][1]: 
            # Xét trên đơn điệu giảm
            if (data[indexs[lenght][0]][1]<y or y<data[indexs[lenght][1]][1]):
                indexs.remove(indexs[lenght])
            else:
                print(-data)
                Lagrange_Newton(-data, indexs[lenght], y)
        else:
            # xét trên đơn điệu tăng
            if data[indexs[lenght][0]][1]>y or y>data[indexs[lenght][1]][1]:
                indexs.remove(indexs[lenght])
            else:
                Lagrange_Newton(data, indexs[lenght], y)
        lenght -= 1
    
    return indexs

# Đơn điệu tăng
def Lagrange_Newton(data, index, y):
    delta_y = []
    if index[1] - index[0] == 1:
        print("Newton")
    else:
        if data[index[0]+1][1] > y and data[index[0]][1] < y:
            print("Newton Tien")
        elif data[index[1]-1][1] < y and data[index[1]][1] > y:
            print("Newton Lui")
        else:
            for i in range(index[1]-index[0]):
                delta = abs(data[index[0]+i][1] - data[index[0]+i+1][1])
                print(data[index[0]+i][1], data[index[0]+i+1][1])
                print(delta)
                delta_y.append(delta)
            if (delta_y[1]/delta_y[0] <= 1.5 and delta_y[1]/delta_y[0] >= 0.67) or (delta_y[-1]/delta_y[-2] <= 1.5 and delta_y[-1]/delta_y[-2] >= 0.67):
                print
                print('Larange')
            else:
                print('Newton')

if __name__ == "__main__":
    # sap xep lai bo du lieu tang dan theo x
    # kiem tra dieu kien noi suy
    # xet tung khoang (L or N)
    data_sort = dataSort(data)
    print(data_sort)
    print(InterpolationConditions(data_sort))
    indexs = FindMonotonousInterval(data_sort)
    print(indexs)
    y = 2.5
    index_y = ConsiderApprox(data, indexs, y)
    print(index_y)
    plt.plot([0,0.2,0.4,0.6,0.8,1,1.2], [1.27,2.14,3.01,3.86,3.45,2.05,1.75] ,'go-')
    plt.show()
