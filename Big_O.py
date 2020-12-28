import matplotlib.pyplot as plt
from scipy.special import gamma
import math
import numpy as np
n = np.linspace(1,101,100)
O1 = gamma(n)
O2 = 2**n
O3 = n**2
O4 = n*np.log(n) / np.log(2)
O5 = n
O6 = np.sqrt(n)
O7 = np.log(n) / np.log(2)
plt.plot(n, O1, '--k', label='n!')
plt.plot(n, O2, '--r', label='2^n')
plt.plot(n, O3, '--g', label='n^2')
plt.plot(n, O4, 'y', label='nlog(n)')
plt.plot(n, O5, 'c', label='n')
plt.plot(n, O6, '--m', label='sqrt(n)')
plt.plot(n, O7, 'b', label='log(n)')
axes = plt.gca()
axes.set(xlim=(0, 100), ylim=(0, 100))
leg = axes.legend()
plt.show()