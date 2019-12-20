import matplotlib.pyplot as plt
lenguajes=["py", "java","node","angular"]
uso=[70, 10,10,10]
plt.bar(lenguajes,uso)
plt.title("Lenguajes más usados")
plt.xlabel("lenguajes")
plt.ylabel("porcenyaje de uso")
plt.savefig("Grafico_barras.png")
plt.show()
