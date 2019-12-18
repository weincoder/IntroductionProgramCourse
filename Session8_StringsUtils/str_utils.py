#aprenderemos algunos trucos con strings
string_raw = "qui dolorem ipsum quia dolor sit amet onsectetur adipisci velit"
#supongmaos que deseamos eliminar todas las q del texto anterior
print (string_raw.split('q'))
#como notamos divide la cadena en una lista donde se produce un salto
# cada vez que se encuentra una q, pero si queremos mostrarlo en una frase?
print (' '.join(string_raw.split('q')))
# la instrucción join une los elementos de una lista separados por lo que 
# contenga las comillas predecesoras en este caso espacio
#por lo tanto si deseo cambiar todas las q por una t ?
print ('t'.join(string_raw.split('q')))
#si deseo separarlo por frases?
print (string_raw.split())
#si deseo saber cual es la palabra mas larga?
palabras =string_raw.split ()
print ("la palabra más larga de la lista es {}".format(
    max(palabras, key=len)))
#tengamos presente que los string en python se manejan como cadenas
#de caracteres por ejemplo le podemos aplicar len pues la colección
#de letras nos retornará la cantidad de espacios ocupados, por ejemplo
#la frase hola mundo tiene nueve letras pero hay un espacio entre las dos
#palabras por lo tanto su len sera igual a 10
print (len ("hola mundo") == 10)

#Si deseamos poner en mayuscula la primera letra de la frase
txt = "hola a todos"
txt_m = txt.capitalize()
print (txt_m)

#Si deseamos convertir a minuscula la cadena completa
txt = "NO ESTOY EN MINUSCULA"
txt_m= txt.casefold()
print(txt_m)
#Si deseamos ubicar en medio de un espacio de n caracteres
#un string en la mitad
txt = "Centro"
print(txt.center(20))

#contar las ocurrencias es decir la cantidad de veces que aparece
txt = "jamas diría las mimas cosas jamas jamas!!"
print(txt.count("jamas"))

#verificar que termine in a specific caracter
txt = "debo terminar en punto ."
print (txt.endswith("."))

#encontrar donde esta una palabra
txt = "donde estara la palabra en medio de tantas palabras?"
print(txt.find("palabra"),txt[16:23])
#nos indica que inicia en el espacio 16 y como palabra tiene 7 
#espacios imprimimos el espacio 16 al 23

#comprobar que sea númerico el contenido del string
txt = "345678"
print (txt.isnumeric())

#reemplazar de forma eficiente en una cadena las palabras
txt = "me gusta programar en java"
print (txt.replace ("java","python"))

#Convertir a mayuscula todas las letras de un string
txt = "estoy claramente en minuscula"
print(txt.upper())
