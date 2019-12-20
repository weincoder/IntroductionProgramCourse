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
dicionario={}
dicionario['Estudiantes']=['Meli','vale','cathe']
dicionario['Profesores']=['Braiam','Diego']
dicionario['aulas']=['A202','A206']
print(dicionario)
print(list(dicionario.keys()))
print(list(dicionario.values()))
print(dicionario['Profesores'])
print(dicionario)
#Los diccionarios nos permiten tener de una forma mas organizada la información
#En ocasiones podemos ver diccionarios de diccionarios
materiales={}
materiales['oro']=['18k','16k']
materiales['marcadores']=['pelikan','paper maker']
print(type(materiales))
dicionario['Elementos']=materiales
print(dicionario['Elementos']['marcadores'])
