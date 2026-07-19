import matplotlib.pyplot as plt
import numpy as np

x=np.array([20,30,40,50])
y=np.array([3,2,5,4])

# plt.plot(x,y,'o')
# plt.plot(x,y,marker='o')
"""plt.plot(x,y,marker='o',ms=15,mec='k',mfc="#72EABA")""" #markersize can be written as ms.marker edge color as mec.mfc as marker face color.
plt.box(x,y)
plt.show()
