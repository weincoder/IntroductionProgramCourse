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





