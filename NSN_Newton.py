import math
import numpy as np

class Newton:
    def __init__(self, Data, y0):
        self.yData = Data[1]
        self.xData = Data[0]
        self.y = y0
        # self.h = xData[1] - xData[0]

    def __Bangsaiphan(self):
        m = len(self.yData)
        a = np.zeros((m,m))
        for k in range(m):
            a[k][0] = self.yData[k]

        for i in range(1,m):
            for j in range(1,i+1):
                a[i][j] = a[i][j-1] - a[i-1][j-1]
        return a


    def Newtontien(self):
        a = __Bangsaiphan()
        pp = 0 # xác định công thức lặp
        heso = []
        for i in range(4):
            heso.append(a[i][i]/a[1][1])

        print(heso)
        t0 = (self.y-a[0][0])/a[1][1]
        __Lapdon(t0, heso, pp)


    def Newtonlui(self):
        a = __Bangsaiphan()
        pp = 1  # xác định công thức lặp
        heso = []
        for i in range(4):
            heso.append(a[3][i]/a[3][1])

        t0 = (self.y-a[3][0])/a[3][1]
        __Lapdon(t0, heso, pp)


    def Betxen(self):
        a = self.__Bangsaiphan()
        pp = 2
        heso = []
        for i in range(3):
            heso.append(a[i][1]/a[2][1])

        t0 = (self.y - a[1][0])/a[2][1]
        self.__Lapdon(t0, heso, pp)


    def __Lapdon(self, t0, heso, pp):
        esp = 0.000001
        max = 1000
        delta = 100
        flag = 1
        i = 1
        t = t0 # xap xi dau
        print(t0)
        while (delta > esp):
            # print("del, esp",delta, esp)
            t1 = t
            # print (t1)
            if (pp == 0):
                t =  self.__g0(t0, t1, heso)
                # print("t ",t)
                # print("t1 ",t1)
            elif (pp == 1):
                # print(heso)
                t = self.__g1(t0, t1, heso)
            elif (pp == 2):
                t = self.__g2(t0, t1, heso)
            print("Lan lap thu", i, "co nghiem la", t)
            delta = math.fabs(t - t1)
            # print("del, esp", delta, esp)
            i += 1
            if (i > max):
                flag = 0
                break
        if (flag == 1):
            # x = t*h + x0
            print("Ket qua: %.5f ", t)
        else:
            print("Khong hoi tu hoac hoi tu cham!")


    def __g0(self, t0, t, heso):
        t1 = t0 - ((heso[2]/2)*t*(t - 1)) - ((heso[3]/(2*3))*t*(t-1)*(t-2))
        return t1
    def __g1(self, t0, t, heso):
        t1 = t0 - (heso[2]/2)*t*(t+1) - (heso[3]/(2*3))*t*(t+1)*(t+2)
        return t1
    def __g2(self, t0, t, heso):
        t1 = t0 + t*(t-1)*(heso[2]-heso[0])
        return t1

# xData = [-2.121, -0.707 , 0.707, 2.121]
# yData = [-6.42062, 1.3536, 0.6464, 8.42018]
# h = xData[1] - xData[0]
# Betxen(h, yData, 0.901, 0.707)


Data = [[-2.121, -0.707 , 0.707, 2.121],[-6.42062, 1.3536, 0.6464, 8.42018]]
tt = Newton(Data, 0.901)
tt.Betxen()