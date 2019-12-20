import matplotlib.pyplot as plt
import numpy as np

sin_x=[2,4,8]
x = np.arange(0, 2*np.pi, 0.02)
sin_list=[]
tuple_legends=[]

for valor in sin_x:
    sin_list.append(np.sin(valor*x))
    aux="Seno de "+str(valor)+"X"
    tuple_legends.append(aux)
print(tuple_legends)
for i in range(len(sin_list)):
    plt.plot(x,sin_list[i])
plt.legend(tuple_legends,loc="upper right")
plt.savefig ("grah_curve_sin_nx.png")
plt.title ("Gráfico de Seno de 2X, 4X, 8X")
plt.show()