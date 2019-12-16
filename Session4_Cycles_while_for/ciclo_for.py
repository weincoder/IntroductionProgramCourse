# Ciclo For. Este ciclo se repito por un número de veces conocidas
# primero veamos la función range
print (range(3))
#como vemos aperece range (0,3) indicando qeu hace una lista del 0 hasta completar 3 digitos
#es decir genera un rango 0,1,2 si pusieramos range(8) generaria el rango 0,1,2,3,4,5,6,7

#En este caso se procede a mostrar en pantalla el valor 0,1,2 ya que i
#aumentará en uno en uno por iteración
for i in range (3) :
    print(i)

#Tambien los ciclos for estan muy relacionados a las listas
#por ejemplo supongamos que tenemos la lista de edades y nombres de unos estudiantes
#una manera de almacenarlo seria en listas

#cuando se crea encerrado en [] indica que es una lista estas son iterables,
#Se pueden modificar en el tiempo, su primera coordenada es la coordenada 0
#por lo tanto para edades la coordenada dos  es 18
edades = [21,22,18,17,16,14]
print (edades[2])
#En el siguiente podemos ver que esta encerrado en () esto indica que es una tupla
#Estas son inmutables es decir  no se puede asignar valor a un campo ya asignado
nombres = ("mafer","gio","nano", "daniel", "gabriel","Olimac")
#Que debería salir al dar esta instrucción?
print (nombres[1])
#supongamos que deseamos mostrar en pantalla los estudiantes y sus edades
#len () es una función que retorna la cantidad de elementos en una lista
#por lo tanto para recorrer la lista completa lo hacemos en el rango de
#su tamaño.
for i in range (len(nombres)):
    print("el estudiante {} tiene una edad de {} años".format(nombres[i],edades[i]))

#Otra forma de mostrar los elementos de una lista es la siguiente :

for elemento in nombres:
    print ("Hola soy el estudiante llamado {}".format(elemento))
#En el caso anterior podemos ver como elemento cada vez que entraba
#En el ciclo se valía igual al elemento correspondiente en la lista.
#Es decir la primera vez que entra al ciclo elemento será igual a 
#mafer, luego gio, luego nano, luego daniel , luego gabriel y en la 
#ultima iteración valdrá Olimac
#para agregar elementos a una lista se utiliza la instrucción append

#para poder asignar algo a una tupla no se puede tocaría volverla lista primero
nombres =list(nombres)
nombres.append (input ("ingresa tu nombre  \n  :"))

print ("bienvenido {} a estos tutoriales, espero que sigas hasta el final!!, animo!!".format(nombres[-1]))

#para acceder a la ultima coordena de una lista denotamos -1, la penultima -2 etc


#----Ejemplo 1 -----#

#agreguemos estudiantes hasta que el usuario diga que no desea agregar mas y luego mostremos
#los estudiantes agregados

#Constantes
pregunta_continuar = "¿desea agregar mas estudiantes? \n 1.Si \n 2. No \n su respuesta : "
pregunta_nombre = "Ingrese nombre del estuantiante a adicionar a la lista \n: "
mostrar_nombres_mensaje="Buenos días soy {} y he quedado registrado satisfactoriamente"
lista_estudiantes = []
validador = 1

while (validador == 1 ):

    lista_estudiantes.append(input(pregunta_nombre))
    validador = int (input (pregunta_continuar))

for nombre in lista_estudiantes:
    print (mostrar_nombres_mensaje.format(nombre))







