#En este archivo hacemos uso del anterior importandolo
# cuando ponemos el termino as es como ponerle un apodo
#de forma que no debemos copiar el nombre del archivo 
#únicamente llamando a su alias
import functions_def as helper

#Constantes
list_of_estudents = ['mafer', 'nano', 'dan' , 'gi']
name_of_file_to_write = 'estudents_file.txt'
file_to_read_name = 'archivo.txt'
message_longest = "el estudiante con nombre mas largo es {}"
a = 2 
b = 3
#para acceder a una función dentro del archivo únicamente debemos
#llamar al alias . el nombre de la función
#debemos ingresar las entradas que configuramos para cada una de ellas
print (helper.read_a_file(file_to_read_name))
helper.create_a_file (list_of_estudents,name_of_file_to_write)
print (message_longest.format (helper.find_the_longest(list_of_estudents)))
print (helper.find_the_biggest(a,b))
#la ventaja de emplear funciones es que si las requerimos en algún otro
#código únicamente necesitamos importarlas, esto ahorra lineas de código
#de forma evidente  y esto hace mas sostenible en el tiempo nuestros 
#desarrollos
