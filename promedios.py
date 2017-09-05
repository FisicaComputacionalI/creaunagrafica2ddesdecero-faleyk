import pylab as pl
import matplotlib.pyplot as plt
X = [1,2,3,4,5]
Y = [7.5,7.7,7.8,8.2,8.6]
plt.scatter(X, Y, s=60, c='red', marker='^')
plt.title('Promedio por semestre')
plt.ylabel('Promedio')
plt.xlabel('Semestre')
plt.savefig('promedios.png')
plt.show()

