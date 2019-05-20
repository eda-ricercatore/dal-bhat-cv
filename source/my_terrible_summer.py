#!/Users/zhiyang/anaconda3/bin/python3
#import numpy as np
import math
import matplotlib.pyplot as plt
x = list(range(10))
print("values of x:::",x,"=")

#y = np.pow(2.5,x)
y = []
for i in x:
  #y[i] = math.pow(2.5,i)
  y.append(math.pow(2.5,i))
print("values of y:::",y,"=")

"""
	matplotlib

	conda
"""

plt.plot(x, y, 'r*')
plt.yscale('log')
plt.xlabel('time (days since early May)')
plt.ylabel('difference between being a LLVM-hacking ASIP design automation engineer and me (dB)')
plt.title('My terrible summer')
plt.show()
