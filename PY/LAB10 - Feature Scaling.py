import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,20,0.4)
y1 = np.sin(x)
y2 = np.cos(x)*50

print(x)
print(y1)
print(y2)

plt.plot(x,y1,'red')
plt.plot(x,y2,'blue')
plt.show()

y1_new = (y1-min(y1))/(max(y1)-min(y1))
y2_new = (y2-min(y2))/(max(y2)-min(y2))

plt.plot(x,y1_new,'red')
plt.plot(x,y2_new,'blue')
plt.show()

#normalisation

y1_new = (y1-np.mean(y1))/(max(y1)-min(y1))
y2_new = (y2-np.mean(y2))/(max(y2)-min(y2))

plt.plot(x,y1_new,'red')
plt.plot(x,y2_new,'blue')
#plt.show()

y1_new = (y1-np.mean(y1))/np.std(y1)
y2_new = (y2-np.mean(y2))/np.std(y2)

plt.plot = (x,y1_new,'red')
plt.plot = (x,y2_new,'green')
plt.show()
