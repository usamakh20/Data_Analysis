import numpy as np
import matplotlib.pyplot as plt

alpha = np.genfromtxt("dataAlpha.txt",names=True)
print("Alpha average RTT: ",alpha["RTT"][alpha["RTT"]>0].mean())
print (alpha["StartTime"][-1]-alpha["StartTime"][0])

bravo = np.genfromtxt("dataBravo.txt",names=True)
print("Bravo average RTT: ",bravo["RTT"][bravo["RTT"]>0].mean())
print (bravo["StartTime"][-1]-bravo["StartTime"][0])

x = alpha["StartTime"]
y = alpha["RTT"]

plt.title("ALPHA vs BRAVO")
plt.xlabel("Time(s)")
plt.ylabel("RTT(ms)")
al=plt.scatter(x, y, color='red',alpha=0.8)
x = bravo["StartTime"]
y = bravo["RTT"]
br=plt.scatter(x, y, alpha=0.4)
plt.legend((al, br),
           ('ALPHA', 'BRAVO'),
           scatterpoints=1,
           loc='upper right',
           ncol=2,
           fontsize=10)

plt.show()

