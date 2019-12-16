#En este caso veremos como podemos leer archivos y 
#Tenemos< en la carpeta el archivo archivo.txt
lista_renglones = []
tranduccion = [ 
    """Ni tampoco hay nadie que ame, persiga y quiera alcanzar el dolor mismo porque sea dolor, sino porque a veces se dan las circunstancias de tal manera, que con esfuerzo y dolor puede obtenerse algún gran placer.""",
"""En efecto, para ir a cosas insignificantes, ¿quién de nosotros asume algún ejercicio físico trabajoso, si no es para conseguir alguna ventaja de él?""",
"""Por otra parte, ¿quién censuraría con razón a aquel que quiere estar en un placer al que no siga ninguna molestia, o a aquel que huye del dolor con el que no se produce ningún placer?""",
"""Pero sin duda acusamos y juzgamos, como los más dignos de un justo aborrecimiento a aquellos que, ablandados y corrompidos por el encanto de los placeres presentes, cegados por el deseo, no prevén los dolores y las molestias que han de sucederles, y están en falta semejante quienes abandonan sus deberes por debilidad de espíritu, es decir, por huir de esfuerzos y dolores."""
]
#de esta forma abrimos el archivo, reader será el objeto lector
#la función open admite el nombre del archivo y el modo a saber
# 'r' indica lectura, 'w' indica escritura  y la 'a' adicionar lineas

with open('archivo.txt','r') as reader:
    # lee, almacena y muestra en pantalla linea a linea del archivo
    for line in reader:
        print(line)
        lista_renglones.append(line)

with open('archivo_traducido.txt', 'w') as writer:
    #En este caso se almacena linea a linea un elemento a la lista
    for elemento in tranduccion :
        #Se debe adcionar el enter para que quede separado por renglones
        writer.write(elemento + "\n")
        print (elemento)

#para adicionar un elemento lo abrimos en modo de adición
with open('archivo_traducido.txt', 'a') as a_writer:
    a_writer.write('-----Fin de la traducción-----')

