#En los diccionarios podemos hacer uso del sistema llave valor
#Esto indica que al igual quen en un diccionario toda palabra tiene
#su significado. Por ejemplo hagamos un diccionario de medios de transporte:
#un diccionario vacio se inicia de la siguiente forma:
diccionario ={}
#incluyendo su contenido
medios_transporte = {
    "carros" : 
    [
        "BMW",
        "AUDI",
        "CHEVROLET",
        "MAZDA"
        ],
    "motos" : ["AKT","HARLEY","AUTECO"]
}
# en el caso de este diccionario podemos ver que se cuenta con
# las llaves carros y motos, cuando se solicita la llave carro se
# devuelve los carros asociados a esta llave. Igualmente para el caso
print ("los elementos que componen la llave carros son : {}".
format(medios_transporte["carros"]))
# de motos
print ("los elementos que componen la llave motos son : {}".
format(medios_transporte["motos"]))

#Si queremos obtener todas las llaves de un diccionario, lo podemos hacer así
print (medios_transporte.keys())
#para poderlas iterar las transformamos en lista
print (list (medios_transporte.keys()))
llaves =  list (medios_transporte.keys())
#para obtener las llaves
print (medios_transporte.values())
#para poderlas iterar las transformamos en lista
print (list (medios_transporte.values()))
valores =  list (medios_transporte.values())
#A continuación otra forma de crear diccionarios
diccionario={}
diccionario['Estudiantes']=['Meli','vale','cathe']
diccionario['Profesores']=['Braiam','Diego']
diccionario['aulas']=['A202','A206']
print(diccionario)
print(list(diccionario.keys()))
print(list(diccionario.values()))
print(diccionario['Profesores'])
print(diccionario)
#Los diccionarios nos permiten tener de una forma mas organizada la información
#En ocasiones podemos ver diccionarios de diccionarios
materiales={}
materiales['oro']=['18k','16k']
materiales['marcadores']=['pelikan','paper maker']
print(type(materiales))
diccionario['Elementos']=materiales
print(diccionario['Elementos']['marcadores'])


#Operaciones con diccionarios

#generar una copia sin afectar el original

diccionario_copia =diccionario.copy()
print(diccionario_copia)

#limpiar el contenido de un diccionario
diccionario_copia.clear()
print (diccionario_copia)

#crear un diccionario con las llaves el valor inicial será el mismo para todos
keys = ["idiomas","carreras"]
values = "soy un valor genérico"
created_dic = dict.fromkeys(keys,values)
print (created_dic)

#sin valor inicial sería
created_dic = dict.fromkeys (keys)
print (created_dic)

#obtener la definición de otra manera directamente en una lista
print (diccionario.get("Profesores"))

#Eliminar un componente del diccionario
diccionario_copy = diccionario.copy()

#se ingresa el específico valor de la llave a eliminar
diccionario_copy.pop("Profesores")
print (diccionario_copy)

#elimina la última llave agregada
diccionario_copy.popitem()
print (diccionario_copy)

#Agregar una llave o si existe sobre escribe su valor
diccionario_copy.setdefault("Computadoras",["Apple","Dell","Lenovo"])
print (diccionario_copy)
print (diccionario_copy.setdefault("Computador",["Apple","Dell","Lenovo","IBM"]))
print (diccionario_copy)
