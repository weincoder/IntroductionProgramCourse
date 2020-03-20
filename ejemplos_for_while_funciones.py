def hablar (mensaje):
    print(mensaje)
    return "exitoso"

def validar_clave (CLAVE_REAL, _claveIngresada):
    if (CLAVE_REAL == _claveIngresada) :
        print ("ingreso exitoso")
        STATE = "Clave valida"
    else :
        print ("clave incorrecta")
        STATE = "Clave invalida"
    return STATE

def mostrar_lista(lista):
    contador =1
    for elemento in lista:
        print(contador, "-",elemento)
        contador += 1

def mostrar_dos_listas(lista_1,lista_2):
    if (len(lista_1) == len(lista_2)):
        print("elemento","precio")
        for i in range(len(lista_1)):
            print(lista_1[i],"$",lista_2[i])

    else:
        print("no se puede mostrar uno a uno")

def bienvenida(): print("Bienvenido al código")

def ingresar():
    intentos = 0
    estado = validar_clave(1234,int(input("ingrese la clave : ")))
    intentos += 1
    while (estado != "Clave valida" and intentos<3):
        estado = validar_clave(1234,int(input("ingrese la clave : ")))
        intentos += 1
    return estado


bienvenida()

if ingresar() == "Clave valida":
    comidas = ["carne","pollo","huevo","Queso"]
    precios = [12345,6789,12232,4500]
    mostrar_lista(comidas)
    mostrar_dos_listas(comidas,precios)
else:
    print("Lo sentimos usted no ingreso correctamente, saliendo del programa")


def llenarLista():
    lista = []
    decicion = input ("ingrese s-->para agragar mas elementos n --> para no agregar mas : ")
    while (decicion == "s"):
        lista.append(input("ingrese un elemento de la lista: "))
        decicion = input ("ingres s-->para agragar mas elementos n --> para no agregar mas : ")
    return lista

print ("Ingrese la lista de alimentos")
comidas = llenarLista ()
print ("Ingrese la lista de precios a esos alimentos")
precios = llenarLista ()
mostrar_dos_listas(comidas,precios)
#Realizar un programa en python que permita lo siguiente
#Archivo con las siguientes funciones.
#Mostrar lista doctores, lista de enfermeros,lista de enfermos 
#Función que permita crear una lista de personas
#Función que permita mostrar el estado de los pacientes
#Utilizar funciones