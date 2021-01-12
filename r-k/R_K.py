import numpy as np
import math
import matplotlib.pyplot as plt

#vd1
#def f(x, y):
#    return x + y
#nghiem dung vd1: y = -x-1-2*e^(x)
#def nghiem(x):
#  return - x - 1 + 2*math.exp(x)

#vd2
def f(x, y):
   return y - 2*x/y
#nghiem dung vd2: y = sqrt(2*x+1)
def nghiem(x):
   return math.sqrt(2*x + 1)


def RK3(x0, y0, x, stepnum):
    h = (x-x0)/stepnum
    xk =[x0]
    yk =[y0]
    print("xk", "".ljust(2),"|","yk", "".ljust(25))
    print("----------------------------")
    print(x0,"".ljust(3),"|",y0,"".ljust(7))
    for i in range(0,stepnum):
        k1 = f(x0,y0)
        k2 = f(x0+h/2, y0+h*k1/2)
        k3 = f(x0+h,y0 - h*k1 +2*h*k2)
        y0 = y0 + h*(k1/6+2/3*k2+k3/6)
        x0 = x0 + h
        print(str(np.round(x0,3)).ljust(5),"|",str(y0).ljust(7))
        xk.append(x0)
        yk.append(y0)
    return np.asanyarray(xk), np.asanyarray(yk)

def RK4(x0, y0, x, stepnum):
    h = (x-x0)/stepnum
    xk = [x0]
    yk = [y0]
    print("xk", "".ljust(2),"|", "yk", "".ljust(7))
    print("----------------------------")
    print(x0,"".ljust(3),"|", y0,"".ljust(8))
    for i in range(0, stepnum):
        k1 = f(x0, y0)
        k2 = f(x0 + h/2, y0 + h*k1/2)
        k3 = f(x0 +h/2, y0 + h*k2/2)
        k4 = f(x0 +h, y0 + h*k3)
        x0 = x0 + h
        y0 = y0 + h*(k1+2*k2+2*k3+k4)/6
        print(str(np.round(x0,3)).ljust(5) , "|", str(y0).ljust(7))
        xk.append(x0)
        yk.append(y0)
    return np.asarray(xk), np.asarray(yk)

def RK5(x0, y0, x, stepnum):
    h = (x-x0)/stepnum
    xk =[x0]
    yk =[y0]
    print("xk", "".ljust(2),"|", "yk", "".ljust(7))
    print("----------------------------")
    print(x0,"".ljust(3),"|", y0,"".ljust(8))
    for i in range(0, stepnum):
        k1 = f(x0, y0)
        k2 = f(x0 + h/4, y0 + h*k1/4)
        k3 = f(x0 + h/4, y0 + h*k1/8 + h*k2/8)
        k4 = f(x0 + h/2, y0 - h*k2/2 + h*k3)
        k5 = f(x0 +3*h/4, y0 +3/16*h*k1+9/16*h*k4)
        k6 = f(x0+ h, y0 - 3/7*h*k1 + 2/7*h*k2 + 12/7*h*k3 - 12/7*h*k4 + 8/7*h*k5)
        x0 = x0 + h
        y0 = y0 + h/90*( 7*k1 + 32*k3 +12*k4 + 32*k5 +7*k6)
        print(str(np.round(x0,3)).ljust(5) , "|", str(y0).ljust(7))
        xk.append(x0)
        yk.append(y0)
    return np.asarray(xk), np.asarray(yk)


#--------Main Frogram--------------
def main(index):
    if(index == 1):#so sanh sai so giua RK3, Rk4, Rk5
        print('RK3')
        s1,s2 = RK3(0, 1, 0.5, 5)
        print('\nRK4')
        s3,s4 = RK4(0, 1, 0.5, 5)
        print('\nRK5')
        s5,s6 = RK5(0, 1,0.5, 5)

        s = []
        ss1 =[]
        ss2 = []
        ss3 = []
        for i in range(0, len(s3)):
            s.append(nghiem(s1[i]))
            ss1.append(math.fabs(s2[i]-s[i]))
            ss2.append(math.fabs(s4[i]-s[i]))
            ss3.append(math.fabs(s6[i]-s[i]))
        fig, (ax1, ax2) = plt.subplots(1,2, sharey = False)
        print('\nNghiệm đúng',s)
        print('\nSai số RK3:', math.fabs(s2[len(s2)-1]-s[len(s2)-1]))
        print("\nSai số RK4:", math.fabs(s4[len(s4)-1]-s[len(s2)-1]))
        print("\nSai số RK5:", math.fabs(s6[len(s4)-1]-s[len(s2)-1]))
        ax1.set_title('SAI SỐ')
        ax1.plot(s1,ss1,'bo--',label='RK3')
        ax1.plot(s1,ss2,'ro--',label = 'RK4')
        ax1.plot(s1,ss3,'go--',label = 'RK5')
        ax1.legend()
        ax2.set_title('BIỂU DIỄN NGHIỆM')
        ax2.plot(s1,s2,'bo--',label = 'RK3')
        ax2.plot(s1,s4, 'ro--',label ='RK4')
        ax2.plot(s1,s6, 'go--',label = 'RK5')
        ax2.plot(s1, s, label = 'Nghiệm đúng')
        ax2.legend()
        plt.show()
    else:#so sanh sai so bằng RK4  voi cac buoc nhay khac nhau
        print('h = 0.1')
        s1, s2 = RK4(0, 1, 0.5, 5)
        print('\nh= 0.05')
        s3, s4 = RK4(0, 1, 0.5, 10)
        ss1 = []
        for i in range(0, len(s1)):
            ss1.append(math.fabs(nghiem(s1[i])-s2[i]))
        ss2 = []
        for i in range(0, len(s3)):
            print(nghiem(s3[i]))
            ss2.append(math.fabs(nghiem(s3[i])- s4[i]))
        print("Sai số với h = 0.1: ",ss1[len(s1)-1])
        print("Sai số với h = 0.05: ",ss2[len(s3)-1])
        plt.plot(s1, ss1,'go--', label = 'h = 0.1')
        plt.plot(s3, ss2, 'ro--', label = 'h = 0.05')
        plt.title('So sánh sai số giữa các bước nhảy')
        plt.legend()
        plt.show()
main(1)#chạy ví dụ bằng RK3, RK4, RK5 và so sánh sai số
#main(2)# chạy ví dụ với 2 bước nhảy khác nhau bằng RK4 và so sánh sai số
