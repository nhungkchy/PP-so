import numpy as np 

# there's an example at the end of file
def validate_input(x, y, f):
	if(len(x) != len(y)):
		print("|x| != |y| !!")
		return False
	if(len(f) < 1):
		print("No function basis")
		return False 
	return True

def least_square(x, y, f):
	if(not validate_input(x,y,f)):
		print("Condition(s) didn't meet")
		return False
	n = len(x);	
	m = len(f); fx = []
	x = np.array(x)
	for i in range(0, m):
		fx.append(f[i](x))
	one = np.array([1]*n).reshape(n,1)
	X = np.array(fx).T
	Y = np.array(y).reshape(n,1)
	XT = X.T
	XTX = XT.dot(X)
	XTY = XT.dot(Y)
	B = np.linalg.inv(XTX).dot(XTY)
	def new_f(x):
		s = 0
		for i in range(0, m):
			s += f[i](x)*B[i]
		return s
	return [new_f, B]

### An example
x = np.arange(9) # x = [0,1,2,3,...8]
y = np.sin(x)*4 + np.random.rand(9) + x**2 + 3

"""
	f1 = 1
	f2 = x
	f3 = sin(x)
"""
f = [np.ones_like, lambda x: x, np.sin]

[f, Bi] = least_square(x, y, f)
print(Bi)
# b3 + x*b2 + b1*x^2 + b0*x^3
# poly_ls_get_formula(Bi,4) # print the formular out

# visualize
import matplotlib.pyplot as plt 
xx = np.linspace(min(x), max(x))
plt.plot(x, y, 's')
plt.plot(xx, f(xx), '--')
plt.show()
