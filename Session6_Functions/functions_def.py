#En esta sección validaremos la creación de funciones
#explicaremos las funciones
#Estas solucionan el problema de escribir muchas veces
#la misma porción de código
#por ejemplo supongamos que se nos pide crear un archivo
#de utilidades de python que sea capas de
#leer archivos, crear archivos a partir de una lista,
#retorna la palabra mas larga de una lista
#determinar el numero mas grande entre dos numeros

#una funcion inicia con la palabra def cuenta con un nombre
#el cual definimos nosotros, tambien cuenta con entradas
#las cuales podemos emplear dentro de ellas

def read_a_file(file_name):
    lineas = []
    with open(file_name,'r') as reader:
        for line in reader: lineas.append(line)
    #al igual que una función podemos retornar  una salida en este caso
    #la lista compuesta por las lineas del archivo
    return lineas

def create_a_file(entry_list,file_name):
    with open(file_name, 'w') as writer:
        for elemento in entry_list : writer.write(elemento + "\n")

def find_the_longest(list_of_swords) :
    mayor_ = ""
    for elemento in list_of_swords :
        if len (elemento) > len(mayor_) : mayor_ = elemento
    return mayor_

def find_the_biggest (numero_a, numero_b) :
    answer = "son iguales"
    preview_message = "el numero mas grande es el {} con un valor de {}"
    if numero_a > numero_b : answer = preview_message.format ('a',numero_a)
    elif numero_b > numero_a : answer = preview_message.format ('b',numero_b)
    return answer
