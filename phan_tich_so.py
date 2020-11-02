# input: mang du lieu(x,y), diem y
# doc file thanh array 2D
# sap xep lai theo thu tu tang dan cua x(viet ham)
# tim khoang don dieu
# tim khoang don dien chua y, xet tinh chat trong khoang ==> lua chon phuong phap?
# output: Khoang(phuong phap giai quyet) + moc noi suy

import pandas as pd 

excel_file = 'data.xlsx'
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
    

    return

def ConsiderApprox(data, indexs, y):
    lenght = len(data)

    for index in indexs:
        if (data[index[0]][1]-data[index[1]][1])>0:
            if (data[index[0]][1]<y or y<data[index[1]][1]):
                indexs.remove(index)
            else:
                # tinh chat can xet trong doan
                # tim va dua ra moc noi suy
        else:
            if data[index[0]][1]>y or y>data[index[1]][1]:
                indexs.remove(index)
            else:
                #tinh chat can xet trong doan
                # tim va dua va moc noi suy
    
    return indexs


data_sort = dataSort(data)
print(data_sort)
indexs = FindMonotonousInterval(data_sort)
print(indexs)
y = 2.5
index_y = ConsiderApprox(data, indexs, y)
print(index_y)

