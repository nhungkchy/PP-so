# input: mang du lieu(x,y), diem y
# doc file thanh array 2D
# sap xep lai theo thu tu tang dan cua x(viet ham)
# tim khoang don dieu
# tim khoang don dien chua y, xet tinh chat trong khoang ==> lua chon phuong phap
# uu nhuoc diem cua 2 pp deu lua chon pp la tot nhat.?????
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

    while lenght >= 0:
        if data[indexs[lenght][0]][1] > data[indexs[lenght][1]][1]:
            if (data[indexs[lenght][0]][1]>y or y>data[indexs[lenght][1]][1]):
                indexs.remove(indexs[lenght])
            else:
                # tinh chat can xet trong doan
                # tim va dua ra moc noi suy
                break
        else:
            if data[indexs[lenght][0]][1]>y or y>data[indexs[lenght][1]][1]:
                indexs.remove(indexs[lenght])
            else:
                #tinh chat can xet trong doan
                # tim va dua va moc noi suy
                break
        lenght -= 1
    
    return indexs

if __name__ == "__main__":
    data_sort = dataSort(data)
    print(data_sort)
    print(InterpolationConditions(data_sort))
    indexs = FindMonotonousInterval(data_sort)
    print(indexs)
    y = 2.5
    index_y = ConsiderApprox(data, indexs, y)
    print(index_y)

# print(10%8)

# s = 0
# for i in range(1,101):
#     for i 
