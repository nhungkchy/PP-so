from scipy.integrate import quad
import numpy as np

def integrand(t,x):
    return np.exp(-x*t) / t

def expint(x):
    return quad(integrand, 1, np.inf, args=(x))[0]

print(expint(1))

result = quad(lambda x: expint(x), 0, np.inf)
print(result)

