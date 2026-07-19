"""import time
import numpy as np
n=10000
m1=[[e for e in range(n)] for i in range(n)] 
m2=[[e for e in range(n)] for i in range(n)] 
start=time.time()
m1=np.array(m1)
m2=np.array(m2)

m1+m2
end=time.time()
print("%.6f sec"%(end-start))"""

"""
start=time.time()
for i in range(n):
    for j in range(n):
        m1[i][j]+m2[i][j]
end=time.time()
print("%.6f sec"%(end-start))

"""
